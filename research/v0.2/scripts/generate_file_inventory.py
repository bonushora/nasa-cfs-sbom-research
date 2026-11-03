#!/usr/bin/env python3
"""Generate a deterministic inventory of objects in pinned cFS Git trees."""

import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import stat
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


OFFICIAL_ORIGIN = "https://github.com/nasa/cFS.git"
LFS_PREFIX = b"version https://git-lfs.github.com/spec/v1\n"
FIELDS = [
    "component_path", "repository", "repo_commit", "repo_relative_path", "file_mode",
    "git_object_id", "git_object_type", "logical_blob_size", "blob_sha256",
    "checkout_sha256", "checkout_state", "selection_class", "exclusion_reason",
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def git(repo, *arguments, text=True):
    result = subprocess.run(
        ["git", "--no-optional-locks", "-C", str(repo), *arguments], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=text,
        env={**os.environ, "GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"},
    )
    return result.stdout


def ls_tree(repo, commit):
    raw = git(repo, "ls-tree", "-r", "-z", "-l", commit, text=False)
    records = []
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, path = item.split(b"\t", 1)
        mode, object_type, oid, size = metadata.decode("ascii").split()
        records.append({
            "mode": mode, "type": object_type, "oid": oid,
            "size": None if size == "-" else int(size),
            "path": path.decode("utf-8", "surrogateescape"),
        })
    return records


class BatchReader:
    def __init__(self, repo):
        self.process = subprocess.Popen(
            ["git", "--no-optional-locks", "-C", str(repo), "cat-file", "--batch"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env={**os.environ, "GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"},
        )

    def read(self, oid):
        self.process.stdin.write((oid + "\n").encode("ascii"))
        self.process.stdin.flush()
        header = self.process.stdout.readline().decode("ascii").strip().split()
        require(len(header) == 3 and header[0] == oid, f"bad cat-file header for {oid}: {header}")
        _, object_type, size_text = header
        size = int(size_text)
        data = self.process.stdout.read(size)
        require(self.process.stdout.read(1) == b"\n", f"missing cat-file delimiter for {oid}")
        return object_type, data

    def close(self):
        self.process.stdin.close()
        stderr = self.process.stderr.read().decode("utf-8", "replace")
        code = self.process.wait()
        require(code == 0, f"git cat-file failed: {stderr}")


def safe_checkout_hash(repo, relative_path, mode, blob):
    path = repo / relative_path
    try:
        info = path.lstat()
    except FileNotFoundError:
        return "", "MISSING"
    if mode == "120000":
        require(stat.S_ISLNK(info.st_mode), f"expected symlink checkout: {path}")
        target = os.readlink(path).encode("utf-8", "surrogateescape")
        require(target == blob, f"symlink target differs from Git blob: {path}")
        return "", "SYMLINK_TARGET_MATCH"
    require(stat.S_ISREG(info.st_mode), f"checkout path is not regular: {path}")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    blob_digest = hashlib.sha256(blob).hexdigest()
    if digest == blob_digest:
        return digest, "BYTE_MATCH"
    attribute = git(repo, "check-attr", "ident", "--", relative_path).strip()
    if attribute.endswith(": ident: set") and b"$Id$" in blob:
        return digest, "IDENT_EXPANDED"
    return digest, "BYTE_DIFFERENT"


def write_deterministic_gzip_csv(path, rows):
    buffer = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buffer, mtime=0) as compressed:
        with io.TextIOWrapper(compressed, encoding="utf-8", newline="", write_through=True) as text:
            writer = csv.DictWriter(text, fieldnames=FIELDS, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
    path.write_bytes(buffer.getvalue())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--clone", required=True, type=Path)
    parser.add_argument("--gitlinks", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    clone = args.clone.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    controlled = json.loads(args.gitlinks.read_text(encoding="utf-8"))
    baseline = controlled["baseline"]
    require(git(clone, "rev-parse", "HEAD").strip() == baseline, "root HEAD mismatch")
    require(git(clone, "remote", "get-url", "origin").strip() == OFFICIAL_ORIGIN, "root origin mismatch")
    require(git(clone, "status", "--porcelain", "--untracked-files=all") == "", "root checkout is dirty")

    root_gitlinks = {
        item["path"]: item for item in ls_tree(clone, baseline) if item["mode"] == "160000"
    }
    require(len(root_gitlinks) == 25, f"expected 25 root gitlinks, got {len(root_gitlinks)}")
    entries = controlled["entries"]
    require({entry["path"] for entry in entries} == set(root_gitlinks), "root gitlink paths differ")
    for entry in entries:
        observed = root_gitlinks[entry["path"]]
        require(observed["oid"] == entry["sha"] and observed["type"] == "commit", f"root gitlink mismatch: {entry['path']}")

    components = [{"path": ".", "repository": "cFS", "commit": baseline, "repo": clone}]
    for entry in entries:
        repo = (clone / entry["path"]).resolve()
        require(repo.is_relative_to(clone), f"component escapes clone: {entry['path']}")
        require(git(repo, "rev-parse", "HEAD").strip() == entry["sha"], f"component HEAD mismatch: {entry['path']}")
        require(git(repo, "status", "--porcelain", "--untracked-files=all") == "", f"component checkout dirty: {entry['path']}")
        components.append({"path": entry["path"], "repository": entry["repository"], "commit": entry["sha"], "repo": repo})

    rows = []
    component_summary = []
    for component in components:
        repo = component["repo"]
        tree = sorted(ls_tree(repo, component["commit"]), key=lambda item: item["path"])
        batch = BatchReader(repo)
        counts = Counter()
        logical_bytes = 0
        try:
            for item in tree:
                mode = item["mode"]
                selection_class = ""
                exclusion_reason = ""
                blob_sha256 = ""
                checkout_sha256 = ""
                checkout_state = "NOT_APPLICABLE"
                if item["type"] == "blob":
                    object_type, blob = batch.read(item["oid"])
                    require(object_type == "blob", f"expected blob: {item}")
                    require(len(blob) == item["size"], f"blob size mismatch: {item}")
                    blob_sha256 = hashlib.sha256(blob).hexdigest()
                    logical_bytes += len(blob)
                    checkout_sha256, checkout_state = safe_checkout_hash(repo, item["path"], mode, blob)
                    if mode == "120000":
                        selection_class = "TRACKED_SYMLINK"
                        exclusion_reason = "symlink_not_followed"
                    elif mode in {"100644", "100755"} and blob.startswith(LFS_PREFIX):
                        selection_class = "GIT_LFS_POINTER"
                        exclusion_reason = "resolved_lfs_content_not_inventoried"
                    elif mode in {"100644", "100755"}:
                        if checkout_state == "BYTE_MATCH":
                            selection_class = "TRACKED_REGULAR"
                        elif checkout_state == "IDENT_EXPANDED":
                            selection_class = "TRACKED_REGULAR_FILTERED_CHECKOUT"
                            exclusion_reason = "checkout_ident_expansion_blob_is_authoritative"
                        else:
                            selection_class = "TRACKED_REGULAR_CHECKOUT_DIFFERENT"
                            exclusion_reason = "checkout_bytes_differ_for_unclassified_reason"
                            raise ValueError(f"checkout bytes differ: {component['path']}:{item['path']}")
                    else:
                        selection_class = "OTHER_BLOB_MODE"
                        exclusion_reason = "unsupported_blob_mode"
                elif item["type"] == "commit" and mode == "160000":
                    selection_class = "TRACKED_GITLINK"
                    exclusion_reason = "nested_content_not_descended_in_parent_tree"
                else:
                    selection_class = "OTHER_GIT_OBJECT"
                    exclusion_reason = "unsupported_git_object_type"
                counts[selection_class] += 1
                rows.append({
                    "component_path": component["path"], "repository": component["repository"],
                    "repo_commit": component["commit"], "repo_relative_path": item["path"],
                    "file_mode": mode, "git_object_id": item["oid"], "git_object_type": item["type"],
                    "logical_blob_size": "" if item["size"] is None else item["size"],
                    "blob_sha256": blob_sha256, "checkout_sha256": checkout_sha256,
                    "checkout_state": checkout_state, "selection_class": selection_class,
                    "exclusion_reason": exclusion_reason,
                })
        finally:
            batch.close()
        component_summary.append({
            "component_path": component["path"], "repository": component["repository"],
            "repo_commit": component["commit"], "tree_entries": len(tree),
            "logical_blob_bytes": logical_bytes, "classes": dict(sorted(counts.items())),
        })

    rows.sort(key=lambda row: (row["component_path"], row["repo_relative_path"]))
    keys = [(row["component_path"], row["repo_relative_path"]) for row in rows]
    require(len(keys) == len(set(keys)), "duplicate component/path inventory keys")
    output = args.output_dir / "file-inventory.csv.gz"
    write_deterministic_gzip_csv(output, rows)
    totals = Counter(row["selection_class"] for row in rows)
    summary = {
        "schema_version": 1,
        "selection_rule": "All recursive leaf entries in the pinned root Git tree and each of its 25 pinned component Git trees; parent trees do not descend into gitlinks.",
        "baseline": baseline,
        "components": component_summary,
        "totals": {
            "components": len(components), "inventory_rows": len(rows),
            "classes": dict(sorted(totals.items())),
            "logical_blob_bytes": sum(item["logical_blob_bytes"] for item in component_summary),
        },
        "artifact": {"path": output.name, "sha256": hashlib.sha256(output.read_bytes()).hexdigest()},
        "hash_semantics": {
            "git_object_id": "Git SHA-1 object identifier from the pinned tree",
            "blob_sha256": "SHA-256 of exact Git blob bytes",
            "checkout_sha256": "SHA-256 of checked-out regular-file bytes when present and byte-equal",
        },
    }
    (args.output_dir / "file-inventory-summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    markdown = [
        "# Pinned Git-tree file inventory", "",
        f"Baseline: `{baseline}`", "",
        f"Total rows: **{len(rows)}** across **{len(components)}** Git trees.", "",
        "| Component | Commit | Entries | Regular | Filtered checkout | Symlinks | Gitlinks | Blob bytes |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for item in component_summary:
        classes = item["classes"]
        markdown.append(
            f"| `{item['component_path']}` | `{item['repo_commit']}` | {item['tree_entries']} | "
            f"{classes.get('TRACKED_REGULAR', 0)} | {classes.get('TRACKED_REGULAR_FILTERED_CHECKOUT', 0)} | "
            f"{classes.get('TRACKED_SYMLINK', 0)} | {classes.get('TRACKED_GITLINK', 0)} | "
            f"{item['logical_blob_bytes']} |"
        )
    markdown += [
        "", "Git object IDs and SHA-256 digests have distinct semantics. Symlinks are recorded",
        "without being followed. Parent Git trees record Gitlinks but do not descend into them;",
        "each of the 25 pinned component trees is enumerated separately.", "",
    ]
    (args.output_dir / "file-inventory-summary.md").write_text("\n".join(markdown), encoding="utf-8")
    print(f"PASS components={len(components)} rows={len(rows)} unique_paths={len(keys)}")
    print("PASS " + " ".join(f"{key.lower()}={value}" for key, value in sorted(totals.items())))
    print(f"PASS artifact_sha256={summary['artifact']['sha256']}")


if __name__ == "__main__":
    main()

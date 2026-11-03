#!/usr/bin/env python3
"""Generate conservative dependency-declaration and license-evidence matrices."""

import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import re
import subprocess
from collections import Counter
from pathlib import Path


DEPENDENCY_FIELDS = [
    "component", "repo_commit", "target", "evidence_location", "relationship_kind",
    "scope", "condition", "confidence", "verification_state", "evidence_sha256",
]
LICENSE_FIELDS = [
    "component", "repo_commit", "evidence_path", "line_span", "evidence_kind",
    "assertion_scope", "declared_expression", "package_conclusion", "text_sha256",
    "evidence_excerpt", "verification_state",
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
    result = []
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, path = item.split(b"\t", 1)
        mode, object_type, oid, size = metadata.decode("ascii").split()
        result.append({
            "mode": mode, "type": object_type, "oid": oid,
            "size": None if size == "-" else int(size),
            "path": path.decode("utf-8", "surrogateescape"),
        })
    return result


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
        require(len(header) == 3 and header[0] == oid and header[1] == "blob", f"bad cat-file header: {header}")
        size = int(header[2])
        data = self.process.stdout.read(size)
        require(self.process.stdout.read(1) == b"\n", "missing cat-file delimiter")
        return data

    def close(self):
        self.process.stdin.close()
        error = self.process.stderr.read().decode("utf-8", "replace")
        require(self.process.wait() == 0, f"git cat-file failed: {error}")


def gzip_csv(path, fields, rows):
    buffer = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buffer, mtime=0) as compressed:
        with io.TextIOWrapper(compressed, encoding="utf-8", newline="", write_through=True) as text:
            writer = csv.DictWriter(text, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
    path.write_bytes(buffer.getvalue())


def cmake_calls(text):
    start_pattern = re.compile(r"(?im)^[ \t]*(find_package|add_subdirectory|target_link_libraries|include)[ \t]*\(")
    for match in start_pattern.finditer(text):
        depth = 1
        position = match.end()
        while position < len(text) and depth:
            character = text[position]
            if character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
            position += 1
        if depth:
            continue
        content = text[match.end():position - 1]
        normalized = " ".join(content.split())
        if len(normalized) > 1000:
            normalized = normalized[:900] + " ... [expression truncated; digest in evidence_sha256]"
        start_line = text.count("\n", 0, match.start()) + 1
        end_line = text.count("\n", 0, position) + 1
        yield match.group(1).lower(), normalized, start_line, end_line, text[match.start():position]


def decode_text(data):
    if b"\0" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def license_file_name(path):
    name = Path(path).name
    return bool(re.match(r"^(license|copying|notice|copyright)(\..*)?$", name, re.I) or "/LICENSES/" in f"/{path}")


def first_excerpt(text):
    for line in text.splitlines():
        value = " ".join(line.strip().split())
        if value:
            return value[:200]
    return ""


def gitmodule_rows(clone, baseline, entries):
    text = git(clone, "show", f"{baseline}:.gitmodules")
    lines = text.splitlines()
    rows = []
    for entry in entries:
        path_line = next((i for i, line in enumerate(lines, 1) if re.fullmatch(rf"\s*path\s*=\s*{re.escape(entry['path'])}\s*", line)), None)
        require(path_line is not None, f"missing .gitmodules path: {entry['path']}")
        url_line = None
        url = ""
        for number in range(path_line + 1, min(path_line + 5, len(lines) + 1)):
            match = re.fullmatch(r"\s*url\s*=\s*(\S+)\s*", lines[number - 1])
            if match:
                url_line, url = number, match.group(1)
                break
        require(url_line is not None, f"missing .gitmodules URL: {entry['path']}")
        evidence = f"path={entry['path']} url={url} sha={entry['sha']}"
        rows.append({
            "component": ".", "repo_commit": baseline,
            "target": f"{entry['path']}@{entry['sha']}",
            "evidence_location": f".gitmodules:{path_line}-{url_line}",
            "relationship_kind": "DECLARED_PINNED_GITLINK", "scope": "source_composition",
            "condition": "unconditional_at_pinned_root_tree", "confidence": "HIGH",
            "verification_state": "VERIFIED_PINNED",
            "evidence_sha256": hashlib.sha256(evidence.encode("utf-8")).hexdigest(),
        })
    return rows


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
    entries = controlled["entries"]
    components = [{"path": ".", "repository": "cFS", "commit": baseline, "repo": clone}]
    components += [
        {"path": entry["path"], "repository": entry["repository"], "commit": entry["sha"], "repo": (clone / entry["path"]).resolve()}
        for entry in entries
    ]

    dependency_rows = gitmodule_rows(clone, baseline, entries)
    license_rows = []
    build_files_scanned = 0
    text_blobs_scanned = 0
    command_types = {
        "find_package": ("DECLARED_EXTERNAL_LOOKUP", "build_configuration"),
        "add_subdirectory": ("DECLARED_SOURCE_INCLUSION", "build_configuration"),
        "target_link_libraries": ("DECLARED_LINK_EXPRESSION", "link_configuration"),
        "include": ("DECLARED_BUILD_INCLUDE", "build_configuration"),
    }
    for component in components:
        batch = BatchReader(component["repo"])
        try:
            for item in sorted(ls_tree(component["repo"], component["commit"]), key=lambda value: value["path"]):
                if item["type"] != "blob" or item["mode"] not in {"100644", "100755"} or item["size"] > 2_000_000:
                    continue
                is_build = Path(item["path"]).name == "CMakeLists.txt" or item["path"].lower().endswith(".cmake")
                is_license = license_file_name(item["path"])
                likely_text = is_build or is_license or Path(item["path"]).suffix.lower() in {
                    ".c", ".h", ".cpp", ".hpp", ".py", ".sh", ".md", ".txt", ".yml", ".yaml", ".json", ".xml",
                }
                if not likely_text:
                    continue
                data = batch.read(item["oid"])
                text = decode_text(data)
                if text is None:
                    continue
                text_blobs_scanned += 1
                if is_build:
                    build_files_scanned += 1
                    for command, expression, start, end, evidence in cmake_calls(text):
                        kind, scope = command_types[command]
                        dependency_rows.append({
                            "component": component["path"], "repo_commit": component["commit"],
                            "target": expression, "evidence_location": f"{item['path']}:{start}-{end}",
                            "relationship_kind": kind, "scope": scope,
                            "condition": "requires_cmake_evaluation", "confidence": "HIGH",
                            "verification_state": "DECLARED_UNRESOLVED",
                            "evidence_sha256": hashlib.sha256(evidence.encode("utf-8")).hexdigest(),
                        })
                if is_license:
                    identifiers = re.findall(r"SPDX-License-Identifier:\s*([^\r\n*]+)", text)
                    license_rows.append({
                        "component": component["path"], "repo_commit": component["commit"],
                        "evidence_path": item["path"], "line_span": f"1-{len(text.splitlines())}",
                        "evidence_kind": "LICENSE_OR_NOTICE_FILE", "assertion_scope": "evidence_file",
                        "declared_expression": identifiers[0].strip() if len(set(identifiers)) == 1 else "",
                        "package_conclusion": "NOASSERTION", "text_sha256": hashlib.sha256(data).hexdigest(),
                        "evidence_excerpt": first_excerpt(text), "verification_state": "EVIDENCE_FILE_PRESENT",
                    })
                for line_number, line in enumerate(text.splitlines(), 1):
                    match = re.search(r"SPDX-License-Identifier:\s*([^\r\n*]+)", line)
                    if not match:
                        continue
                    expression = match.group(1).strip().rstrip("*/ ")
                    license_rows.append({
                        "component": component["path"], "repo_commit": component["commit"],
                        "evidence_path": item["path"], "line_span": str(line_number),
                        "evidence_kind": "SPDX_IDENTIFIER", "assertion_scope": "file",
                        "declared_expression": expression, "package_conclusion": "NOASSERTION",
                        "text_sha256": hashlib.sha256(line.encode("utf-8")).hexdigest(),
                        "evidence_excerpt": " ".join(line.strip().split())[:200],
                        "verification_state": "EXPLICIT_FILE_DECLARATION",
                    })
        finally:
            batch.close()

    dependency_rows.sort(key=lambda row: tuple(row[field] for field in DEPENDENCY_FIELDS))
    license_rows.sort(key=lambda row: tuple(row[field] for field in LICENSE_FIELDS))
    dep_keys = [tuple(row[field] for field in DEPENDENCY_FIELDS) for row in dependency_rows]
    lic_keys = [tuple(row[field] for field in LICENSE_FIELDS) for row in license_rows]
    require(len(dep_keys) == len(set(dep_keys)), "duplicate dependency rows")
    require(len(lic_keys) == len(set(lic_keys)), "duplicate license rows")
    require(sum(row["verification_state"] == "VERIFIED_PINNED" for row in dependency_rows) == 25, "pinned gitlink evidence count mismatch")
    require(all(row["package_conclusion"] == "NOASSERTION" for row in license_rows), "unsupported package license conclusion")

    dep_path = args.output_dir / "dependency-evidence.csv.gz"
    lic_path = args.output_dir / "license-evidence.csv.gz"
    gzip_csv(dep_path, DEPENDENCY_FIELDS, dependency_rows)
    gzip_csv(lic_path, LICENSE_FIELDS, license_rows)
    summary = {
        "schema_version": 1,
        "dependency_method": "Pinned .gitmodules/gitlink verification plus syntactic extraction of find_package, add_subdirectory, target_link_libraries, and include expressions from pinned CMake blobs. CMake semantics are not executed.",
        "license_method": "Pinned license/notice files and explicit SPDX-License-Identifier lines are recorded as evidence; package-wide conclusions remain NOASSERTION.",
        "scanned": {"components": 26, "text_blobs": text_blobs_scanned, "cmake_files": build_files_scanned},
        "dependencies": {
            "rows": len(dependency_rows),
            "relationship_kinds": dict(sorted(Counter(row["relationship_kind"] for row in dependency_rows).items())),
            "verification_states": dict(sorted(Counter(row["verification_state"] for row in dependency_rows).items())),
            "artifact_sha256": hashlib.sha256(dep_path.read_bytes()).hexdigest(),
        },
        "licenses": {
            "rows": len(license_rows),
            "evidence_kinds": dict(sorted(Counter(row["evidence_kind"] for row in license_rows).items())),
            "declared_expressions": dict(sorted(Counter(row["declared_expression"] or "NONE" for row in license_rows).items())),
            "package_conclusion": "NOASSERTION",
            "artifact_sha256": hashlib.sha256(lic_path.read_bytes()).hexdigest(),
        },
        "limits": [
            "CMake expressions are declaration evidence, not resolved build or runtime dependency edges.",
            "Transitive, linker-confirmed, generated, binary, and runtime dependencies are not assessed.",
            "License evidence does not imply package-wide or compatibility conclusions.",
        ],
    }
    (args.output_dir / "evidence-matrix-summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"PASS dependency_rows={len(dependency_rows)} verified_pinned=25 cmake_files={build_files_scanned}")
    print(f"PASS license_rows={len(license_rows)} package_conclusion=NOASSERTION text_blobs={text_blobs_scanned}")
    print(f"PASS dependency_sha256={summary['dependencies']['artifact_sha256']}")
    print(f"PASS license_sha256={summary['licenses']['artifact_sha256']}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate a deterministic cFS v7.0.1 VDD/gitlink crosswalk."""

import argparse
import csv
import hashlib
import io
import json
import re
import tarfile
from pathlib import Path, PurePosixPath


SHA40 = re.compile(r"^[0-9a-f]{40}$")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def normalize_component(value):
    return re.sub(r"[^a-z0-9]", "", value.lower())


def inspect_archive(archive, vdd_dir):
    records = []
    names = set()
    with tarfile.open(archive, "r:gz") as bundle:
        for member in bundle.getmembers():
            path = PurePosixPath(member.name)
            reasons = []
            if path.is_absolute() or member.name.startswith("/"):
                reasons.append("absolute_path")
            if any(part == ".." for part in path.parts):
                reasons.append("parent_traversal")
            if "\\" in member.name:
                reasons.append("backslash_path")
            if member.name in names:
                reasons.append("duplicate_name")
            names.add(member.name)
            if member.issym():
                reasons.append("symlink")
            if member.islnk():
                reasons.append("hardlink")
            if member.isdev():
                reasons.append("device")
            if member.isfifo():
                reasons.append("fifo")
            if not (member.isfile() or member.isdir()):
                reasons.append("unsupported_type")
            require(not reasons, f"unsafe archive member {member.name}: {reasons}")
            kind = "file" if member.isfile() else "directory"
            record = {"path": member.name, "type": kind, "size": member.size}
            if member.isfile():
                source = bundle.extractfile(member)
                require(source is not None, f"cannot read {member.name}")
                data = source.read()
                extracted = vdd_dir.parent / member.name
                require(extracted.is_file(), f"missing extracted file: {extracted}")
                require(extracted.read_bytes() == data, f"extracted bytes differ: {member.name}")
                record["sha256"] = sha256_bytes(data)
            records.append(record)
    require(len(records) == 32, f"expected 32 archive members, got {len(records)}")
    require(sum(r["type"] == "file" for r in records) == 27, "expected 27 files")
    return records


def line_match(lines, pattern):
    hits = [(number, line) for number, line in enumerate(lines, 1) if re.search(pattern, line)]
    require(len(hits) == 1, f"expected one match for {pattern}, got {len(hits)}")
    return hits[0]


def parse_individual_documents(vdd_dir):
    documents = {}
    for path in sorted(vdd_dir.glob("[0-9][0-9]-*/*.md")):
        identity = re.sub(r"^\d+-", "", path.stem)
        lines = path.read_text(encoding="utf-8").splitlines()
        heading_line, heading = line_match(lines, r"^# Version Description Document")
        version_line, version_text = line_match(lines, r"^>\*\*Version:\*\*")
        revision_line, revision_text = line_match(lines, r"^>\*\*Document Version:\*\*")
        identification_line, _ = line_match(lines, r"^This document details")
        version = re.search(r"Open Source (v\d+\.\d+\.\d+)", version_text)
        revision = re.search(r"Document Version:\*\*\s*(Rev\s+[A-Z])", revision_text)
        require(version is not None and revision is not None, f"bad identity block: {path}")
        history = []
        for line in lines:
            match = re.match(r"^\|\s*(Rev\s+[A-Z])\s*\|", line)
            if match and match.group(1) not in history:
                history.append(match.group(1))
        key = normalize_component(identity)
        require(key not in documents, f"duplicate document identity: {identity}")
        documents[key] = {
            "path": path.relative_to(vdd_dir.parent).as_posix(),
            "sha256": sha256_bytes(path.read_bytes()),
            "heading": heading.removeprefix("# "),
            "heading_line": heading_line,
            "software_version": version.group(1),
            "version_line": version_line,
            "document_revision_header": revision.group(1),
            "revision_line": revision_line,
            "document_history_revisions": history,
            "identification_line": identification_line,
        }
    require(len(documents) == 25, f"expected 25 component VDDs, got {len(documents)}")
    return documents


def parse_section7(vdd_dir):
    path = vdd_dir / "00-cfs.md"
    table = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.fullmatch(
            r"\|\s*([^|]+?)\s*\|\s*(v[^| ]+)\s*\|\s*([0-9a-f]{40})\s*\|", line
        )
        if not match:
            continue
        component, version, sha = match.groups()
        key = normalize_component(component)
        require(key not in table, f"duplicate Section 7 component: {component}")
        table[key] = {"component": component, "version": version, "sha": sha, "line": number}
    require(len(table) == 25, f"expected 25 Section 7 rows, got {len(table)}")
    return path, table


def write_csv(path, rows):
    fields = [
        "ordinal", "gitlink_path", "repository", "published_git_sha", "vdd_component",
        "vdd_version", "vdd_git_sha", "sha_status", "top_level_reference",
        "individual_vdd", "individual_reference", "individual_software_version",
        "document_revision_header", "document_history_revisions", "comparison_status",
    ]
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path, rows, archive_hash, top_hash):
    lines = [
        "# NASA cFS v7.0.1 VDD / published gitlink crosswalk", "",
        f"Official VDD archive SHA-256: `{archive_hash}`  ",
        f"Top-level VDD SHA-256: `{top_hash}`", "",
        "`MATCH` requires equal component identity and exact 40-hex Git SHA. The individual VDD",
        "supports the software version label but does not independently supply the Git SHA.", "",
        "| # | Published path | Published Git SHA | VDD source | Individual VDD | Result |",
        "|---:|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['ordinal']} | `{row['gitlink_path']}` | `{row['published_git_sha']}` | "
            f"`{row['top_level_reference']}` ({row['vdd_component']} {row['vdd_version']}) | "
            f"`{row['individual_reference']}` | `{row['comparison_status']}` |"
        )
    lines += [
        "", "## Counts", "", "```text", "MATCH=25", "PARTIAL_MATCH=0", "MISMATCH=0",
        "NOT_DOCUMENTED=0", "NOT_COMPARABLE=0", "TOTAL=25", "```", "",
        "This reconciliation covers the 25 pinned source Gitlinks. It does not establish",
        "file-, dependency-, build-, binary-, runtime-, vulnerability-, or licensing completeness.", "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--vdd-dir", required=True, type=Path)
    parser.add_argument("--gitlinks", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    archive_bytes = args.archive.read_bytes()
    archive_hash = sha256_bytes(archive_bytes)
    require(len(archive_bytes) == 13850, f"unexpected archive size: {len(archive_bytes)}")
    require(archive_hash == "ee1fa901a49091274a19dc475564fbf541c36278714b73bf12cd980a4f165aa3", "archive hash mismatch")
    members = inspect_archive(args.archive, args.vdd_dir)
    top_path, section7 = parse_section7(args.vdd_dir)
    documents = parse_individual_documents(args.vdd_dir)
    controlled = json.loads(args.gitlinks.read_text(encoding="utf-8"))
    entries = controlled["entries"]
    require(len(entries) == 25, "controlled table does not have 25 entries")
    controlled_keys = {normalize_component(entry["repository"]) for entry in entries}
    require(len(controlled_keys) == 25, "controlled component aliases collide")
    require(controlled_keys == set(section7) == set(documents), "component sets differ")

    rows = []
    for ordinal, entry in enumerate(entries, 1):
        key = normalize_component(entry["repository"])
        vdd = section7[key]
        document = documents[key]
        require(SHA40.fullmatch(entry["sha"]) is not None, f"invalid controlled SHA: {entry}")
        require(entry["sha"] == vdd["sha"], f"Git SHA mismatch: {entry['path']}")
        require(vdd["version"] == document["software_version"] == "v7.0.1", f"version mismatch: {entry['path']}")
        references = [
            document["heading_line"], document["version_line"], document["revision_line"],
            document["identification_line"],
        ]
        rows.append({
            "ordinal": ordinal,
            "gitlink_path": entry["path"],
            "repository": entry["repository"],
            "published_git_sha": entry["sha"],
            "vdd_component": vdd["component"],
            "vdd_version": vdd["version"],
            "vdd_git_sha": vdd["sha"],
            "sha_status": "EXACT_MATCH",
            "top_level_reference": f"vdd/00-cfs.md:{vdd['line']}",
            "individual_vdd": document["path"],
            "individual_reference": f"{document['path']}:{','.join(map(str, references))}",
            "individual_software_version": document["software_version"],
            "document_revision_header": document["document_revision_header"],
            "document_history_revisions": ",".join(document["document_history_revisions"]),
            "comparison_status": "MATCH",
        })

    top_hash = sha256_bytes(top_path.read_bytes())
    result = {
        "schema_version": 1,
        "baseline": controlled["baseline"],
        "sources": {
            "official_archive": {"size": len(archive_bytes), "sha256": archive_hash},
            "top_level_vdd": {"path": "vdd/00-cfs.md", "sha256": top_hash, "section": "7", "lines": "316-344"},
            "gitlinks_table": {"sha256": sha256_bytes(args.gitlinks.read_bytes()), "entries": 25},
        },
        "summary": {"total": 25, "match": 25, "exact_git_sha_match": 25, "software_version_v7_0_1": 25},
        "rows": rows,
    }
    (args.output_dir / "vdd-crosswalk.json").write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_csv(args.output_dir / "vdd-crosswalk.csv", rows)
    write_markdown(args.output_dir / "vdd-crosswalk.md", rows, archive_hash, top_hash)
    source_manifest = {
        "schema_version": 1,
        "archive": {"size": len(archive_bytes), "sha256": archive_hash},
        "members": members,
        "component_documents": sorted(documents.values(), key=lambda item: item["path"]),
    }
    (args.output_dir / "vdd-source-manifest.json").write_text(
        json.dumps(source_manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("PASS archive members=32 files=27 unsafe=0")
    print("PASS VDD Section7 rows=25 exact_sha_matches=25")
    print("PASS individual_component_vdds=25 software_version_v7.0.1=25")


if __name__ == "__main__":
    main()

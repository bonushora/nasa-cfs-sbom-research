#!/usr/bin/env python3
"""Fail-closed validation for the v0.2 supplemental research package."""

import argparse
import csv
import gzip
import hashlib
import json
import os
import re
import stat
import subprocess
from collections import Counter
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path, compressed=False):
    opener = gzip.open if compressed else open
    with opener(path, "rt", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def git(repo, *arguments):
    return subprocess.run(
        ["git", "--no-optional-locks", "-C", str(repo), *arguments], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        env={**os.environ, "GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"},
    ).stdout


def validate_crosswalk(package):
    data = json.loads((package / "vdd/vdd-crosswalk.json").read_text(encoding="utf-8"))
    csv_rows = read_csv(package / "vdd/vdd-crosswalk.csv")
    rows = data["rows"]
    require(len(rows) == len(csv_rows) == 25, "crosswalk row count differs")
    require(data["summary"] == {"exact_git_sha_match": 25, "match": 25, "software_version_v7_0_1": 25, "total": 25}, "crosswalk summary differs")
    require(all(row["comparison_status"] == "MATCH" and row["sha_status"] == "EXACT_MATCH" for row in rows), "crosswalk contains non-match")
    require(all(row["published_git_sha"] == row["vdd_git_sha"] for row in rows), "crosswalk SHA differs")
    fields = list(csv_rows[0])
    for json_row, csv_row in zip(rows, csv_rows):
        normalized = {key: str(json_row[key]) for key in fields}
        require(normalized == csv_row, f"CSV/JSON semantic difference at row {json_row['ordinal']}")
    markdown = (package / "vdd/vdd-crosswalk.md").read_text(encoding="utf-8")
    table_rows = [line for line in markdown.splitlines() if re.match(r"^\|\s*\d+\s*\|", line)]
    require(len(table_rows) == 25 and all("`MATCH`" in line for line in table_rows), "Markdown crosswalk differs")
    for row, line in zip(rows, table_rows):
        require(row["published_git_sha"] in line and row["gitlink_path"] in line, "Markdown row identity differs")
    source = json.loads((package / "vdd/vdd-source-manifest.json").read_text(encoding="utf-8"))
    require(len(source["members"]) == 32, "VDD source member count differs")
    require(sum(item["type"] == "file" for item in source["members"]) == 27, "VDD source file count differs")
    require(len(source["component_documents"]) == 25, "component VDD count differs")
    require(source["archive"]["sha256"] == "ee1fa901a49091274a19dc475564fbf541c36278714b73bf12cd980a4f165aa3", "VDD archive hash differs")
    print("PASS crosswalk csv=json=markdown rows=25 exact_sha=25")


def validate_inventory(package):
    summary = json.loads((package / "inventory/file-inventory-summary.json").read_text(encoding="utf-8"))
    artifact = package / "inventory/file-inventory.csv.gz"
    require(sha256(artifact) == summary["artifact"]["sha256"], "inventory artifact hash differs")
    rows = read_csv(artifact, compressed=True)
    require(len(rows) == summary["totals"]["inventory_rows"], "inventory row count differs")
    keys = [(row["component_path"], row["repo_relative_path"]) for row in rows]
    require(len(keys) == len(set(keys)), "duplicate inventory keys")
    require(keys == sorted(keys), "inventory is not stably sorted")
    counts = dict(sorted(Counter(row["selection_class"] for row in rows).items()))
    require(counts == summary["totals"]["classes"], "inventory class counts differ")
    require(summary["totals"]["components"] == len(summary["components"]) == 26, "component count differs")
    require(counts.get("TRACKED_GITLINK") == 25, "expected 25 Gitlinks")
    require(counts.get("TRACKED_SYMLINK") == 5, "expected five symlinks")
    require(counts.get("TRACKED_REGULAR_FILTERED_CHECKOUT") == 1, "expected one filtered checkout")
    require(all(row["checkout_state"] == "BYTE_MATCH" for row in rows if row["selection_class"] == "TRACKED_REGULAR"), "regular checkout mismatch")
    print(f"PASS inventory components=26 rows={len(rows)} unique={len(keys)} classes={counts}")


def component_map(clone, controlled):
    result = {".": {"repo": clone, "commit": controlled["baseline"]}}
    for entry in controlled["entries"]:
        result[entry["path"]] = {"repo": (clone / entry["path"]).resolve(), "commit": entry["sha"]}
    return result


def parse_location(value):
    match = re.fullmatch(r"(.+):(\d+)(?:-(\d+))?", value)
    require(match is not None, f"invalid evidence location: {value}")
    start = int(match.group(2))
    end = int(match.group(3) or match.group(2))
    require(1 <= start <= end, f"invalid evidence line span: {value}")
    return match.group(1), start, end


def validate_matrices(package, clone):
    controlled = json.loads((package / "inputs/cfs-v7.0.1-gitlinks.json").read_text(encoding="utf-8"))
    components = component_map(clone, controlled)
    summary = json.loads((package / "evidence-matrices/evidence-matrix-summary.json").read_text(encoding="utf-8"))
    dep_artifact = package / "evidence-matrices/dependency-evidence.csv.gz"
    lic_artifact = package / "evidence-matrices/license-evidence.csv.gz"
    require(sha256(dep_artifact) == summary["dependencies"]["artifact_sha256"], "dependency artifact hash differs")
    require(sha256(lic_artifact) == summary["licenses"]["artifact_sha256"], "license artifact hash differs")
    dependencies = read_csv(dep_artifact, compressed=True)
    licenses = read_csv(lic_artifact, compressed=True)
    require(len(dependencies) == summary["dependencies"]["rows"], "dependency row count differs")
    require(len(licenses) == summary["licenses"]["rows"], "license row count differs")
    require(sum(row["verification_state"] == "VERIFIED_PINNED" for row in dependencies) == 25, "verified Gitlink count differs")
    require(all(row["package_conclusion"] == "NOASSERTION" for row in licenses), "unsupported package license conclusion")
    require(len({tuple(row.items()) for row in dependencies}) == len(dependencies), "duplicate dependency row")
    require(len({tuple(row.items()) for row in licenses}) == len(licenses), "duplicate license row")
    cache = {}
    for row in dependencies:
        require(row["component"] in components, f"unknown dependency component: {row['component']}")
        path, start, end = parse_location(row["evidence_location"])
        key = (row["component"], path)
        if key not in cache:
            source = components[row["component"]]
            cache[key] = git(source["repo"], "show", f"{source['commit']}:{path}").splitlines()
        require(end <= len(cache[key]), f"dependency evidence lines missing: {row['evidence_location']}")
    for row in licenses:
        require(row["component"] in components, f"unknown license component: {row['component']}")
        path = row["evidence_path"]
        key = (row["component"], path)
        if key not in cache:
            source = components[row["component"]]
            cache[key] = git(source["repo"], "show", f"{source['commit']}:{path}").splitlines()
        span = row["line_span"].split("-")
        require(int(span[-1]) <= len(cache[key]), f"license evidence lines missing: {path}")
    print(f"PASS evidence matrices dependencies={len(dependencies)} licenses={len(licenses)} evidence_files={len(cache)}")


def validate_status_documents(package):
    findings = read_csv(package / "security/vulnerability-findings.csv")
    require(findings and all(row["status"] == "POTENTIALLY_RELEVANT" for row in findings), "vulnerability status overstated")
    report = (package / "security/vulnerability-research.md").read_text(encoding="utf-8")
    require("Status: `CONFIRMED_AFFECTED`" not in report, "confirmed affected status found")
    require("no vulnerabilities found" in report.lower(), "missing explicit forbidden-clearance phrase")
    queries = read_csv(package / "security/query-log.csv")
    require(len(queries) >= 7, "query log is incomplete")
    standards = read_csv(package / "standards/standards-mapping.csv")
    allowed = {"PASS", "PARTIAL", "UNKNOWN", "NOT_APPLICABLE", "NOT_EVALUATED"}
    require(all(row["status"] in allowed for row in standards), "invalid standards status")
    require(any(row["element"] == "Supplier Name" and row["status"] == "PARTIAL" for row in standards), "supplier gap missing")
    require(not (package / "standards/bom.json").exists(), "unvalidated CycloneDX BOM present")
    print(f"PASS status documents vulnerability_rows={len(findings)} queries={len(queries)} standards_rows={len(standards)}")


def validate_package_security(package):
    private_patterns = [b"/" + b"home/", b"/" + b"Users/", b"C:" + b"\\Users\\"]
    secret_patterns = [
        re.compile(rb"AKIA[0-9A-Z]{16}"), re.compile(rb"ghp_[A-Za-z0-9]{36}"),
        re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    files = []
    for path in sorted(package.rglob("*")):
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"symlink in package: {path}")
        require(path.name != ".git", f"Git metadata in package: {path}")
        if not path.is_file():
            continue
        require(info.st_size <= 50_000_000, f"unexpectedly large file: {path}")
        files.append(path)
        if info.st_size > 2_000_000 or path.suffix == ".gz":
            continue
        data = path.read_bytes()
        require(not any(pattern in data for pattern in private_patterns), f"private path in package: {path}")
        require(not any(pattern.search(data) for pattern in secret_patterns), f"secret-like pattern in package: {path}")
    require(files, "empty package")
    print(f"PASS package security files={len(files)} symlinks=0 git_metadata=0 private_paths=0 secrets=0")
    return files


def validate_manifest(package, files):
    manifest = package / "SHA256SUMS"
    if not manifest.exists():
        print("NOTE SHA256SUMS not present; pre-seal validation")
        return
    records = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, f"bad manifest line: {line}")
        digest, name = match.groups()
        require(name != "SHA256SUMS" and name not in records, f"bad manifest target: {name}")
        records[name] = digest
    actual = {path.relative_to(package).as_posix(): sha256(path) for path in files if path != manifest}
    require(records == actual, "manifest coverage or digest differs")
    print(f"PASS SHA256SUMS files={len(records)} nonrecursive=true")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True, type=Path)
    parser.add_argument("--clone", required=True, type=Path)
    args = parser.parse_args()
    package = args.package.resolve()
    clone = args.clone.resolve()
    require(sha256(package / "inputs/cfs-v7.0.1-gitlinks.json") == "7e4bf8a5e27247d8a04136b490eabd37f897a40b19aac3d41f5e14a787e0e7ff", "controlled table hash differs")
    validate_crosswalk(package)
    validate_inventory(package)
    validate_matrices(package, clone)
    validate_status_documents(package)
    files = validate_package_security(package)
    validate_manifest(package, files)
    print("PASS ENRICHMENT_V02_LOCAL_VALIDATION")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        raise SystemExit(f"FAIL {error}")

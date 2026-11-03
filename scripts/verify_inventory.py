#!/usr/bin/env python3
"""Verify the controlled gitlink table against the SBOM and, optionally, a clone."""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cfs-v7.0.1-gitlinks.json"
SBOM = ROOT / "sbom" / "cfs-v7.0.1.spdx.json"
OFFICIAL_ORIGIN = "https://github.com/nasa/cFS.git"
GIT_ENV = {**os.environ, "GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def git(cwd: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "--no-optional-locks", "-C", str(cwd), *args],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=GIT_ENV,
    )
    return result.stdout


def load_controlled() -> tuple[str, dict[str, dict[str, str]]]:
    document = json.loads(DATA.read_text(encoding="utf-8"))
    entries = {entry["path"]: entry for entry in document["entries"]}
    require(len(document["entries"]) == len(entries) == 25, "controlled data must have 25 unique paths")
    require(all(entry["mode"] == "160000" for entry in entries.values()), "invalid controlled mode")
    require(all(entry["type"] == "commit" for entry in entries.values()), "invalid controlled type")
    return document["baseline"], entries


def load_spdx() -> dict[str, dict[str, str]]:
    document = json.loads(SBOM.read_text(encoding="utf-8"))
    packages = {package["SPDXID"]: package for package in document["packages"]}
    result = {}
    for relation in document["relationships"]:
        if relation["relationshipType"] != "CONTAINS":
            continue
        comment = relation.get("comment", "")
        require(comment.startswith("Git submodule path: "), "CONTAINS relationship lacks path")
        path = comment.removeprefix("Git submodule path: ")
        package = packages[relation["relatedSpdxElement"]]
        result[path] = {
            "name": package["name"],
            "sha": package["downloadLocation"].rsplit("@", 1)[-1],
        }
    require(len(result) == 25, "SPDX must contain 25 submodule relationships")
    return result


def tree_gitlinks(clone: Path, baseline: str) -> dict[str, dict[str, str]]:
    result = {}
    for line in git(clone, "ls-tree", "-r", baseline).splitlines():
        metadata, path = line.split("\t", 1)
        mode, object_type, sha = metadata.split()
        if mode == "160000":
            result[path] = {"mode": mode, "type": object_type, "sha": sha}
    return result


def verify_clone(clone: Path, baseline: str, controlled: dict[str, dict[str, str]]) -> None:
    require(clone.is_dir(), f"clone directory does not exist: {clone}")
    require(git(clone, "rev-parse", "HEAD").strip() == baseline, "clone HEAD differs from baseline")
    require(git(clone, "remote", "get-url", "origin").strip() == OFFICIAL_ORIGIN, "clone origin is not official cFS")
    tree = tree_gitlinks(clone, baseline)
    require(set(tree) == set(controlled), "physical tree path set differs from controlled data")
    status = {}
    for line in git(clone, "submodule", "status").splitlines():
        prefix = line[0]
        fields = line[1:].split()
        status[fields[1]] = {"prefix": prefix, "sha": fields[0]}
    require(set(status) == set(controlled), "submodule status path set differs")
    for path in sorted(controlled):
        expected = controlled[path]
        require(tree[path] == {"mode": expected["mode"], "type": expected["type"], "sha": expected["sha"]}, f"tree mismatch: {path}")
        require(status[path] == {"prefix": " ", "sha": expected["sha"]}, f"uninitialized or divergent checkout: {path}")
        checkout = (clone / path).resolve()
        require(checkout.is_relative_to(clone.resolve()), f"checkout escapes clone: {path}")
        require(git(checkout, "rev-parse", "HEAD").strip() == expected["sha"], f"checkout mismatch: {path}")
        require(git(checkout, "cat-file", "-t", expected["sha"]).strip() == "commit", f"object is not commit: {path}")
    print(f"PASS physical-clone origin={OFFICIAL_ORIGIN} baseline={baseline} gitlinks=25 checkouts=25")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--clone", type=Path, help="optional independent nasa/cFS v7.0.1 clone")
    args = parser.parse_args()
    baseline, controlled = load_controlled()
    spdx = load_spdx()
    require(set(controlled) == set(spdx), "controlled and SPDX path sets differ")
    for path in sorted(controlled):
        require(controlled[path]["sha"] == spdx[path]["sha"], f"SPDX revision mismatch: {path}")
        print(f"PASS path={path} sha={controlled[path]['sha']}")
    print(f"PASS controlled-vs-spdx baseline={baseline} gitlinks=25")
    if args.clone:
        verify_clone(args.clone.resolve(), baseline, controlled)
    else:
        print("NOTE physical clone verification not requested; use --clone /path/to/cFS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyError, OSError, ValueError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        sys.exit(1)

#!/usr/bin/env python3
"""Fail-closed structural and mission-specific validation for the SPDX JSON."""

import json
import re
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SBOM = ROOT / "sbom" / "cfs-v7.0.1.spdx.json"
ID_RE = re.compile(r"^SPDXRef-[A-Za-z0-9.-]+$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> int:
    document = json.loads(SBOM.read_text(encoding="utf-8"))
    require(document["spdxVersion"] == "SPDX-2.3", "spdxVersion must be SPDX-2.3")
    require(document["dataLicense"] == "CC0-1.0", "dataLicense must be CC0-1.0")
    require(document["SPDXID"] == "SPDXRef-DOCUMENT", "document SPDXID invalid")
    require(document["documentNamespace"].startswith("https://"), "namespace is not an HTTPS URI")
    datetime.fromisoformat(document["creationInfo"]["created"].replace("Z", "+00:00"))
    require(document["creationInfo"]["creators"], "creationInfo creators missing")

    packages = document["packages"]
    require(len(packages) == 26, f"expected 26 packages, got {len(packages)}")
    ids = [package["SPDXID"] for package in packages]
    require(len(ids) == len(set(ids)), "package SPDXIDs are not unique")
    require(all(ID_RE.fullmatch(identifier) for identifier in ids), "invalid package SPDXID")

    known = set(ids) | {"SPDXRef-DOCUMENT"}
    exact_vcs = 0
    unresolved_vcs = 0
    for package in packages:
        for field in (
            "name",
            "SPDXID",
            "downloadLocation",
            "filesAnalyzed",
            "licenseConcluded",
            "licenseDeclared",
            "copyrightText",
        ):
            require(field in package, f"{package.get('name', '?')}: missing {field}")
        require(package["filesAnalyzed"] is False, f"{package['name']}: filesAnalyzed must be false")
        require("packageVerificationCode" not in package, f"{package['name']}: unexpected verification code")
        if package["name"] != "cFS":
            revision = package["downloadLocation"].rsplit("@", 1)[-1]
            if SHA_RE.fullmatch(revision):
                exact_vcs += 1
            else:
                unresolved_vcs += 1

    relationships = document["relationships"]
    require(len(relationships) == 26, f"expected 26 relationships, got {len(relationships)}")
    for relationship in relationships:
        require(relationship["spdxElementId"] in known, "relationship source is unknown")
        require(relationship["relatedSpdxElement"] in known, "relationship target is unknown")
        require(relationship["relationshipType"] in {"DESCRIBES", "CONTAINS"}, "unexpected relation")

    describes = [r for r in relationships if r["relationshipType"] == "DESCRIBES"]
    contains = [r for r in relationships if r["relationshipType"] == "CONTAINS"]
    require(len(describes) == 1, "expected exactly one DESCRIBES relationship")
    require(describes[0]["relatedSpdxElement"] == "SPDXRef-Package-cFS", "wrong described package")
    require(len(contains) == 25, f"expected 25 CONTAINS relationships, got {len(contains)}")
    require(exact_vcs == 25, f"expected 25 exact component commits, got {exact_vcs}")
    require(unresolved_vcs == 0, f"expected no unresolved component gitlinks, got {unresolved_vcs}")

    sample_lib = next(package for package in packages if package["name"] == "sample_lib")
    sample_revision = sample_lib["downloadLocation"].rsplit("@", 1)[-1]
    require(
        sample_revision == "2d8b7e862673ef90da4355890e18e92822e8acd7",
        f"unexpected libs/sample_lib gitlink: {sample_revision}",
    )

    print("PASS json-parse")
    print("PASS spdx-2.3-required-fields")
    print("PASS spdx-id-uniqueness-and-syntax")
    print("PASS relationship-referential-integrity")
    print("PASS package-count=26 relationship-count=26 contains-count=25")
    print("PASS exact-component-gitlinks=25 unresolved-gitlinks=0")
    print("PASS libs/sample_lib=2d8b7e862673ef90da4355890e18e92822e8acd7")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        sys.exit(1)

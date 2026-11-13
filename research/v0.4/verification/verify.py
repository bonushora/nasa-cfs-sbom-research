#!/usr/bin/env python3
"""Offline verification of published v0.4 metadata."""
import argparse
import hashlib
import json
import pathlib
import re
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent

def req(ok, msg):
    if not ok:
        raise RuntimeError(msg)

def h(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def load(name):
    return json.loads((ROOT / name).read_text())

def main():
    args = argparse.ArgumentParser()
    args.add_argument("--schema", type=pathlib.Path)
    args = args.parse_args()

    # Exact payload coverage, not just listed files.
    manifest = {}

    for line in (
        ROOT / "SHA256SUMS"
    ).read_text().splitlines():
        m = re.fullmatch(
            r"([0-9a-f]{64})  (.+)", line
        )

        req(m is not None, "MANIFEST_FORMAT")

        digest, name = m.groups()
        n = pathlib.Path(name)
        p = ROOT / n

        req(
            name not in manifest
            and not n.is_absolute()
            and ".." not in n.parts
            and p.is_file()
            and not p.is_symlink()
            and p.resolve() == p,
            "MANIFEST_PATH"
        )

        req(h(p) == digest, "HASH:" + name)
        manifest[name] = digest

    actual = set()

    for p in ROOT.rglob("*"):
        req(not p.is_symlink(), "SYMLINK")

        if p.is_file():
            name = str(p.relative_to(ROOT))

            if name != "SHA256SUMS":
                actual.add(name)

    req(actual == set(manifest), "MANIFEST_COVERAGE")

    prov = load("PROVENANCE.json")

    req(
        prov["research_version"] == "v0.4"
        and prov["upstream_commit"]
        == "088b2fa828db9ff7e00733f1908e0eeb59f66ce3",
        "BASELINE"
    )

    for x in prov["derivations"]:
        name = x["public_artifact"]

        req(
            manifest[name] == x["public_sha256"],
            "DERIVATIVE_HASH"
        )

        req(
            re.fullmatch(
                r"[0-9a-f]{64}", x["source_sha256"]
            ) is not None,
            "ORIGINAL_HASH_FORMAT"
        )

        if x["transformation"] == "BYTE_IDENTICAL":
            req(
                x["source_sha256"]
                == x["public_sha256"],
                "BYTE_IDENTICAL"
            )

    docs = sorted(
        (ROOT / "sbom").glob("*.spdx.json")
    )

    req(len(docs) == 7, "DOCUMENT_COUNT")

    namespaces = set()
    index = {}

    for p in docs:
        d = json.loads(p.read_text())

        req(
            d["spdxVersion"] == "SPDX-2.3"
            and d["dataLicense"] == "CC0-1.0",
            "SPDX_FORMAT"
        )

        ns = d["documentNamespace"]
        req(ns not in namespaces, "NAMESPACE")
        namespaces.add(ns)

        elements = (
            d.get("files", [])
            + d.get("packages", [])
        )

        ids = [d["SPDXID"]] + [
            x["SPDXID"] for x in elements
        ]

        req(
            len(ids) == len(set(ids)), "DUP_ID"
        )

        known = set(ids)

        for x in d["relationships"]:
            req(
                x["spdxElementId"] in known
                and x["relatedSpdxElement"] in known,
                "REFERENCE"
            )

        for x in d.get("files", []):
            hashes = {
                c["algorithm"]: c["checksumValue"]
                for c in x["checksums"]
            }

            req(
                re.fullmatch(
                    r"[0-9a-f]{40}", hashes["SHA1"]
                ) is not None
                and re.fullmatch(
                    r"[0-9a-f]{64}", hashes["SHA256"]
                ) is not None,
                "FILE_HASH_FORMAT"
            )

        index[p.name] = d

    def doc(tag):
        return index["native-eds-" + tag + ".spdx.json"]

    counts = {
        "build-toolchain": (7, 10, 17),
        "compiled-artifacts": (0, 565, 565),
        "dynamic-dependencies": (0, 483, 483),
        "generated-artifacts": (0, 545, 545),
        "link-commands": (0, 333, 333),
        "source-composition": (22, 1192, 1214)
    }

    for tag, expected in counts.items():
        d = doc(tag)

        req(
            (
                len(d.get("packages", [])),
                len(d.get("files", [])),
                len(d["relationships"])
            ) == expected,
            "DOC_COUNT:" + tag
        )

        req(
            all(
                x["relationshipType"] == "DESCRIBES"
                for x in d["relationships"]
            ),
            "ORIGINAL_RELATIONS"
        )

    def filehash(x):
        return next(
            c["checksumValue"] for c in x["checksums"]
            if c["algorithm"] == "SHA256"
        )

    def fmap(d):
        return {
            x["fileName"]: filehash(x)
            for x in d["files"]
        }

    installed = load("evidence/ELF-INSTALL.json")
    build = load("evidence/ELF-BUILD.json")

    req(
        len(installed) == 483 and len(build) == 2071,
        "ELF_COUNTS"
    )

    expected = Counter()
    elf_hashes = {}

    for scope, rows in [
        ("install", installed), ("build", build)
    ]:
        for x in rows:
            name = scope + "/" + x["path"]
            req(name not in elf_hashes, "ELF_PATH_DUP")
            elf_hashes[name] = x["sha256"]

            for n in x["needed"]:
                expected[(name, n)] += 1

    req(sum(expected.values()) == 840, "ELF_EDGES")

    expected_installed = {
        "install/" + x["path"]: x["sha256"]
        for x in installed
    }

    req(
        fmap(doc("dynamic-dependencies"))
        == expected_installed,
        "DYNAMIC_ELF_RECONCILIATION"
    )

    compiled = fmap(doc("compiled-artifacts"))

    for name, digest in expected_installed.items():
        req(
            compiled[name] == digest,
            "COMPILED_ELF_RECONCILIATION"
        )

    s = doc("semantic-dependencies")

    fn = {
        x["SPDXID"]: x["fileName"]
        for x in s["files"]
    }

    pn = {
        x["SPDXID"]: x["name"]
        for x in s["packages"]
    }

    sf = fmap(s)

    actual_edges = Counter()
    physical = []

    for rel in s["relationships"]:
        if rel["relationshipType"] == "DEPENDS_ON":
            a = fn[rel["spdxElementId"]]
            b = rel["relatedSpdxElement"]

            if b in pn:
                actual_edges[(a, pn[b])] += 1
            else:
                physical.append((a, fn[b]))

    req(actual_edges == expected, "GRAPH_EDGES")
    req(len(physical) == 1, "PHYSICAL_EDGE_COUNT")

    for name, dep in expected:
        req(
            sf[name] == elf_hashes[name],
            "GRAPH_ELF_HASH"
        )

    evidence = load("evidence/DEPENDENCY-EVIDENCE.json")

    req(len(evidence) == 841, "EVIDENCE_COUNT")

    req(
        Counter(
            (x["file"], x["needed"])
            for x in evidence
            if x["kind"] == "DECLARED_DIRECT"
        ) == expected,
        "EDGE_EVIDENCE"
    )

    for x in evidence:
        req(
            x["file_sha256"] == elf_hashes[x["file"]],
            "EDGE_FILE_HASH"
        )

    obs = [
        x for x in evidence
        if x["kind"] == "PHYSICAL_PROVIDER_OBSERVED"
    ]

    req(
        len(obs) == 1
        and (obs[0]["file"], obs[0]["provider"])
            == physical[0],
        "PROVIDER_EVIDENCE"
    )

    lua = load(
        "evidence/LUA-SEDSTOOL-PROVENANCE.json"
    )

    req(
        obs[0]["file"] == "build/tools/eds/tool/sedstool"
        and obs[0]["file_sha256"]
            == lua["sedstool_sha256"]
        and obs[0]["provider_sha256"]
            == lua["runtime_sha256"]
        and sf[obs[0]["provider"]]
            == lua["runtime_sha256"]
        and obs[0]["observed_runs"] == 2
        and len(lua["observed_runs"]) == 2
        and all(
            x["local_lua_open"]
            and not x["other_lua_opens"]
            for x in lua["observed_runs"]
        ),
        "LUA_PROVIDER"
    )

    req(
        len(lua["packages"]) == 3
        and len(lua["headers"]) == 5,
        "LUA_COUNTS"
    )

    candidates = load(
        "evidence/EDS-CANDIDATE-CLASSIFICATION.json"
    )

    req(
        len(candidates) == 545
        and {
            "build/" + x["path"]: x["sha256"]
            for x in candidates
        } == fmap(doc("generated-artifacts")),
        "CANDIDATE_RECONCILIATION"
    )

    c = load(
        "evidence/STD-EDS-COMPARISON.json"
    )

    fd = c["file_delta"]

    req(
        len(fd["added"]) == 54
        and len(fd["removed"]) == 35
        and len(fd["common_changed"]) == 509
        and len(fd["common_identical"]) == 2
        and fd["std_installed"] == 546
        and fd["eds_installed"] == 565,
        "STD_EDS_DELTA"
    )

    req(
        dict(Counter(
            n for x in installed for n in x["needed"]
        )) == c["installed_needed"]
        and dict(Counter(
            n for x in build for n in x["needed"]
        )) == c["build_needed"],
        "DEPENDENCY_TOTALS"
    )

    t = load(
        "evidence/EDSLIB-CTEST-STATIC-RESOLUTION.json"
    )

    affected = [
        x for x in installed
        if t["needed"] in x["needed"]
    ]

    req(
        len(affected) == 12
        and len({x["sha256"] for x in affected}) == 6,
        "AFFECTED_ELF"
    )

    req(
        {
            (x["path"], x["sha256"])
            for x in affected
        } == {
            (x["path"], x["sha256"])
            for x in t["installed_paths"]
        },
        "FINDING_ELF"
    )

    req(
        len(t["tests"]) == 6
        and t["resolution_counts"] == {"STATIC_MATCH":6}
        and all(
            x["resolution"] == "STATIC_MATCH"
            and x["matches_installed_identity"]
            for x in t["tests"]
        )
        and t["runtime_resolution"] == "NOT_VERIFIED"
        and t["vulnerability"] == "NOT_ESTABLISHED",
        "CTEST_SCOPE"
    )

    lib_hashes = {
        x["sha256"] for x in t["library_candidates"]
    }

    req(
        len(t["library_candidates"]) == 2
        and len(lib_hashes) == 1
        and all(
            x["candidate_sha256"] in lib_hashes
            for x in t["tests"]
        ),
        "CTEST_LIBRARY"
    )

    target_hashes = {
        (pathlib.Path(x["path"]).name, x["sha256"])
        for x in affected
    }

    req(
        {
            (x["target"], x["command_sha256"])
            for x in t["tests"]
        } == target_hashes,
        "CTEST_COMMAND_IDENTITY"
    )

    schema_state = "NOT_REQUESTED"

    if args.schema:
        req(
            h(args.schema) == prov["schema_sha256"],
            "SCHEMA_HASH"
        )

        import jsonschema

        schema = json.loads(args.schema.read_text())

        V = jsonschema.validators.validator_for(schema)
        V.check_schema(schema)

        for d in index.values():
            V(schema).validate(d)

        schema_state = "PASS"

    print("PUBLIC_MANIFEST=PASS")
    print("PUBLIC_SPDX_DOCUMENTS=7/7")
    print("DECLARED_DEPENDENCY_EDGES=840")
    print("OBSERVED_PROVIDER_EDGES=1")
    print("CTEST_STATIC_MATCH=6/6")
    print("OPTIONAL_SCHEMA=" + schema_state)
    print("PUBLIC_METADATA_VERIFICATION=PASS")
    print("ORIGINAL_BINARY_REPRODUCTION=NOT_PERFORMED")
    print("RUNTIME_RESOLUTION=NOT_VERIFIED")

if __name__ == "__main__":
    main()

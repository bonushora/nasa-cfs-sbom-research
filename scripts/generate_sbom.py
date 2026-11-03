#!/usr/bin/env python3
"""Generate the experimental cFS v7.0.1 source-bundle SPDX document."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "sbom" / "cfs-v7.0.1.spdx.json"
CREATED = "2026-11-03T10:48:05Z"


COMPONENTS = [
    # path, repository, git commit/tag, recovered exact gitlink, asserted product version
    ("cfe", "cFE", "c5fb2b4d540bd55eb6c3707da7dd13eee679d4dd", True, "7.0.1"),
    ("osal", "osal", "d2d877a69cff47452bcca274b309147d48e6c16f", True, "7.0.1"),
    ("psp", "PSP", "c4b3b0b65b119e106481ad8e20976ae4d7f554e3", True, "7.0.1"),
    ("apps/ci_lab", "ci_lab", "f5d36625336249312ee9d5815bc875e231815bb4", True, "git:f5d36625336249312ee9d5815bc875e231815bb4"),
    ("apps/to_lab", "to_lab", "38f7312ec4c1109b8f1c0738730b6e5ac5860f05", True, "git:38f7312ec4c1109b8f1c0738730b6e5ac5860f05"),
    ("apps/sch_lab", "sch_lab", "bc848cd8a6c0407023b959191e8aa39a01928444", True, "git:bc848cd8a6c0407023b959191e8aa39a01928444"),
    ("apps/sample_app", "sample_app", "2f93d1a4159a02b18d67ee83342c9e96b90e23e4", True, "git:2f93d1a4159a02b18d67ee83342c9e96b90e23e4"),
    ("libs/sample_lib", "sample_lib", "2d8b7e862673ef90da4355890e18e92822e8acd7", True, "7.0.1"),
    ("tools/cFS-GroundSystem", "cFS-GroundSystem", "07a33a81fe7a88d248d9a5dc59bcf433e34594d7", True, "git:07a33a81fe7a88d248d9a5dc59bcf433e34594d7"),
    ("tools/elf2cfetbl", "elf2cfetbl", "118b55fe1d128b48dc45fd36278b87827c6d3faa", True, "git:118b55fe1d128b48dc45fd36278b87827c6d3faa"),
    ("tools/tblCRCTool", "tblCRCTool", "cc61e89535db9fabe35fe26d1a600889f06b3104", True, "git:cc61e89535db9fabe35fe26d1a600889f06b3104"),
    ("tools/eds", "EdsLib", "2acc963b34f77692c6396555dcfb10ef43eb1046", True, "git:2acc963b34f77692c6396555dcfb10ef43eb1046"),
    ("apps/cf", "CF", "15a871e66cad7ec75e1be78989a93075ff142055", True, "git:15a871e66cad7ec75e1be78989a93075ff142055"),
    ("apps/cs", "CS", "8510c5c0bd3e3b777086ad4b48aee3e79875553a", True, "git:8510c5c0bd3e3b777086ad4b48aee3e79875553a"),
    ("apps/ds", "DS", "c31e982eca47739dfcf31d4b40cad6068423e6a2", True, "git:c31e982eca47739dfcf31d4b40cad6068423e6a2"),
    ("apps/fm", "FM", "ed51c5733c0f2d2f521d72f80d1b9254d2c8b5d0", True, "git:ed51c5733c0f2d2f521d72f80d1b9254d2c8b5d0"),
    ("apps/hk", "HK", "766dab1591b95ff89d99baaab9b43d234de4e699", True, "git:766dab1591b95ff89d99baaab9b43d234de4e699"),
    ("apps/hs", "HS", "947b903174bca0878210e7fbc53104cff8e7b335", True, "git:947b903174bca0878210e7fbc53104cff8e7b335"),
    ("apps/lc", "LC", "a1c3a47ea1fa5c0d7751d6ff88848dc9bd8a6c7a", True, "git:a1c3a47ea1fa5c0d7751d6ff88848dc9bd8a6c7a"),
    ("apps/md", "MD", "7e027886b22eb9e6492d59700cdc4549b116c698", True, "git:7e027886b22eb9e6492d59700cdc4549b116c698"),
    ("apps/mm", "MM", "f3ee4e678df1fe64b9ee267b7e2a888352e178d5", True, "git:f3ee4e678df1fe64b9ee267b7e2a888352e178d5"),
    ("apps/sbn", "SBN", "3b7b37572d63c3f8e85b1f0fa95853c1b78dcf96", True, "git:3b7b37572d63c3f8e85b1f0fa95853c1b78dcf96"),
    ("apps/sc", "SC", "76db5f7b0dde4ea22b41d19962564826967bc123", True, "git:76db5f7b0dde4ea22b41d19962564826967bc123"),
    ("tools/cfs-cosmos-plugin", "cfs-cosmos-plugin", "358339d9fbb0516fdf00306cafc6d2cc7f869cd0", True, "git:358339d9fbb0516fdf00306cafc6d2cc7f869cd0"),
    ("tools/commandline-tools", "cfs-commandline-tools", "d70c56ec035694c9a64b317897403266166f5d68", True, "git:d70c56ec035694c9a64b317897403266166f5d68"),
]


def spdx_id(name: str) -> str:
    normalized = "".join(c if c.isalnum() or c in ".-" else "-" for c in name)
    return f"SPDXRef-Package-{normalized}"


def package(path: str, repo: str, revision: str, exact: bool, version: str) -> dict:
    locator = f"git+https://github.com/nasa/{repo}.git@{revision}"
    if exact:
        source = f"Exact gitlink recovered from nasa/cFS tag v7.0.1 at path {path}."
    else:
        source = (
            f"Submodule declared at path {path}; public tag v7.0.1 verified in nasa/{repo}, "
            "but the exact cFS gitlink SHA was not recovered in this network-isolated run."
        )
    return {
        "name": repo,
        "SPDXID": spdx_id(repo),
        "versionInfo": version,
        "downloadLocation": locator,
        "filesAnalyzed": False,
        "licenseConcluded": "NOASSERTION",
        "licenseDeclared": "NOASSERTION",
        "copyrightText": "NOASSERTION",
        "sourceInfo": source,
        "externalRefs": [
            {
                "referenceCategory": "OTHER",
                "referenceType": "vcs",
                "referenceLocator": locator,
            }
        ],
        "comment": (
            "Experimental source-component record. Commit identity is not a package-content checksum. "
            "No file or binary analysis was performed."
        ),
    }


def build_document() -> dict:
    root_id = "SPDXRef-Package-cFS"
    root_package = {
        "name": "cFS",
        "SPDXID": root_id,
        "versionInfo": "7.0.1",
        "supplier": "Organization: National Aeronautics and Space Administration",
        "downloadLocation": "git+https://github.com/nasa/cFS.git@088b2fa828db9ff7e00733f1908e0eeb59f66ce3",
        "filesAnalyzed": False,
        "licenseConcluded": "NOASSERTION",
        "licenseDeclared": "Apache-2.0",
        "copyrightText": "NOASSERTION",
        "sourceInfo": (
            "NASA cFS release tag v7.0.1 resolves to commit "
            "088b2fa828db9ff7e00733f1908e0eeb59f66ce3."
        ),
        "externalRefs": [
            {
                "referenceCategory": "PACKAGE-MANAGER",
                "referenceType": "purl",
                "referenceLocator": "pkg:github/nasa/cFS@v7.0.1",
            },
            {
                "referenceCategory": "OTHER",
                "referenceType": "vcs",
                "referenceLocator": "git+https://github.com/nasa/cFS.git@088b2fa828db9ff7e00733f1908e0eeb59f66ce3",
            },
        ],
        "comment": (
            "Experimental inventory of the source bundle, not an official NASA SBOM and not a binary SBOM. "
            "The release page states Apache-2.0 for the open-source bundle."
        ),
    }

    packages = [root_package]
    relationships = [
        {
            "spdxElementId": "SPDXRef-DOCUMENT",
            "relationshipType": "DESCRIBES",
            "relatedSpdxElement": root_id,
            "comment": "The document describes the experimental cFS v7.0.1 source-bundle inventory.",
        }
    ]
    for component in COMPONENTS:
        pkg = package(*component)
        packages.append(pkg)
        relationships.append(
            {
                "spdxElementId": root_id,
                "relationshipType": "CONTAINS",
                "relatedSpdxElement": pkg["SPDXID"],
                "comment": f"Git submodule path: {component[0]}",
            }
        )

    return {
        "spdxVersion": "SPDX-2.3",
        "dataLicense": "CC0-1.0",
        "SPDXID": "SPDXRef-DOCUMENT",
        "name": "Experimental NASA cFS v7.0.1 source-bundle inventory",
        "documentNamespace": (
            "https://bonushora.example.invalid/spdxdocs/"
            "cfs-v7.0.1-experimental-r2-r1-20261103-088b2fa8"
        ),
        "creationInfo": {
            "created": CREATED,
            "creators": [
                "Tool: nasa-cfs-sbom-research-v0.1/generate_sbom.py",
                "Organization: Bonus Hora research (experimental)",
            ],
            "comment": (
                "Created from public GitHub release, tag, tree, gitlink and repository evidence "
                "consulted on 2026-11-03. No NASA endorsement is claimed."
            ),
        },
        "documentDescribes": [root_id],
        "packages": packages,
        "relationships": relationships,
        "annotations": [
            {
                "annotationDate": CREATED,
                "annotationType": "OTHER",
                "annotator": "Tool: nasa-cfs-sbom-research-v0.1/generate_sbom.py",
                "comment": (
                    "Coverage: 25 declared submodules plus the cFS bundle; all 25 submodule gitlink "
                    "SHAs are recorded. The libs/sample_lib gitlink is "
                    "2d8b7e862673ef90da4355890e18e92822e8acd7. Build-selected files, toolchain, "
                    "OS packages, generated code, dynamic "
                    "loads and final binary contents were not observed."
                ),
            }
        ],
    }


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(build_document(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"generated {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

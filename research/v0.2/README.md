# NASA cFS v7.0.1 SBOM supplemental research v0.2

This is an independent, unofficial research supplement for the source-level SPDX
2.3 inventory of the NASA core Flight System (cFS) v7.0.1 bundle. It is not a NASA
publication and does not imply NASA endorsement, flight qualification, security
certification, or binary/runtime SBOM completeness.

## Fixed identities

- cFS root commit: `088b2fa828db9ff7e00733f1908e0eeb59f66ce3`
- published gitlink table SHA-256:
  `7e4bf8a5e27247d8a04136b490eabd37f897a40b19aac3d41f5e14a787e0e7ff`
- original SPDX SHA-256:
  `10cdb17573d186a59a42de73915e21cd36e3a44a1bf5737a0eebdfe063e8249f`
- official VDD archive SHA-256:
  `ee1fa901a49091274a19dc475564fbf541c36278714b73bf12cd980a4f165aa3`

The original SPDX document is not modified or replaced by this supplement.

## Results

| Dimension | Result | Meaning |
|---|---|---|
| VDD crosswalk | PASS | 25/25 exact component Git SHA matches; 25/25 individual VDDs identify v7.0.1. |
| Git-tree inventory | PASS | 4,341 bounded tree entries across the root and 25 pinned component trees. |
| Dependency evidence | PASS_WITH_LIMITS | 316 declaration rows; only 25 Gitlinks are verified pinned relationships. |
| License evidence | PASS_WITH_LIMITS | 28 evidence rows; package-wide conclusions remain `NOASSERTION`. |
| Vulnerability research | DEFERRED_PARTIAL | Potentially relevant public records exist; no commit-level affectedness conclusion is made. |
| NTIA/SPDX self-assessment | PASS_WITH_GAPS | Field-level mapping records supplier and process gaps; no compliance claim. |
| CycloneDX conversion | DEFERRED | No CycloneDX BOM was emitted without a locally validated schema/toolchain. |

## Contents

- [`vdd/`](vdd/): CSV, JSON, Markdown, and primary-source manifest for the VDD crosswalk.
- [`inventory/`](inventory/): compressed deterministic Git-tree inventory and per-component summary.
- [`evidence-matrices/`](evidence-matrices/): compressed dependency and license evidence.
- [`security/`](security/): narrow, status-accurate vulnerability research and query log.
- [`standards/`](standards/): NTIA/SPDX field mapping and CycloneDX mapping design.
- [`scripts/`](scripts/): deterministic generators and fail-closed validator.
- [`inputs/`](inputs/): controlled 25-gitlink table and immutable input hashes.

## Scope boundary

The inventory enumerates leaf objects in each pinned Git tree. Regular Git blobs,
symlinks, Gitlinks, and checkout-filter behavior are explicitly distinguished.
It does not claim that tracked source equals the composition of a compiled image.
Generated files, toolchains, transitive dependencies, linked binaries, deployment
configuration, and runtime-loaded content are not resolved.

See [`METHODOLOGY.md`](METHODOLOGY.md), [`PROVENANCE.md`](PROVENANCE.md), and
[`REPRODUCING.md`](REPRODUCING.md) before interpreting the artifacts.

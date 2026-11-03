# Methodology

## R3 — VDD reconciliation

The official gzip/TAR identity is checked before member inspection. Absolute and
parent-traversal paths, backslashes, duplicate names, symbolic/hard links,
devices, FIFOs, and unsupported types are rejected. Each extracted file must be
byte-equal to the corresponding TAR stream.

The Section 7 table in `vdd/00-cfs.md` is parsed as exactly 25 unique components
with 40-hex Git SHAs. Component aliases are normalized only for case and
punctuation joining; SHA values are never normalized or shortened. The published
table, Section 7, and 25 individual VDDs must have equal component sets.

## R4 — bounded Git-tree inventory

Selection rule: enumerate every recursive leaf entry in the pinned root Git tree
and every recursive leaf entry in each of its 25 pinned component Git trees.
Parent trees do not descend through Gitlinks. The resulting key is
`(component_path, repo_relative_path)` and must be unique.

Classes are explicit:

- `TRACKED_REGULAR`: regular/executable blob whose checkout bytes equal the blob;
- `TRACKED_REGULAR_FILTERED_CHECKOUT`: regular blob with a documented clean-tree
  checkout filter difference;
- `TRACKED_SYMLINK`: link target is verified against the Git blob but never
  followed;
- `TRACKED_GITLINK`: commit object recorded without descending in the parent tree;
- `GIT_LFS_POINTER`: pointer bytes recorded, resolved content excluded.

The inventory does not include untracked/generated files or assert binary/runtime
composition. Compressed CSV uses stable row ordering and gzip timestamp zero.

## R5 — declaration and license evidence

Dependency evidence includes 25 verified pinned Gitlinks and syntax extracted
from four CMake commands: `find_package`, `add_subdirectory`,
`target_link_libraries`, and `include`. CMake expressions remain
`DECLARED_UNRESOLVED`; conditional semantics, transitive closure, link results,
and runtime loading are not inferred.

License evidence includes pinned license/notice files and explicit
`SPDX-License-Identifier` lines. Evidence path, commit, line, text hash, and
scope are recorded. All package conclusions remain `NOASSERTION`.

## R6 and R7

Vulnerability research is a bounded documentary query, not active testing.
Version-level public records are not promoted to commit-level affectedness without
explicit mapping. Standards mapping uses the NTIA 2021 Minimum Elements report
and SPDX 2.3/2.3.1 text. It is a self-assessment, not a regulatory compliance
attestation. CycloneDX conversion is deferred unless an exact official schema and
validated toolchain are locally available.

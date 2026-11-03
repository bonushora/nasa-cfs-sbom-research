# Dependency and license evidence matrices

`dependency-evidence.csv.gz` contains 316 evidence rows:

- 25 pinned Gitlinks with `VERIFIED_PINNED` status;
- 291 unevaluated CMake declarations from 355 pinned build files;
- 46 `include`, 2 `find_package`, 121 `add_subdirectory`, and 122
  `target_link_libraries` expressions.

The CMake rows prove that the declaration text exists at the pinned commit. They
do not prove that a condition evaluates true, a target resolves, a linker selects
the dependency, or a runtime loads it.

`license-evidence.csv.gz` contains 28 rows from 26 license/notice files and two
explicit file-level `MIT-0` SPDX identifiers. Every package-level conclusion is
`NOASSERTION`; evidence is not promoted to ownership, compatibility, or
package-wide license conclusions.

Both compressed CSV files use deterministic gzip timestamp zero and stable row
ordering. `evidence-matrix-summary.json` records the exact counts and hashes.

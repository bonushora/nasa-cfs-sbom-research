# Methodology and evidence boundaries

## Method summary

This research inventories the top-level source bundle and its Git-linked
components at one immutable upstream revision. It combines direct Git-tree
observation, a controlled 25-entry gitlink table, an SPDX 2.3 representation, and
deterministic local validation. The method is intentionally source-level and does
not infer build or runtime behavior from repository structure.

## Reference object

The unit of inventory is the public NASA cFS `v7.0.1` source bundle, not an
executable or operational mission image. The release tag resolves to:

```text
088b2fa828db9ff7e00733f1908e0eeb59f66ce3
```

The published research package is anchored independently at commit:

```text
1beb2f48fd0aea86bd817cc3829f0d35026445c2
```

These commits identify different objects: the first is the upstream NASA cFS
baseline; the second is the published independent research package.

## Evidence collection

The cFS baseline tree contains 25 entries with Git mode `160000` and object type
`commit`. For each entry, the path, mode, object type, and revision were read from
`git ls-tree` in an independent clone and compared with the initialized local
submodule checkout. The controlled observations are recorded in
`data/cfs-v7.0.1-gitlinks.json`.

The evidence flow is:

1. resolve the cFS `v7.0.1` tag to its immutable commit;
2. enumerate gitlinks directly from the baseline Git tree;
3. compare all 25 paths and revisions with physical submodule checkouts;
4. compare the controlled table with the SPDX packages and relationships;
5. validate the SPDX document structurally and against the included official
   SPDX 2.3 JSON Schema;
6. regenerate the SBOM deterministically and compare its SHA-256 digest.

## SPDX representation

The document contains:

- one package for the cFS bundle;
- 25 packages for declared submodules;
- one `DESCRIBES` relationship;
- 25 `CONTAINS` relationships;
- VCS locators pinned to full Git commit identifiers;
- `filesAnalyzed: false` and no package verification code;
- `NOASSERTION` wherever a licensing or other conclusion was not independently
  established.

No `DEPENDS_ON` relationship is inferred from architecture, directory placement,
or naming. Presence in the source bundle does not establish CMake selection,
static or dynamic linkage, deployment, or runtime loading.

## Validation layers

The package supports four complementary checks:

- `SHA256SUMS` verifies the bytes and inventory of the package;
- `validate_sbom.py` checks project-specific SPDX structure and relationships;
- `validate_spdx_schema.py` validates against the included official schema;
- `verify_inventory.py` compares the controlled table with the SPDX document and,
  when requested, an independent physical cFS clone.

Passing these checks establishes internal consistency and reproducibility within
the stated scope. It does not establish the completeness of a build, binary, or
runtime SBOM.

## Provenance sources

- cFS repository: <https://github.com/nasa/cFS>
- cFS release: <https://github.com/nasa/cFS/releases/tag/v7.0.1>
- baseline tree API: <https://api.github.com/repos/nasa/cFS/git/trees/088b2fa828db9ff7e00733f1908e0eeb59f66ce3?recursive=1>
- official SPDX 2.3 schema: <https://raw.githubusercontent.com/spdx/spdx-spec/v2.3/schemas/spdx-schema.json>
- published independent research: <https://github.com/bonushora/nasa-cfs-sbom-research>

The candidate includes the controlled evidence table and schema needed for
offline validation. It does not include the cFS source clone, Git object database,
internal research history, or raw laboratory logs.

## Coverage boundaries

The work does not establish:

- file-level source composition;
- build dependencies or transitive host packages;
- compiler, toolchain, or operating-system identity;
- generated source or downloaded build inputs;
- binary composition or source-to-binary equivalence;
- runtime-loaded modules, configuration, or behavior;
- the license of a component left as `NOASSERTION`;
- NASA approval, flight readiness, or deployment authorization.

## Interpretation and citation

Results should be interpreted as an inventory of declared Git-linked source
components at a pinned upstream tree. When citing the research, include both the
published research commit and the distinct cFS baseline so that readers can
reconstruct the evidence boundary without conflating the two repositories.

# Methodology and evidence boundaries

## Unit of inventory

The unit is the public cFS `v7.0.1` source bundle, not an executable or operational
mission image. The release tag resolves to:

```text
088b2fa828db9ff7e00733f1908e0eeb59f66ce3
```

The bundle contains 25 Git links. Each path, mode, object type, and revision was
read directly from `git ls-tree` in an independent clone and matched to the local
submodule checkout. The controlled results are in
`data/cfs-v7.0.1-gitlinks.json`.

## SPDX model

The document contains:

- one package for the cFS bundle;
- 25 packages for declared submodules;
- one `DESCRIBES` relationship;
- 25 `CONTAINS` relationships;
- VCS locators pinned to full Git commit identifiers;
- `filesAnalyzed: false` and no package verification code;
- `NOASSERTION` where a conclusion was not established.

No `DEPENDS_ON` relationship is inferred from architecture or naming. Presence in
the source bundle does not establish selection by CMake, static or dynamic linkage,
deployment, or runtime loading.

## Provenance sources

- cFS repository: <https://github.com/nasa/cFS>
- cFS release: <https://github.com/nasa/cFS/releases/tag/v7.0.1>
- baseline tree API: <https://api.github.com/repos/nasa/cFS/git/trees/088b2fa828db9ff7e00733f1908e0eeb59f66ce3?recursive=1>
- official SPDX 2.3 schema: <https://raw.githubusercontent.com/spdx/spdx-spec/v2.3/schemas/spdx-schema.json>

The candidate packages the evidence table and schema required for offline
validation. It does not package the cFS source clone, Git object database, internal
research history, or raw execution logs.

## Coverage limitations

The work does not establish:

- file-level composition;
- build dependencies or transitive host packages;
- compiler, toolchain, or operating-system identity;
- generated source or downloaded build inputs;
- binary composition or source-to-binary equivalence;
- runtime-loaded modules, configuration, or behavior;
- NASA approval, flight readiness, or deployment authorization.

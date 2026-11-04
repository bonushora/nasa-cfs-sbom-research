# Experimental NASA cFS v7.0.1 Source-Level SPDX SBOM

**Languages:** English (scientific reference) | [Português brasileiro — complementary translation](README.pt-BR.md).
**Research v0.2:** [supplemental results, methodology and limitations](research/v0.2/README.md). The v0.1/v0.1.1 material below is preserved as historical documentation.

This repository contains an independent, experimental SPDX 2.3 inventory of the
public NASA Core Flight System (cFS) `v7.0.1` source bundle. It is unofficial and
is not produced, endorsed, certified, or approved by NASA. It is not a
flight-qualification artifact or a binary/runtime SBOM.

## Version and publication status

The published `v0.1` package is available at
<https://github.com/bonushora/nasa-cfs-sbom-research> and is anchored by the
immutable Git commit:

```text
1beb2f48fd0aea86bd817cc3829f0d35026445c2
```

This v0.1.1 editorial update improves the English-language presentation and navigation while preserving the scientific inventory, scripts, schema, dependency pin, and license text from the original published v0.1 package.

## What the inventory describes

The inventory describes the public `nasa/cFS` `v7.0.1` source bundle at commit:

```text
088b2fa828db9ff7e00733f1908e0eeb59f66ce3
```

It records the 25 Git submodule links observed in that Git tree and represents
them as `CONTAINS` relationships in an SPDX 2.3 JSON document. Each component is
pinned to its full Git commit identifier. The inventory makes no inference that a
component was selected for a build, linked into a binary, deployed, or loaded at
runtime.

## Documentation guide

| Document | Purpose |
|---|---|
| [`METHODOLOGY.md`](METHODOLOGY.md) | Evidence model, SPDX representation, and coverage boundaries. |
| [`REPRODUCING.md`](REPRODUCING.md) | Integrity, validation, deterministic regeneration, and optional physical-clone checks. |
| [`ATTRIBUTIONS.md`](ATTRIBUTIONS.md) | Licensing and attribution review for included material. |
| [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) | Upstream sources, licenses, and notices. |
| [`RIGHTS_ATTESTATION.md`](RIGHTS_ATTESTATION.md) | Historical v0.1 factual authority statement by the responsible human. |
| [`PUBLICATION-READINESS.md`](PUBLICATION-READINESS.md) | Historical v0.1 pre-publication qualification record. |

The two historical v0.1 documents retain their original chronology. They are not statements of current publication status.

## Package contents

- `sbom/cfs-v7.0.1.spdx.json` — experimental SPDX 2.3 inventory.
- `data/cfs-v7.0.1-gitlinks.json` — controlled table of 25 Git links.
- `schemas/spdx-schema-v2.3.json` — included official SPDX 2.3 JSON Schema.
- `scripts/generate_sbom.py` — deterministic SBOM generator.
- `scripts/validate_sbom.py` — project-specific structural checks.
- `scripts/validate_spdx_schema.py` — official-schema validation.
- `scripts/verify_inventory.py` — table/SBOM comparison and optional clone check.
- `scripts/check_package.py` — manifest, symlink, path, and secret checks.
- `SHA256SUMS` — non-self-referential package integrity manifest.

## Quick verification

Python 3.10 or newer is recommended. From a package directory that does not
contain Git administrative metadata:

```bash
python3 -m pip install -r requirements.txt
sha256sum -c SHA256SUMS
python3 scripts/validate_sbom.py
python3 scripts/validate_spdx_schema.py
python3 scripts/verify_inventory.py
python3 scripts/check_package.py
```

See [`REPRODUCING.md`](REPRODUCING.md) for deterministic regeneration, guidance
for validating a Git clone through a clean export, and optional verification
against an independent cFS clone.

## Coverage boundaries

- `filesAnalyzed` is `false`; individual source files are not inventoried.
- No build, binary, container image, toolchain, operating-system package,
  generated input, dynamic module, or runtime behavior was observed.
- A Git submodule relationship does not demonstrate inclusion in a selected
  build or executable.
- Component licenses remain `NOASSERTION` unless independently established.
- The work does not establish NASA approval, deployment authorization, or flight
  readiness.

## Citation guidance

For reproducible reference to the published research, cite the repository URL,
the published version (`v0.1`), the research commit
`1beb2f48fd0aea86bd817cc3829f0d35026445c2`, and the NASA cFS baseline
`088b2fa828db9ff7e00733f1908e0eeb59f66ce3`. Cite the SPDX document separately
when the inventory itself is the object of analysis.

For the v0.1.1 editorial update, cite the specific Git commit containing the documentation being referenced.

## Licensing and attribution

Apache License 2.0 applies only to covered original research material for which
the necessary authority exists. Upstream and separately licensed materials retain
their own terms. See [`NOTICE`](NOTICE), [`ATTRIBUTIONS.md`](ATTRIBUTIONS.md),
[`RIGHTS_ATTESTATION.md`](RIGHTS_ATTESTATION.md), and
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

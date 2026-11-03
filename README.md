# Experimental NASA cFS v7.0.1 Source-Level SPDX SBOM

This is an **independent, experimental, unofficial NASA cFS source-level SPDX
SBOM**. It is not produced, endorsed, certified, or approved by NASA. The package
does not represent a flight-qualified system or a binary/runtime SBOM.

The inventory describes the public `nasa/cFS` `v7.0.1` source bundle at commit:

```text
088b2fa828db9ff7e00733f1908e0eeb59f66ce3
```

It records the 25 Git submodule links physically verified from that Git tree and
models them as `CONTAINS` relationships in an SPDX 2.3 JSON document.

## Package contents

- `sbom/cfs-v7.0.1.spdx.json` — experimental SPDX 2.3 inventory.
- `data/cfs-v7.0.1-gitlinks.json` — controlled table of the 25 Git links.
- `scripts/generate_sbom.py` — deterministic SBOM generator.
- `scripts/validate_sbom.py` — mission-specific structural checks.
- `scripts/validate_spdx_schema.py` — official SPDX 2.3 JSON Schema validation.
- `scripts/verify_inventory.py` — table/SBOM comparison and optional physical-clone check.
- `scripts/check_package.py` — package manifest, symlink, path, and secret checks.
- `REPRODUCING.md` — reproduction and validation instructions.
- `METHODOLOGY.md` — evidence model and coverage boundaries.
- `ATTRIBUTIONS.md` — licensing and attribution review.
- `RIGHTS_ATTESTATION.md` — responsible human's factual authority statement.
- `THIRD_PARTY_NOTICES.md` — upstream notices and license provenance.
- `LICENSE` and `NOTICE` — Apache-2.0 framework and scope notice.
- `PUBLICATION-READINESS.md` — pre-publication gate report.
- `SHA256SUMS` — candidate file inventory and integrity manifest.

## Quick verification

Python 3.10 or newer is recommended.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/generate_sbom.py
python3 scripts/validate_sbom.py
python3 scripts/validate_spdx_schema.py
python3 scripts/verify_inventory.py
python3 scripts/check_package.py
```

See `REPRODUCING.md` for independent verification against a separate cFS clone.

## Important limitations

- `filesAnalyzed` is `false`; individual source files were not inventoried.
- No build, binary, container image, toolchain, operating-system package, dynamic
  module, or runtime was observed.
- A Git submodule relationship does not prove inclusion in a selected build or
  binary.
- Component licenses remain `NOASSERTION` unless independently established.

## Publication status

This directory is a local review candidate. Publication is not authorized.
The responsible human has registered a factual licensing-authority attestation for
the covered original and AI-assisted research materials. Apache-2.0 applies only
to covered original material; upstream materials retain their respective terms.
The local readiness assessment passes, but a separate human publication decision
is still required. See `RIGHTS_ATTESTATION.md`, `NOTICE`,
`THIRD_PARTY_NOTICES.md`, and `PUBLICATION-READINESS.md`.

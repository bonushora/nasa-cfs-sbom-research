# NASA cFS SBOM Research v0.4

## Configuration-aware SBOM and dependency evidence

Independent research by **Thales Rangel**  
ORCID: https://orcid.org/0000-0002-0629-9731

This contribution extends the independent v0.3 research
with a second qualified native build of NASA cFS v7.0.1,
with Electronic Data Sheets (EDS) enabled.

Upstream source commit:
`088b2fa828db9ff7e00733f1908e0eeb59f66ce3`.

Previous public research:
https://github.com/bonushora/nasa-cfs-sbom-research/tree/da53788b15c290b5e14afda3332a016aada8f0e0/research/v0.3

## Main contribution

- Seven complementary SPDX 2.3 documents for native EDS.
- Comparison against the previously qualified native STD
  configuration.
- Verified provenance of Lua 5.3.6 Ubuntu Jammy packages
  and observations of sedstool during the build.
- 840 direct ELF dependency declarations and one
  additional relationship to the observed physical
  Lua provider.
- Static reconciliation of six EdsLib CTest registrations.

The six native STD SPDX documents remain in v0.3.
Together, the two research versions provide thirteen
complementary SPDX documents. This is not a claim of
thirteen mutually exclusive inventories.

## Contents

- `sbom/`: SPDX documents.
- `evidence/`: selected machine-readable evidence.
- `verification/verify.py`: offline public verifier.
- `PROVENANCE.md`: experimental and publication lineage.
- `PROVENANCE.json`: input seals and derivation mapping.
- `METHODOLOGY.md`, `RESULTS.md`, `LIMITATIONS.md`:
  scientific interpretation and boundaries.
- `RIGHTS_REVIEW.md`: attribution and rights boundary.
- `SHA256SUMS`: integrity manifest.

## Verification

From the package root:

    sha256sum -c SHA256SUMS
    python3 -B verification/verify.py

For additional JSON Schema validation, supply the
SPDX 2.3 JSON schema identified in PROVENANCE.json:

    python3 -B verification/verify.py --schema /path/to/schema.json

The standard-library verification checks published
metadata and cross-document consistency. The optional
schema check requires an existing jsonschema installation.

Neither mode recreates the original build or independently
verifies binary bytes that are not distributed here.

## Independence and attribution

The research was human-directed and AI-assisted.
The researcher established the scope, authorized
experimental steps and reviewed the evidence.
AI assistance supported implementation, analysis
and preparation of documentation.

This is unofficial, independent research. It is not
a NASA-produced, endorsed, certified or flight-qualified
SBOM. See LIMITATIONS.md before interpreting the results.

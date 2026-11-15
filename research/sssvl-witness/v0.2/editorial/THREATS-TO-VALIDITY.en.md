# Threats to Validity — English Editorial Supplement

## Scope and attribution

Author: Thales Rangel — Independent Researcher.
ORCID: https://orcid.org/0000-0002-0629-9731

Editorial supplement to the published v0.1 research.
Original DOI: 10.5281/zenodo.24230342.

The historical source contains eight threat descriptions in Portuguese and corresponding responses in English. This supplement translates the eight descriptions and retains the existing English responses and residual states.

This is an editorial translation, not a new scientific assessment. No original file or experimental result is modified. All residual limitations remain open.

Prepared with AI assistance under human direction. New editorial licensing has been approved by the author. Human editorial acceptance of E5-C is approved.

Historical sources:

- [Threats to validity](../original-v0.1/research/v0.1/THREATS-TO-VALIDITY.md)
- [Scientific report](../original-v0.1/research/v0.1/SCIENTIFIC-REPORT.md)
- [Portuguese translation](../translations/pt-BR/THREATS-TO-VALIDITY.md)

## T1

Cases designed by the comparator team; pre-registered oracles do not guarantee methodological independence.

Response: Pre-registration mitigates post-hoc adjustment, not shared design bias; independent replication recommended.

Residual: OPEN_LIMITATION

## T2

The inventories and reference share the same build lineage; this is not an independent reproduction of the build.

Response: Freeze reference before mutation; shared build lineage remains a limitation.

Residual: OPEN_LIMITATION

## T3

Deterministic repetitions are not independent statistical samples.

Response: Report distinct cases and paired repetitions separately; no pooled statistical rate.

Residual: OPEN_LIMITATION

## T4

W04 uses synthetic entities and edges; B2-A uses files and direct declarations, not packages or providers.

Response: Distinguish W04 synthetic entities/edges from B2-A file/declaration roles.

Residual: OPEN_LIMITATION

## T5

Formal validity is limited to schema and reference checks; REAL-07 preserves SHA1 and changes the SHA256 claim.

Response: Limit schema claims to Draft7 and implemented reference checks; distinguish false hash claim from changed bytes.

Residual: OPEN_LIMITATION

## T6

Configuration is authenticated by the caller; REAL-08 tests an explicit mismatch, not autonomous discovery.

Response: Report explicit configuration mismatch, not autonomous inference.

Residual: OPEN_LIMITATION

## T7

No real scanner, runtime, vulnerability discovery or operational security has been demonstrated.

Response: No scanner, exploit or runtime safety conclusion; further work requires separate authorization.

Residual: OPEN_LIMITATION

## T8

No qualified OS isolation; Evidence Vault remains pending.

Response: Process separation is not sandbox isolation; vault and MT06 remain blocked/unverified.

Residual: OPEN_LIMITATION


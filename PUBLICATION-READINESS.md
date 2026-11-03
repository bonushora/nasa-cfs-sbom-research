# Publication readiness report

**Candidate:** `NASA-CFS-SBOM-RESEARCH-v0.1`  
**Candidate version:** `v0.1`  
**Review mode:** local pre-publication review  
**Publication authorization:** not granted  
**Decision:** `PUBLICATION_READINESS=PASS`

## Candidate inventory

The candidate contains 19 files including `SHA256SUMS`:

- eight English documentation, attestation, notice, and review files;
- one complete Apache License 2.0 text;
- one pinned Python requirements file;
- one controlled 25-gitlink data file;
- one SPDX 2.3 JSON inventory;
- one vendored official SPDX 2.3 JSON Schema;
- five portable Python scripts;
- one SHA-256 manifest.

It contains no cFS source clone, Git repository metadata, internal historical
snapshots, raw laboratory logs, build output, or binary artifacts.

## Gate results

| Gate | State | Evidence |
|---|---|---|
| R3 evidence integrity | PASS | R3 and historical manifests passed before candidate creation. |
| Provenance | PASS | Baseline, release, 25 Git links, upstream URLs, and verification method documented. |
| Reproducibility | PASS | Regeneration and validators pass from a standalone package copy; optional clone verification is documented. |
| Package integrity | PASS | Every candidate file is inventoried in `SHA256SUMS`. |
| Licensing authority | PASS | The responsible human registered a scoped factual authority attestation for covered original and AI-assisted research material. |
| Third-party attribution | PASS | NASA references, SPDX/CC BY 3.0, SBOM/CC0-1.0, Apache text, and jsonschema/MIT remain separated. |
| Sensitive-information review | PASS | No private paths, email addresses, common secret patterns, or unnecessary local records found. |
| Hidden laboratory dependencies | PASS | Scripts use package-relative paths; no snapshot or author-clone dependency. |
| Symlink containment | PASS | No symlinks are present. |
| Non-affiliation clarity | PASS | README prominently states independent, experimental, unofficial, and not NASA-endorsed. |

## Reproducibility checks

The required local checks are:

```bash
python3 scripts/generate_sbom.py
python3 scripts/validate_sbom.py
python3 scripts/validate_spdx_schema.py
python3 scripts/verify_inventory.py
python3 scripts/check_package.py
sha256sum -c SHA256SUMS
```

The optional physical-clone mode is documented in `REPRODUCING.md` and performs no
remote mutation.

Observed results in this review:

```text
PASS controlled-vs-spdx baseline=088b2fa828db9ff7e00733f1908e0eeb59f66ce3 gitlinks=25
PASS physical-clone origin=https://github.com/nasa/cFS.git baseline=088b2fa828db9ff7e00733f1908e0eeb59f66ce3 gitlinks=25 checkouts=25
PASS official-spdx-2.3-json-schema errors=0
PASS manifest files=18
PASS symlinks=0 git-directories=0
PASS private-paths=0 emails=0 common-secret-patterns=0
PASS isolated-copy-before=10cdb17573d186a59a42de73915e21cd36e3a44a1bf5737a0eebdfe063e8249f after=10cdb17573d186a59a42de73915e21cd36e3a44a1bf5737a0eebdfe063e8249f equal=yes
```

Key content hashes:

```text
10cdb17573d186a59a42de73915e21cd36e3a44a1bf5737a0eebdfe063e8249f  sbom/cfs-v7.0.1.spdx.json
9cf356a5646faf012a9f2ad170847158c4bed4c6ee2ab7c4f8b7dddda4bc500d  schemas/spdx-schema-v2.3.json
7e4bf8a5e27247d8a04136b490eabd37f897a40b19aac3d41f5e14a787e0e7ff  data/cfs-v7.0.1-gitlinks.json
b4b20c37d4db0ee70fcd73b7424032cf0ca6d8111fa792cb9eb236d4a9c505b6  RIGHTS_ATTESTATION.md
```

## Privacy and sensitive-information review

The candidate is checked for:

- absolute home-directory and author-workspace fragments;
- email addresses;
- common cloud, GitHub, Slack, private-key, password, token, secret, and API-key patterns;
- symlinks and `.git` content;
- unlisted or unexpectedly large files.

No positive finding was retained in the package.

## File-by-file rights and provenance matrix

The initial pre-closure candidate had 15 files. The licensing review added
`LICENSE`, `NOTICE`, and `THIRD_PARTY_NOTICES.md`; this rights closure adds
`RIGHTS_ATTESTATION.md`, producing the 19-file final review set.

| Path | Artifact / origin | Rights state | Applicable license | Distribution and attribution | Modification / decision |
|---|---|---|---|---|---|
| `ATTRIBUTIONS.md` | Original/AI-assisted research documentation | VERIFIED | Apache-2.0 for covered original material | Human authority statement registered; upstream terms remain separate | Revised for factual closure; INCLUDE |
| `data/cfs-v7.0.1-gitlinks.json` | Research compilation of public Git facts | VERIFIED | Apache-2.0 for covered compilation | Attribute NASA only as upstream factual source; no exclusive claim over facts | Human selection/review confirmed; INCLUDE |
| `LICENSE` | Official Apache License 2.0 text, copied from verified cFS release clone | VERIFIED | Apache-2.0 license text | Redistributable as complete unmodified text; source recorded | No substantive modification; INCLUDE |
| `METHODOLOGY.md` | Original/AI-assisted research documentation | VERIFIED | Apache-2.0 for covered original material | Human direction, review, and approval confirmed | English public summary; INCLUDE |
| `NOTICE` | Original/AI-assisted scope and non-affiliation notice | VERIFIED | Apache-2.0 for covered original material | Does not assert exclusive ownership | Revised for factual closure; INCLUDE |
| `PUBLICATION-READINESS.md` | Original/AI-assisted review report | VERIFIED | Apache-2.0 for covered original material | Human direction, review, and approval confirmed | Expanded with final tests and matrix; INCLUDE |
| `README.md` | Original/AI-assisted research documentation | VERIFIED | Apache-2.0 for covered original material | NASA non-affiliation remains prominent | Revised rights status; INCLUDE |
| `REPRODUCING.md` | Original/AI-assisted research documentation | VERIFIED | Apache-2.0 for covered original material | Human direction, review, and approval confirmed | Portable English instructions; INCLUDE |
| `requirements.txt` | Dependency declaration | NOT_APPLICABLE | No substantive work asserted | `jsonschema` license recorded separately | Version pin only; INCLUDE |
| `RIGHTS_ATTESTATION.md` | Human-provided factual authority statement | VERIFIED | Apache-2.0 for covered original material | Textual confirmation by Thales Rangel; not a handwritten or cryptographic signature | Registered locally; INCLUDE |
| `sbom/cfs-v7.0.1.spdx.json` | Generated factual inventory | VERIFIED | Declares CC0-1.0 as SPDX data license | NASA is upstream source, not author of this SBOM; no exclusive claim over facts | Human selection/review and distribution authority confirmed; INCLUDE |
| `schemas/spdx-schema-v2.3.json` | SPDX Workgroup schema | VERIFIED | CC BY 3.0 Unported | Attribution and license URI required and present | JSON formatting normalized; INCLUDE |
| `scripts/check_package.py` | Original/AI-assisted research script | VERIFIED | Apache-2.0 for covered original material | Human direction, review, and approval confirmed | Package review script; INCLUDE |
| `scripts/generate_sbom.py` | Original/AI-assisted research script | VERIFIED | Apache-2.0 for covered original material | Human direction, review, and approval confirmed | Package-relative deterministic generator; INCLUDE |
| `scripts/validate_sbom.py` | Original/AI-assisted research script | VERIFIED | Apache-2.0 for covered original material | Human direction, review, and approval confirmed | Package-relative validator; INCLUDE |
| `scripts/validate_spdx_schema.py` | Original/AI-assisted script using `jsonschema` API | VERIFIED | Apache-2.0 for covered original material | `jsonschema` is not vendored; upstream MIT notice retained | Adapted to vendored schema; INCLUDE |
| `scripts/verify_inventory.py` | Original/AI-assisted research script | VERIFIED | Apache-2.0 for covered original material | Human direction, review, and approval confirmed | Portable optional-clone verifier; INCLUDE |
| `THIRD_PARTY_NOTICES.md` | Original/AI-assisted attribution compilation | VERIFIED | Apache-2.0 for covered original compilation | Preserves NASA, SPDX, Apache, and `jsonschema` provenance | Revised for factual closure; INCLUDE |
| `SHA256SUMS` | Mechanically generated hash manifest | NOT_APPLICABLE | No substantive work asserted | No attribution required | Regenerated after closure; INCLUDE |

The 14 formerly CONDITIONAL records are VERIFIED for the limited question of
documented distribution authority, based on the responsible human's factual
attestation and the preserved technical provenance. VERIFIED does not assert
line-by-line human authorship, exclusive ownership of AI-assisted output, or
ownership of public facts or third-party material.

## Limitations

This is a source-bundle inventory. It does not analyze individual files, builds,
binaries, containers, toolchains, operating-system packages, dynamic modules, or
runtime behavior. It is not an official NASA SBOM and does not establish flight
readiness or deployment approval.

## Decision boundary

The mandatory local pre-publication gates pass. The candidate is
`READY_FOR_HUMAN_PUBLICATION_DECISION`, but this status does not authorize a
repository, push, release, publication, contact with third parties, NASA
endorsement, operational deployment, or flight qualification. Any content change
requires renewed rights, integrity, and reproducibility review.

# Research v0.4 — Release candidate

## Configuration-aware SBOM and dependency evidence

Author: Thales Rangel

ORCID: https://orcid.org/0000-0002-0629-9731

This release candidate preserves all 22 payload files
of the MT36 public preparation package byte for byte.

Four additional files record the final rights grant,
license scope, license text and release status.

RIGHTS_REVIEW.md and PROVENANCE.json are retained as
historical preparation-stage records. Their pending
rights-review fields describe MT36, not the subsequent
bounded authorization recorded in RIGHTS_ATTESTATION.md.

The scientific conclusions are unchanged:

- Seven complementary native EDS SPDX 2.3 documents.
- 840 directly declared ELF dependency relationships.
- One additional observed physical Lua provider edge.
- Six static matches for the examined EdsLib CTest
  registrations.

This package is an independent research candidate.
It does not establish operational execution,
transitive dependency closure, a complete vulnerability
inventory or flight qualification.

Publication is a distinct action requiring separate
human authorization.

The integrity manifest covers all release payloads.
It is not a digital signature.

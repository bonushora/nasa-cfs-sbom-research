# Licensing and attribution review

This file records the licensing status of material included in this candidate. It
is not legal advice.

## NASA cFS

The package references NASA cFS repository names, public URLs, tags, and commit
identifiers. It does **not** redistribute the cFS source tree. The cFS `v7.0.1`
bundle declares Apache License 2.0:

- <https://github.com/nasa/cFS/blob/v7.0.1/LICENSE>

Component packages remain `NOASSERTION` in the experimental SBOM unless their
license was independently established. The bundle license is not automatically
propagated to every submodule.

NASA names are used only to identify the upstream public software and evidence.
No NASA logo is included. No affiliation, endorsement, certification, or official
SBOM status is claimed.

## SPDX document

`sbom/cfs-v7.0.1.spdx.json` declares `dataLicense: CC0-1.0`, as required for the
SPDX document data.

## SPDX 2.3 JSON Schema

`schemas/spdx-schema-v2.3.json` is derived from the official `spdx/spdx-spec`
`v2.3` schema. The upstream specification repository is licensed under Creative
Commons Attribution 3.0 Unported:

- source: <https://github.com/spdx/spdx-spec/blob/v2.3/schemas/spdx-schema.json>
- license: <https://github.com/spdx/spdx-spec/blob/v2.3/LICENSE>

Attribution: SPDX Workgroup, “SPDX 2.3 JSON Schema.” The local copy was parsed and
re-serialized with normalized JSON formatting; its semantics were not intentionally
changed. The license URI above is provided with the copy.

## Original research scripts and documentation

The responsible human, Thales Rangel, registered the factual statement in
`RIGHTS_ATTESTATION.md` as independent project maintainer and research coordinator.
It confirms sole human direction, selection, review, and approval of the original
research materials with AI assistance; lack of known contractual assignment or
additional substantive third-party contribution; and approval of Apache License
2.0 only where the necessary licensing authority exists.

The complete license text is included in `LICENSE`, with scope clarification in
`NOTICE`. The attestation is the documentary basis for distribution authority; it
does not claim line-by-line human authorship, exclusive rights over AI-assisted
content, or authority over upstream material. Any changed material requires a new
rights and integrity review.

See `THIRD_PARTY_NOTICES.md` for the SPDX schema, `jsonschema`, NASA references,
and other separately licensed material.

# Licensing and attribution

This document identifies the licensing and attribution status of material in the
research package. It is informational and is not legal advice.

## NASA cFS references

The package references NASA cFS repository names, public URLs, tags, and commit
identifiers. It does not redistribute the cFS source tree. The cFS `v7.0.1`
bundle declares the Apache License, Version 2.0:

- source: <https://github.com/nasa/cFS>
- license: <https://github.com/nasa/cFS/blob/v7.0.1/LICENSE>

Licensing information for the top-level bundle is not automatically attributed
to every Git-linked component. Component packages remain `NOASSERTION` in the
experimental SBOM unless their licensing was independently established.

NASA names are used solely to identify the upstream public software and evidence.
The package includes no NASA logo and claims no affiliation, endorsement,
certification, approval, or official SBOM status.

## SPDX document data

`sbom/cfs-v7.0.1.spdx.json` declares `dataLicense: CC0-1.0`, as required for SPDX
document data. The SBOM is an independent research artifact, not a NASA-authored
or NASA-approved SBOM.

## SPDX 2.3 JSON Schema

`schemas/spdx-schema-v2.3.json` is derived from the official `spdx/spdx-spec`
`v2.3` schema. The upstream specification repository is licensed under Creative
Commons Attribution 3.0 Unported:

- source: <https://github.com/spdx/spdx-spec/blob/v2.3/schemas/spdx-schema.json>
- license: <https://github.com/spdx/spdx-spec/blob/v2.3/LICENSE>
- attribution: SPDX Workgroup, “SPDX 2.3 JSON Schema”

The local copy was parsed and re-serialized with normalized JSON formatting. Its
semantics were not intentionally changed.

## Original research material

The responsible human, Thales Rangel, registered the factual statement in
`RIGHTS_ATTESTATION.md` in the capacity of independent project maintainer and
research coordinator. The statement records human direction, selection, review,
and approval of original research material developed with AI assistance. It also
records the absence of known contractual assignment or additional substantive
third-party contribution and approves Apache-2.0 only where the necessary
licensing authority exists.

The complete Apache-2.0 text is included in `LICENSE`, and `NOTICE` clarifies its
scope. The attestation does not claim line-by-line human authorship, exclusive
rights over AI-assisted content, or authority over upstream material. It is a historical v0.1 record and does not replace the review of editorial changes introduced in v0.1.1.

Any changed material requires a corresponding rights and integrity review. See
`THIRD_PARTY_NOTICES.md` for NASA, SPDX, `jsonschema`, Apache, and other upstream
provenance.

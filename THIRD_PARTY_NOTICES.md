# Third-party notices

## NASA cFS references

The package references public NASA cFS names, URLs, release identifiers, and Git
commit identifiers. It does not redistribute the cFS source tree. The upstream
cFS `v7.0.1` bundle declares the Apache License, Version 2.0:

- source: <https://github.com/nasa/cFS>
- license: <https://github.com/nasa/cFS/blob/v7.0.1/LICENSE>

NASA names are used only for factual identification. No affiliation, endorsement,
certification, approval, or official SBOM status is claimed.

## SPDX 2.3 JSON Schema

`schemas/spdx-schema-v2.3.json` is derived from the SPDX Workgroup's official
SPDX 2.3 schema and is included under Creative Commons Attribution 3.0 Unported.

- source: <https://github.com/spdx/spdx-spec/blob/v2.3/schemas/spdx-schema.json>
- license: <https://github.com/spdx/spdx-spec/blob/v2.3/LICENSE>
- attribution: SPDX Workgroup, “SPDX 2.3 JSON Schema”

The local copy was parsed and re-serialized using normalized JSON formatting. No
semantic change was intentionally made.

## SPDX document data

`sbom/cfs-v7.0.1.spdx.json` declares `dataLicense: CC0-1.0`.

## `jsonschema` dependency

The package does not vendor the `jsonschema` Python library. Validation was tested
with `jsonschema==3.2.0`, as declared in `requirements.txt`. That upstream release
is available under the MIT License and identifies Julian Berman as copyright
holder:

- source and license: <https://github.com/python-jsonschema/jsonschema/blob/v3.2.0/COPYING>

Users install this dependency separately; it is not included in the package.

## Apache License text

`LICENSE` contains the complete, unmodified Apache License, Version 2.0, January
2004 text. The copy was taken from the verified cFS `v7.0.1` clone and compared
with the system common-license copy; the two copies differed only by one initial
blank line.

- authoritative text: <https://www.apache.org/licenses/LICENSE-2.0.txt>

Including the license text does not establish ownership of, or licensing
authority over, every original research contribution. The limited factual
authority statement in `RIGHTS_ATTESTATION.md` applies only to covered original
material and does not relicense any third-party material identified here.

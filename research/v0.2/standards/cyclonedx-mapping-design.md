# CycloneDX interoperability design — conversion deferred

Status: `DEFERRED`; no CycloneDX BOM is included.

The authoritative CycloneDX site identified version 1.7 and the JSON schema URL
`https://cyclonedx.org/schema/bom-1.7.schema.json`. The exact schema and a trusted
validated conversion tool were not available locally, and shell DNS access was
blocked. Emitting an unvalidated `bom.json` would create false interoperability
evidence.

## Prospective mapping

| SPDX 2.3 / supplement | CycloneDX design target | Constraint |
|---|---|---|
| Document creation info | `metadata` | Preserve independent-research authorship and timestamp. |
| 26 packages | `components` | Choose component types only with evidence; do not invent supplier. |
| VCS external references | component external references / properties | Preserve full immutable Git SHA. |
| 25 `CONTAINS` relationships | dependency graph or composition | Do not reinterpret containment as build/runtime dependency. |
| License `NOASSERTION` | omitted/unknown license evidence | Do not promote evidence files to package conclusions. |
| File inventory supplement | properties or external artifact | Avoid turning every tracked file into a binary component. |
| Potential vulnerability rows | separate research references | Do not emit CycloneDX vulnerability assertions without commit-level proof. |

Future conversion requires acquisition and SHA-256 recording of the exact 1.7
schema, a documented conversion algorithm, schema validation with zero errors,
round-trip field-loss analysis, and independent comparison to the original SPDX.

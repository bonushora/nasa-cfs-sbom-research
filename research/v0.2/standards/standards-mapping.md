# SPDX and minimum-elements self-assessment

This is a field-level self-assessment, not a declaration of regulatory compliance.

## Authoritative references

- U.S. Department of Commerce / NTIA, *The Minimum Elements for a Software Bill
  of Materials (SBOM)*, July 12, 2021:
  `https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom`
- SPDX Specification 2.3.1, a maintenance release of 2.3 with no added or removed
  fields: `https://spdx.github.io/spdx-spec/v2.3/`
- SPDX Annex L mapping of 2021 NTIA elements:
  `https://spdx.github.io/spdx-spec/v2.3.1/regulations-compliance/`

The original artifact declares `SPDX-2.3` and validates against its included
official JSON schema.

## NTIA 2021 data fields

| Minimum field | Actual evidence | Status | Interpretation |
|---|---|---|---|
| Supplier Name | `supplier` present for 1/26 packages | `PARTIAL` | The 25 component suppliers are absent; no inference is made from repository ownership. |
| Component Name | `name` present for 26/26 | `PASS` | Unique names are present. |
| Version of Component | `versionInfo` present for 26/26 | `PASS` | Five semantic `7.0.1` labels and 21 explicit `git:<sha>` identifiers. |
| Other Unique Identifiers | 26 SPDXIDs, 26 VCS locators, 27 external references | `PASS` | Immutable Git revisions are present for all source components. |
| Dependency Relationship | 25 `CONTAINS` plus one `DESCRIBES` | `PASS` | Pass is limited to pinned bundle containment, not a runtime dependency graph. |
| Author of SBOM Data | two `creationInfo.creators` values | `PASS` | Research organization and generator are identified. |
| Timestamp | `2026-11-03T10:48:05Z` | `PASS` | Assembly timestamp is present. |

## Automation support and practices

| Element | Evidence | Status |
|---|---|---|
| Machine-readable format | SPDX 2.3 JSON and deterministic supplemental CSV/JSON | `PASS` |
| Automated generation | Original and supplemental generators are included | `PASS` |
| Frequency | No recurring generation cadence is promised | `UNKNOWN` |
| Depth | Direct 25-Gitlink depth and explicit Git-tree file selection are documented | `PASS` |
| Known unknowns | Binary/runtime, transitive, generated, vulnerability, and license limits are explicit | `PASS` |
| Distribution and delivery | Original is public; this v0.2 candidate requires a separate successful publication gate | `PARTIAL` |
| Access control | Intended public research artifact | `NOT_APPLICABLE` |
| Accommodation of mistakes | Versioned additive history and nonrecursive manifests | `PASS` |

Supplier coverage and the unpublished candidate state prevent an unqualified
minimum-elements conclusion. This table is intentionally more conservative than
schema validity alone.

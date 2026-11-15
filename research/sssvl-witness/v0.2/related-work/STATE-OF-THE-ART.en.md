# State of the Art and Scientific Positioning

## Scope and method

This is a targeted exploratory documentary review, not an
exhaustive systematic literature review or a comparative
benchmark. It examines public primary sources concerning
configuration assurance, SBOM correctness, provenance and
evidence-based acceptance.

No competing tool was executed. No new experiment was performed.
The study does not claim access to internal NASA processes,
NASA endorsement, formal NASA compliance, or external peer review.

## Related work

### R01 — NASA. Software Assurance and Software Safety Standard. NASA-STD-8739.8B, 2022.

Defines a lifecycle framework for software assurance, software safety and independent verification and validation.

### R02 — NASA. Software Engineering Handbook, Revision D. SWE-084: Configuration Audits.

Configuration audits compare the actual configuration items with the records that define them.

### R03 — Yu, S.; Song, W.; Hu, X.; Yin, H. On the Correctness of Metadata-Based SBOM Generation: A Differential Analysis Approach. IEEE/IFIP DSN, 2024.

A differential evaluation of four metadata-based SBOM generators found discrepancies and missing dependencies across 7,876 open-source projects.

### R04 — Xiao, Y.; Kirat, D.; Schales, D. L.; Jang, J.; Xing, L.; Liao, X. JBomAudit: Assessing the Landscape, Compliance, and Security Implications of Java SBOMs. NDSS, 2025.

JBomAudit evaluates declared dependencies against associated Java artifacts. Its study examined 25,882 SBOMs and associated JAR files and reported 7,907 SBOMs missing direct dependencies.

### R05 — SPDX. SPDX Specification v2.3.1, Clause 7: Package information.

Specifies package identifiers and descriptive fields, including package-level integrity information.

### R06 — Ecma International. ECMA-424: CycloneDX Bill of Materials Specification. Second edition, December 2025; CycloneDX v1.7.

Provides structured representation of components, dependencies, compositions and supporting evidence.

### R07 — SLSA. Version 1.2: Build Provenance.

Build provenance records production context, parameters, outputs and resolved dependencies when known.

### R08 — in-toto Witness. Policies.

Signed policies evaluate attestations, trusted signers, artifact consistency and policy conditions.

### R09 — CycloneDX Project. CycloneDX CLI.

Documents BOM validation, comparison, conversion and related operations.

### R10 — Interlynk. sbomqs.

Documents SBOM quality scoring and compliance checks.

### R11 — CISA. CISA, U.S. Government and International Partners Release Updated Minimum Elements for a Software Bill of Materials. 29 July 2026.

Announces updated SBOM guidance addressing component hashes and generation context among other fields.


## Scientific contribution and limits

Configuration auditing, inventory quality, cryptographic
integrity and evidence-based trust decisions are established
practices. Inventory-to-artifact reconciliation has direct
methodological antecedents, notably JBomAudit [R04].
In-toto Witness [R08] is an antecedent of policy-based
acceptance using attestations and artifact consistency.

This study does not claim to be the first implementation of
SBOM reconciliation. The general approach has established
precedents, and worldwide novelty of the specific experimental
combination has not been established.

Its documented contribution is a bounded experimental
evaluation of typed reconciliation using installed snapshots
of NASA cFS STD and EDS configurations, frozen references,
file identities, hashes, direct dynamic declarations and
pre-registered acceptance and blocking criteria.

The reference was frozen before the experimental mutations
and is independent of the mutated documents, but shares the
build lineage. The experiment modified inventories, not cFS
binaries. STD and EDS use different historical representations
of dynamic declarations.

The synthetic campaign and the cFS-derived campaign remain
unchanged. Repetitions are not statistically independent
samples. No new empirical result is introduced by this edition.

The evaluation concerns exact snapshots, not the complete
mission-required software universe. File and ELF counts are
not package counts. Direct dynamic declarations do not
establish runtime resolution, static composition or transitive
dependency closure.

The study does not establish global completeness, operational
security, superiority over existing tools, a NASA vulnerability,
or a defect in a commercial scanner. External independent
reproduction remains unqualified.

## Editorial status

This is a v0.2 editorial candidate derived from the published
v0.1. Scientific claims and limitations remain frozen.
Licensing of eligible new contributions has been approved by the author.
Human editorial acceptance of E5-C is approved. Publication is not authorized.

See [references](REFERENCES.md), the
[comparative matrix](COMPARATIVE-MATRIX.json), and the
[Portuguese edition](STATE-OF-THE-ART.pt-BR.md).

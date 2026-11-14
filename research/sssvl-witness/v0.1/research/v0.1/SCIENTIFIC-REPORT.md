# Beyond SBOM Validity: A Configuration-Aware Composition Witness for Software Supply Chain Assurance

An Experimental Study Using Synthetic Inventories and NASA Core Flight System Configurations

## Abstract
This independent experimental study separates SBOM documentary validity from sufficiency against a frozen composition reference. A synthetic witness evaluated 11 cases in two profiles (44 executions); a distinct typed comparator evaluated eight cases derived from NASA cFS STD and EDS installed snapshots (16 evaluations). All 16 real-derived evaluations agreed with pre-registered oracles; eight pairs repeated identically. Six negative cases and two positive controls were each evaluated twice, with zero observed false acceptances (0/12) and false blocks (0/4). The findings concern file identities and direct dynamic declarations, not global completeness, vulnerability discovery or operational assurance.

## Method
References were frozen before deliberate changes. W04 compares synthetic entities and edges; B2-A compares configuration-qualified file paths, SHA-256 claims and direct DT_NEEDED declarations, not package identities or resolved providers. STD uses historical DYNAMIC_LINK; EDS uses JSON comments. B2-B1 materialized and checked 16 SPDX documents before evaluation; B2-B2 ran eight primary and eight repeat evaluations in separate processes. Schema Draft7 and implemented reference checks are not full normative SPDX certification. The reference is separate from submitted mutations but shares build lineage.

## Results
STD: 546 installed files, 474 ELF, 432 direct declarations; EDS: 565, 483, 458. ELF is a subset of installed files. Counts are configuration-specific occurrences. Synthetic: 11 distinct cases, 44 executions, 330+330 leaf assertions, 22/22 pairs, 3/3 paired checks. Original profile: false acceptance 0/11, false blocking N/A (no positives); supplemented: 0/8 and 0/3. Real-derived: 8 distinct cases, 16 evaluations, 16/16 oracle agreement, 8/8 pairs, false acceptance 0/12, false blocking 0/4. Primary: 0/6 and 0/2; repeat: 0/6 and 0/2. Do not pool units or treat repeats as independent cases.

## Claims
### H1 — SUPPORTED_SYNTHETIC_ONLY
A naive policy is not a scanner defect.
The planted advisory positive control and paired omission support the counterfactual only. A scoped no-match or blocked broad verdict is not a failure.
No claim about any real scanner.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/COMPARISON.json SHA256 37c307b6646c17cbfbb7bd269f90513228f286b117cdd5a1ca27ce8e696599b5
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/METRICS.json SHA256 07795a1f894faf587b9e0e09f31da83e92a21b601de6a45161a399507289566e
- SSSVL-SBOM-WITNESS-CFS-v0.1-W01-W02-R1-20261113T141925.233282Z/HYPOTHESES.md SHA256 37dfa5911a84f6148ee6a9b8e764f8f025f2ba025a61dee30b74f2b38faa2ece
### H2 — SUPPORTED_BOUNDED
Cases designed with the evaluator can favor its implementation.
Missing identities, hash mismatch and absent declarations were detected in selected cases. An accepted required mismatch would refute the prediction.
W04 and B2-A are distinct; reference independent of submitted mutations, not independent build.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/COMPARISON.json SHA256 37c307b6646c17cbfbb7bd269f90513228f286b117cdd5a1ca27ce8e696599b5
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/METRICS.json SHA256 f32199df0cc27feb829a9926987395b2c380b693f7ab0ec7b5c54fe9a895d98b
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/ORACLE.json SHA256 4a4fe5b8c2c7dbfdf6491849ae43aa60cbe85c0471e3596bdf2f99e09579622e
- SSSVL-SBOM-WITNESS-CFS-v0.1-W01-W02-R1-20261113T141925.233282Z/HYPOTHESES.md SHA256 37dfa5911a84f6148ee6a9b8e764f8f025f2ba025a61dee30b74f2b38faa2ece
### H3 — SUPPORTED_BOUNDED
Schema and regenerated document hashes do not prove full normative compliance.
REAL-03/04 omit a reference identity; schema and implemented integrity checks pass while scoped coverage fails. A schema/checksum failure would invalidate this construction.
REAL-07 is a different test: SHA256 claim changes, SHA1 remains; no physical alteration.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B1-20261114T164606.435303Z/REPORT.json SHA256 27e02fc452d8a0108f13206d818b7188d251eae016642dc1eecc33d0ef82782a
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B1-20261114T164606.435303Z/MATERIALIZATION.json SHA256 4da5aa562fb93d20f0de495ab7d729206ac9ab40075df05f4e861e7bfbb8d1ab
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/METRICS.json SHA256 f32199df0cc27feb829a9926987395b2c380b693f7ab0ec7b5c54fe9a895d98b
- SSSVL-SBOM-WITNESS-CFS-v0.1-W01-W02-R1-20261113T141925.233282Z/HYPOTHESES.md SHA256 37dfa5911a84f6148ee6a9b8e764f8f025f2ba025a61dee30b74f2b38faa2ece
### H4 — SUPPORTED_BOUNDED
Caller supplies configuration; REAL-08 blocks before roles.
Explicit mismatch is detected; equivalent required universes would defeat the claimed distinction. Do not mix source/build/install/runtime.
No autonomous configuration discovery or spoofing resistance.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/COMPARISON.json SHA256 37c307b6646c17cbfbb7bd269f90513228f286b117cdd5a1ca27ce8e696599b5
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/primary-REAL-08.json SHA256 4f2cfccf7f277342e1316f839795c7234689bed8cfc6546985bdc48e08e32de3
- SSSVL-SBOM-WITNESS-CFS-v0.1-W01-W02-R1-20261113T141925.233282Z/HYPOTHESES.md SHA256 37dfa5911a84f6148ee6a9b8e764f8f025f2ba025a61dee30b74f2b38faa2ece
### H5 — SUPPORTED_SYNTHETIC_ONLY
Optional exclusion does not establish legitimate duplicate handling.
EXP-SBOM-08 supports justified exclusion only. Incorrect blocking of justified exclusions or legitimate duplicates would refute specificity.
PARTIAL_COVERAGE; legitimate duplicates NOT_ESTABLISHED; real specificity NOT_TESTED.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/PRIMARY.json SHA256 a139139b81357770dbc3d84e989ed94d81bff93e5f75daf83922395b6f67662a
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/ORACLE-FROZEN.json SHA256 99a573305e661829a27b0e48ff276ba903609a38803935bf1d1cfc29243f80a1
- SSSVL-SBOM-WITNESS-CFS-v0.1-W01-W02-R1-20261113T141925.233282Z/HYPOTHESES.md SHA256 37dfa5911a84f6148ee6a9b8e764f8f025f2ba025a61dee30b74f2b38faa2ece
### C6 — SUPPORTED_BOUNDED
Shared build lineage may share systematic omissions.
Exact installed snapshots match 546/474/432 STD and 565/483/458 EDS.
Not a mission-required universe; no provider/package/transitive/runtime promotion.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B1-Q1-M1-20261114T162308.349789Z/METRICS.json SHA256 d0a721c0cae53a54701e95bcdec45719d45154b3e5153022ee9d61744b30c7ff
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/REFERENCE.json SHA256 d33c6b9c28e6dd0743d76cce64ecab9a0aba2baf8d70d2a112dc01bbc1cf11fb
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/primary-REAL-01.json SHA256 956809121580cfe88152096adc27ceae8d21ac8bb59cb876db4d2d23a115b384
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/primary-REAL-02.json SHA256 6a0e9214427ff8ff0a78ab97f49a2efb5cf00205cf89692e9e20e18abe714496
### C7 — SUPPORTED_BOUNDED
Repeated runs are not independent samples.
8 distinct cases, 16 evaluations, 8 identical pairs.
No population error rate, external reproducibility or OS isolation claim.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/METRICS.json SHA256 f32199df0cc27feb829a9926987395b2c380b693f7ab0ec7b5c54fe9a895d98b
### C8 — NOT_ESTABLISHED
No scanner or exploit tested.
No evidence of commercial scanner defect or cFS vulnerability.
Keep claims separate and unestablished.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/REPORT.json SHA256 5b7ffa7966f481e80a3fd13e47f496095390d5268c283e29a92ac3fbbf85bff4
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/REPORT.json SHA256 b9b7cd109818c55bc4f8a79c00bda379537df3b527931daa595678c9954aa896
### C9 — NOT_ESTABLISHED
Snapshot scope omits runtime and other composition dimensions.
Sufficiency verdict has no operational security authority.
Package/version, provider, static, transitive and runtime remain UNKNOWN/NOT_VERIFIED.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/REPORT.json SHA256 5b7ffa7966f481e80a3fd13e47f496095390d5268c283e29a92ac3fbbf85bff4
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/CONTRACT.json SHA256 a6f53691a4458485b1fc45bf325765c0dbd3d818c0d2400a55513c2163e1d109

## Threats
### T1
Casos desenhados pela equipe do comparador; oraculos pre-registrados nao garantem independencia metodologica.
Response: Pre-registration mitigates post-hoc adjustment, not shared design bias; independent replication recommended.
Residual: OPEN_LIMITATION
### T2
Mesma linhagem de build entre inventarios e referencia; nao reproducao independente de compilacao.
Response: Freeze reference before mutation; shared build lineage remains a limitation.
Residual: OPEN_LIMITATION
### T3
Repeticoes deterministicas nao sao amostra estatistica independente.
Response: Report distinct cases and paired repetitions separately; no pooled statistical rate.
Residual: OPEN_LIMITATION
### T4
W04 usa entidades e arestas sinteticas; B2-A usa arquivo e declaracao direta, nao pacote ou provedor.
Response: Distinguish W04 synthetic entities/edges from B2-A file/declaration roles.
Residual: OPEN_LIMITATION
### T5
Validade formal limitada a schema/referencias; REAL-07 preserva SHA1 e altera alegacao SHA256.
Response: Limit schema claims to Draft7 and implemented reference checks; distinguish false hash claim from changed bytes.
Residual: OPEN_LIMITATION
### T6
Configuracao autenticada pelo chamador; REAL-08 testa incompatibilidade explicita, nao descoberta autonoma.
Response: Report explicit configuration mismatch, not autonomous inference.
Residual: OPEN_LIMITATION
### T7
Sem scanner real, runtime, vulnerabilidade ou seguranca operacional demonstrada.
Response: No scanner, exploit or runtime safety conclusion; further work requires separate authorization.
Residual: OPEN_LIMITATION
### T8
Sem isolamento OS qualificado; Evidence Vault pendente.
Response: Process separation is not sandbox isolation; vault and MT06 remain blocked/unverified.
Residual: OPEN_LIMITATION

## Limits
Scope: EXACT_SNAPSHOT_NOT_MISSION_REQUIRED_UNIVERSE. Package/version mapping, provider resolution, static components and transitive closure UNKNOWN; runtime NOT_VERIFIED. MT06 NOT_VERIFIED; witness OS isolation BLOCKED; Evidence Vault BLOCKED_PENDING_HUMAN_ACTION. No commercial scanner failure, cFS vulnerability, global completeness or operational security established. Novelty NOT_ESTABLISHED; literature review NOT_AUTHORIZED; external peer review NOT_PERFORMED.

## Conclusion
Scoped reconciliation detected the selected omissions and mismatches despite the implemented documentary checks passing. This is bounded experimental evidence, not a claim of novelty or security certification.

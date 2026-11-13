# NASA cFS SBOM — R5-A runtime evidence supplement

Mission: R5A-PILOT01-CONSOLIDATION-v0.1
Baseline: `088b2fa828db9ff7e00733f1908e0eeb59f66ce3`
Consolidation runner: v0.2; canonical alias groups verified: 1. See runtime-evidence.public.json for selected public evidence.

## Results

| Test | Assertions | Segments | Status |
|---|---:|---:|---|
| cpu1-shared-sockets | 117 | 16 | PASS_RECONCILED |
| cpu1-vxworks-loader | 10 | 4 | PASS |
| cpu2-shared-sockets | 117 | 16 | PASS |
| cpu2-vxworks-loader | 10 | 4 | PASS |
| Total | 254 | 40 | PASS |

## Method and preservation

Four native_std unit-test executions under Bubblewrap; UtAssert summaries, segment reconciliation, trace policy and GCOV header pairing independently read back. Original v0.1 remains BLOCKED due to a parser format mismatch; sentinel reconciled without rerun. v0.2 resumed the other three tests. R4 physical manifests and historical seals verified.

## SBOM linkage

- cpu1-shared-sockets: EXACT_ARTIFACT_MATCH; source/build evidence linked independently.
- cpu1-vxworks-loader: EXACT_ARTIFACT_MATCH; source/build evidence linked independently.
- cpu2-shared-sockets: EXACT_ARTIFACT_MATCH; source/build evidence linked independently.
- cpu2-vxworks-loader: EXACT_ARTIFACT_MATCH; source/build evidence linked independently.

Six sealed SPDX 2.3 documents are referenced without modifying them. See SBOM-LINKAGE.public.json for actual identifiers and checksums.

## Limitations

- No coverage percentage calculated
- No operational network or VxWorks hardware validation
- Trace policy readback is not exhaustive proof of absence of effects
- 392 other CTest registrations not qualified by this pilot
- native_eds blocked by Lua; global GREEN blocked

## Evidence

See runtime-evidence.public.json and ORIGINAL-ANCHORS.json for paths and hashes. The original SHA256SUMS seals four original payload files; it is not a digital signature.

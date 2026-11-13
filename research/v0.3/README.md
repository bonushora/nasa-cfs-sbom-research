# NASA cFS SBOM Enrichment: Artifact Identity and Runtime Evidence Qualification

Independent research, version 0.3. Author: Thales Rangel, Independent Researcher ([ORCID](https://orcid.org/0000-0002-0629-9731)). Upstream NASA cFS v7.0.1 commit `088b2fa828db9ff7e00733f1908e0eeb59f66ce3`. Publication base `d659af1fda004ac2c5f47208a055aecfc1d8882e`.

Four isolated native_std OSAL unit-test executions: 254/254 assertions, 40 segments, four GCOV header pairs, and eight exact SPDX file records across two documents. CPU1/CPU2 are build configurations; sockets and VxWorks loader use stubs. This is not NASA endorsement, flight qualification, or complete runtime SBOM validation.

See [results](RUNTIME-EVIDENCE-SUPPLEMENT.md), [reproduction](REPRODUCIBILITY.md), [limitations](LIMITATIONS.md), [citation](CITATION.cff), and [provenance](ORIGINAL-ANCHORS.json). Original evidence remains sealed locally; selected public records are derivatives. All six SPDX documents are included in their original bytes. This release package was qualified locally; GitHub publication requires separate authorization.

## Verification

Run `sha256sum -c SHA256SUMS` and `python3 -B verify_public_package.py` from this directory. Review the distribution status in SBOM-LINKAGE.public.json. No test execution is needed for package integrity verification.

# External VDD-to-SBOM Reconciliation — cFS Discussion #1188

## Scope

This document records the relationship between a
public technical discussion in the NASA cFS GitHub
repository and an independent source-level SPDX 2.3
SBOM research artifact produced by Bonushora.

Discussion:
https://github.com/nasa/cFS/discussions/1188

Research:
https://github.com/bonushora/nasa-cfs-sbom-research

## External documentary reference

In discussion #1188, Goncalo Esteves asked about
the availability of a published SBOM for cFS.

Bonushora provided a reference to its independently
published experimental source-level SPDX 2.3 SBOM.

A participant identified as irowebbn then pointed
to the official cFS Version Description Document
(VDD) package and explained that it lists components
and their versions.

Source comment:
https://github.com/nasa/cFS/discussions/1188#discussioncomment-19379719

Official release artifact:
https://github.com/nasa/cFS/releases/download/v7.0.1/cfs_vdd_package.tar.gz

The participant did not directly confirm the
research inventory's count of 25 Gitlinks.

The participant's formal maintainer role has not
been independently established in this document.

## Independent reconciliation

Following that reference, Bonushora reported
an independent comparison between the official
cFS v7.0.1 VDD package and the experimental
source-level SPDX 2.3 inventory.

The reported reconciliation found:

- 25/25 matching Git-linked component revisions.
- Exact matches of the full 40-character Git
  commit identifiers in Section 7 of the
  top-level VDD.
- 25 individual component VDDs identifying
  software version v7.0.1.

Bonushora's public response:
https://github.com/nasa/cFS/discussions/1188#discussioncomment-19382743

## Research evidence

The corresponding technical evidence is documented
in the published research v0.2 package.

Relevant artifacts include:

- research/v0.2/README.md
- research/v0.2/METHODOLOGY.md
- research/v0.2/inputs/cfs-v7.0.1-gitlinks.json

Fixed upstream cFS baseline:
088b2fa828db9ff7e00733f1908e0eeb59f66ce3

This document adds external discussion provenance.
It does not replace the original reconciliation
artifacts or independently rerun the comparison.

## Scientific interpretation

The VDD and the experimental SPDX SBOM are distinct
artifacts serving different purposes.

The reconciliation supports consistency of the
source-level component revisions represented in
the independent research.

It does not establish:

- Complete build or binary dependency coverage;
- Runtime or deployment dependency completeness;
- Flight qualification;
- NASA validation, certification, or endorsement.

## Provenance status

EXTERNAL_VDD_REFERENCE=DOCUMENTED
VDD_TO_SBOM_RECONCILIATION=REPORTED_25_OF_25
EXPERIMENT_REEXECUTION=NOT_PERFORMED
NASA_ENDORSEMENT=NOT_CLAIMED

This is independent, unofficial research.

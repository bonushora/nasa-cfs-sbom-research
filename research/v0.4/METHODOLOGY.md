# Methodology

## Research baseline

The upstream baseline is NASA cFS v7.0.1 at commit
088b2fa828db9ff7e00733f1908e0eeb59f66ce3.
The historical source reconciliation established
25 pinned Gitlink identities.

## Experimental sequence

MT30 qualified a local Lua prefix using three Ubuntu
Jammy amd64 packages at version 5.3.6-1build1.
The archive signature and package index hash chain
were verified against cached authenticated metadata.

MT31 built and installed native EDS in a separate
workspace using the qualified local Lua prefix.
The official preparation and installation targets
were used within the authorized isolation boundary.
Only build-required generators were executed.

MT32 independently read back the build and installation
inventories and recovered the STD-versus-EDS comparison.

MT33 generated six SPDX 2.3 inventories, including
file identities and conservative descriptions.
MT34 read back their counts, hashes and references.

MT35-R2 added a semantic dependency supplement and
examined literal generated CTest registrations without
running tests or evaluating CMake scripts.

## Evidence model

The study distinguishes source declarations, observed
compilation inputs, installed artifacts, ELF dependency
declarations, physical provider observations and actual
runtime behavior.

A declared DT_NEEDED name is represented as a logical
dependency target. It is not necessarily an identified
operating-system package or a resolved physical provider.

The additional sedstool-to-Lua relationship is supported
by the prior build observations and sealed identities.
Those observations are successful library opens,
not a complete dynamic-loader trace.

The public package is prepared from sealed evidence.
Public derivatives omit private local paths and raw
execution material. Source and derivative identities
are recorded in PROVENANCE.json.

## Governance

The work used human authorization, fail-closed controls,
preservation baselines, checkpoints, bounded execution
and evidence readback under BH-SEP/BH-SDP v2.3.

The initial MT35 attempt was blocked by an incorrect
JSON field assumption. MT35-R1 was blocked by failure
to recover the previous shell command. MT35-R2 corrected
both issues and passed the final qualification.

Those blocked attempts are not reclassified as passes.

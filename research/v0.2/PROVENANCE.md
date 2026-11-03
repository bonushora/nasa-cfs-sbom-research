# Provenance

## Primary anchors

| Object | Identity |
|---|---|
| NASA cFS Git tree | `088b2fa828db9ff7e00733f1908e0eeb59f66ce3` |
| Controlled 25-Gitlink table | SHA-256 `7e4bf8a5e27247d8a04136b490eabd37f897a40b19aac3d41f5e14a787e0e7ff` |
| Original SPDX 2.3 document | SHA-256 `10cdb17573d186a59a42de73915e21cd36e3a44a1bf5737a0eebdfe063e8249f` |
| Published v0.1.1 manifest | SHA-256 `6b19d557a57222723aba1aa5d7a0d37fa73efb85b219304353180747ec48ddeb` |
| Official VDD release archive | 13,850 bytes; SHA-256 `ee1fa901a49091274a19dc475564fbf541c36278714b73bf12cd980a4f165aa3` |
| Top-level VDD Markdown | SHA-256 `b915ee52c9eec9be4f64cb335ac118b6a7ff2be0d0b3b95e86caff8fd7bbf01e` |

The Git checkout origin was observed as `https://github.com/nasa/cFS.git`.
Root HEAD and all 25 initialized component checkouts were physically compared to
the controlled table before generation. No fetch, checkout, submodule update,
build, or execution of source code was performed.

## Artifact lineage

1. `inputs/cfs-v7.0.1-gitlinks.json` is byte-identical to the controlled table in
   the published v0.1.1 package.
2. VDD outputs are derived from the official archive and its safely extracted 27
   Markdown files. The archive itself is referenced by hash and is not
   redistributed here.
3. File inventory rows are derived from `git ls-tree` and `git cat-file` at the
   pinned commits. Git SHA-1 object IDs and SHA-256 blob/checkout digests are
   separate fields with separate semantics.
4. Dependency rows are exact syntactic evidence from `.gitmodules` and pinned
   CMake blobs. CMake was not evaluated.
5. License rows are exact evidence-file or `SPDX-License-Identifier` observations.
   They do not create package-wide license conclusions.

## Historical boundaries

The earlier v0.1, v0.1.1, VDD R1, and VDD R2 objects are historical inputs and
remain unchanged. This v0.2 directory is additive. The known public repository
head at authorization was `5c1f75da5bfa772619ceeb67686945ba142c5ef4`;
publication and remote identity require separate live readback and CAS gates.

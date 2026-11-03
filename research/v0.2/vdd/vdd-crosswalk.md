# NASA cFS v7.0.1 VDD / published gitlink crosswalk

Official VDD archive SHA-256: `ee1fa901a49091274a19dc475564fbf541c36278714b73bf12cd980a4f165aa3`  
Top-level VDD SHA-256: `b915ee52c9eec9be4f64cb335ac118b6a7ff2be0d0b3b95e86caff8fd7bbf01e`

`MATCH` requires equal component identity and exact 40-hex Git SHA. The individual VDD
supports the software version label but does not independently supply the Git SHA.

| # | Published path | Published Git SHA | VDD source | Individual VDD | Result |
|---:|---|---|---|---|---|
| 1 | `cfe` | `c5fb2b4d540bd55eb6c3707da7dd13eee679d4dd` | `vdd/00-cfs.md:320` (cFE v7.0.1) | `vdd/01-core/01-cFE.md:1,5,13,27` | `MATCH` |
| 2 | `osal` | `d2d877a69cff47452bcca274b309147d48e6c16f` | `vdd/00-cfs.md:321` (osal v7.0.1) | `vdd/01-core/02-osal.md:1,5,13,26` | `MATCH` |
| 3 | `psp` | `c4b3b0b65b119e106481ad8e20976ae4d7f554e3` | `vdd/00-cfs.md:322` (psp v7.0.1) | `vdd/01-core/03-psp.md:1,5,13,26` | `MATCH` |
| 4 | `apps/ci_lab` | `f5d36625336249312ee9d5815bc875e231815bb4` | `vdd/00-cfs.md:324` (ci_lab v7.0.1) | `vdd/02-apps/02-ci_lab.md:1,5,13,26` | `MATCH` |
| 5 | `apps/to_lab` | `38f7312ec4c1109b8f1c0738730b6e5ac5860f05` | `vdd/00-cfs.md:337` (to_lab v7.0.1) | `vdd/02-apps/15-to_lab.md:1,5,13,26` | `MATCH` |
| 6 | `apps/sch_lab` | `bc848cd8a6c0407023b959191e8aa39a01928444` | `vdd/00-cfs.md:336` (sch_lab v7.0.1) | `vdd/02-apps/14-sch_lab.md:1,5,13,26` | `MATCH` |
| 7 | `apps/sample_app` | `2f93d1a4159a02b18d67ee83342c9e96b90e23e4` | `vdd/00-cfs.md:333` (sample_app v7.0.1) | `vdd/02-apps/11-sample_app.md:1,5,13,26` | `MATCH` |
| 8 | `libs/sample_lib` | `2d8b7e862673ef90da4355890e18e92822e8acd7` | `vdd/00-cfs.md:338` (sample_lib v7.0.1) | `vdd/03-libs/01-sample_lib.md:1,5,13,26` | `MATCH` |
| 9 | `tools/cFS-GroundSystem` | `07a33a81fe7a88d248d9a5dc59bcf433e34594d7` | `vdd/00-cfs.md:339` (cFS-GroundSystem v7.0.1) | `vdd/04-tools/01-cFS_GroundSystem.md:1,5,13,26` | `MATCH` |
| 10 | `tools/elf2cfetbl` | `118b55fe1d128b48dc45fd36278b87827c6d3faa` | `vdd/00-cfs.md:341` (elf2cfetbl v7.0.1) | `vdd/04-tools/03-elf2cfetbl.md:1,5,13,26` | `MATCH` |
| 11 | `tools/tblCRCTool` | `cc61e89535db9fabe35fe26d1a600889f06b3104` | `vdd/00-cfs.md:342` (tblCRCTool v7.0.1) | `vdd/04-tools/04-tblCRCTool.md:1,5,13,26` | `MATCH` |
| 12 | `tools/eds` | `2acc963b34f77692c6396555dcfb10ef43eb1046` | `vdd/00-cfs.md:340` (EDSLib v7.0.1) | `vdd/04-tools/02-EDSLib.md:1,5,13,26` | `MATCH` |
| 13 | `apps/cf` | `15a871e66cad7ec75e1be78989a93075ff142055` | `vdd/00-cfs.md:323` (cf v7.0.1) | `vdd/02-apps/01-cf.md:1,5,13,26` | `MATCH` |
| 14 | `apps/cs` | `8510c5c0bd3e3b777086ad4b48aee3e79875553a` | `vdd/00-cfs.md:325` (cs v7.0.1) | `vdd/02-apps/03-cs.md:1,5,13,26` | `MATCH` |
| 15 | `apps/ds` | `c31e982eca47739dfcf31d4b40cad6068423e6a2` | `vdd/00-cfs.md:326` (ds v7.0.1) | `vdd/02-apps/04-ds.md:1,5,13,26` | `MATCH` |
| 16 | `apps/fm` | `ed51c5733c0f2d2f521d72f80d1b9254d2c8b5d0` | `vdd/00-cfs.md:327` (fm v7.0.1) | `vdd/02-apps/05-fm.md:1,5,13,26` | `MATCH` |
| 17 | `apps/hk` | `766dab1591b95ff89d99baaab9b43d234de4e699` | `vdd/00-cfs.md:328` (hk v7.0.1) | `vdd/02-apps/06-hk.md:1,5,13,26` | `MATCH` |
| 18 | `apps/hs` | `947b903174bca0878210e7fbc53104cff8e7b335` | `vdd/00-cfs.md:329` (hs v7.0.1) | `vdd/02-apps/07-hs.md:1,5,13,26` | `MATCH` |
| 19 | `apps/lc` | `a1c3a47ea1fa5c0d7751d6ff88848dc9bd8a6c7a` | `vdd/00-cfs.md:330` (lc v7.0.1) | `vdd/02-apps/08-lc.md:1,5,13,26` | `MATCH` |
| 20 | `apps/md` | `7e027886b22eb9e6492d59700cdc4549b116c698` | `vdd/00-cfs.md:331` (md v7.0.1) | `vdd/02-apps/09-md.md:1,5,13,26` | `MATCH` |
| 21 | `apps/mm` | `f3ee4e678df1fe64b9ee267b7e2a888352e178d5` | `vdd/00-cfs.md:332` (mm v7.0.1) | `vdd/02-apps/10-mm.md:1,5,13,26` | `MATCH` |
| 22 | `apps/sbn` | `3b7b37572d63c3f8e85b1f0fa95853c1b78dcf96` | `vdd/00-cfs.md:334` (sbn v7.0.1) | `vdd/02-apps/12-sbn.md:1,5,13,26` | `MATCH` |
| 23 | `apps/sc` | `76db5f7b0dde4ea22b41d19962564826967bc123` | `vdd/00-cfs.md:335` (sc v7.0.1) | `vdd/02-apps/13-sc.md:1,5,13,26` | `MATCH` |
| 24 | `tools/cfs-cosmos-plugin` | `358339d9fbb0516fdf00306cafc6d2cc7f869cd0` | `vdd/00-cfs.md:343` (cFS-COSMOS-Plugin v7.0.1) | `vdd/04-tools/05-cfs-cosmos-plugin.md:1,5,13,26` | `MATCH` |
| 25 | `tools/commandline-tools` | `d70c56ec035694c9a64b317897403266166f5d68` | `vdd/00-cfs.md:344` (cFS-CommandLine-Tools v7.0.1) | `vdd/04-tools/06-cfs-commandline-tools.md:1,5,13,26` | `MATCH` |

## Counts

```text
MATCH=25
PARTIAL_MATCH=0
MISMATCH=0
NOT_DOCUMENTED=0
NOT_COMPARABLE=0
TOTAL=25
```

This reconciliation covers the 25 pinned source Gitlinks. It does not establish
file-, dependency-, build-, binary-, runtime-, vulnerability-, or licensing completeness.

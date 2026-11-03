# Pinned Git-tree file inventory

Baseline: `088b2fa828db9ff7e00733f1908e0eeb59f66ce3`

Total rows: **4341** across **26** Git trees.

| Component | Commit | Entries | Regular | Filtered checkout | Symlinks | Gitlinks | Blob bytes |
|---|---|---:|---:|---:|---:|---:|---:|
| `.` | `088b2fa828db9ff7e00733f1908e0eeb59f66ce3` | 150 | 120 | 0 | 5 | 25 | 1927626 |
| `cfe` | `c5fb2b4d540bd55eb6c3707da7dd13eee679d4dd` | 683 | 683 | 0 | 0 | 0 | 7873875 |
| `osal` | `d2d877a69cff47452bcca274b309147d48e6c16f` | 854 | 854 | 0 | 0 | 0 | 4052904 |
| `psp` | `c4b3b0b65b119e106481ad8e20976ae4d7f554e3` | 497 | 497 | 0 | 0 | 0 | 2346973 |
| `apps/ci_lab` | `f5d36625336249312ee9d5815bc875e231815bb4` | 52 | 52 | 0 | 0 | 0 | 124780 |
| `apps/to_lab` | `38f7312ec4c1109b8f1c0738730b6e5ac5860f05` | 57 | 57 | 0 | 0 | 0 | 161339 |
| `apps/sch_lab` | `bc848cd8a6c0407023b959191e8aa39a01928444` | 30 | 30 | 0 | 0 | 0 | 64847 |
| `apps/sample_app` | `2f93d1a4159a02b18d67ee83342c9e96b90e23e4` | 71 | 71 | 0 | 0 | 0 | 173810 |
| `libs/sample_lib` | `2d8b7e862673ef90da4355890e18e92822e8acd7` | 25 | 25 | 0 | 0 | 0 | 55085 |
| `tools/cFS-GroundSystem` | `07a33a81fe7a88d248d9a5dc59bcf433e34594d7` | 296 | 296 | 0 | 0 | 0 | 403956 |
| `tools/elf2cfetbl` | `118b55fe1d128b48dc45fd36278b87827c6d3faa` | 24 | 24 | 0 | 0 | 0 | 172912 |
| `tools/tblCRCTool` | `cc61e89535db9fabe35fe26d1a600889f06b3104` | 15 | 15 | 0 | 0 | 0 | 33718 |
| `tools/eds` | `2acc963b34f77692c6396555dcfb10ef43eb1046` | 260 | 260 | 0 | 0 | 0 | 3620267 |
| `apps/cf` | `15a871e66cad7ec75e1be78989a93075ff142055` | 137 | 137 | 0 | 0 | 0 | 1704335 |
| `apps/cs` | `8510c5c0bd3e3b777086ad4b48aee3e79875553a` | 107 | 107 | 0 | 0 | 0 | 1327810 |
| `apps/ds` | `c31e982eca47739dfcf31d4b40cad6068423e6a2` | 91 | 91 | 0 | 0 | 0 | 5811419 |
| `apps/fm` | `ed51c5733c0f2d2f521d72f80d1b9254d2c8b5d0` | 94 | 94 | 0 | 0 | 0 | 2033239 |
| `apps/hk` | `766dab1591b95ff89d99baaab9b43d234de4e699` | 78 | 78 | 0 | 0 | 0 | 455994 |
| `apps/hs` | `947b903174bca0878210e7fbc53104cff8e7b335` | 89 | 89 | 0 | 0 | 0 | 3477115 |
| `apps/lc` | `a1c3a47ea1fa5c0d7751d6ff88848dc9bd8a6c7a` | 93 | 93 | 0 | 0 | 0 | 5298864 |
| `apps/md` | `7e027886b22eb9e6492d59700cdc4549b116c698` | 94 | 94 | 0 | 0 | 0 | 672905 |
| `apps/mm` | `f3ee4e678df1fe64b9ee267b7e2a888352e178d5` | 96 | 96 | 0 | 0 | 0 | 3482441 |
| `apps/sbn` | `3b7b37572d63c3f8e85b1f0fa95853c1b78dcf96` | 155 | 154 | 1 | 0 | 0 | 1456987 |
| `apps/sc` | `76db5f7b0dde4ea22b41d19962564826967bc123` | 104 | 104 | 0 | 0 | 0 | 4923956 |
| `tools/cfs-cosmos-plugin` | `358339d9fbb0516fdf00306cafc6d2cc7f869cd0` | 175 | 175 | 0 | 0 | 0 | 1209746 |
| `tools/commandline-tools` | `d70c56ec035694c9a64b317897403266166f5d68` | 14 | 14 | 0 | 0 | 0 | 115825 |

Git object IDs and SHA-256 digests have distinct semantics. Symlinks are recorded
without being followed. Parent Git trees record Gitlinks but do not descend into them;
each of the 25 pinned component trees is enumerated separately.

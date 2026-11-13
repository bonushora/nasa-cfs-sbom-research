# Scientific results

## Configuration comparison

| Metric | Native STD | Native EDS |
|---|---:|---:|
| Build files | 18267 | 11617 |
| Installed regular files | 546 | 565 |
| Installed ELF files | 474 | 483 |
| Recorded link commands | 651 | 333 |
| Distinct installed DT_NEEDED strings | 1 | 4 |

The installed-file comparison identifies 54 EDS-only
paths, 35 STD-only paths, 509 common paths with different
hashes, and two byte-identical common paths.

The 509 differences are not attributed exclusively to
EDS. Build layout, paths, toolchain configuration and
debug metadata may also influence file identities.

The link-command counts are observations of two
different build layouts, not normalized dependency counts.

## EDS candidates

The study classified 545 EDS output candidates:
228 C source candidates, 217 header candidates,
24 static archives and 76 shared ELF files.
Individual generation by sedstool is not universally
established.

## Dependency supplement

The supplement represents 458 installed ELF dependency
declarations and 382 build ELF dependency declarations.
These 840 observations are joined by one physical-provider
relationship from sedstool to the qualified Lua runtime.

The total of 841 relationships is not a count of
unique libraries or a transitive dependency closure.

## EdsLib relative dependency observation

Twelve installed ELF paths, representing six distinct
binary identities, declare:

    ../../../obj/ut_eds_db.so

Two library candidates in the build have the same SHA-256.

All six examined CTest registrations statically resolve
the relative path from their recorded working directories
to the expected library identity.

The evidence therefore supports resolution in the
examined CTest configuration. It does not establish
successful loader execution or a passing test.

The portability of separately installed test binaries
outside that environment is not established.

No vulnerability is claimed.

# Reproducing and validating the candidate

## Requirements

- Python 3.10 or newer
- `jsonschema==3.2.0` for official-schema validation
- Git, only for optional verification against an independent physical clone
- `sha256sum`, or the included Python package checker

Create an isolated environment if desired:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
```

The virtual environment is local build state and must not be added to the package.

## Deterministic regeneration

From the package root:

```bash
python3 scripts/generate_sbom.py
python3 -m json.tool sbom/cfs-v7.0.1.spdx.json >/dev/null
python3 scripts/validate_sbom.py
python3 scripts/validate_spdx_schema.py
python3 scripts/verify_inventory.py
python3 scripts/check_package.py
```

The generator uses a fixed evidence table and creation timestamp. Regeneration
must reproduce the SBOM hash recorded in `SHA256SUMS`.

`verify_inventory.py` without `--clone` checks the consistency of two packaged
representations. It is useful but is not an independent Git-tree observation.

## Independent physical verification

Obtain a separate read-only clone of the official public repository outside this
package. Network access is needed only for the clone operation itself.

```bash
git clone --branch v7.0.1 --recurse-submodules \
  https://github.com/nasa/cFS.git /path/to/cFS-v7.0.1

python3 scripts/verify_inventory.py --clone /path/to/cFS-v7.0.1
```

The verifier requires:

- official cFS origin URL;
- HEAD `088b2fa828db9ff7e00733f1908e0eeb59f66ce3`;
- exactly 25 `160000 commit` Git-tree entries;
- initialized and aligned submodule checkouts;
- identical paths and revisions in the controlled table and SPDX document.

It performs no fetch, checkout, update, build, push, or remote mutation.

## Manifest verification

```bash
sha256sum -c SHA256SUMS
```

Or use:

```bash
python3 scripts/check_package.py
```

The Python checker also rejects symlinks, unlisted files, common credential
patterns, email addresses, and private/laboratory path fragments.

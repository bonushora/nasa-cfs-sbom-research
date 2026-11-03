# Reproducing and validating the package

## Scope of this guide

These procedures validate package integrity, the SPDX 2.3 structure, the
controlled 25-gitlink inventory, and deterministic SBOM generation. They do not
build cFS and do not establish binary or runtime composition.

The published `v0.1` reference is commit
`1beb2f48fd0aea86bd817cc3829f0d35026445c2`. The v0.1.1 editorial update retains the same technical inventory and SBOM.

## Requirements

- Python 3.10 or newer
- `jsonschema==3.2.0` for official-schema validation
- Git for optional physical-clone verification
- `sha256sum`, or the included Python package checker

An isolated Python environment is recommended:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
```

The virtual environment is local state and must not be added to the package.

## 1. Verify package integrity

From the package root, verify the non-self-referential manifest before running a
generator:

```bash
sha256sum -c SHA256SUMS
```

The command must validate every listed file. `SHA256SUMS` itself is deliberately
not listed, avoiding a circular hash dependency.

## 2. Parse and validate the SPDX document

```bash
python3 -m json.tool data/cfs-v7.0.1-gitlinks.json >/dev/null
python3 -m json.tool sbom/cfs-v7.0.1.spdx.json >/dev/null
python3 -m json.tool schemas/spdx-schema-v2.3.json >/dev/null
python3 scripts/validate_sbom.py
python3 scripts/validate_spdx_schema.py
python3 scripts/verify_inventory.py
```

The last command compares the packaged gitlink table with the SPDX packages and
relationships. Without `--clone`, it checks two packaged representations and is
not an independent observation of the upstream Git tree.

## 3. Regenerate the SBOM deterministically

```bash
sha256sum sbom/cfs-v7.0.1.spdx.json
python3 scripts/generate_sbom.py
sha256sum sbom/cfs-v7.0.1.spdx.json
git diff -- sbom/cfs-v7.0.1.spdx.json 2>/dev/null || true
```

The before and after digests must both be:

```text
10cdb17573d186a59a42de73915e21cd36e3a44a1bf5737a0eebdfe063e8249f
```

The generator uses a fixed evidence table and creation timestamp. If the digest
changes, stop and investigate rather than updating the expected value.

## 4. Run package-security checks

`scripts/check_package.py` intentionally rejects Git administrative metadata. Run
it directly in a delivered package directory or clean export that does not
contain `.git`:

```bash
python3 scripts/check_package.py
```

When validating a Git clone, create an isolated export first:

```bash
export_dir="$(mktemp -d)"
git archive --format=tar HEAD | tar -xf - -C "$export_dir"
python3 "$export_dir/scripts/check_package.py"
(cd "$export_dir" && sha256sum -c SHA256SUMS)
```

The checker rejects symlinks, unlisted files, Git metadata, common credential
patterns, email addresses, private paths, and unexpectedly large files.

## 5. Perform optional physical verification

Obtain a separate read-only clone of the official public cFS repository outside
this package. This step requires network access but does not require modifying an
upstream repository.

```bash
git clone --branch v7.0.1 --recurse-submodules \
  https://github.com/nasa/cFS.git /path/to/cFS-v7.0.1

python3 scripts/verify_inventory.py --clone /path/to/cFS-v7.0.1
```

The verifier requires:

- origin `https://github.com/nasa/cFS.git`;
- HEAD `088b2fa828db9ff7e00733f1908e0eeb59f66ce3`;
- exactly 25 Git-tree entries with mode `160000` and type `commit`;
- 25 initialized and aligned submodule checkouts;
- identical paths and revisions in the controlled table and SPDX document.

The verifier performs no fetch, checkout, update, build, push, or remote mutation.

## Expected results

A successful validation establishes that the package is internally consistent,
matches its manifest, conforms to the included SPDX schema, and deterministically
reproduces the published SBOM bytes. It does not demonstrate file-level,
build-time, binary, deployment, or runtime completeness.

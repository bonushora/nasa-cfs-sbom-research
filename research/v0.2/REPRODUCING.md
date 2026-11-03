# Reproducing the v0.2 supplement

## Requirements

- Python 3.10 or newer;
- Git;
- the official VDD archive matching the hash in `PROVENANCE.md`;
- a clean, initialized cFS checkout at the pinned root and component commits;
- the safely extracted VDD directory.

No package installation or execution of cFS source is required.

## Generate

```bash
python3 scripts/generate_vdd_crosswalk.py \
  --archive /path/to/cfs_vdd_package.tar.gz \
  --vdd-dir /path/to/extracted/vdd \
  --gitlinks inputs/cfs-v7.0.1-gitlinks.json \
  --output-dir vdd

python3 scripts/generate_file_inventory.py \
  --clone /path/to/cFS-v7.0.1 \
  --gitlinks inputs/cfs-v7.0.1-gitlinks.json \
  --output-dir inventory

python3 scripts/generate_evidence_matrices.py \
  --clone /path/to/cFS-v7.0.1 \
  --gitlinks inputs/cfs-v7.0.1-gitlinks.json \
  --output-dir evidence-matrices
```

Generate into a second empty directory and compare SHA-256 digests. Deterministic
gzip files must be byte-identical, not merely semantically equal.

## Validate

```bash
python3 scripts/validate_outputs.py --package . --clone /path/to/cFS-v7.0.1
sha256sum -c SHA256SUMS
```

Validation checks cross-format VDD semantics, cardinalities, unique inventory
keys, artifact digests, matrix state constraints, evidence paths, package
manifest coverage, symlinks, Git metadata, private paths, common credential
patterns, and unexpected files.

These procedures validate the documentary package. They do not compile cFS,
resolve dependencies, test vulnerabilities, or reproduce a deployed system.

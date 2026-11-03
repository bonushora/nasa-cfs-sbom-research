#!/usr/bin/env python3
"""Fail closed on manifest, symlink, private-path, and common secret issues."""

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "SHA256SUMS"
REQUIRED = {
    "README.md",
    "REPRODUCING.md",
    "METHODOLOGY.md",
    "ATTRIBUTIONS.md",
    "LICENSE",
    "NOTICE",
    "PUBLICATION-READINESS.md",
    "RIGHTS_ATTESTATION.md",
    "THIRD_PARTY_NOTICES.md",
    "requirements.txt",
    "data/cfs-v7.0.1-gitlinks.json",
    "sbom/cfs-v7.0.1.spdx.json",
    "schemas/spdx-schema-v2.3.json",
    "scripts/generate_sbom.py",
    "scripts/validate_sbom.py",
    "scripts/validate_spdx_schema.py",
    "scripts/verify_inventory.py",
    "scripts/check_package.py",
}
FORBIDDEN_FRAGMENTS = [
    b"/" + b"home/",
    b"/Users" + b"/",
    b"snap" + b"shots/",
]
SECRET_PATTERNS = [
    re.compile(rb"AKIA[0-9A-Z]{16}"),
    re.compile(rb"(?:ghp|github_pat)_[A-Za-z0-9_]{20,}"),
    re.compile(rb"xox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(rb"(?i)(?:password|passwd|secret|token|api[_-]?key)\s*[:=]\s*['\"]?[A-Za-z0-9+/=_-]{12,}"),
]
EMAIL = re.compile(rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> int:
    if not MANIFEST.is_file():
        fail("SHA256SUMS is missing")
    files = sorted(path for path in ROOT.rglob("*") if path.is_file() or path.is_symlink())
    if any(path.is_symlink() for path in files):
        fail("candidate contains a symlink")
    if any(part == ".git" for path in files for part in path.relative_to(ROOT).parts):
        fail("candidate contains .git content")
    regular = {path.relative_to(ROOT).as_posix() for path in files if path != MANIFEST}
    if not REQUIRED.issubset(regular):
        fail(f"required files missing: {sorted(REQUIRED - regular)}")

    listed = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        if name in listed:
            fail(f"duplicate manifest entry: {name}")
        listed[name] = digest
    if set(listed) != regular:
        fail(f"manifest inventory mismatch missing={sorted(regular-set(listed))} extra={sorted(set(listed)-regular)}")

    for name in sorted(regular):
        path = ROOT / name
        data = path.read_bytes()
        if len(data) > 2_000_000:
            fail(f"unexpectedly large file: {name}")
        actual = hashlib.sha256(data).hexdigest()
        if actual != listed[name]:
            fail(f"hash mismatch: {name}")
        if any(fragment in data for fragment in FORBIDDEN_FRAGMENTS):
            fail(f"private or laboratory path fragment: {name}")
        if EMAIL.search(data):
            fail(f"email address found: {name}")
        if any(pattern.search(data) for pattern in SECRET_PATTERNS):
            fail(f"possible credential or secret: {name}")

    print(f"PASS manifest files={len(regular)}")
    print("PASS symlinks=0 git-directories=0")
    print("PASS private-paths=0 emails=0 common-secret-patterns=0")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        sys.exit(1)

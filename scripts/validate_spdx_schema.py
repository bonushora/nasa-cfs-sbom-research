#!/usr/bin/env python3
"""Validate the candidate SBOM against the vendored official SPDX 2.3 schema."""

import json
import platform
import sys
from pathlib import Path
from urllib.parse import urlparse

import jsonschema
from jsonschema import Draft7Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "spdx-schema-v2.3.json"
DOCUMENT = ROOT / "sbom" / "cfs-v7.0.1.spdx.json"
ORIGIN = "https://raw.githubusercontent.com/spdx/spdx-spec/v2.3/schemas/spdx-schema.json"


def json_path(parts) -> str:
    value = "$"
    for part in parts:
        value += f"[{part}]" if isinstance(part, int) else f".{part}"
    return value


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    document = json.loads(DOCUMENT.read_text(encoding="utf-8"))
    print(f"validator=jsonschema version={jsonschema.__version__}")
    print(f"python={platform.python_version()}")
    print(f"schema_origin={ORIGIN}")
    print(f"schema_id={schema.get('$id')}")
    print(f"document={DOCUMENT.relative_to(ROOT)}")

    Draft7Validator.check_schema(schema)
    errors = sorted(Draft7Validator(schema).iter_errors(document), key=lambda error: list(error.path))
    if errors:
        print(f"FAIL official-spdx-2.3-json-schema errors={len(errors)}")
        for index, error in enumerate(errors, 1):
            print(f"ERROR {index} instance_path={json_path(error.path)}")
            print(f"  schema_path={json_path(error.schema_path)}")
            print(f"  message={error.message}")
        return 1
    print("PASS official-schema-is-valid-draft-07")
    print("PASS official-spdx-2.3-json-schema errors=0")

    namespace = document.get("documentNamespace", "")
    parsed = urlparse(namespace)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        print(f"FAIL documentNamespace is not an absolute HTTP(S) URI: {namespace}")
        return 1
    refs = [ref for package in document.get("packages", []) for ref in package.get("externalRefs", [])]
    required = {"referenceCategory", "referenceType", "referenceLocator"}
    if any(not required.issubset(ref) for ref in refs):
        print("FAIL one or more externalRefs lack required fields")
        return 1
    print(f"PASS documentNamespace absolute_uri={namespace}")
    print(f"PASS externalRefs required_fields count={len(refs)}")
    print("NOTE schema validation does not establish binary or runtime completeness")
    return 0


if __name__ == "__main__":
    sys.exit(main())

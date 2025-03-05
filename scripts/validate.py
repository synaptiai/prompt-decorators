#!/usr/bin/env python3
"""
Simple validation script for prompt decorator JSON files.
"""

import json
import os
import sys

from jsonschema import validate


def validate_file(file_path, schema_path):
    """Validate a file against a schema."""
    try:
        with open(schema_path, "r") as f:
            schema = json.load(f)

        with open(file_path, "r") as f:
            data = json.load(f)

        validate(instance=data, schema=schema)
        print(f"✅ Validation successful for {file_path}")
        return True
    except Exception as e:
        print(f"❌ Validation failed for {file_path}: {e}")
        return False


def main():
    """Main function."""
    if len(sys.argv) < 3:
        print("Usage: python validate.py <file_path> <schema_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    schema_path = sys.argv[2]

    success = validate_file(file_path, schema_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

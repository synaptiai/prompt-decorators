#!/usr/bin/env python3
"""Validate registry entries against the schema."""

import json
from jsonschema import validate
import glob
import sys

def main():
    """Validate all registry entries."""
    # Load schema
    with open('schemas/registry-entry.schema.json') as f:
        schema = json.load(f)

    # Track validation status
    all_valid = True

    # Validate all registry entries
    for entry_file in glob.glob('registry/core/*.json'):
        print(f'\nValidating {entry_file}...')
        with open(entry_file) as f:
            entry = json.load(f)
        try:
            validate(instance=entry, schema=schema)
            print('✓ Valid')
        except Exception as e:
            print(f'✗ Invalid: {str(e)}')
            all_valid = False

    # Exit with appropriate status
    sys.exit(0 if all_valid else 1)

if __name__ == '__main__':
    main() 
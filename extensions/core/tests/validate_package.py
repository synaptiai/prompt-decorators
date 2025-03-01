#!/usr/bin/env python3
"""Validate the extension package against the schema."""

import json
import os
import sys
from pathlib import Path
from jsonschema import validate, ValidationError, RefResolver

def main():
    """Validate the extension package and its decorators."""
    # Get the root directory
    root_dir = Path(__file__).parent.parent.parent.parent
    schemas_dir = root_dir / "schemas"
    package_dir = root_dir / "extensions" / "core"
    
    # Load schemas
    with open(schemas_dir / "extension-package.schema.json") as f:
        package_schema = json.load(f)
    
    with open(schemas_dir / "registry-entry.schema.json") as f:
        decorator_schema = json.load(f)
    
    # Create a resolver for schema references
    schema_store = {}
    for schema_file in schemas_dir.glob("*.schema.json"):
        with open(schema_file) as f:
            schema = json.load(f)
            schema_uri = f"file://{schema_file.resolve()}"
            schema_store[schema_uri] = schema
            
            # Also store with just the filename as key for relative references
            schema_store[schema_file.name] = schema
    
    # Load the package.json
    with open(package_dir / "package.json") as f:
        package = json.load(f)
    
    # Validate the package
    print("Validating package.json...")
    try:
        # Create a base URI for the resolver
        base_uri = f"file://{schemas_dir.resolve()}/extension-package.schema.json"
        resolver = RefResolver(base_uri, package_schema, store=schema_store)
        validate(instance=package, schema=package_schema, resolver=resolver)
        print("✓ Package is valid")
    except ValidationError as e:
        print(f"✗ Package validation error: {e}")
        return 1
    
    # Validate each decorator
    all_valid = True
    for i, decorator in enumerate(package.get("decorators", [])):
        print(f"\nValidating decorator #{i+1}: {decorator.get('decoratorName', 'Unknown')}...")
        try:
            # Create a base URI for the resolver
            base_uri = f"file://{schemas_dir.resolve()}/registry-entry.schema.json"
            resolver = RefResolver(base_uri, decorator_schema, store=schema_store)
            validate(instance=decorator, schema=decorator_schema, resolver=resolver)
            print(f"✓ {decorator.get('decoratorName', 'Unknown')} is valid")
        except ValidationError as e:
            print(f"✗ Validation error: {e}")
            all_valid = False
    
    return 0 if all_valid else 1

if __name__ == "__main__":
    sys.exit(main()) 
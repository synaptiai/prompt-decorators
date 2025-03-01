#!/usr/bin/env python3
"""
Decorator Validator Tool

This script validates prompt decorator definitions against the appropriate JSON schemas.
It can validate individual decorator files, registry entries, API requests, and extension packages.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union, Any

try:
    from jsonschema import validate, ValidationError, RefResolver
except ImportError:
    print("Error: jsonschema package is required. Install it with: pip install jsonschema")
    sys.exit(1)


class DecoratorValidator:
    """Validator for Prompt Decorators and related artifacts."""

    def __init__(self, schemas_dir: Union[str, Path]):
        """Initialize the validator with schemas directory.

        Args:
            schemas_dir: Path to the directory containing JSON schemas
        """
        self.schemas_dir = Path(schemas_dir)
        self.schema_store = {}
        self._load_schemas()

    def _load_schemas(self) -> None:
        """Load all schemas from the schemas directory."""
        schema_files = [
            "decorator.schema.json",
            "registry-entry.schema.json",
            "api-request.schema.json",
            "extension-package.schema.json"
        ]

        for schema_file in schema_files:
            schema_path = self.schemas_dir / schema_file
            if not schema_path.exists():
                print(f"Warning: Schema file not found: {schema_path}")
                continue

            try:
                with open(schema_path, "r") as f:
                    schema = json.load(f)
                    # Store with full URI
                    schema_uri = f"file://{schema_path.resolve()}"
                    self.schema_store[schema_uri] = schema
                    # Also store with just the filename as key for relative references
                    self.schema_store[schema_file] = schema
            except json.JSONDecodeError as e:
                print(f"Error loading schema {schema_file}: {e}")
                sys.exit(1)

    def _get_resolver(self, schema_file: str) -> RefResolver:
        """Create a resolver for a specific schema.

        Args:
            schema_file: Name of the schema file

        Returns:
            RefResolver instance
        """
        base_uri = f"file://{(self.schemas_dir / schema_file).resolve()}"
        return RefResolver(base_uri, self.schema_store[schema_file], store=self.schema_store)

    def validate_decorator(self, file_path: Union[str, Path]) -> bool:
        """Validate a decorator definition against the decorator schema.

        Args:
            file_path: Path to the decorator JSON file

        Returns:
            True if valid, False otherwise
        """
        return self._validate_file(file_path, "decorator.schema.json", "Decorator")

    def validate_registry_entry(self, file_path: Union[str, Path]) -> bool:
        """Validate a registry entry against the registry-entry schema.

        Args:
            file_path: Path to the registry entry JSON file

        Returns:
            True if valid, False otherwise
        """
        return self._validate_file(file_path, "registry-entry.schema.json", "Registry entry")

    def validate_api_request(self, file_path: Union[str, Path]) -> bool:
        """Validate an API request against the api-request schema.

        Args:
            file_path: Path to the API request JSON file

        Returns:
            True if valid, False otherwise
        """
        return self._validate_file(file_path, "api-request.schema.json", "API request")

    def validate_extension_package(self, file_path: Union[str, Path]) -> bool:
        """Validate an extension package against the extension-package schema.

        Args:
            file_path: Path to the extension package JSON file

        Returns:
            True if valid, False otherwise
        """
        return self._validate_file(file_path, "extension-package.schema.json", "Extension package")

    def _validate_file(self, file_path: Union[str, Path], schema_file: str, label: str) -> bool:
        """Validate a file against a schema.

        Args:
            file_path: Path to the file to validate
            schema_file: Name of the schema file
            label: Label for error messages

        Returns:
            True if valid, False otherwise
        """
        file_path = Path(file_path)
        if not file_path.exists():
            print(f"Error: File not found: {file_path}")
            return False

        try:
            with open(file_path, "r") as f:
                instance = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {file_path}: {e}")
            return False

        try:
            schema = self.schema_store.get(schema_file)
            if not schema:
                print(f"Error: Schema {schema_file} not found")
                return False

            resolver = self._get_resolver(schema_file)
            validate(instance=instance, schema=schema, resolver=resolver)
            print(f"✓ {label} is valid: {file_path}")
            return True
        except ValidationError as e:
            print(f"✗ {label} validation error in {file_path}:")
            print(f"  - {e.message}")
            if e.path:
                path_str = " → ".join(str(p) for p in e.path)
                print(f"  - Path: {path_str}")
            if e.schema_path:
                schema_path_str = " → ".join(str(p) for p in e.schema_path)
                print(f"  - Schema path: {schema_path_str}")
            return False

    def validate_directory(self, dir_path: Union[str, Path], schema_type: str) -> bool:
        """Validate all JSON files in a directory against a specific schema.

        Args:
            dir_path: Path to the directory containing JSON files
            schema_type: Type of schema to validate against (decorator, registry, api, package)

        Returns:
            True if all files are valid, False otherwise
        """
        dir_path = Path(dir_path)
        if not dir_path.exists() or not dir_path.is_dir():
            print(f"Error: Directory not found: {dir_path}")
            return False

        schema_map = {
            "decorator": "decorator.schema.json",
            "registry": "registry-entry.schema.json",
            "api": "api-request.schema.json",
            "package": "extension-package.schema.json"
        }

        if schema_type not in schema_map:
            print(f"Error: Unknown schema type: {schema_type}")
            print(f"Valid types: {', '.join(schema_map.keys())}")
            return False

        schema_file = schema_map[schema_type]
        label_map = {
            "decorator": "Decorator",
            "registry": "Registry entry",
            "api": "API request",
            "package": "Extension package"
        }
        label = label_map[schema_type]

        all_valid = True
        for file_path in dir_path.glob("**/*.json"):
            if not self._validate_file(file_path, schema_file, label):
                all_valid = False

        return all_valid


def main():
    """Run the validator tool."""
    parser = argparse.ArgumentParser(description="Validate prompt decorator files against schemas")
    parser.add_argument("--schemas-dir", default="schemas",
                        help="Directory containing schema files (default: schemas)")
    
    subparsers = parser.add_subparsers(dest="command", help="Validation command")
    
    # Validate decorator
    decorator_parser = subparsers.add_parser("decorator", help="Validate a decorator file")
    decorator_parser.add_argument("file", help="Path to the decorator JSON file")
    
    # Validate registry entry
    registry_parser = subparsers.add_parser("registry", help="Validate a registry entry file")
    registry_parser.add_argument("file", help="Path to the registry entry JSON file")
    
    # Validate API request
    api_parser = subparsers.add_parser("api", help="Validate an API request file")
    api_parser.add_argument("file", help="Path to the API request JSON file")
    
    # Validate extension package
    package_parser = subparsers.add_parser("package", help="Validate an extension package file")
    package_parser.add_argument("file", help="Path to the extension package JSON file")
    
    # Validate directory
    dir_parser = subparsers.add_parser("directory", help="Validate all JSON files in a directory")
    dir_parser.add_argument("path", help="Path to the directory")
    dir_parser.add_argument("--type", choices=["decorator", "registry", "api", "package"],
                           required=True, help="Type of schema to validate against")
    
    # Parse arguments
    args = parser.parse_args()
    
    # No command provided, show help
    if not args.command:
        parser.print_help()
        return 1
    
    # Create validator
    validator = DecoratorValidator(args.schemas_dir)
    
    # Execute command
    if args.command == "decorator":
        success = validator.validate_decorator(args.file)
    elif args.command == "registry":
        success = validator.validate_registry_entry(args.file)
    elif args.command == "api":
        success = validator.validate_api_request(args.file)
    elif args.command == "package":
        success = validator.validate_extension_package(args.file)
    elif args.command == "directory":
        success = validator.validate_directory(args.path, args.type)
        
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main()) 
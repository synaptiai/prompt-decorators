#!/usr/bin/env python3
"""Test script for the YAML to JSON Schema Converter.

This script tests the YAML to JSON Schema Converter with a small sample YAML file.
It's useful for verifying that the converter works correctly without processing
a large number of decorators.

Example usage:
    $ python scripts/test_yaml_to_schema.py

Returns:
    int: 0 for success, non-zero for errors
"""

import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict

import yaml

# Add the parent directory to the path so we can import the converter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.yaml_to_schema_converter import SchemaConverter


def create_test_yaml() -> str:
    """Create a test YAML file with a sample decorator.

    Returns:
        str: Path to the test YAML file
    """
    test_yaml = {
        "version": "1.0.0",
        "author": {
            "name": "Test Author",
            "email": "test@example.com",
            "url": "https://example.com",
        },
        "decorators": [
            {
                "name": "TestDecorator",
                "category": "Testing",
                "description": "A test decorator for testing the converter",
                "parameters": [
                    {
                        "name": "test_param",
                        "type": "enum",
                        "description": "A test parameter",
                        "values": ["value1", "value2", "value3"],
                        "default": "value1",
                    },
                    {
                        "name": "flag",
                        "type": "boolean",
                        "description": "A boolean flag",
                        "default": False,
                    },
                ],
                "example": "+++TestDecorator(test_param=value2, flag=true)\nThis is a test prompt.",
            }
        ],
    }

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Write the YAML file
    yaml_path = os.path.join(temp_dir, "test.yml")
    with open(yaml_path, "w") as f:
        yaml.dump(test_yaml, f)

    return yaml_path


def test_converter(api_key: str) -> bool:
    """Test the YAML to JSON Schema Converter.

    Args:
        api_key: Anthropic API key

    Returns:
        bool: Whether the test was successful
    """
    # Create a test YAML file
    yaml_path = create_test_yaml()

    # Create a temporary output directory
    output_dir = os.path.join(os.path.dirname(yaml_path), "output")
    os.makedirs(output_dir, exist_ok=True)

    # Create a converter
    converter = SchemaConverter(
        api_key=api_key,
        schema_path="schemas/registry-entry.schema.json",
        cache_dir=os.path.join(os.path.dirname(yaml_path), "cache"),
        verbose=True,
    )

    # Process the YAML file
    total, success, error = converter.process_yaml(
        yaml_path=yaml_path,
        output_dir=output_dir,
        force=True,
    )

    # Check if the processing was successful
    if error > 0:
        print(f"Error: {error} decorators failed to process")
        return False

    # Check if the output file exists
    output_file = os.path.join(output_dir, "testing", "testdecorator.json")
    if not os.path.exists(output_file):
        print(f"Error: Output file not found: {output_file}")
        return False

    # Load the output file
    with open(output_file, "r") as f:
        schema = json.load(f)

    # Print the schema
    print("Generated schema:")
    print(json.dumps(schema, indent=2))

    # Validate the schema
    if not converter.validate_schema(schema):
        print("Error: Generated schema is invalid")
        return False

    print("Test successful!")
    return True


def main() -> int:
    """Main entry point.

    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    # Get API key from environment variable
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(
            "Error: Anthropic API key not provided. Set ANTHROPIC_API_KEY environment variable."
        )
        return 1

    # Run the test
    success = test_converter(api_key)

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())

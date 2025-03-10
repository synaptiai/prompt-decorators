#!/usr/bin/env python3
"""
Prompt Decorators Validation CLI.

A unified command-line interface for validating prompt decorators,
wrapping existing validation functionality without modifying core code.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


def setup_parser() -> argparse.ArgumentParser:
    """Set up the command line argument parser."""
    parser = argparse.ArgumentParser(
        description="Prompt Decorators Validation CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate a decorator schema file
  python prompt_validator.py schema -f registry/core/reasoning/deductive.json

  # Validate decorator syntax in a prompt
  python prompt_validator.py syntax -t "+++Reasoning(depth=comprehensive)\\nExplain quantum computing."

  # Validate all files in a directory against registry schema
  python prompt_validator.py directory -d registry/core -s registry
  """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Schema validation parser
    schema_parser = subparsers.add_parser(
        "schema", help="Validate a file against a JSON schema"
    )
    schema_parser.add_argument("-f", "--file", required=True, help="File to validate")
    schema_parser.add_argument(
        "-s",
        "--schema",
        choices=["decorator", "registry", "api", "package"],
        default="registry",
        help="Schema type to validate against (default: registry)",
    )

    # Syntax validation parser
    syntax_parser = subparsers.add_parser(
        "syntax", help="Validate decorator syntax in a prompt"
    )
    syntax_text = syntax_parser.add_mutually_exclusive_group(required=True)
    syntax_text.add_argument("-t", "--text", help="Prompt text to validate")
    syntax_text.add_argument(
        "-f", "--file", help="File containing prompt text to validate"
    )

    # Directory validation parser
    dir_parser = subparsers.add_parser(
        "directory", help="Validate all files in a directory"
    )
    dir_parser.add_argument(
        "-d", "--directory", required=True, help="Directory to validate"
    )
    dir_parser.add_argument(
        "-s",
        "--schema",
        choices=["decorator", "registry", "api", "package"],
        default="registry",
        help="Schema type to validate against (default: registry)",
    )
    dir_parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recursively validate subdirectories",
    )

    return parser


def validate_schema(file_path: str, schema_type: str = "registry") -> bool:
    """
    Validate a file against a JSON schema.

    Args:
        file_path: Path to the file to validate
        schema_type: Type of schema to validate against

    Returns:
        True if validation successful, False otherwise
    """
    # Import validate_decorators only when needed to avoid loading unnecessary modules
    from importlib import import_module

    try:
        # Try importing the validator module
        module = import_module("validate_decorators")
        validator_class = getattr(module, "DecoratorValidator", None)

        if not validator_class:
            print("Error: DecoratorValidator class not found in validate_decorators")
            return False

        # Create validator instance
        validator = validator_class()

        # Call the appropriate validation method
        if schema_type == "decorator":
            return validator.validate_decorator(file_path)
        elif schema_type == "registry":
            return validator.validate_registry_entry(file_path)
        elif schema_type == "api":
            return validator.validate_api_request(file_path)
        elif schema_type == "package":
            return validator.validate_extension_package(file_path)
        else:
            print(f"Error: Unknown schema type '{schema_type}'")
            return False
    except ImportError:
        # Fall back to using the validate_decorators.py script directly
        import subprocess

        cmd = [
            sys.executable,
            os.path.join(os.path.dirname(__file__), "validate_decorators.py"),
            schema_type,
            "--file",
            file_path,
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Validation failed: {result.stderr}")
            return False
        return True


def validate_syntax(text: str) -> bool:
    """
    Validate decorator syntax in a prompt.

    Args:
        text: Prompt text to validate

    Returns:
        True if syntax is valid, False otherwise
    """
    try:
        # Import the parser functions from the dynamic_decorator module
        from prompt_decorators.core.dynamic_decorator import extract_decorators

        # Extract decorators from the prompt
        decorators, cleaned_text = extract_decorators(text)

        # Print found decorators
        print(f"Found {len(decorators)} decorator(s):")
        for i, decorator in enumerate(decorators, 1):
            print(f"{i}. {decorator.name} with parameters: {decorator.parameters}")

        return True
    except ImportError:
        print(
            "Error: Could not import extract_decorators. Make sure prompt_decorators is installed."
        )
        return False
    except Exception as e:
        print(f"Syntax validation failed: {str(e)}")
        return False


def validate_directory(
    dir_path: str, schema_type: str = "registry", recursive: bool = False
) -> bool:
    """
    Validate all files in a directory.

    Args:
        dir_path: Path to the directory to validate
        schema_type: Type of schema to validate against
        recursive: Whether to validate subdirectories recursively

    Returns:
        True if all validations successful, False otherwise
    """
    # Import validate_decorators only when needed
    from importlib import import_module

    try:
        # Try importing the validator module
        module = import_module("validate_decorators")
        validator_class = getattr(module, "DecoratorValidator", None)

        if not validator_class:
            print("Error: DecoratorValidator class not found in validate_decorators")
            return False

        # Create validator instance
        validator = validator_class()

        # Call the validate_directory method
        return validator.validate_directory(dir_path, schema_type)
    except ImportError:
        # Fall back to using the validate_decorators.py script directly
        import subprocess

        cmd = [
            sys.executable,
            os.path.join(os.path.dirname(__file__), "validate_decorators.py"),
            "directory",
            "--path",
            dir_path,
            "--type",
            schema_type,
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Directory validation failed: {result.stderr}")
            return False
        return True


def main() -> int:
    """Main function."""
    parser = setup_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    if args.command == "schema":
        success = validate_schema(args.file, args.schema)
    elif args.command == "syntax":
        if args.text:
            success = validate_syntax(args.text)
        else:
            try:
                with open(args.file, "r") as f:
                    text = f.read()
                success = validate_syntax(text)
            except Exception as e:
                print(f"Error reading file: {str(e)}")
                success = False
    elif args.command == "directory":
        success = validate_directory(args.directory, args.schema, args.recursive)
    else:
        print(f"Unknown command: {args.command}")
        success = False

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())

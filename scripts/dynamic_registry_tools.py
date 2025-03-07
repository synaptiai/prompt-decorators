#!/usr/bin/env python
"""
Command-line tool for managing dynamic decorators.

This script provides utilities for:
1. Listing available decorators
2. Validating decorator definitions
3. Testing decorators with sample prompts
"""

import argparse
import json
import logging
import sys
from typing import Any, Dict, List, Optional

from prompt_decorators.core.dynamic_decorator import DynamicDecorator
from prompt_decorators.dynamic_decorators_module import (
    DecoratorDefinition,
    apply_dynamic_decorators,
    create_decorator_instance,
    get_available_decorators,
    load_decorator_definitions,
)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("dynamic-registry-tools")


def list_decorators(args: argparse.Namespace) -> None:
    """List all available decorators."""
    logger.info("Listing available decorators...")

    # Get all available decorators
    decorators = get_available_decorators()

    print(f"Found {len(decorators)} decorators:")

    # Filter decorators if category is specified
    if args.category:
        filtered_decorators = [
            d for d in decorators if d.category.lower() == args.category.lower()
        ]
        print(
            f"Filtered to {len(filtered_decorators)} decorators in category '{args.category}':"
        )
        decorators = filtered_decorators

    # Sort decorators by name
    decorators.sort(key=lambda d: d.name)

    # Determine output format
    if args.format == "json":
        # Format as JSON
        decorator_list = [d.to_dict() for d in decorators]
        print(json.dumps(decorator_list, indent=2))
    else:
        # Format as text table
        for i, decorator in enumerate(decorators, 1):
            print(
                f"{i:3d}. {decorator.name:25} - {decorator.category:15} - {decorator.description}"
            )


def validate_decorators(args: argparse.Namespace) -> None:
    """Validate all decorator definitions."""
    logger.info("Validating decorator definitions...")

    # Get all available decorators
    decorators = get_available_decorators()

    print(f"Validating {len(decorators)} decorator definitions...")

    valid_count = 0
    invalid_count = 0
    invalid_decorators = []

    for decorator_def in decorators:
        try:
            # Attempt to create a decorator class from the definition
            DynamicDecorator.from_definition(decorator_def)
            valid_count += 1
        except Exception as e:
            invalid_count += 1
            invalid_decorators.append({"name": decorator_def.name, "error": str(e)})

    print(f"Validation complete: {valid_count} valid, {invalid_count} invalid")

    if invalid_count > 0:
        print("\nInvalid decorators:")
        for invalid in invalid_decorators:
            print(f"- {invalid['name']}: {invalid['error']}")
        sys.exit(1)


def test_decorator(args: argparse.Namespace) -> None:
    """Test a specific decorator with a sample prompt."""
    decorator_name = args.decorator
    prompt = args.prompt

    logger.info(f"Testing decorator '{decorator_name}' with prompt: {prompt}")

    # Create decorator instance
    try:
        decorator = create_decorator_instance(decorator_name, **vars(args))
        print(f"Created decorator instance: {decorator}")
    except Exception as e:
        print(f"Error creating decorator instance: {e}")
        sys.exit(1)

    # Apply decorator to prompt
    try:
        # Apply with dynamic decorators module
        modified_prompt = f"+++{decorator_name}"

        # Add parameters if provided
        params = {}
        for param_name, param_value in vars(args).items():
            if (
                param_name not in ["decorator", "prompt", "func"]
                and param_value is not None
            ):
                params[param_name] = param_value

        if params:
            param_str = ", ".join(
                f"{k}='{v}'" if isinstance(v, str) else f"{k}={v}"
                for k, v in params.items()
            )
            modified_prompt = f"+++{decorator_name}({param_str})"

        modified_prompt += f"\n{prompt}"

        result = apply_dynamic_decorators(modified_prompt)

        print("\nTest Results:")
        print(f"Original prompt: {prompt}")
        print(f"Modified prompt with decorator syntax: {modified_prompt}")
        print(f"Transformed prompt: {result}")
    except Exception as e:
        print(f"Error applying decorator: {e}")
        sys.exit(1)


def main() -> None:
    """Main function for the registry tools."""
    parser = argparse.ArgumentParser(
        description="Tools for managing prompt decorators."
    )
    subparsers = parser.add_subparsers(
        title="commands", dest="command", help="Command to run"
    )

    # List decorators command
    list_parser = subparsers.add_parser("list", help="List all available decorators")
    list_parser.add_argument("--category", help="Filter decorators by category")
    list_parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    list_parser.set_defaults(func=list_decorators)

    # Validate decorators command
    validate_parser = subparsers.add_parser(
        "validate", help="Validate all decorator definitions"
    )
    validate_parser.set_defaults(func=validate_decorators)

    # Test decorator command
    test_parser = subparsers.add_parser(
        "test", help="Test a specific decorator with a sample prompt"
    )
    test_parser.add_argument(
        "--decorator", required=True, help="Name of the decorator to test"
    )
    test_parser.add_argument(
        "--prompt", required=True, help="Sample prompt to test with"
    )
    # Add additional parameters that can be passed to decorators
    test_parser.add_argument("--depth", help="Depth parameter (for some decorators)")
    test_parser.add_argument("--style", help="Style parameter (for some decorators)")
    test_parser.add_argument(
        "--numbered",
        action="store_true",
        help="Numbered parameter (for some decorators)",
    )
    test_parser.add_argument("--format", help="Format parameter (for some decorators)")
    test_parser.add_argument(
        "--language", help="Language parameter (for some decorators)"
    )
    test_parser.set_defaults(func=test_decorator)

    # Parse arguments
    args = parser.parse_args()

    # If no command is specified, show help
    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    # Run the specified command
    try:
        # Load decorator definitions
        load_decorator_definitions()

        # Execute the selected function
        args.func(args)
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""Registry Tools for Prompt Decorators.

This module provides a unified command-line interface for working with the 
prompt decorators registry. It includes tools for:

1. Validating registry JSON files
2. Generating Python code for decorators defined in the registry
3. Generating tests for the Python decorator implementations

The registry is the source of truth for all decorator definitions.
This tool helps maintain consistency between the registry definitions,
the Python implementation, and the tests.

Example usage:
    
    # Validate the registry
    $ python scripts/registry_tools.py validate
    
    # Generate Python code
    $ python scripts/registry_tools.py generate-code
    
    # Generate tests 
    $ python scripts/registry_tools.py generate-tests
    
    # Run all the above in one command
    $ python scripts/registry_tools.py all

Returns:
    None: This script doesn't return anything but performs the requested actions.
"""

import argparse
import glob
import json
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Union

from jsonschema import validate


def setup_logging(verbose: bool = False) -> None:
    """Set up logging with appropriate verbosity.
    
    Args:
        verbose: Whether to enable verbose (DEBUG) logging
        
    Returns:
        None
    """
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def validate_registry(
    registry_dir: str = "registry", 
    verbose: bool = False
) -> bool:
    """Validate all decorator definitions in the registry.
    
    Args:
        registry_dir: Path to the decorator registry directory
        verbose: Whether to enable verbose output
        
    Returns:
        bool: True if validation passed, False otherwise
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Validating registry in {registry_dir}")
    
    try:
        # Load the schema
        schema_path = "schemas/registry-entry.schema.json"
        if not os.path.exists(schema_path):
            logger.error(f"Schema file not found: {schema_path}")
            return False
            
        with open(schema_path) as f:
            schema = json.load(f)
        
        # Track validation status
        all_valid = True
        issues = []
        
        # Get all JSON files in the registry
        registry_path = Path(registry_dir)
        json_files = []
        for pattern in ["*/*/decorator.json", "*/*/*.json"]:
            json_files.extend(registry_path.glob(pattern))
        
        if not json_files:
            logger.error(f"No JSON files found in {registry_dir}")
            return False
            
        logger.info(f"Found {len(json_files)} JSON files to validate")
        
        # Validate each file
        for entry_file in json_files:
            if verbose:
                logger.debug(f"Validating {entry_file}...")
                
            try:
                with open(entry_file) as f:
                    entry = json.load(f)
                
                validate(instance=entry, schema=schema)
                if verbose:
                    logger.debug(f"✓ {entry_file} is valid")
            except Exception as e:
                error_msg = f"✗ {entry_file} is invalid: {str(e)}"
                issues.append(error_msg)
                logger.error(error_msg)
                all_valid = False
                
        if all_valid:
            logger.info("✓ Registry validation passed successfully!")
            return True
        else:
            logger.error("✗ Registry validation failed with the following issues:")
            for issue in issues:
                logger.error(f"  - {issue}")
            return False
    
    except Exception as e:
        logger.error(f"Error validating registry: {e}", exc_info=True)
        return False


def generate_code(
    registry_dir: str = "registry",
    output_dir: str = "prompt_decorators/decorators/generated",
    template_dir: Optional[str] = None,
    verbose: bool = False
) -> bool:
    """Generate Python code for all decorators in the registry.
    
    Args:
        registry_dir: Path to the decorator registry directory
        output_dir: Path to output directory for generated code
        template_dir: Optional path to template directory
        verbose: Whether to enable verbose output
        
    Returns:
        bool: True if code generation succeeded, False otherwise
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Generating code from registry in {registry_dir}")
    
    try:
        # Import the code generator
        from prompt_decorators.generator.registry import RegistryScanner
        from prompt_decorators.generator.code_gen import CodeGenerator
    except ImportError as e:
        logger.error(f"Failed to import code generator: {e}")
        logger.error("Make sure prompt-decorators package is installed and in your PYTHONPATH")
        return False
    
    try:
        # Scan registry for decorator definitions
        scanner = RegistryScanner(registry_dir)
        decorators = scanner.scan()
        logger.info(f"Found {len(decorators)} decorators in registry")
        
        # Create generator and generate code
        generator = CodeGenerator(decorators)
        generator._collect_enums()  # Need to collect enums first
        generated_files = generator.generate_all()
        
        # Write to files
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        file_count = 0
        for rel_path, content in generated_files.items():
            full_path = output_path / rel_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            file_count += 1
            if verbose:
                logger.debug(f"Generated {full_path}")
        
        logger.info(f"✓ Successfully generated {file_count} files in {output_dir}")
        return True
    except Exception as e:
        logger.error(f"Error generating code: {e}", exc_info=True)
        return False


def generate_tests(
    registry_dir: str = "registry",
    output_dir: str = "tests/auto",
    template_dir: Optional[str] = None,
    verbose: bool = False
) -> bool:
    """Generate tests for all decorators in the registry.
    
    Args:
        registry_dir: Path to the decorator registry directory
        output_dir: Path where test files will be generated
        template_dir: Optional path to test template directory
        verbose: Whether to enable verbose output
        
    Returns:
        bool: True if test generation succeeded, False otherwise
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Generating tests from registry in {registry_dir}")
    
    try:
        # Import the test generator
        from prompt_decorators.generator.test_gen import TestGenerator
    except ImportError as e:
        logger.error(f"Failed to import test generator: {e}")
        logger.error("Make sure prompt-decorators package is installed and in your PYTHONPATH")
        return False
    
    try:
        # Create the test generator
        generator = TestGenerator(
            registry_dir=registry_dir,
            output_dir=output_dir,
            template_dir=template_dir,
        )
        
        # Generate tests
        generated_files = generator.generate_all_tests()
        
        if verbose:
            for file_path in generated_files:
                logger.debug(f"Generated: {file_path}")
        
        logger.info(f"✓ Successfully generated {len(generated_files)} test files in {output_dir}")
        logger.info("\nTo run the generated tests, install pytest and run:")
        logger.info(f"  python -m pytest {output_dir} -v")
        return True
    except Exception as e:
        logger.error(f"Error generating tests: {e}", exc_info=True)
        return False


def main() -> None:
    """Parse command-line arguments and run the requested actions."""
    parser = argparse.ArgumentParser(
        description="Registry tools for prompt decorators",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Validate command
    validate_parser = subparsers.add_parser(
        "validate", help="Validate the decorator registry"
    )
    validate_parser.add_argument(
        "--registry-dir",
        "-r",
        default="registry",
        help="Path to the decorator registry directory",
    )
    validate_parser.add_argument(
        "--verbose", 
        "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    # Generate code command
    code_parser = subparsers.add_parser(
        "generate-code", help="Generate Python code for decorators"
    )
    code_parser.add_argument(
        "--registry-dir",
        "-r",
        default="registry",
        help="Path to the decorator registry directory",
    )
    code_parser.add_argument(
        "--output-dir",
        "-o",
        default="prompt_decorators/decorators/generated",
        help="Path to output directory for generated code",
    )
    code_parser.add_argument(
        "--template-dir",
        "-t",
        default=None,
        help="Optional path to template directory",
    )
    code_parser.add_argument(
        "--verbose", 
        "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    # Generate tests command
    tests_parser = subparsers.add_parser(
        "generate-tests", help="Generate tests for decorators"
    )
    tests_parser.add_argument(
        "--registry-dir",
        "-r",
        default="registry",
        help="Path to the decorator registry directory",
    )
    tests_parser.add_argument(
        "--output-dir",
        "-o",
        default="tests/auto",
        help="Path where test files will be generated",
    )
    tests_parser.add_argument(
        "--template-dir",
        "-t",
        default=None,
        help="Optional path to test template directory",
    )
    tests_parser.add_argument(
        "--verbose", 
        "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    # All command
    all_parser = subparsers.add_parser(
        "all", help="Run validate, generate-code, and generate-tests"
    )
    all_parser.add_argument(
        "--registry-dir",
        "-r",
        default="registry",
        help="Path to the decorator registry directory",
    )
    all_parser.add_argument(
        "--code-output-dir",
        default="prompt_decorators/decorators/generated",
        help="Path to output directory for generated code",
    )
    all_parser.add_argument(
        "--tests-output-dir",
        default="tests/auto",
        help="Path where test files will be generated",
    )
    all_parser.add_argument(
        "--template-dir",
        "-t",
        default=None,
        help="Optional path to template directory",
    )
    all_parser.add_argument(
        "--verbose", 
        "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Set up logging
    setup_logging(args.verbose if hasattr(args, 'verbose') else False)
    
    # Execute the requested command
    if args.command == "validate":
        success = validate_registry(
            registry_dir=args.registry_dir,
            verbose=args.verbose,
        )
        if not success:
            sys.exit(1)
    
    elif args.command == "generate-code":
        success = generate_code(
            registry_dir=args.registry_dir,
            output_dir=args.output_dir,
            template_dir=args.template_dir,
            verbose=args.verbose,
        )
        if not success:
            sys.exit(1)
    
    elif args.command == "generate-tests":
        success = generate_tests(
            registry_dir=args.registry_dir,
            output_dir=args.output_dir,
            template_dir=args.template_dir,
            verbose=args.verbose,
        )
        if not success:
            sys.exit(1)
    
    elif args.command == "all":
        # Run all commands in sequence
        logger = logging.getLogger(__name__)
        logger.info("Running all commands: validate, generate-code, generate-tests")
        
        validation_success = validate_registry(
            registry_dir=args.registry_dir,
            verbose=args.verbose,
        )
        
        if not validation_success:
            logger.error("Validation failed, stopping the process")
            sys.exit(1)
        
        code_success = generate_code(
            registry_dir=args.registry_dir,
            output_dir=args.code_output_dir,
            template_dir=args.template_dir,
            verbose=args.verbose,
        )
        
        if not code_success:
            logger.error("Code generation failed, stopping the process")
            sys.exit(1)
        
        tests_success = generate_tests(
            registry_dir=args.registry_dir,
            output_dir=args.tests_output_dir,
            template_dir=args.template_dir,
            verbose=args.verbose,
        )
        
        if not tests_success:
            logger.error("Test generation failed")
            sys.exit(1)
        
        logger.info("✓ All operations completed successfully")
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main() 
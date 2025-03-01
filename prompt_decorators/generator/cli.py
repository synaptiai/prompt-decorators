#!/usr/bin/env python
"""
CLI for the prompt decorators generator.

This module provides a command-line interface for:
1. Scanning the registry for decorator definitions
2. Generating Python code for the decorators
3. Generating tests for the decorators
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Optional, Dict, Any
import json

from .registry import RegistryScanner
from .code_gen import CodeGenerator
from .test_gen import TestGenerator

def scan_registry(args: argparse.Namespace) -> None:
    """
    Scan the registry and report on found decorators.
    
    Args:
        args: Command-line arguments
    """
    scanner = RegistryScanner(args.registry_dir)
    decorator_files = scanner.scan()
    
    print(f"Found {len(decorator_files)} decorator files:")
    for file in decorator_files:
        print(f"  - {file}")

def generate_code(args: argparse.Namespace) -> None:
    """
    Generate Python code for decorators in the registry.
    
    Args:
        args: Command-line arguments
    """
    scanner = RegistryScanner(args.registry_dir)
    decorator_files = scanner.scan()
    
    # Load decorator data
    decorators = []
    for file_path in decorator_files:
        with open(file_path, 'r') as f:
            data = json.load(f)
            data['_source_file'] = str(file_path)
            decorators.append(data)
    
    # Create generator
    generator = CodeGenerator(decorators)
    
    # Generate code
    generated_files = generator.generate_all()
    
    # Write to files
    output_dir = Path(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)
    
    file_count = 0
    for rel_path, content in generated_files.items():
        file_path = output_dir / rel_path
        os.makedirs(file_path.parent, exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        file_count += 1
    
    if args.verbose:
        print(f"Generated {file_count} files:")
        for rel_path in generated_files.keys():
            print(f"  - {output_dir / rel_path}")
    else:
        print(f"Generated {file_count} files.")

def generate_tests(args: argparse.Namespace) -> None:
    """
    Generate tests for decorators in the registry.
    
    Args:
        args: Command-line arguments
    """
    generator = TestGenerator(
        registry_dir=args.registry_dir,
        output_dir=args.output_dir,
        template_dir=args.template_dir
    )
    
    generated_files = generator.generate_all_tests()
    
    if args.verbose:
        print(f"Generated {len(generated_files)} test files:")
        for file in generated_files:
            print(f"  - {file}")
    else:
        print(f"Generated {len(generated_files)} test files.")

def main() -> None:
    """
    Main entry point for the CLI.
    """
    parser = argparse.ArgumentParser(
        description="Generator tool for prompt decorators",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Scan command
    scan_parser = subparsers.add_parser(
        "scan", 
        help="Scan the registry for decorator definitions"
    )
    scan_parser.add_argument(
        "--registry-dir", "-r",
        default="registry",
        help="Path to the decorator registry directory"
    )
    
    # Generate code command
    generate_parser = subparsers.add_parser(
        "generate", 
        help="Generate Python code for decorators"
    )
    generate_parser.add_argument(
        "--registry-dir", "-r",
        default="registry",
        help="Path to the decorator registry directory"
    )
    generate_parser.add_argument(
        "--output-dir", "-o",
        default="prompt_decorators/decorators/generated",
        help="Path to the output directory for generated code"
    )
    generate_parser.add_argument(
        "--template-dir", "-t",
        default=None,
        help="Path to the template directory (optional)"
    )
    generate_parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    # Generate tests command
    tests_parser = subparsers.add_parser(
        "tests", 
        help="Generate tests for decorators"
    )
    tests_parser.add_argument(
        "--registry-dir", "-r",
        default="registry",
        help="Path to the decorator registry directory"
    )
    tests_parser.add_argument(
        "--output-dir", "-o",
        default="tests/auto",
        help="Path to the output directory for generated tests"
    )
    tests_parser.add_argument(
        "--template-dir", "-t",
        default=None,
        help="Path to the template directory (optional)"
    )
    tests_parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    if args.command == "scan":
        scan_registry(args)
    elif args.command == "generate":
        generate_code(args)
    elif args.command == "tests":
        generate_tests(args)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main() 
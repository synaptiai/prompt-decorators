#!/usr/bin/env python
"""
Test Runner for Prompt Decorators

This script runs the test suite for prompt decorators. It can:
1. Generate tests for all decorators in the registry
2. Run the tests and report results
3. Generate a test coverage report

Usage:
    python run_tests.py [options]

Options:
    --generate              Generate tests before running
    --coverage              Generate coverage report
    --verbose, -v           Verbose output
    --test-dir=PATH         Path to test directory (default: tests)
    --registry-dir=PATH     Path to registry directory (default: registry)
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
import importlib.util

# Check if pytest is available
try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False

# Check if coverage is available
try:
    import coverage
    COVERAGE_AVAILABLE = True
except ImportError:
    COVERAGE_AVAILABLE = False


def check_requirements():
    """Check if all required packages are installed."""
    missing = []
    
    if not PYTEST_AVAILABLE:
        missing.append("pytest")
    
    if missing:
        print("Error: Missing required packages:")
        for package in missing:
            print(f"  - {package}")
        print("\nPlease install the missing packages with:")
        print(f"  pip install {' '.join(missing)}")
        sys.exit(1)


def generate_tests(args):
    """Generate tests for decorators."""
    # Import the test generator
    try:
        from prompt_decorators.generator.test_gen import TestGenerator
    except ImportError:
        print("Error: Could not import TestGenerator. Make sure prompt-decorators is installed.")
        sys.exit(1)
    
    # Create the generator
    generator = TestGenerator(
        registry_dir=args.registry_dir,
        output_dir=os.path.join(args.test_dir, "auto"),
        template_dir=None
    )
    
    # Generate tests
    print("Generating decorator tests...")
    generated_files = generator.generate_all_tests()
    
    print(f"Generated {len(generated_files)} test files.")
    if args.verbose:
        for file_path in generated_files:
            print(f"  - {file_path}")


def run_tests(args):
    """Run the test suite."""
    check_requirements()
    
    # Build pytest arguments
    pytest_args = [args.test_dir]
    
    if args.verbose:
        pytest_args.append("-v")
    
    # Run with coverage if requested
    if args.coverage and COVERAGE_AVAILABLE:
        pytest_args = [
            "--cov=prompt_decorators",
            "--cov-report=term",
            "--cov-report=html:coverage_html"
        ] + pytest_args
    
    print(f"Running tests with pytest...")
    return pytest.main(pytest_args)


def main():
    """Main entry point for the test runner."""
    parser = argparse.ArgumentParser(
        description="Test runner for prompt decorators",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "--generate",
        action="store_true",
        help="Generate tests before running"
    )
    
    parser.add_argument(
        "--coverage",
        action="store_true",
        help="Generate coverage report"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    
    parser.add_argument(
        "--test-dir",
        default="tests",
        help="Path to test directory"
    )
    
    parser.add_argument(
        "--registry-dir",
        default="registry",
        help="Path to registry directory"
    )
    
    args = parser.parse_args()
    
    # Generate tests if requested
    if args.generate:
        generate_tests(args)
    
    # Run tests
    result = run_tests(args)
    
    # Return exit code
    sys.exit(result)


if __name__ == "__main__":
    main() 
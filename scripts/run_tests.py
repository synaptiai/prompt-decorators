#!/usr/bin/env python
"""Test Runner for Prompt Decorators

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
import argparse
import os
import sys

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
    """
    Check if all required packages are installed.

    Returns:
        None
    """
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
    """
    Generate tests for decorators.

    Args:
        args: Command-line arguments

    Returns:
        None
    """
    # Use registry_tools.py for test generation instead of duplicating logic
    try:
        from scripts.registry_tools import generate_tests as registry_generate_tests
    except ImportError:
        print(
            "Error: Could not import generate_tests from registry_tools. Make sure "
            "the script is available."
        )
        sys.exit(1)

    # Call the generate_tests function from registry_tools
    print("Generating decorator tests...")
    success = registry_generate_tests(
        registry_dir=args.registry_dir,
        output_dir=os.path.join(args.test_dir, "auto"),
        verbose=args.verbose,
    )

    if not success:
        print("Error: Test generation failed.")
        sys.exit(1)

    print("Test generation completed successfully.")


def run_tests(args):
    """
    Run the test suite.

    Args:
        args: Command-line arguments

    Returns:
        Exit code from pytest
    """
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
            "--cov-report=html:coverage_html",
        ] + pytest_args

    print("Running tests with pytest...")
    return pytest.main(pytest_args)


def main():
    """
    Main entry point for the test runner.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        description="Test runner for prompt decorators",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--generate", action="store_true", help="Generate tests before running"
    )

    parser.add_argument(
        "--coverage", action="store_true", help="Generate coverage report"
    )

    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    parser.add_argument("--test-dir", default="tests", help="Path to test directory")

    parser.add_argument(
        "--registry-dir", default="registry", help="Path to registry directory"
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

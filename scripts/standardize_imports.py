#!/usr/bin/env python3
"""
This script uses isort to sort and format imports according to the configuration
in pyproject.toml.
"""

import argparse
import subprocess
import sys


def run_isort(directory, check_only=False):
    """
    Run isort on the specified directory.

    Args:
        directory: The directory to run isort on
        check_only: If True, only check for issues without modifying files

    Returns:
        The exit code from the isort command
    """
    try:
        # Build the isort command
        cmd = ["isort"]

        # Add check flag if requested
        if check_only:
            cmd.append("--check")

        # Add the directory to process
        cmd.append(directory)

        # Run the command
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)

        # Print output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)

        # Return the exit code
        return result.returncode

    except FileNotFoundError:
        print("Error: isort not found. Please install it with: pip install isort")
        return 1
    except Exception as e:
        print(f"Error running isort: {e}")
        return 1


def main():
    """
    Main function to run isort on the prompt_decorators package.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    parser = argparse.ArgumentParser(description="Sort and format imports using isort")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check for issues without modifying files",
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to process (default: current directory)",
    )

    args = parser.parse_args()
    return run_isort(args.directory, args.check)


if __name__ == "__main__":
    sys.exit(main())

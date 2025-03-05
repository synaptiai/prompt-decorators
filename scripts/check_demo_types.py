#!/usr/bin/env python3
"""
Run strict type checking on the demo directory.

This script applies the same strict mypy settings that are used in CI to validate
the demo directory. It should be run manually before pushing changes to ensure
the CI pipeline will pass.
"""

import os
import subprocess
import sys
from pathlib import Path


def main():
    """Run mypy with strict settings on the demo directory."""
    print("Running strict type checking on demo directory...")

    # Get the repo root directory (assuming script is in scripts/ directory)
    repo_root = Path(__file__).parent.parent

    # Change to the repo root directory
    os.chdir(repo_root)

    # Run mypy with the same settings as used in CI
    result = subprocess.run(
        ["poetry", "run", "mypy", "--warn-return-any", "demo/"],
        capture_output=True,
        text=True,
    )

    # Print output
    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr, file=sys.stderr)

    # Return the exit code
    if result.returncode != 0:
        print("Type checking failed! Please fix the issues before pushing.")
        return 1
    else:
        print("Type checking passed successfully.")
        return 0


if __name__ == "__main__":
    sys.exit(main())

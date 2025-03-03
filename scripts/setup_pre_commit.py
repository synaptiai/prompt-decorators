#!/usr/bin/env python
"""
This script helps developers set up pre-commit hooks for the project.
It installs pre-commit and the hooks defined in .pre-commit-config.yaml.
"""

import os
import subprocess
import sys
from pathlib import Path


def check_pre_commit_installed():
    """
    Check if pre-commit is installed.

    Returns:
        bool: True if pre-commit is installed, False otherwise
    """
    try:
        subprocess.run(
            ["pre-commit", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False


def install_pre_commit():
    """
    Install pre-commit using pip.

    Returns:
        bool: True if installation was successful, False otherwise
    """
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "pre-commit"], check=True
        )
        return True
    except subprocess.SubprocessError:
        return False


def install_hooks():
    """
    Install pre-commit hooks.

    Returns:
        bool: True if hooks installation was successful, False otherwise
    """
    try:
        subprocess.run(["pre-commit", "install"], check=True)
        return True
    except subprocess.SubprocessError:
        return False


def run_hooks_on_all_files():
    """
    Run pre-commit hooks on all files.

    Returns:
        bool: True if hook run was successful, False otherwise
    """
    try:
        subprocess.run(
            ["pre-commit", "run", "--all-files"],
            check=False,  # Don't fail if hooks find issues
        )
        return True
    except subprocess.SubprocessError:
        return False


def main():
    """
    Main function to set up pre-commit hooks.

    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
    # Ensure we're in the project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)

    print("Setting up pre-commit hooks for Prompt Decorators project")
    print("=" * 60)

    # Check if pre-commit is installed
    if not check_pre_commit_installed():
        if not install_pre_commit():
            print("Failed to install pre-commit. Please install it manually with:")
            print("    pip install pre-commit")
            return 1

    # Install the hooks
    if not install_hooks():
        print("Failed to install pre-commit hooks.")
        return 1

    # Run hooks on all files
    run_hooks_on_all_files()

    print("=" * 60)
    print("Pre-commit hooks setup complete!")
    print("Hooks will now run automatically on each commit.")
    print("To run hooks manually on all files, use: pre-commit run --all-files")
    print("To run hooks manually on staged files, use: pre-commit run")

    return 0


if __name__ == "__main__":
    sys.exit(main())

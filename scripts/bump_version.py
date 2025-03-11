#!/usr/bin/env python
"""
Version bumping script for prompt-decorators.

This script automates the process of bumping the version in pyproject.toml,
creating a git commit and tag, and optionally pushing changes to GitHub.

Usage:
    python scripts/bump_version.py patch|minor|major [--push]
"""

import argparse
import subprocess
import sys


def run_command(cmd, check=True):
    """Run a shell command and return the output."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    return result.stdout.strip()


def main():
    """Main function to handle version bumping."""
    parser = argparse.ArgumentParser(description="Bump version and create git tag")
    parser.add_argument(
        "bump_type",
        choices=["patch", "minor", "major"],
        help="Type of version bump",
    )
    parser.add_argument("--push", action="store_true", help="Push to GitHub")
    args = parser.parse_args()

    # Check if there are uncommitted changes
    status = run_command(["git", "status", "--porcelain"])
    if status:
        print(
            "Error: There are uncommitted changes. Please commit or stash them first."
        )
        sys.exit(1)

    # Bump version in pyproject.toml
    run_command(["poetry", "version", args.bump_type])

    # Get the new version
    version = run_command(["poetry", "version", "-s"])

    # Check if tag already exists
    tags = run_command(["git", "tag"])
    if f"v{version}" in tags.split("\n"):
        print(f"Error: Tag v{version} already exists.")
        sys.exit(1)

    # Commit the change
    run_command(["git", "add", "pyproject.toml"])
    run_command(["git", "commit", "-m", f"Bump version to {version}"])

    # Create a tag
    run_command(["git", "tag", f"v{version}"])

    if args.push:
        run_command(["git", "push", "origin", "main"])
        run_command(["git", "push", "origin", f"v{version}"])

    print(f"\n✅ Version bumped to {version}")
    if not args.push:
        print("\nRemember to push changes with:")
        print(f"  git push origin main && git push origin v{version}")

    print("\nNext steps:")
    print("1. Push changes to GitHub (if not done automatically)")
    print("2. Go to GitHub and create a release from the tag")
    print("   https://github.com/synaptiai/prompt-decorators/releases/new")
    print(
        "3. The GitHub Action will automatically publish to PyPI when the release is created"
    )


if __name__ == "__main__":
    main()

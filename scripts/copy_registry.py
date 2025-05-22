#!/usr/bin/env python
"""
Script to copy registry files to the package directory.

This script copies the registry files from the source directory to the package directory
during the build process. It is intended to be run before building the package.

Usage:
    python scripts/copy_registry.py

The script will:
1. Check if the source registry directory exists
2. Create the package registry directory if it doesn't exist
3. Copy all files from the source registry to the package registry
"""

import shutil
import sys
from pathlib import Path


def copy_registry() -> bool:
    """Copy registry files to the package directory.

    Returns:
        bool: True if copy was successful, False otherwise
    """
    # Get the current directory
    current_dir = Path.cwd()

    # Define the paths
    source_registry = current_dir / "registry"
    package_registry = current_dir / "prompt_decorators" / "registry"

    # Check if the source registry directory exists
    if not source_registry.exists():
        print(f"Source registry directory not found: {source_registry}")
        return False

    # Create the package registry directory if it doesn't exist
    package_registry.mkdir(parents=True, exist_ok=True)

    # Copy all files from the source registry to the package registry
    print(f"Copying files from {source_registry} to {package_registry}")

    # Create subdirectories
    for subdir in ["core", "extensions", "simplified_decorators"]:
        source_subdir = source_registry / subdir
        package_subdir = package_registry / subdir

        if source_subdir.exists():
            # Create the subdirectory in the package registry
            package_subdir.mkdir(exist_ok=True)

            # Copy all files from the source subdirectory to the package subdirectory
            for item in source_subdir.glob("**/*"):
                if item.is_file():
                    # Create the corresponding path in the package registry
                    rel_path = item.relative_to(source_subdir)
                    dest_path = package_subdir / rel_path

                    # Create parent directories if they don't exist
                    dest_path.parent.mkdir(parents=True, exist_ok=True)

                    # Copy the file
                    shutil.copy2(item, dest_path)
                    print(f"Copied {item} to {dest_path}")

    return True


if __name__ == "__main__":
    if copy_registry():
        print("Registry files copied successfully.")
    else:
        print("Failed to copy registry files.")
        sys.exit(1)

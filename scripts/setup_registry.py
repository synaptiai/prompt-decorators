#!/usr/bin/env python
"""
Setup script for the registry directory.

This script creates a symlink from the registry directory to the prompt_decorators/registry
directory for backward compatibility. It is intended to be run during installation.

Usage:
    python scripts/setup_registry.py

The script will:
1. Check if the prompt_decorators/registry directory exists
2. Check if the registry directory exists
3. If the registry directory doesn't exist, create a symlink to prompt_decorators/registry
4. If the registry directory exists but is not a symlink, copy the files to the package registry
   and then create a symlink
"""

import os
import shutil
import sys
from pathlib import Path


def setup_registry() -> bool:
    """Set up the registry directory.

    Returns:
        bool: True if setup was successful, False otherwise
    """
    # Get the current directory
    current_dir = Path.cwd()

    # Define the paths
    package_registry = current_dir / "prompt_decorators" / "registry"
    source_registry = current_dir / "registry"

    # Check if the package registry directory exists
    if not package_registry.exists():
        print(f"Creating package registry directory: {package_registry}")
        package_registry.mkdir(parents=True, exist_ok=True)

        # Create subdirectories
        for subdir in ["core", "extensions", "simplified_decorators"]:
            (package_registry / subdir).mkdir(exist_ok=True)

    # Check if the source registry directory exists
    if source_registry.exists():
        if source_registry.is_symlink():
            print(f"Registry directory is already a symlink: {source_registry}")
            return True

        # If it's a regular directory, copy files to package registry
        print(f"Copying files from {source_registry} to {package_registry}")
        for item in source_registry.glob("**/*"):
            if item.is_file():
                # Create the corresponding path in the package registry
                rel_path = item.relative_to(source_registry)
                dest_path = package_registry / rel_path

                # Create parent directories if they don't exist
                dest_path.parent.mkdir(parents=True, exist_ok=True)

                # Copy the file
                shutil.copy2(item, dest_path)

        # Rename the original registry directory
        backup_registry = current_dir / "registry.bak"
        print(f"Renaming {source_registry} to {backup_registry}")
        source_registry.rename(backup_registry)

    # Create a symlink from registry to prompt_decorators/registry
    print(f"Creating symlink from {source_registry} to {package_registry}")
    try:
        # Use relative path for the symlink target
        rel_path_str = os.path.relpath(str(package_registry), str(current_dir))
        # Convert the Path object to string for os.symlink
        source_registry_str = str(source_registry)
        os.symlink(rel_path_str, source_registry_str, target_is_directory=True)
        print(f"Symlink created successfully: {source_registry} -> {rel_path_str}")
    except OSError as e:
        print(f"Error creating symlink: {e}")
        print("You may need to run this script with administrator privileges.")
        return False

    return True


if __name__ == "__main__":
    if setup_registry():
        print("Registry setup completed successfully.")
    else:
        print("Registry setup failed.")
        sys.exit(1)

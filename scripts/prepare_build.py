#!/usr/bin/env python3
"""Pre-build script to ensure registry files are copied during build process.

This script ensures that registry files from the source directory are properly
copied to the package directory before building, preventing the registry loading
issues that occur when the package is installed without its built-in decorators.
"""

import os
import shutil
import sys
from pathlib import Path
from typing import List, Tuple


def find_project_root() -> Path:
    """Find the project root directory by looking for pyproject.toml."""
    current = Path(__file__).parent
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent
    raise RuntimeError("Could not find project root (no pyproject.toml found)")


def copy_registry_files(source_dir: Path, target_dir: Path) -> Tuple[int, List[str]]:
    """Copy registry files from source to target directory.

    Args:
        source_dir: Source registry directory
        target_dir: Target registry directory

    Returns:
        Tuple of (files_copied, error_messages)
    """
    files_copied = 0
    errors = []

    if not source_dir.exists():
        errors.append(f"Source registry directory not found: {source_dir}")
        return files_copied, errors

    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)

    # Copy subdirectories and their contents
    subdirs = ["core", "extensions", "simplified_decorators"]

    for subdir in subdirs:
        source_subdir = source_dir / subdir
        target_subdir = target_dir / subdir

        if not source_subdir.exists():
            print(f"Warning: Source subdirectory not found: {source_subdir}")
            continue

        # Create target subdirectory
        target_subdir.mkdir(parents=True, exist_ok=True)

        # Copy all JSON files recursively
        for json_file in source_subdir.rglob("*.json"):
            try:
                # Calculate relative path from source subdir
                rel_path = json_file.relative_to(source_subdir)
                target_file = target_subdir / rel_path

                # Create parent directories if needed
                target_file.parent.mkdir(parents=True, exist_ok=True)

                # Copy the file
                shutil.copy2(json_file, target_file)
                files_copied += 1
                print(f"Copied: {json_file} -> {target_file}")

            except Exception as e:
                error_msg = f"Error copying {json_file}: {e}"
                errors.append(error_msg)
                print(f"Error: {error_msg}")

    return files_copied, errors


def main() -> int:
    """Main function to prepare build by copying registry files."""
    try:
        # Find project root
        project_root = find_project_root()
        print(f"Project root: {project_root}")

        # Define source and target directories
        source_registry = project_root / "registry"
        target_registry = project_root / "prompt_decorators" / "registry"

        print(f"Source registry: {source_registry}")
        print(f"Target registry: {target_registry}")

        # Copy registry files
        files_copied, errors = copy_registry_files(source_registry, target_registry)

        # Report results
        print(f"\nBuild preparation completed:")
        print(f"  Files copied: {files_copied}")
        print(f"  Errors: {len(errors)}")

        if errors:
            print("\nErrors encountered:")
            for error in errors:
                print(f"  - {error}")
            return 1

        if files_copied == 0:
            print(
                "Warning: No registry files were copied. This may cause runtime issues."
            )
            return 1

        print("✅ Registry files successfully prepared for build")
        return 0

    except Exception as e:
        print(f"Fatal error during build preparation: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

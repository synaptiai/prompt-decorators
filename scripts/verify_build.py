#!/usr/bin/env python3
"""Post-build verification script to ensure registry files are included in the package.

This script verifies that the built package contains all necessary registry files
and that they can be loaded properly. It helps catch build issues before distribution.
"""

import json
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Dict, List, Tuple


def find_project_root() -> Path:
    """Find the project root directory by looking for pyproject.toml."""
    current = Path(__file__).parent
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent
    raise RuntimeError("Could not find project root (no pyproject.toml found)")


def find_wheel_file(dist_dir: Path) -> Path:
    """Find the most recent wheel file in the dist directory."""
    wheel_files = list(dist_dir.glob("*.whl"))
    if not wheel_files:
        raise RuntimeError(f"No wheel files found in {dist_dir}")

    # Return the most recently created wheel file
    return max(wheel_files, key=lambda p: p.stat().st_mtime)


def verify_wheel_contents(wheel_path: Path) -> Tuple[bool, List[str], Dict[str, int]]:
    """Verify that the wheel contains the expected registry files.

    Args:
        wheel_path: Path to the wheel file

    Returns:
        Tuple of (success, errors, file_counts)
    """
    errors = []
    file_counts = {"core": 0, "extensions": 0, "simplified_decorators": 0}

    try:
        with zipfile.ZipFile(wheel_path, "r") as wheel:
            # List all files in the wheel
            all_files = wheel.namelist()

            # Check for registry directory structure
            registry_files = [
                f for f in all_files if "prompt_decorators/registry/" in f
            ]

            if not registry_files:
                errors.append("No registry files found in wheel")
                return False, errors, file_counts

            # Count files in each subdirectory
            for file_path in registry_files:
                if file_path.endswith(".json"):
                    if "/core/" in file_path:
                        file_counts["core"] += 1
                    elif "/extensions/" in file_path:
                        file_counts["extensions"] += 1
                    elif "/simplified_decorators/" in file_path:
                        file_counts["simplified_decorators"] += 1

            # Verify we have files in at least one subdirectory
            total_files = sum(file_counts.values())
            if total_files == 0:
                errors.append(
                    "No JSON decorator files found in registry subdirectories"
                )
                return False, errors, file_counts

            # Try to validate a few JSON files
            json_files = [f for f in registry_files if f.endswith(".json")]
            validated_files = 0

            for json_file in json_files[:5]:  # Validate up to 5 files
                try:
                    content = wheel.read(json_file)
                    data = json.loads(content.decode("utf-8"))

                    # Basic validation - check for required fields
                    if "decoratorName" not in data:
                        errors.append(
                            f"Invalid decorator file {json_file}: missing 'decoratorName'"
                        )
                    else:
                        validated_files += 1

                except json.JSONDecodeError as e:
                    errors.append(f"Invalid JSON in {json_file}: {e}")
                except Exception as e:
                    errors.append(f"Error reading {json_file}: {e}")

            print(f"Validated {validated_files} JSON files successfully")

    except Exception as e:
        errors.append(f"Error reading wheel file: {e}")
        return False, errors, file_counts

    return len(errors) == 0, errors, file_counts


def verify_package_installation() -> Tuple[bool, List[str]]:
    """Verify that the package can be imported and registry loaded.

    Returns:
        Tuple of (success, errors)
    """
    errors = []

    try:
        # Try to import the package
        import prompt_decorators
        from prompt_decorators.core.dynamic_decorator import DynamicDecorator

        # Try to load the registry
        DynamicDecorator.load_registry()

        # Check how many decorators were loaded
        decorator_count = len(DynamicDecorator._registry)

        if decorator_count == 0:
            errors.append(
                "No decorators loaded from registry - package installation may be incomplete"
            )
        else:
            print(f"Successfully loaded {decorator_count} decorators from registry")

            # List a few decorator names for verification
            decorator_names = list(DynamicDecorator._registry.keys())[:5]
            print(f"Sample decorators: {decorator_names}")

    except ImportError as e:
        errors.append(f"Failed to import prompt_decorators: {e}")
    except Exception as e:
        errors.append(f"Error during package verification: {e}")

    return len(errors) == 0, errors


def main() -> int:
    """Main function to verify build output."""
    try:
        project_root = find_project_root()
        dist_dir = project_root / "dist"

        print(f"Project root: {project_root}")
        print(f"Dist directory: {dist_dir}")

        if not dist_dir.exists():
            print("Error: dist directory not found. Run build first.")
            return 1

        # Find and verify wheel file
        try:
            wheel_path = find_wheel_file(dist_dir)
            print(f"Verifying wheel: {wheel_path}")
        except RuntimeError as e:
            print(f"Error: {e}")
            return 1

        # Verify wheel contents
        success, errors, file_counts = verify_wheel_contents(wheel_path)

        print(f"\nWheel verification results:")
        print(f"  Registry files found:")
        for subdir, count in file_counts.items():
            print(f"    {subdir}: {count} files")

        if errors:
            print(f"\nErrors found:")
            for error in errors:
                print(f"  - {error}")

        if not success:
            print("❌ Wheel verification failed")
            return 1

        print("✅ Wheel verification passed")

        # Verify package can be imported (if installed)
        print("\nTesting package import...")
        import_success, import_errors = verify_package_installation()

        if import_errors:
            print("Package import issues (may be expected if not installed):")
            for error in import_errors:
                print(f"  - {error}")
        elif import_success:
            print("✅ Package import and registry loading successful")

        return 0

    except Exception as e:
        print(f"Fatal error during build verification: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

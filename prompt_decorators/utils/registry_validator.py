"""Registry validation and auto-repair utilities.

This module provides comprehensive validation and automatic repair capabilities
for the prompt decorators registry, helping to diagnose and fix common installation
issues where registry files are missing or incomplete.
"""

import json
import logging
import shutil
from importlib import resources
from pathlib import Path

# Ensure Literal is imported
from typing import Any, Dict, List, Literal, Optional, Tuple, TypedDict, Union, cast

logger = logging.getLogger(__name__)


class _InfoSubdirectoriesEntry(TypedDict):
    """Structure for package and source file counts within a subdirectory."""

    package: int
    source: int


class _InfoSubdirectoriesType(TypedDict):
    """TypedDict for subdirectories core, extensions, and simplified_decorators."""

    core: _InfoSubdirectoriesEntry
    extensions: _InfoSubdirectoriesEntry
    simplified_decorators: _InfoSubdirectoriesEntry


class InfoDictStructure(TypedDict):
    """TypedDict for the overall registry information structure."""

    package_registry_exists: bool
    source_registry_exists: bool
    package_file_count: int
    source_file_count: int
    package_registry_path: Optional[str]
    source_registry_path: Optional[str]
    subdirectories: _InfoSubdirectoriesType


class RegistryValidator:
    """Utility class for validating and repairing the decorator registry."""

    @staticmethod
    def get_registry_info() -> InfoDictStructure:  # Changed return type
        """Get comprehensive information about the registry state.

        Returns:
            Dictionary containing registry status information
        """
        # Explicitly type the info dictionary using the TypedDict
        info: InfoDictStructure = {
            "package_registry_exists": False,
            "source_registry_exists": False,
            "package_file_count": 0,
            "source_file_count": 0,
            "package_registry_path": None,
            "source_registry_path": None,
            "subdirectories": {
                "core": {"package": 0, "source": 0},
                "extensions": {"package": 0, "source": 0},
                "simplified_decorators": {"package": 0, "source": 0},
            },
        }

        # Define the literal keys to iterate over
        subdir_keys: List[Literal["core", "extensions", "simplified_decorators"]] = [
            "core",
            "extensions",
            "simplified_decorators",
        ]

        # Check package registry
        try:
            # Try to find package registry using importlib.resources
            try:
                from importlib.resources import files

                package_registry = files("prompt_decorators").joinpath("registry")
                if package_registry.is_dir():
                    info["package_registry_exists"] = True
                    info["package_registry_path"] = str(package_registry)

                    # Count files in each subdirectory
                    for key_literal in subdir_keys:
                        subdir_path = package_registry.joinpath(key_literal)
                        if subdir_path.is_dir():
                            json_files = [
                                f
                                for f in subdir_path.iterdir()  # type: ignore[attr-defined]
                                if f.is_file() and f.name.endswith(".json")  # type: ignore[attr-defined]
                            ]
                            info["subdirectories"][key_literal]["package"] = len(
                                json_files
                            )
                            info["package_file_count"] = info[
                                "package_file_count"
                            ] + len(json_files)

            except (ImportError, AttributeError):
                # Fallback for older Python versions
                if resources.is_resource("prompt_decorators", "registry"):
                    info["package_registry_exists"] = True
                    # Note: Counting files is more complex with older API

        except Exception as e:
            logger.debug(f"Error checking package registry: {e}")

        # Check source registry (relative to project root)
        try:
            # Find project root by looking for common project files
            current = Path(__file__).parent
            project_root = None

            # Walk up the directory tree looking for project indicators
            while current != current.parent:
                if any(
                    (current / indicator).exists()
                    for indicator in ["pyproject.toml", "setup.py", ".git"]
                ):
                    project_root = current
                    break
                current = current.parent

            if project_root:
                source_registry_dir = (
                    project_root / "registry"
                )  # Renamed to avoid confusion with Path object
                if source_registry_dir.exists():
                    info["source_registry_exists"] = True
                    info["source_registry_path"] = str(source_registry_dir)

                    # Count files in each subdirectory
                    for key_literal in subdir_keys:
                        subdir_path = source_registry_dir / key_literal
                        if subdir_path.exists():
                            json_files = list(subdir_path.glob("**/*.json"))
                            info["subdirectories"][key_literal]["source"] = len(
                                json_files
                            )
                            info["source_file_count"] = info["source_file_count"] + len(
                                json_files
                            )

        except Exception as e:
            logger.debug(f"Error checking source registry: {e}")

        return info

    @staticmethod
    def validate_registry() -> (
        Dict[str, Any]
    ):  # Keep Any for result for now, or define another TypedDict
        """Validate the current registry state.

        Returns:
            Dictionary containing validation results
        """
        result: Dict[str, Any] = {
            "status": "unknown",
            "issues": [],
            "recommendations": [],
        }

        info = RegistryValidator.get_registry_info()

        # Check if package registry exists and has files
        if not info["package_registry_exists"]:
            result["issues"].append("Package registry directory not found")
            result["status"] = "critical"
        elif info["package_file_count"] == 0:
            result["issues"].append(
                "Package registry exists but contains no decorator files"
            )
            result["status"] = "needs_repair"
        else:
            # Check individual subdirectories
            missing_subdirs: List[str] = []
            # Iterate using the predefined literal keys for type safety
            subdir_literal_keys: List[
                Literal["core", "extensions", "simplified_decorators"]
            ] = [
                "core",
                "extensions",
                "simplified_decorators",
            ]
            for key in subdir_literal_keys:
                counts_entry = info["subdirectories"][key]
                if counts_entry["package"] == 0:
                    missing_subdirs.append(key)

            if missing_subdirs:
                result["issues"].append(
                    f"Missing decorators in subdirectories: {missing_subdirs}"
                )
                result["status"] = "needs_repair"

        # Check if source registry is available for repair
        if info["source_registry_exists"] and info["source_file_count"] > 0:
            result["recommendations"].append(
                "Source registry available for auto-repair"
            )  # Removed type: ignore

        # Determine overall status
        if result["status"] == "unknown":
            if len(result["issues"]) == 0:
                result["status"] = "healthy"
            else:
                result["status"] = "needs_repair"

        return result

    @staticmethod
    def auto_repair_registry() -> Tuple[bool, str]:
        """Attempt to automatically repair the registry by copying from source.

        Returns:
            Tuple of (success, message)
        """
        try:
            info = RegistryValidator.get_registry_info()

            # Check if source registry is available and path is set
            if (
                not info["source_registry_exists"]
                or info["source_registry_path"] is None
            ):
                return (
                    False,
                    "Source registry not found or path is missing - cannot auto-repair",
                )

            if info["source_file_count"] == 0:
                return False, "Source registry is empty - cannot auto-repair"

            # Get package registry path
            try:
                from importlib.resources import files

                package_registry = files("prompt_decorators").joinpath("registry")

                # Check if we can write to the package directory
                # This is tricky because package resources might be read-only
                # We'll try to create the directories and copy files

                # Path constructor is now safe as info["source_registry_path"] is confirmed str
                source_registry_path_obj = Path(info["source_registry_path"])

                # Copy each subdirectory
                files_copied = 0
                subdirs_to_copy: List[
                    Literal["core", "extensions", "simplified_decorators"]
                ] = ["core", "extensions", "simplified_decorators"]

                for subdir_name in subdirs_to_copy:
                    source_subdir = source_registry_path_obj / subdir_name
                    if not source_subdir.exists():
                        continue

                    # Try to create target subdirectory
                    try:
                        target_subdir = package_registry.joinpath(subdir_name)
                        # This might fail if the package is installed read-only

                        # Copy JSON files
                        for json_file in source_subdir.glob("**/*.json"):
                            rel_path = json_file.relative_to(source_subdir)
                            target_file = target_subdir.joinpath(
                                str(rel_path)
                            )  # Convert rel_path to str

                            # Create parent directories
                            # Assuming target_file.parent is valid; Traversable.parent exists
                            target_file.parent.mkdir(parents=True, exist_ok=True)  # type: ignore[attr-defined]

                            # Copy file
                            shutil.copy2(
                                str(json_file), str(target_file)
                            )  # Convert both to str
                            files_copied += 1

                    except Exception as e:
                        logger.debug(f"Error copying {subdir_name}: {e}")
                        # Continue with other subdirectories

                if files_copied > 0:
                    return True, f"Successfully copied {files_copied} registry files"
                else:
                    return False, "No files could be copied (package may be read-only)"

            except (ImportError, AttributeError):
                # Fallback for older Python versions
                return False, "Auto-repair not supported on this Python version"

        except Exception as e:
            logger.error(f"Auto-repair failed: {e}")
            return False, f"Auto-repair failed: {e}"

    @staticmethod
    def copy_source_to_package() -> Tuple[bool, str]:
        """Copy registry files from source to package directory.

        This is used during development and build processes.

        Returns:
            Tuple of (success, message)
        """
        try:
            info = RegistryValidator.get_registry_info()

            if (
                not info["source_registry_exists"]
                or info["source_registry_path"] is None
            ):
                return False, "Source registry not found or path is missing"

            # Find package directory
            import prompt_decorators

            package_dir = Path(prompt_decorators.__file__).parent
            target_registry = package_dir / "registry"

            # Path constructor is now safe
            source_registry_path_obj = Path(info["source_registry_path"])

            # Copy subdirectories
            files_copied = 0
            subdirs_to_copy: List[
                Literal["core", "extensions", "simplified_decorators"]
            ] = ["core", "extensions", "simplified_decorators"]
            for subdir_name in subdirs_to_copy:
                source_subdir = source_registry_path_obj / subdir_name
                target_subdir = target_registry / subdir_name

                if not source_subdir.exists():
                    continue

                # Create target directory
                target_subdir.mkdir(parents=True, exist_ok=True)

                # Copy JSON files
                for json_file in source_subdir.glob("**/*.json"):
                    rel_path = json_file.relative_to(source_subdir)
                    target_file = target_subdir / str(
                        rel_path
                    )  # Convert rel_path to str

                    # Create parent directories
                    target_file.parent.mkdir(parents=True, exist_ok=True)

                    # Copy file
                    shutil.copy2(
                        str(json_file), str(target_file)
                    )  # Convert both to str
                    files_copied += 1

            return True, f"Copied {files_copied} files from source to package registry"

        except Exception as e:
            return False, f"Copy operation failed: {e}"

    @staticmethod
    def validate_decorator_file(file_path: Path) -> Tuple[bool, List[str]]:
        """Validate a single decorator JSON file.

        Args:
            file_path: Path to the JSON file to validate

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Check required fields
            required_fields = ["decoratorName", "description"]
            for field in required_fields:
                if field not in data:
                    errors.append(f"Missing required field: {field}")

            # Validate decorator name
            if "decoratorName" in data:
                name = data["decoratorName"]
                if not isinstance(name, str) or not name.strip():
                    errors.append("decoratorName must be a non-empty string")

            # Validate parameters if present
            if "parameters" in data:
                if not isinstance(data["parameters"], list):
                    errors.append("parameters must be a list")
                else:
                    for i, param in enumerate(data["parameters"]):
                        if not isinstance(param, dict):
                            errors.append(f"Parameter {i} must be an object")
                            continue

                        if "name" not in param:
                            errors.append(f"Parameter {i} missing 'name' field")

                        if "type" not in param:
                            errors.append(f"Parameter {i} missing 'type' field")

            # Validate transformation template if present
            if "transformationTemplate" in data:
                template = data["transformationTemplate"]
                if not isinstance(template, dict):
                    errors.append("transformationTemplate must be an object")
                elif "instruction" not in template:
                    errors.append("transformationTemplate missing 'instruction' field")

        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON: {e}")
        except Exception as e:
            errors.append(f"Error reading file: {e}")

        return len(errors) == 0, errors

    @staticmethod
    def get_diagnostic_info() -> Dict[str, Any]:
        """Get comprehensive diagnostic information for troubleshooting.

        Returns:
            Dictionary containing diagnostic information
        """
        import sys

        import prompt_decorators

        # Ensure source_registry_path is handled if None for Path()
        registry_info_val = RegistryValidator.get_registry_info()
        # The validation_result is already Dict[str, Any]
        validation_result_val = RegistryValidator.validate_registry()

        diag_info: Dict[str, Any] = {
            "python_version": sys.version,
            "package_version": getattr(prompt_decorators, "__version__", "Unknown"),
            "package_location": str(
                Path(prompt_decorators.__file__).resolve()
            ),  # Ensure str
            "registry_info": registry_info_val,
            "validation_result": validation_result_val,
            "loaded_decorators": 0,  # Default value
            "sample_decorators": [],  # Default value
            "decorator_loading_error": None,  # Default value
        }

        # Try to load decorators and get count
        try:
            from prompt_decorators.core.dynamic_decorator import DynamicDecorator

            DynamicDecorator._loaded = False  # Force reload
            DynamicDecorator.load_registry()
            diag_info["loaded_decorators"] = len(DynamicDecorator._registry)
            diag_info["sample_decorators"] = list(DynamicDecorator._registry.keys())[:5]
        except Exception as e:
            diag_info["decorator_loading_error"] = str(e)

        return diag_info

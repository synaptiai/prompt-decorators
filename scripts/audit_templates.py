#!/usr/bin/env python3
"""
Audit transformation templates in decorator registry entries.

This script analyzes all decorator registry entries to ensure consistency
in transformation templates without modifying any files.
"""

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple


def audit_transformation_templates(registry_dir: str) -> Tuple[int, int, List[str]]:
    """
    Audit transformation templates in decorator registry entries.

    Args:
        registry_dir: Path to registry directory

    Returns:
        Tuple containing:
        - Number of files analyzed
        - Number of files with transformation templates
        - List of error messages
    """
    required_fields = [
        "instruction",
        "parameterMapping",
        "placement",
        "compositionBehavior",
    ]

    files_analyzed = 0
    files_with_templates = 0
    error_messages = []

    for root, dirs, files in os.walk(registry_dir):
        for file in files:
            if file.endswith(".json"):
                files_analyzed += 1
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)

                    if "transformationTemplate" in data:
                        files_with_templates += 1
                        template = data["transformationTemplate"]

                        # Check required fields
                        missing_fields = [
                            field for field in required_fields if field not in template
                        ]

                        if missing_fields:
                            error_messages.append(
                                f"Missing fields in {file_path}: {missing_fields}"
                            )

                        # Check parameter mappings
                        if "parameterMapping" in template and "parameters" in data:
                            param_names = {
                                param["name"] for param in data["parameters"]
                            }
                            mapping_names = set(template["parameterMapping"].keys())

                            # Parameters in mapping but not in parameters
                            extra_mappings = mapping_names - param_names
                            if extra_mappings:
                                error_messages.append(
                                    f"Parameters in mapping but not defined: "
                                    f"{file_path}: {extra_mappings}"
                                )

                            # Check each mapping
                            for param, mapping in template["parameterMapping"].items():
                                if param in param_names:
                                    if not isinstance(mapping, dict):
                                        error_messages.append(
                                            f"Invalid mapping format for {param} in "
                                            f"{file_path}: not a dictionary"
                                        )
                                    elif not (
                                        "valueMap" in mapping or "format" in mapping
                                    ):
                                        error_messages.append(
                                            f"Mapping for {param} in {file_path} "
                                            f"missing either valueMap or format"
                                        )

                        # Check placement value
                        if "placement" in template:
                            valid_placements = ["prepend", "append", "replace", "wrap"]
                            if template["placement"] not in valid_placements:
                                error_messages.append(
                                    f"Invalid placement value in {file_path}: "
                                    f"{template['placement']} (valid: {valid_placements})"
                                )

                        # Check composition behavior
                        if "compositionBehavior" in template:
                            valid_behaviors = [
                                "accumulate",
                                "override",
                                "selective-override",
                            ]
                            if template["compositionBehavior"] not in valid_behaviors:
                                error_messages.append(
                                    f"Invalid compositionBehavior in {file_path}: "
                                    f"{template['compositionBehavior']} (valid: {valid_behaviors})"
                                )
                    else:
                        # Check if this decorator has a custom transform_function instead
                        if "transform_function" not in data:
                            error_messages.append(
                                f"No transformationTemplate or transform_function in {file_path}"
                            )

                except json.JSONDecodeError:
                    error_messages.append(f"Invalid JSON in {file_path}")
                except Exception as e:
                    error_messages.append(f"Error processing {file_path}: {str(e)}")

    return files_analyzed, files_with_templates, error_messages


def main():
    """Main function."""
    registry_dir = "registry"
    if len(sys.argv) > 1:
        registry_dir = sys.argv[1]

    print(f"Auditing transformation templates in {registry_dir}...")

    files_analyzed, files_with_templates, errors = audit_transformation_templates(
        registry_dir
    )

    print(f"\nAudit Summary:")
    print(f"- Files analyzed: {files_analyzed}")
    print(f"- Files with transformation templates: {files_with_templates}")
    print(f"- Errors found: {len(errors)}")

    if errors:
        print("\nErrors:")
        for i, error in enumerate(errors, 1):
            print(f"{i}. {error}")
        return 1

    print("\nAll transformation templates are consistent!")
    return 0


if __name__ == "__main__":
    sys.exit(main())

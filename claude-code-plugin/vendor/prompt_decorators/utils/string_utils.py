"""String utilities for working with prompt decorators.

This module provides utility functions for extracting and replacing decorators in text.
"""

import re
from typing import Any, Dict, List, Tuple


def extract_decorators_from_text(text: str) -> Tuple[List[Dict[str, Any]], str]:
    """Extract decorator annotations from text.

    Args:
        text: Text containing decorator annotations

    Returns:
        Tuple of (list of decorator dictionaries, clean text)
    """
    # Regular expression for matching decorator annotations
    decorator_pattern = (
        r"\+\+\+([A-Za-z][A-Za-z0-9]*(?::v[0-9]+(?:\.[0-9]+(?:\.[0-9]+)?)?)?)"
        r"(?:\(([^)]*)\))?"
    )

    # Regular expression for matching parameters
    param_pattern = (
        r'([a-zA-Z0-9_]+)=(?:"([^"]*)"|(True|False|[0-9]+(?:\.[0-9]+)?|[a-zA-Z0-9_]+))'
    )

    # Find all decorator annotations
    matches = re.finditer(decorator_pattern, text, re.MULTILINE)
    decorators = []
    clean_text = text

    # Process each match
    for match in matches:
        # Get the full decorator text
        decorator_text = match.group(0)

        # Extract decorator name and parameters
        name = match.group(1)
        params_str = match.group(2) or ""

        # Parse parameters
        params = {}
        if params_str:
            for param_match in re.finditer(param_pattern, params_str):
                param_name = param_match.group(1)
                # Use the quoted value if available, otherwise use the unquoted value
                param_value = (
                    param_match.group(2)
                    if param_match.group(2) is not None
                    else param_match.group(3)
                )

                # Convert value to appropriate type
                if param_value == "True":
                    param_value = True
                elif param_value == "False":
                    param_value = False
                elif param_value is not None and re.match(r"^[0-9]+$", param_value):
                    param_value = int(param_value)
                elif param_value is not None and re.match(
                    r"^[0-9]+\.[0-9]+$", param_value
                ):
                    param_value = float(param_value)

                params[param_name] = param_value

        # Add decorator to list
        decorators.append({"name": name, "parameters": params})

        # Remove the decorator from the text
        clean_text = clean_text.replace(decorator_text, "", 1)

    # Clean up any extra whitespace
    clean_text = clean_text.strip()

    return decorators, clean_text


def replace_decorators_in_text(text: str, decorators: List[Dict[str, Any]]) -> str:
    """Replace decorator annotations in text.

    Args:
        text: Text to modify
        decorators: List of decorator dictionaries

    Returns:
        Text with decorator annotations replaced
    """
    # Create decorator strings
    decorator_strings = []
    for decorator in decorators:
        name = decorator["name"]
        parameters = decorator.get("parameters", {})

        # Create the decorator string
        if parameters:
            param_str = ", ".join(
                f"{k}='{v}'" if isinstance(v, str) else f"{k}={v}"
                for k, v in parameters.items()
            )
            decorator_str = f"+++{name}({param_str})"
        else:
            decorator_str = f"+++{name}"

        decorator_strings.append(decorator_str)

    # Combine decorators with the text
    if decorator_strings:
        return "\n".join(decorator_strings) + f"\n{text}"
    else:
        return text

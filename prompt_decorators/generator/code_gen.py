"""Code Generator Module.

This module generates Python code from decorator definitions in the registry.
"""

import logging
import re
import textwrap
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from .registry import DecoratorData

# Configure logging
logger = logging.getLogger(__name__)


def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case."""
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def snake_to_camel(name: str) -> str:
    """Convert snake_case to CamelCase."""
    components = name.split("_")
    return "".join(x.title() for x in components)


class CodeGenerator:
    """Generator for Python code from decorator definitions."""

    # Python keywords that can't be used as variable names
    python_keywords = [
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
    ]

    def __init__(self, decorators: List[DecoratorData]):
        """
        Initialize the code generator.

        Args:
            decorators: List of decorator data dictionaries from the registry
        """
        self.decorators = decorators
        self.enum_definitions: Dict[
            str, Tuple[str, List[str]]
        ] = {}  # Maps enum name to (description, values)

    def _split_text_into_chunks(self, text: str, max_length: int = 70) -> List[str]:
        """
        Split text into chunks that don't exceed the maximum length.

        Args:
            text: The text to split
            max_length: Maximum length of each chunk

        Returns:
            List of text chunks
        """
        if not text:
            return []

        # Use textwrap for better line wrapping
        return textwrap.wrap(text, width=max_length)

    def _format_long_string(
        self,
        text: str,
        indent: str = "",
        max_line_length: int = 70,
        quote_style: str = '"',
        line_continuation: bool = False,
    ) -> List[str]:
        """
        Format a long string into multiple lines.

        Args:
            text: The text to format
            indent: Indentation to add to each line
            max_line_length: Maximum length of each line
            quote_style: Quote style to use (single or double)
            line_continuation: Whether to use line continuation with parentheses

        Returns:
            List of formatted lines
        """
        if not text:
            return [f"{indent}{quote_style}{quote_style}"]

        # Split the text into chunks
        chunks = self._split_text_into_chunks(text, max_line_length)

        # Format the chunks
        lines = []

        if line_continuation:
            lines.append(f"{indent}{quote_style}{chunks[0]}{quote_style}")
            for chunk in chunks[1:]:
                lines.append(f"{indent}    {quote_style}{chunk}{quote_style}")
        else:
            for i, chunk in enumerate(chunks):
                if i == 0:
                    lines.append(f"{indent}{quote_style}{chunk}{quote_style}")
                else:
                    lines.append(f"{indent}{quote_style}{chunk}{quote_style}")

        return lines

    def _has_validation_rules(self, param: Dict[str, Any]) -> bool:
        """Check if the parameter has any validation rules.

        Args:
            param: The parameter definition dictionary

        Returns:
            bool: True if the parameter has validation rules, False otherwise
        """
        # Check for various validation rules
        validation_attrs = [
            "required",
            "pattern",
            "minimum",
            "maximum",
            "minItems",
            "maxItems",
            "items",
            "enum",
        ]

        for attr in validation_attrs:
            if attr in param:
                return True

        # Check if items has type validation
        if (
            "items" in param
            and isinstance(param["items"], dict)
            and "type" in param["items"]
        ):
            return True

        return False

    def generate_all(self) -> dict[str, str]:
        """
        Generate all Python files for the decorator package.

        Args:
            self: The CodeGenerator instance.

        Returns:
            A dictionary mapping file paths to generated code.
        """
        result = {}  # type: dict[str, str]

        # Generate decorator classes
        decorators_init = self._generate_decorators_init()
        result["decorators/__init__.py"] = decorators_init

        # Generate individual decorator files
        for decorator in self.decorators:
            file_name = self._get_decorator_file_name(decorator)
            code = self._generate_decorator_code(decorator)
            result[f"decorators/{file_name}"] = code

        # Generate enums module
        enums_code = self._generate_enums_module()
        result["decorators/enums.py"] = enums_code

        return result

    def _generate_decorators_init(self) -> str:
        """
        Generate the __init__.py file for the decorators package.

        Args:
            self: The CodeGenerator instance.

        Returns:
            Generated code as a string
        """
        code = [
            '"""',
            "Decorator Classes",
            "",
            "This package provides classes for all decorators in the Prompt Decorators specification.",
            '"""',
            "",
            "# Import all decorators",
        ]

        # Import statements for all decorators
        imports = []
        for decorator in self.decorators:
            name = decorator["decoratorName"]
            file_name = self._convert_to_snake_case(name)
            imports.append(f"from .{file_name} import {name}")

        code.extend(sorted(imports))

        # Export all decorators
        decorator_names = [decorator["decoratorName"] for decorator in self.decorators]
        code.append("")
        code.append("__all__ = [")
        for name in sorted(decorator_names):
            code.append(f'    "{name}",')
        code.append("]")

        return "\n".join(code)

    def _generate_decorator_code(self, decorator: Union[DecoratorData, Dict]) -> str:
        """
        Generate Python code for a single decorator.

        Args:
            decorator: The decorator data

        Returns:
            Generated Python code for the decorator
        """
        if not isinstance(decorator, dict):
            decorator = decorator.to_dict()

        name = decorator["decoratorName"]
        description = decorator.get("description", "")
        params = decorator.get("parameters", [])
        snake_name = self._convert_to_snake_case(name)

        # Check if we need to import Literal for enum types
        needs_literal_import = any(param.get("type") == "enum" for param in params)

        # Generate imports
        imports = [
            '"""',
            f"Implementation of the {name} decorator.",
            "",
            f"This module provides the {name} decorator class for use in prompt engineering.",
            "",
            description,
            '"""',
            "",
            "import re",
            "from typing import Any, Dict, List, Optional, Union, cast",
        ]

        # Add Literal import if needed
        if needs_literal_import:
            imports[
                -1
            ] = "from typing import Any, Dict, List, Literal, Optional, Union, cast"

        # Add import for BaseDecorator
        imports.extend(
            [
                "",
                "from prompt_decorators.core.base import BaseDecorator, ValidationError",
            ]
        )

        # Check if we need to import any enums
        enum_imports = self._get_enums_for_decorator(decorator)
        if enum_imports:
            imports.append(
                "from prompt_decorators.decorators.generated.decorators.enums import ("
            )
            for enum in enum_imports:
                imports.append(f"    {enum},")
            imports.append(")")

        # Generate class header
        code = []
        code.append("")
        code.append("")
        code.append(f"class {name}(BaseDecorator):")
        code.append('    """')

        # Class docstring
        if description:
            formatted_description = self._split_text_into_chunks(description)
            for line in formatted_description:
                code.append(f"    {line}")
            code.append("")

        # Add parameter documentation
        if params:
            code.append("    Attributes:")
            for param in params:
                param_name = param["name"]
                param_desc = param.get("description", "")
                param_type = self._get_python_type(param, decorator)
                formatted_desc_lines = self._split_text_into_chunks(
                    param_desc, max_length=60
                )

                code.append(f"        {param_name}: {param_desc}")

        code.append('    """')
        code.append("")

        # Add class variables
        code.append(f'    decorator_name = "{snake_name}"')
        code.append('    version = "1.0.0"  # Initial version')
        code.append("")

        # Generate __init__ method
        code.append("    def __init__(")
        code.append("        self,")

        # Add parameters
        for param in params:
            param_name = param["name"]
            param_type = self._get_python_type(param, decorator)
            is_required = param.get("required", False)

            if is_required:
                code.append(f"        {param_name}: {param_type},")
            else:
                default = self._format_default_value(param)
                code.append(f"        {param_name}: {param_type} = {default},")

        code.append("    ) -> None:")
        code.append('        """')
        code.append(f"        Initialize the {name} decorator.")
        code.append("")
        code.append("        Args:")

        # Add parameter documentation in __init__
        for param in params:
            param_name = param["name"]
            param_desc = param.get("description", "")
            formatted_desc_lines = self._split_text_into_chunks(
                param_desc, max_length=60
            )

            # Start with parameter name
            param_line = f"            {param_name}: {formatted_desc_lines[0]}"
            code.append(param_line)

            # Add remaining description lines with proper indentation
            for line in formatted_desc_lines[1:]:
                code.append(f"                {line}")

        # Add Returns section to fix docstring issue
        code.append("")
        code.append("        Returns:")
        code.append("            None")

        code.append('        """')

        # Add validation code
        code.append("        # Initialize with base values")
        code.append("        super().__init__()")
        code.append("")
        code.append("        # Store parameters")
        for param in params:
            param_name = param["name"]
            code.append(f"        self._{param_name} = {param_name}")
        code.append("")
        code.append("        # Validate parameters")
        self._add_validation_code(decorator, params, code)

        # Add getters for each parameter
        code.append("")
        self._add_get_property_methods(decorator, params, code)

        # Add to_dict method
        code.append("    def to_dict(self) -> Dict[str, Any]:")
        code.append('        """')
        code.append("        Convert the decorator to a dictionary.")
        code.append("")
        code.append("        Returns:")
        code.append("            Dictionary representation of the decorator")
        code.append('        """')
        code.append("        return {")
        code.append(f'            "name": "{snake_name}",')
        for param in params:
            param_name = param["name"]
            code.append(f'            "{param_name}": self.{param_name},')
        code.append("        }")

        # Add to_string method
        code.append("")
        code.append("    def to_string(self) -> str:")
        code.append('        """')
        code.append("        Convert the decorator to a string.")
        code.append("")
        code.append("        Returns:")
        code.append("            String representation of the decorator")
        code.append('        """')
        code.append("        params = []")
        for param in params:
            param_name = param["name"]
            code.append(f"        if self.{param_name} is not None:")
            code.append(
                f'            params.append(f"{param_name}={{self.{param_name}}}")'
            )
        code.append("")
        code.append("        if params:")
        code.append(
            '            return f"@{self.decorator_name}(" + ", ".join(params) + ")"'
        )
        code.append("        else:")
        code.append('            return f"@{self.decorator_name}"')

        return "\n".join(imports + code)

    def _add_get_property_methods(
        self,
        decorator: Union[DecoratorData, Dict],
        params: List[Dict[str, Any]],
        code: List[str],
    ) -> None:
        """
        Add property getter methods for all parameters.

        Args:
            decorator: The decorator data
            params: List of parameters
            code: List of code lines to append to

        Returns:
            None
        """
        if not params:
            return

        for param in params:
            param_name = param["name"]
            param_type = self._get_python_type(param, decorator)

            code.append("    @property")
            code.append(f"    def {param_name}(self) -> {param_type}:")
            code.append('        """')
            code.append(f"        Get the {param_name} parameter value.")
            code.append("")
            code.append("        Args:")
            code.append("            self: The decorator instance")
            code.append("")
            code.append("        Returns:")
            code.append(f"            The {param_name} parameter value")
            code.append('        """')
            code.append(f"        return self._{param_name}")
            code.append("")

        return

    def _add_validation_code(
        self,
        decorator: Union[DecoratorData, Dict],
        params: List[Dict[str, Any]],
        code: List[str],
    ) -> None:
        """Add validation code for parameters."""
        if not params:
            return

        for param_index, param in enumerate(params):
            param_name = param["name"]
            param_type = param.get("type", "string")

            # Only add validation if there are rules to check
            if not self._has_validation_rules(param):
                continue

            # Required parameter validation
            if param.get("required", False):
                code.append(f"        if self._{param_name} is None:")
                code.append(
                    f'            raise ValidationError("The parameter \'{param_name}\' is required for {decorator["decoratorName"]} decorator.")'
                )
                code.append("")

            # Skip validation for None values (if not required)
            code.append(f"        if self._{param_name} is not None:")

            # Add indentation for all validation checks
            indent = "            "

            # Type validation based on parameter type
            if param_type == "string":
                # String validation
                code.append(f"{indent}if not isinstance(self._{param_name}, str):")
                code.append(
                    f"{indent}    raise ValidationError(\"The parameter '{param_name}' must be a string value.\")"
                )

                # Pattern validation
                if "pattern" in param:
                    # Handle special regex escape sequences
                    pattern = param["pattern"]
                    # Make raw string by escaping backslashes
                    pattern = pattern.replace("\\", "\\\\")
                    # Fix common escape sequences that shouldn't be double-escaped
                    pattern = pattern.replace("\\\\d", "\\d")  # Digits
                    pattern = pattern.replace("\\\\w", "\\w")  # Word chars
                    pattern = pattern.replace("\\\\s", "\\s")  # Whitespace
                    pattern = pattern.replace("\\\\b", "\\b")  # Word boundary

                    code.append(f"{indent}import re")
                    code.append(
                        f'{indent}if not re.match(r"{pattern}", self._{param_name}):'
                    )
                    code.append(
                        f"{indent}    raise ValidationError(\"The parameter '{param_name}' value '\" + str(self._{param_name}) + \"' does not match the required pattern.\")"
                    )

            elif param_type == "integer":
                # Integer validation
                code.append(
                    f"{indent}if not isinstance(self._{param_name}, int) or isinstance(self._{param_name}, bool):"
                )
                code.append(
                    f"{indent}    raise ValidationError(\"The parameter '{param_name}' must be an integer value.\")"
                )

                # Minimum validation
                if "minimum" in param:
                    code.append(f"{indent}if self._{param_name} < {param['minimum']}:")
                    code.append(
                        f'{indent}    raise ValidationError("The parameter \'{param_name}\' must be at least {param["minimum"]}.")'
                    )

                # Maximum validation
                if "maximum" in param:
                    code.append(f"{indent}if self._{param_name} > {param['maximum']}:")
                    code.append(
                        f'{indent}    raise ValidationError("The parameter \'{param_name}\' must be at most {param["maximum"]}.")'
                    )

            elif param_type == "number":
                # Number validation
                code.append(
                    f"{indent}if not isinstance(self._{param_name}, (int, float)) or isinstance(self._{param_name}, bool):"
                )
                code.append(
                    f"{indent}    raise ValidationError(\"The parameter '{param_name}' must be a numeric value.\")"
                )

                # Minimum validation
                if "minimum" in param:
                    code.append(f"{indent}if self._{param_name} < {param['minimum']}:")
                    code.append(
                        f'{indent}    raise ValidationError("The parameter \'{param_name}\' must be at least {param["minimum"]}.")'
                    )

                # Maximum validation
                if "maximum" in param:
                    code.append(f"{indent}if self._{param_name} > {param['maximum']}:")
                    code.append(
                        f'{indent}    raise ValidationError("The parameter \'{param_name}\' must be at most {param["maximum"]}.")'
                    )

            elif param_type == "boolean":
                # Boolean validation
                code.append(f"{indent}if not isinstance(self._{param_name}, bool):")
                code.append(
                    f"{indent}    raise ValidationError(\"The parameter '{param_name}' must be a boolean value.\")"
                )

            elif param_type == "array":
                # Array validation
                code.append(
                    f"{indent}if not isinstance(self._{param_name}, (list, tuple)):"
                )
                code.append(
                    f"{indent}    raise ValidationError(\"The parameter '{param_name}' must be an array.\")"
                )

                # MinItems validation
                if "minItems" in param:
                    code.append(
                        f"{indent}if len(self._{param_name}) < {param['minItems']}:"
                    )
                    code.append(
                        f'{indent}    raise ValidationError("The parameter \'{param_name}\' must have at least {param["minItems"]} items.")'
                    )

                # MaxItems validation
                if "maxItems" in param:
                    code.append(
                        f"{indent}if len(self._{param_name}) > {param['maxItems']}:"
                    )
                    code.append(
                        f'{indent}    raise ValidationError("The parameter \'{param_name}\' must have at most {param["maxItems"]} items.")'
                    )

                # Items validation
                if "items" in param and "type" in param["items"]:
                    item_type = param["items"]["type"]
                    if item_type == "string":
                        code.append(f"{indent}for item in self._{param_name}:")
                        code.append(f"{indent}    if not isinstance(item, str):")
                        code.append(
                            f"{indent}        raise ValidationError(\"All items in '{param_name}' must be strings.\")"
                        )
                    elif item_type == "integer":
                        code.append(f"{indent}for item in self._{param_name}:")
                        code.append(
                            f"{indent}    if not isinstance(item, int) or isinstance(item, bool):"
                        )
                        code.append(
                            f"{indent}        raise ValidationError(\"All items in '{param_name}' must be integers.\")"
                        )
                    elif item_type == "number":
                        code.append(f"{indent}for item in self._{param_name}:")
                        code.append(
                            f"{indent}    if not isinstance(item, (int, float)) or isinstance(item, bool):"
                        )
                        code.append(
                            f"{indent}        raise ValidationError(\"All items in '{param_name}' must be numbers.\")"
                        )

            elif param_type == "enum":
                # Enum validation
                if "enum" in param:
                    enum_values = param["enum"]
                    enum_str = ", ".join([f'"{val}"' for val in enum_values])
                    code.append(f"{indent}valid_values = [{enum_str}]")
                    code.append(f"{indent}if self._{param_name} not in valid_values:")
                    code.append(
                        f'{indent}    raise ValidationError("The parameter \'{param_name}\' must be one of the following values: " + ", ".join(valid_values))'
                    )

            # Add a pass statement if no validation rules were added
            else:
                code.append(
                    f"{indent}pass  # No specific validation for this parameter type"
                )

            # Add a blank line after each parameter validation block
            code.append("")

    def _generate_enums_module(self) -> str:
        """Generate the enums.py module with all enum definitions.

        Args:
            self: The CodeGenerator instance.

        Returns:
            Generated code as a string
        """
        code = [
            '"""',
            "Decorator Enum Definitions",
            "",
            "This module provides enum types used by decorators.",
            '"""',
            "",
            "from enum import Enum",
            "",
        ]

        # Generate enums in alphabetical order
        for enum_name in sorted(self.enum_definitions.keys()):
            description, values = self.enum_definitions[enum_name]

            code.append("")
            code.append(f"class {enum_name}(str, Enum):")
            code.append(f'    """{description}"""')

            for value in values:
                constant_name = self._convert_to_enum_constant(value)
                code.append(f'    {constant_name} = "{value}"')

        return "\n".join(code)

    def _collect_enums(self) -> None:
        """Collect all enum types from all decorators."""
        self.enum_definitions = {}

        for decorator in self.decorators:
            name = decorator["decoratorName"]

            for param in decorator.get("parameters", []):
                if param.get("type") == "enum" and "enum" in param:
                    param_name = param["name"]
                    enum_name = f"{name}{param_name.capitalize()}Enum"
                    description = param.get(
                        "description", f"Options for {name}.{param_name}"
                    )
                    values = param["enum"]

                    self.enum_definitions[enum_name] = (description, values)

    def _get_enums_for_decorator(self, decorator: DecoratorData) -> List[str]:
        """Get list of enum types used by a decorator.

        Args:
            decorator: Decorator data

        Returns:
            List of enum class names
        """
        result = []
        name = decorator["decoratorName"]

        for param in decorator.get("parameters", []):
            if param.get("type") == "enum" and "enum" in param:
                param_name = param["name"]
                enum_name = f"{name}{param_name.capitalize()}Enum"

                # Ensure the enum exists in our definitions
                if enum_name not in self.enum_definitions:
                    description = param.get(
                        "description", f"Options for {name}.{param_name}"
                    )
                    values = param["enum"]
                    self.enum_definitions[enum_name] = (description, values)

                result.append(enum_name)

        return result

    def _get_python_type(
        self, param: Dict[str, Any], current_decorator: Optional[Dict[str, Any]] = None
    ) -> str:
        """Get the Python type for a parameter.

        Args:
            param: Parameter definition
            current_decorator: Optional decorator data for context

        Returns:
            Python type as string
        """
        param_type = param.get("type", "string")
        if param_type == "string":
            return "str"
        elif param_type == "integer":
            return "int"
        elif param_type == "float":
            return "float"
        elif param_type == "boolean":
            return "bool"
        elif param_type == "enum":
            # Use Literal type for enum values
            if "enum" in param:
                values = [self._format_literal_value(val) for val in param["enum"]]
                return f"Literal[{', '.join(values)}]"
            return "str"
        elif param_type == "array":
            # If items type is specified, use that
            if "items" in param and "type" in param["items"]:
                item_type = self._get_python_type(param["items"])
                return f"List[{item_type}]"
            return "List[Any]"
        elif param_type == "object":
            return "Dict[str, Any]"
        else:
            return "Any"

    def _format_literal_value(self, value: Any) -> str:
        """Format a value for use in a Literal type.

        Args:
            value: Value to format

        Returns:
            Formatted value as string
        """
        if isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, bool):
            # Use Python's True/False instead of JavaScript's true/false
            return str(value)
        else:
            return str(value)

    def _format_default_value(self, param: Dict[str, Any]) -> str:
        """
        Format the default value for a parameter.

        Args:
            param: Parameter definition

        Returns:
            Formatted default value as a string
        """
        if "default" not in param:
            return "None"

        default = param["default"]
        param_type = param.get("type", "string")

        if param_type == "string":
            # Always quote string values
            return f'"{str(default)}"'
        elif param_type == "boolean":
            # Use Python's True/False instead of JavaScript's true/false
            if isinstance(default, bool):
                return str(default)
            # Handle string representations from JSON
            if str(default).lower() in ("true", "false"):
                return "True" if str(default).lower() == "true" else "False"
            return str(default)
        elif param_type == "array":
            if not default:
                return "[]"
            # This is a simplification - would need more complex handling for non-primitive items
            items = [self._format_literal_value(item) for item in default]
            return f"[{', '.join(items)}]"
        elif param_type == "enum":
            # Always quote enum values
            return f'"{str(default)}"'
        elif param_type == "number":
            # Handle numeric values
            try:
                float(default)  # Validate it's a number
                return str(default)
            except (ValueError, TypeError):
                return "0.0"  # Default to 0.0 for invalid numbers
        elif param_type == "integer":
            # Handle integer values
            try:
                int(default)  # Validate it's an integer
                return str(default)
            except (ValueError, TypeError):
                return "0"  # Default to 0 for invalid integers
        else:
            # For unknown types, convert to string and quote
            return f'"{str(default)}"'

    def _convert_to_snake_case(self, name: str) -> str:
        """Convert camelCase or PascalCase to snake_case.

        Args:
            name: Name to convert

        Returns:
            snake_case version of the name
        """
        # Handle common acronyms that should stay together
        name = re.sub(r"JSON", "Json", name)
        name = re.sub(r"XML", "Xml", name)
        name = re.sub(r"YAML", "Yaml", name)
        name = re.sub(r"HTML", "Html", name)
        name = re.sub(r"CSS", "Css", name)
        name = re.sub(r"URL", "Url", name)
        name = re.sub(r"API", "Api", name)

        # Convert camelCase to snake_case
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

        # Replace spaces with underscores
        return s2.replace(" ", "_")

    def _convert_to_enum_constant(self, value: str) -> str:
        """Convert a string value to a valid enum constant name.

        Args:
            value: Value to convert

        Returns:
            Valid enum constant name
        """
        # Replace special characters with underscores
        result = re.sub(r"[^a-zA-Z0-9]", "_", str(value))

        # Convert to uppercase
        result = result.upper()

        # Ensure it starts with a letter
        if result and not result[0].isalpha():
            result = "VALUE_" + result

        # Handle empty string
        if not result:
            result = "EMPTY"

        return result

    def _get_decorator_file_name(self, decorator: DecoratorData) -> str:
        """Get the file name for a decorator module.

        Args:
            decorator: Decorator data

        Returns:
            File name for the decorator module
        """
        name = decorator["decoratorName"]
        snake_case = self._convert_to_snake_case(name)
        return f"{snake_case}.py"

    def _escape_string(self, s: str) -> str:
        """Escape a string for use in Python code."""
        if s is None:
            return ""
        # Replace backslashes first to avoid double escaping
        s = s.replace("\\", "\\\\")
        # Replace double quotes
        s = s.replace('"', '\\"')
        return s


def generate_code(
    decorators: List[DecoratorData], output_dir: Optional[Union[str, Path]] = None
) -> Dict[str, str]:
    """Generate Python code from decorator definitions.

    Args:
        decorators: List of decorator definitions
        output_dir: Optional output directory to write files to

    Returns:
        Dictionary mapping file paths to generated code
    """
    # Initialize the code generator
    generator = CodeGenerator(decorators)

    # Collect enum definitions
    generator._collect_enums()

    # Generate code
    generated_files = generator.generate_all()

    # Write to files if output_dir is specified
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        for file_path, content in generated_files.items():
            full_path = output_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

            logger.info(f"Generated {full_path}")

    return generated_files


if __name__ == "__main__":
    # Simple test when run directly
    import sys

    from .registry import scan_registry

    if len(sys.argv) > 1:
        registry_dir = sys.argv[1]
    else:
        # Default to registry directory relative to this file
        script_dir = Path(__file__).parent.parent.parent
        registry_dir = script_dir / "registry"

    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    else:
        output_dir = Path(__file__).parent.parent / "decorators" / "generated"

    print(f"Scanning registry at: {registry_dir}")
    print(f"Output directory: {output_dir}")

    try:
        # Scan registry
        decorators = scan_registry(registry_dir)

        # Generate code
        generate_code(decorators, output_dir)

        print(f"Generated {len(decorators)} decorator classes")
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)

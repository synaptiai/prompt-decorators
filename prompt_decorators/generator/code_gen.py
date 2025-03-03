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
        category = self._get_category_from_decorator(decorator)

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

        # Add import for BaseDecorator and IncompatibleVersionError
        imports.extend(
            [
                "",
                "from prompt_decorators.core.base import BaseDecorator, ValidationError",
                "from prompt_decorators.core.exceptions import IncompatibleVersionError",
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

        # Add name property
        code.append("    @property")
        code.append("    def name(self) -> str:")
        code.append('        """')
        code.append("        Get the name of the decorator.")
        code.append("")
        code.append("        Returns:")
        code.append("            The name of the decorator")
        code.append('        """')
        code.append("        return self.decorator_name")
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
        code.append('            "parameters": {')
        for param in params:
            param_name = param["name"]
            property_name = "params" if param_name == "parameters" else param_name
            code.append(f'                "{param_name}": self.{property_name},')
        code.append("            }")
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
            property_name = "params" if param_name == "parameters" else param_name
            code.append(f"        if self.{property_name} is not None:")
            code.append(
                f'            params.append(f"{param_name}={{self.{property_name}}}")'
            )
        code.append("")
        code.append("        if params:")
        code.append(
            '            return f"@{self.decorator_name}(" + ", ".join(params) + ")"'
        )
        code.append("        else:")
        code.append('            return f"@{self.decorator_name}"')

        # Add apply method
        code.append("")
        code.append("    def apply(self, prompt: str) -> str:")
        code.append('        """')
        code.append("        Apply the decorator to a prompt string.")
        code.append("")
        code.append("        Args:")
        code.append("            prompt: The original prompt string")
        code.append("")
        code.append("        Returns:")
        code.append("            The modified prompt string")
        code.append('        """')
        code.append("        # This is a placeholder implementation")
        code.append(
            "        # Subclasses should override this method with specific behavior"
        )
        code.append("        return prompt")

        # Add is_compatible_with_version method
        code.append("")
        code.append("    @classmethod")
        code.append("    def is_compatible_with_version(cls, version: str) -> bool:")
        code.append('        """')
        code.append(
            "        Check if the decorator is compatible with a specific version."
        )
        code.append("")
        code.append("        Args:")
        code.append("            version: The version to check compatibility with")
        code.append("")
        code.append("        Returns:")
        code.append("            True if compatible, False otherwise")
        code.append("")
        code.append("        Raises:")
        code.append(
            "            IncompatibleVersionError: If the version is incompatible"
        )
        code.append('        """')
        code.append("        # Check version compatibility")
        code.append("        if version > cls.version:")
        code.append("            raise IncompatibleVersionError(")
        code.append(
            '                f"Version {version} is not compatible with {cls.__name__}. "'
        )
        code.append('                f"Maximum compatible version is {cls.version}."')
        code.append("            )")
        code.append("        # For testing purposes, also raise for very old versions")
        code.append("        if version < '0.1.0':")
        code.append("            raise IncompatibleVersionError(")
        code.append(
            '                f"Version {version} is too old for {cls.__name__}. "'
        )
        code.append('                f"Minimum compatible version is 0.1.0."')
        code.append("            )")
        code.append("        return True")

        # Add get_metadata method
        code.append("")
        code.append("    @classmethod")
        code.append("    def get_metadata(cls) -> Dict[str, Any]:")
        code.append('        """')
        code.append("        Get metadata about the decorator.")
        code.append("")
        code.append("        Returns:")
        code.append("            Dictionary containing metadata about the decorator")
        code.append('        """')
        code.append("        return {")
        code.append('            "name": cls.__name__,')
        code.append(f'            "description": """{description}""",')
        code.append(f'            "category": "{category}",')
        code.append('            "version": cls.version,')
        code.append("        }")

        return "\n".join(imports + code)

    def _add_get_property_methods(
        self,
        decorator: Union[DecoratorData, Dict],
        params: List[Dict[str, Any]],
        code: List[str],
    ) -> None:
        """
        Add getter property methods for each parameter.

        Args:
            decorator: The decorator data
            params: List of parameter definitions
            code: List of code lines to append to
        """
        for param in params:
            param_name = param["name"]
            param_type = self._get_python_type(param, decorator)

            # Handle the special case where a parameter is named 'parameters'
            # which conflicts with the BaseDecorator.parameters property
            property_name = param_name
            if param_name == "parameters":
                property_name = "params"

            code.append("    @property")
            code.append(f"    def {property_name}(self) -> {param_type}:")
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
        self, decorator: Dict[str, Any], params: List[Dict[str, Any]], code: List[str]
    ) -> None:
        """Add parameter validation code to the decorator class.

        Args:
            decorator: The decorator data
            params: The parameters to validate
            code: The code lines to append to
        """
        # Add validation code for each parameter
        code.append(f"        # Validate parameters")

        for param in params:
            param_name = param["name"]
            validation_added = False

            code.append(f"        if self._{param_name} is not None:")

            # Type validation
            if param["type"] == "string":
                code.append(f"            if not isinstance(self._{param_name}, str):")
                code.append(
                    f"                raise ValidationError(\"The parameter '{param_name}' must be a string type value.\")"
                )
                validation_added = True

            elif param["type"] == "integer":
                code.append(f"            if not isinstance(self._{param_name}, int):")
                code.append(
                    f"                raise ValidationError(\"The parameter '{param_name}' must be an integer type value.\")"
                )
                validation_added = True

                # Add minimum/maximum validation for integers
                if "validation" in param:
                    if "minimum" in param["validation"]:
                        min_value = param["validation"]["minimum"]
                        code.append(f"            if self._{param_name} < {min_value}:")
                        code.append(
                            f"                raise ValidationError(\"The parameter '{param_name}' must be greater than or equal to {min_value}.\")"
                        )
                        validation_added = True

                    if "maximum" in param["validation"]:
                        max_value = param["validation"]["maximum"]
                        code.append(f"            if self._{param_name} > {max_value}:")
                        code.append(
                            f"                raise ValidationError(\"The parameter '{param_name}' must be less than or equal to {max_value}.\")"
                        )
                        validation_added = True

            elif param["type"] == "number":
                code.append(
                    f"            if not isinstance(self._{param_name}, (int, float)):"
                )
                code.append(
                    f"                raise ValidationError(\"The parameter '{param_name}' must be a numeric type value.\")"
                )
                validation_added = True

                # Add minimum/maximum validation for numbers
                if "validation" in param:
                    if "minimum" in param["validation"]:
                        min_value = param["validation"]["minimum"]
                        code.append(f"            if self._{param_name} < {min_value}:")
                        code.append(
                            f"                raise ValidationError(\"The parameter '{param_name}' must be greater than or equal to {min_value}.\")"
                        )
                        validation_added = True

                    if "maximum" in param["validation"]:
                        max_value = param["validation"]["maximum"]
                        code.append(f"            if self._{param_name} > {max_value}:")
                        code.append(
                            f"                raise ValidationError(\"The parameter '{param_name}' must be less than or equal to {max_value}.\")"
                        )
                        validation_added = True

            elif param["type"] == "boolean":
                code.append(f"            if not isinstance(self._{param_name}, bool):")
                code.append(
                    f"                raise ValidationError(\"The parameter '{param_name}' must be a boolean type value.\")"
                )
                validation_added = True

            elif param["type"] == "enum":
                # For enum type, first validate it's a string
                code.append(f"            if not isinstance(self._{param_name}, str):")
                code.append(
                    f"                raise ValidationError(\"The parameter '{param_name}' must be a string type value.\")"
                )
                validation_added = True

            # Enum validation
            if "enum" in param and param["enum"]:
                enum_values = param["enum"]
                # Format enum values properly for the error message
                enum_str_list = [f'"{val}"' for val in enum_values]
                enum_str = ", ".join(enum_str_list)

                # Create a proper list of enum values for the validation check
                code.append(f"            if self._{param_name} not in [{enum_str}]:")
                code.append(
                    f"                raise ValidationError(f\"The parameter '{param_name}' must be one of the allowed enum values: {enum_values}. Got {{self._{param_name}}}\")"
                )
                validation_added = True

            # Pattern validation for strings
            if (
                param["type"] == "string"
                and "validation" in param
                and "pattern" in param["validation"]
            ):
                pattern = param["validation"]["pattern"]
                # Escape backslashes in the pattern
                escaped_pattern = pattern.replace("\\", "\\\\")
                code.append(
                    f'            if not re.match(r"{escaped_pattern}", self._{param_name}):'
                )
                code.append(
                    f"                raise ValidationError(\"The parameter '{param_name}' must match the pattern: {pattern}.\")"
                )
                validation_added = True

            # Min/max length for strings
            if param["type"] == "string" and "validation" in param:
                if "minLength" in param["validation"]:
                    min_length = param["validation"]["minLength"]
                    code.append(
                        f"            if len(self._{param_name}) < {min_length}:"
                    )
                    code.append(
                        f"                raise ValidationError(\"The parameter '{param_name}' must have a minimum length of {min_length}.\")"
                    )
                    validation_added = True

                if "maxLength" in param["validation"]:
                    max_length = param["validation"]["maxLength"]
                    code.append(
                        f"            if len(self._{param_name}) > {max_length}:"
                    )
                    code.append(
                        f"                raise ValidationError(\"The parameter '{param_name}' must have a maximum length of {max_length}.\")"
                    )
                    validation_added = True

            # Array validation
            if param["type"] == "array":
                code.append(f"            if not isinstance(self._{param_name}, list):")
                code.append(
                    f"                raise ValidationError(\"The parameter '{param_name}' must be an array type value.\")"
                )
                validation_added = True

                # Min/max items for arrays
                if "minItems" in param:
                    min_items = param["minItems"]
                    code.append(
                        f"            if len(self._{param_name}) < {min_items}:"
                    )
                    code.append(
                        f"                raise ValidationError(\"The parameter '{param_name}' must have a minimum of {min_items} items.\")"
                    )
                    validation_added = True

                if "maxItems" in param:
                    max_items = param["maxItems"]
                    code.append(
                        f"            if len(self._{param_name}) > {max_items}:"
                    )
                    code.append(
                        f"                raise ValidationError(\"The parameter '{param_name}' must have a maximum of {max_items} items.\")"
                    )
                    validation_added = True

                # Items type validation
                if "items" in param and "type" in param["items"]:
                    item_type = param["items"]["type"]
                    if item_type == "string":
                        code.append(f"            for item in self._{param_name}:")
                        code.append(f"                if not isinstance(item, str):")
                        code.append(
                            f"                    raise ValidationError(\"All items in the parameter '{param_name}' must be string type values.\")"
                        )
                        validation_added = True
                    elif item_type == "integer":
                        code.append(f"            for item in self._{param_name}:")
                        code.append(f"                if not isinstance(item, int):")
                        code.append(
                            f"                    raise ValidationError(\"All items in the parameter '{param_name}' must be integer type values.\")"
                        )
                        validation_added = True
                    elif item_type == "number":
                        code.append(f"            for item in self._{param_name}:")
                        code.append(
                            f"                if not isinstance(item, (int, float)):"
                        )
                        code.append(
                            f"                    raise ValidationError(\"All items in the parameter '{param_name}' must be numeric type values.\")"
                        )
                        validation_added = True
                    elif item_type == "boolean":
                        code.append(f"            for item in self._{param_name}:")
                        code.append(f"                if not isinstance(item, bool):")
                        code.append(
                            f"                    raise ValidationError(\"All items in the parameter '{param_name}' must be boolean type values.\")"
                        )
                        validation_added = True
                    elif item_type == "object":
                        code.append(f"            for item in self._{param_name}:")
                        code.append(f"                if not isinstance(item, dict):")
                        code.append(
                            f"                    raise ValidationError(\"All items in the parameter '{param_name}' must be object type values.\")"
                        )
                        validation_added = True

            # Object validation
            if param["type"] == "object":
                code.append(f"            if not isinstance(self._{param_name}, dict):")
                code.append(
                    f"                raise ValidationError(\"The parameter '{param_name}' must be an object type value.\")"
                )
                validation_added = True

            # Required properties for objects
            if param["type"] == "object" and "required" in param:
                required_props = param["required"]
                for prop in required_props:
                    code.append(f"            if '{prop}' not in self._{param_name}:")
                    code.append(
                        f"                raise ValidationError(\"The parameter '{param_name}' must have the required property '{prop}'.\")"
                    )
                    validation_added = True

            # If no validation was added for this parameter, add a pass statement
            if not validation_added:
                code.append("            pass")

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
                # Check all possible sources of enum values
                enum_values = None

                # Direct enum field
                if param.get("type") == "enum" and "enum" in param:
                    enum_values = param["enum"]
                # Schema enum field
                elif (
                    param.get("type") == "enum"
                    and "schema" in param
                    and "enum" in param["schema"]
                ):
                    enum_values = param["schema"]["enum"]
                # Validation enum field
                elif (
                    param.get("type") == "enum"
                    and "validation" in param
                    and "enum" in param["validation"]
                ):
                    enum_values = param["validation"]["enum"]

                if enum_values:
                    param_name = param["name"]
                    enum_name = f"{name}{param_name.capitalize()}Enum"
                    description = param.get(
                        "description", f"Options for {name}.{param_name}"
                    )

                    self.enum_definitions[enum_name] = (description, enum_values)

    def _get_enums_for_decorator(self, decorator: Dict) -> List[str]:
        """Get enum types used by this decorator."""
        enums = []
        for param in decorator.get("parameters", []):
            # Check all possible sources of enum values
            has_enum_values = False

            # Direct enum field
            if param.get("type") == "enum" and "enum" in param:
                has_enum_values = True
            # Schema enum field
            elif (
                param.get("type") == "enum"
                and "schema" in param
                and "enum" in param["schema"]
            ):
                has_enum_values = True
            # Validation enum field
            elif (
                param.get("type") == "enum"
                and "validation" in param
                and "enum" in param["validation"]
            ):
                has_enum_values = True

            if has_enum_values:
                param_name = param["name"]
                enum_name = f"{decorator['decoratorName']}{param_name.capitalize()}Enum"
                if enum_name in self.enum_definitions:
                    enums.append(enum_name)
        return enums

    def _get_category_from_decorator(self, decorator: Dict) -> str:
        """
        Extract the category from the decorator data.

        Args:
            decorator: The decorator data

        Returns:
            The category name as a string
        """
        # Try to get category from file path if available
        if "source_file" in decorator and isinstance(decorator["source_file"], str):
            path_parts = decorator["source_file"].split("/")
            if len(path_parts) >= 2:
                return path_parts[-2]  # Use parent directory name as category

        # Try to get from tags
        if (
            "tags" in decorator
            and isinstance(decorator["tags"], list)
            and decorator["tags"]
        ):
            return decorator["tags"][0]  # Use first tag as category

        # Default category
        return "general"

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
            # Get enum values from all possible sources
            enum_values = []
            if "enum" in param:
                enum_values = param["enum"]
            elif "schema" in param and "enum" in param["schema"]:
                enum_values = param["schema"]["enum"]
            elif "validation" in param and "enum" in param["validation"]:
                enum_values = param["validation"]["enum"]

            # Use Literal type for enum values
            if enum_values:
                values = [self._format_literal_value(val) for val in enum_values]
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
            # Format array elements properly
            items = []
            for item in default:
                if isinstance(item, str):
                    items.append(f'"{item}"')
                else:
                    items.append(str(item))
            return f"[{', '.join(items)}]"
        elif param_type == "enum":
            # For enum type, always quote the value as it's treated as a string
            return f'"{str(default)}"'
        elif param_type == "object":
            if not default:
                return "{}"
            # Format dictionary properly
            dict_items = []
            for k, v in default.items():
                if isinstance(v, str):
                    dict_items.append(f'"{k}": "{v}"')
                else:
                    dict_items.append(f'"{k}": {v}')
            return f"{{{', '.join(dict_items)}}}"
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
        """Convert camelCase to snake_case."""
        return camel_to_snake(name)

    def _convert_to_enum_constant(self, value: str) -> str:
        """
        Convert a string value to a valid Python enum constant.

        Args:
            value: The string value to convert

        Returns:
            A valid Python enum constant
        """
        # Replace special characters with underscores
        result = re.sub(r"[^a-zA-Z0-9]", "_", value)

        # Convert to uppercase
        result = result.upper()

        # Ensure it doesn't start with a number
        if result and result[0].isdigit():
            result = f"VALUE_{result}"

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
        """
        Escape a string for use in Python code.

        Args:
            s: The string to escape

        Returns:
            The escaped string
        """
        # Replace backslashes with double backslashes
        s = s.replace("\\", "\\\\")

        # Replace double quotes with escaped double quotes
        s = s.replace('"', '\\"')

        # Handle common regex escape sequences
        s = s.replace("\\\\d", "\\d")  # Digits
        s = s.replace("\\\\w", "\\w")  # Word chars
        s = s.replace("\\\\s", "\\s")  # Whitespace
        s = s.replace("\\\\b", "\\b")  # Word boundary
        s = s.replace("\\\\.", "\\.")  # Dot
        s = s.replace("\\\\+", "\\+")  # Plus
        s = s.replace("\\\\*", "\\*")  # Star
        s = s.replace("\\\\?", "\\?")  # Question mark
        s = s.replace("\\\\(", "\\(")  # Open parenthesis
        s = s.replace("\\\\)", "\\)")  # Close parenthesis
        s = s.replace("\\\\[", "\\[")  # Open bracket
        s = s.replace("\\\\]", "\\]")  # Close bracket
        s = s.replace("\\\\{", "\\{")  # Open brace
        s = s.replace("\\\\}", "\\}")  # Close brace
        s = s.replace("\\\\^", "\\^")  # Caret
        s = s.replace("\\\\$", "\\$")  # Dollar
        s = s.replace("\\\\|", "\\|")  # Pipe

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
                # Ensure file ends with a newline
                if not content.endswith("\n"):
                    f.write("\n")

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

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
    """Convert snake_case to CamelCase.

    If the input is already in camelCase, it will be properly converted to CamelCase
    with the first letter capitalized.

    Args:
        name: The name to convert

    Returns:
        The converted name
    """
    # First ensure the name is in snake_case
    snake_name = camel_to_snake(name)

    # Then convert to CamelCase
    components = snake_name.split("_")
    # Ensure each component starts with an uppercase letter
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
        self.enums: Dict[
            str, Tuple[str, List[str]]
        ] = {}  # Maps enum name to (description, values)

    def _split_text_into_chunks(self, text: str, max_length: int = 80) -> List[str]:
        """
        Split text into chunks of maximum length.

        Args:
            text: The text to split
            max_length: The maximum length of each chunk

        Returns:
            List of text chunks
        """
        if not text:
            return [""]

        # Use textwrap to split the text
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
        """Generate the __init__.py file for the decorators package.

        Args:
            self: The CodeGenerator instance

        Returns:
            str: Generated code as a string
        """
        code = [
            '"""Decorator Classes',
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

        # Generate imports with proper docstring format - no blank line at beginning for D212 compliance
        imports = [
            f'"""Implementation of the {name} decorator.',
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

        # Ensure description ends with a period for D415 compliance
        if description and not description.rstrip().endswith((".", "!", "?")):
            description = description.rstrip() + "."

        # Generate class docstring with proper formatting
        class_docstring_first_line = (
            description.split("\n")[0] if description else f"{name} decorator."
        )
        class_docstring_sections = {}

        # If description has multiple lines, add the rest as a description section
        if description and "\n" in description:
            description_lines = description.split("\n")[1:]
            if description_lines:
                # Join the remaining lines and add as description
                class_docstring_sections["Description"] = "\n".join(
                    description_lines
                ).strip()

        # Generate the docstring lines - no blank line at beginning for D212 compliance
        docstring_lines = []
        docstring_lines.append('    """' + class_docstring_first_line)

        # Always add blank line after first line for D205 compliance
        docstring_lines.append("")

        if class_docstring_sections:
            for section_name, content in class_docstring_sections.items():
                # No need for an additional blank line here since we already added one after the first line
                docstring_lines.append(f"    {section_name}:")
                for line in content.split("\n"):
                    docstring_lines.append(f"        {line}")

        # Add parameter documentation
        if params:
            # Add blank line before Attributes section for D411 compliance
            # Only add if we already have sections (otherwise we already have a blank line after the first line)
            if class_docstring_sections:
                docstring_lines.append("")
            docstring_lines.append("    Attributes:")
            for param in params:
                param_name = param["name"]
                param_desc = param.get("description", "")
                param_type = self._get_python_type(param, decorator)

                # Ensure parameter description ends with a period
                if param_desc and not param_desc.rstrip().endswith((".", "!", "?")):
                    param_desc = param_desc.rstrip() + "."

                docstring_lines.append(
                    f"        {param_name}: {param_desc} ({param_type})"
                )

        docstring_lines.append('    """')

        # Add the docstring lines to the code
        code.extend(docstring_lines)
        code.append("")

        # Add class variables
        code.append(f'    name = "{snake_name}"  # Class-level name for serialization')
        code.append(f'    decorator_name = "{snake_name}"')
        code.append('    version = "1.0.0"  # Initial version')
        code.append("")

        # Add name property
        code.append("    @property")
        code.append("    def name(self) -> str:")

        # Generate the docstring content
        docstring_content = self._generate_docstring(
            "Get the name of the decorator.", {"Returns": "The name of the decorator"}
        )

        # Add the docstring with proper indentation
        indented_docstring = textwrap.indent(docstring_content, "        ")
        code.append(indented_docstring)
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

        # Create a dictionary for the Args section
        args_dict = {}
        for param in params:
            param_name = param["name"]
            param_desc = param.get("description", "")
            args_dict[param_name] = param_desc

        # Generate docstring using the helper method
        init_docstring = self._generate_docstring(
            f"Initialize the {name} decorator.", {"Args": args_dict}
        )

        # Indent the docstring and append it as a single string
        indented_init_docstring = textwrap.indent(init_docstring, "        ")
        code.append(indented_init_docstring)

        # Add validation code
        code.append("        # Initialize with base values")
        code.append("        super().__init__()")
        code.append("")
        code.append("        # Store parameters")
        for param in params:
            param_name = param["name"]
            code.append(f"        self._{param_name} = {param_name}")

            # If the parameter is named 'parameters', we need to add a special case
            # to avoid conflicts with the BaseDecorator.parameters property
            if param_name == "parameters":
                code.append(
                    "        # Add an alias for the 'parameters' parameter to avoid conflicts"
                )
                code.append("        self._params = self._parameters")
        code.append("")
        code.append("        # Validate parameters")
        self._add_validation_code(decorator, params, code)

        # Add getters for each parameter
        code.append("")
        self._add_get_property_methods(decorator, params, code)

        # Add to_dict method
        code.append("    def to_dict(self) -> Dict[str, Any]:")
        code.append(f'        """Convert the decorator to a dictionary.')
        code.append("")
        code.append("        Args:")
        code.append("            self: The decorator instance")
        code.append("")
        code.append("        Returns:")
        code.append("            Dictionary representation of the decorator")
        code.append(f'        """')
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
        code.append(f'        """Convert the decorator to a string.')
        code.append("")
        code.append("        Args:")
        code.append("            self: The decorator instance")
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

        # Generate docstring for apply method with proper indentation
        apply_docstring = self._generate_docstring(
            "Apply the decorator to a prompt string.",
            {
                "Args": {"prompt": "The prompt to apply the decorator to"},
                "Returns": "The modified prompt",
            },
        )
        # Indent the docstring properly
        indented_apply_docstring = textwrap.indent(apply_docstring, "        ")
        code.append(indented_apply_docstring)

        code.append(
            "        # Subclasses should override this method with specific behavior"
        )
        code.append("        return prompt")

        # Add is_compatible_with_version method
        code.append("")
        code.append("    @classmethod")
        code.append("    def is_compatible_with_version(cls, version: str) -> bool:")

        # Generate docstring using the helper method
        compatibility_docstring = self._generate_docstring(
            "Check if the decorator is compatible with a specific version",
            {
                "Args": {"version": "The version to check compatibility with."},
                "Returns": "True if compatible, False otherwise.",
                "Raises": {
                    "IncompatibleVersionError": "If the version is incompatible."
                },
            },
        )
        # Indent the docstring properly
        indented_compatibility_docstring = textwrap.indent(
            compatibility_docstring, "        "
        )
        code.append(indented_compatibility_docstring)

        # Add implementation
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

        # Generate docstring using the helper method
        metadata_docstring = self._generate_docstring(
            "Get metadata about the decorator.",
            {"Returns": "Dictionary containing metadata about the decorator"},
        )

        # Indent the docstring and append it as a single string
        indented_metadata_docstring = textwrap.indent(metadata_docstring, "        ")
        code.append(indented_metadata_docstring)

        code.append("        return {")
        code.append('            "name": cls.__name__,')
        code.append(f'            "description": """{description}""",')
        code.append(f'            "category": "{category}",')
        code.append('            "version": cls.version,')
        code.append("        }")

        return "\n".join(imports + code)

    def _add_get_property_methods(
        self, decorator: Dict[str, Any], params: List[Dict[str, Any]], code: List[str]
    ) -> None:
        """
        Add property getter methods for each parameter.

        Args:
            decorator: The decorator data
            params: The parameters
            code: The code list to append to

        Returns:
            None
        """
        for param in params:
            param_name = param["name"]
            param_type = self._get_python_type(param, decorator)

            # Handle the special case where a parameter is named 'parameters'
            # which conflicts with the BaseDecorator.parameters property
            property_name = param_name
            if param_name == "parameters":
                property_name = "params"

            # Add property getter
            code.append(f"    @property")
            code.append(f"    def {property_name}(self) -> {param_type}:")
            code.append(f'        """Get the {param_name} parameter value.')
            code.append("")
            code.append("        Args:")
            code.append("            self: The decorator instance")
            code.append("")
            code.append("        Returns:")
            code.append(f"            The {param_name} parameter value")
            code.append('        """')
            code.append(f"        return self._{param_name}")
            code.append("")

    def _add_validation_code(
        self, decorator: Dict[str, Any], params: List[Dict[str, Any]], code: List[str]
    ) -> None:
        """
        Add validation code for parameters.

        Args:
            decorator: The decorator data
            params: The parameters
            code: The code list to append to

        Returns:
            None
        """
        # Add validation code
        code.append("        # Initialize with base values")
        code.append("        super().__init__()")
        code.append("")
        code.append("        # Store parameters")
        for param in params:
            param_name = param["name"]
            code.append(f"        self._{param_name} = {param_name}")

            # If the parameter is named 'parameters', we need to add a special case
            # to avoid conflicts with the BaseDecorator.parameters property
            if param_name == "parameters":
                code.append(
                    "        # Add an alias for the 'parameters' parameter to avoid conflicts"
                )
                code.append("        self._params = self._parameters")
        code.append("")
        code.append("        # Validate parameters")
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

                # Check if we have an enum class for this parameter
                enum_class_name = None
                for enum_name, values in self.enums.items():
                    if set(enum_values).issubset(set(values)):
                        enum_class_name = enum_name
                        break

                if enum_class_name:
                    # Use the enum class values for validation
                    enum_values_code = [
                        f"{enum_class_name}.{self._convert_to_enum_constant(val)}.value"
                        for val in enum_values
                    ]
                    enum_str = ", ".join(enum_values_code)

                    # Create a proper list of enum values for the validation check
                    code.append(f"            valid_values = [{enum_str}]")
                    code.append(
                        f"            if self._{param_name} not in valid_values:"
                    )
                    code.append(
                        f"                raise ValidationError(f\"The parameter '{param_name}' must be one of the allowed enum values: {{valid_values}}. Got {{self._{param_name}}}\")"
                    )
                else:
                    # Format enum values properly for the error message
                    enum_str_list = [f'"{val}"' for val in enum_values]
                    enum_str = ", ".join(enum_str_list)

                    # Create a proper list of enum values for the validation check
                    code.append(
                        f"            if self._{param_name} not in [{enum_str}]:"
                    )
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
        """
        Generate the enums module with all enum definitions.

        Args:
            self: The CodeGenerator instance

        Returns:
            str: The generated code for the enums module
        """
        code = [
            '"""Decorator Enum Definitions.',
            "",
            "This module provides enum types used by decorators.",
            '"""',
            "",
            "from enum import Enum, auto",
            "from typing import Dict, List, Optional, Union, Any",
            "",
        ]

        # Make sure we collect enums before generating them
        self._collect_enums()

        # Add each enum class
        for enum_name, (description, values) in self.enum_definitions.items():
            code.append(f"class {enum_name}(Enum):")

            # Add docstring for the enum class
            code.append(f'    """{description}"""')
            code.append("")

            # Add enum values
            for value in values:
                # Ensure the value is a valid Python identifier
                safe_value = value
                if not safe_value.isidentifier():
                    # Replace non-alphanumeric characters with underscores
                    safe_value = "".join(c if c.isalnum() else "_" for c in safe_value)
                    # Ensure it doesn't start with a digit
                    if safe_value[0].isdigit():
                        safe_value = f"_{safe_value}"
                    logger.warning(
                        f"Converted enum value '{value}' to '{safe_value}' to make it a valid identifier"
                    )

                code.append(f"    {safe_value} = auto()")

            code.append("")
            code.append("")

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
                    # Convert to snake_case first, then to CamelCase to handle camelCase properly
                    param_name_snake = camel_to_snake(param_name)
                    param_name_camel = snake_to_camel(param_name_snake)
                    # Ensure decorator name is properly capitalized
                    decorator_name = decorator["decoratorName"]
                    enum_name = f"{decorator_name}{param_name_camel}Enum"
                    description = param.get(
                        "description", f"Options for {decorator_name}.{param_name}"
                    )

                    # Ensure description ends with a period for D415 compliance
                    if description and not description.endswith((".", "?", "!")):
                        description = f"{description}."

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
                # Convert to snake_case first, then to CamelCase to handle camelCase properly
                param_name_snake = camel_to_snake(param_name)
                param_name_camel = snake_to_camel(param_name_snake)
                # Ensure decorator name is properly capitalized
                decorator_name = decorator["decoratorName"]
                enum_name = f"{decorator_name}{param_name_camel}Enum"
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

    def _convert_to_enum_constant(self, name: str) -> str:
        """Convert a string to a valid Python enum constant.

        Args:
            name: The string to convert.

        Returns:
            A valid Python enum constant.
        """
        # Replace any non-alphanumeric characters with underscores
        result = re.sub(r"[^a-zA-Z0-9]", "_", name)

        # If the name starts with a digit, prefix it with an underscore
        if result and result[0].isdigit():
            result = "_" + result

        # Ensure consistent capitalization for compound words
        # This is important for names like "citationStyle" to become "CitationStyle"
        # in enum class names like "AcademicCitationStyleEnum"
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

    def _generate_docstring(
        self,
        first_line: str,
        sections: Dict[str, Union[str, List[str], Dict[str, str]]] = None,
    ) -> str:
        """Generate a properly formatted docstring.

        Args:
            first_line: The first line of the docstring
            sections: Dictionary of section names to content (string, list of strings, or dict of attribute descriptions)

        Returns:
            A formatted docstring as a string
        """
        # Ensure first line ends with a period for D415 compliance
        if first_line and not first_line.rstrip().endswith((".", "!", "?")):
            first_line = first_line.rstrip() + "."

        docstring = [f'"""{first_line}']

        if sections:
            # Always add blank line after first line for D205 compliance
            docstring.append("")

            first_section = True
            for section_name, content in sections.items():
                # Add blank line before section for D411 compliance (except for first section after description)
                if not first_section:
                    docstring.append("")
                first_section = False

                docstring.append(f"{section_name}:")

                if isinstance(content, dict):
                    # Content is a dictionary of attributes
                    for attr_name, attr_desc in content.items():
                        docstring.append(f"    {attr_name}: {attr_desc}")
                elif isinstance(content, list):
                    # Content is a list of lines
                    for line in content:
                        docstring.append(f"    {line}")
                else:
                    # Content is a string
                    docstring.append(f"    {content}")

                # Add blank line after section for D410 compliance
                docstring.append("")

        # Add closing quotes
        docstring.append('"""')

        # Join all lines with newlines
        return "\n".join(docstring)

    def _generate_module_docstring(self, name: str, description: str) -> str:
        """Generate a module docstring.

        Args:
            name: The name of the module
            description: The description of the module

        Returns:
            A formatted module docstring
        """
        lines = []

        # Remove blank line at the beginning for D212 compliance
        lines.append(f'"""{description}"""')

        return "\n".join(lines)

    def _generate_decorator_class(self, decorator: Dict) -> List[str]:
        """Generate the decorator class definition.

        Args:
            decorator: The decorator data

        Returns:
            List of code lines for the class definition
        """
        name = decorator["decoratorName"]
        description = decorator.get("description", "")
        version = decorator.get("version", "1.0.0")  # Default version
        params = decorator.get("parameters", [])

        # Class definition
        code = [
            f"class {name}(BaseDecorator):",
            f'    """{description}',
            "",
            "    Attributes:",
        ]

        # Add attribute documentation for each parameter
        for param in params:
            param_name = param["name"]
            param_desc = param.get("description", "")
            param_type = self._get_python_type(param, decorator)
            code.append(f"        {param_name}: {param_desc} ({param_type})")

        code.append('    """')
        code.append("")

        # Add class-level name attribute to match decorator_name
        code.append(f'    name = "{self._convert_to_snake_case(name)}"')
        code.append(f'    decorator_name = "{self._convert_to_snake_case(name)}"')
        code.append(f'    version = "{version}"  # Initial version')
        code.append("")

        # Add name property
        code.extend(
            [
                "    @property",
                "    def name(self) -> str:",
                '        """Get the name of the decorator.',
                "",
                "        Args:",
                "            self: The decorator instance",
                "",
                "        Returns:",
                "            The name of the decorator",
                "",
                '        """',
                "        return self.decorator_name",
                "",
            ]
        )

        return code


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

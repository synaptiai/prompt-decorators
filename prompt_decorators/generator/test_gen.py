#!/usr/bin/env python
"""Test Generator for Prompt Decorators.

This module generates comprehensive unit tests for all decorators defined in the registry.
It creates test cases for:
1. Decorator initialization with valid and invalid parameters
2. Parameter validation
3. Apply method functionality
4. Serialization/deserialization
5. Compatibility checks

The generated tests follow pytest conventions and can be run with standard pytest commands.
"""

import glob
import json
import logging
import os
import re
import sys
import textwrap
import unittest
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from prompt_decorators.core.base import Parameter, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.generator.registry import DecoratorData, RegistryScanner


# Define our own Parameter class for test generation
class Parameter:
    """Parameter class for test generation."""

    def __init__(
        self,
        name: str,
        type: str = "string",
        required: bool = False,
        validation: Optional[Dict[str, Any]] = None,
        schema: Optional[Dict[str, Any]] = None,
        enum: Optional[List[str]] = None,
        description: Optional[str] = None,
    ):
        """Initialize a Parameter.

        Args:
            name: The name of the parameter
            type: The type of the parameter
            required: Whether the parameter is required
            validation: Validation rules for the parameter
            schema: Schema for the parameter
            enum: Enum values for the parameter
            description: Description of the parameter
        """
        self.name = name

        # Normalize type to one of the allowed values
        if type in ["string", "integer", "float", "boolean", "enum", "array", "object"]:
            self.type = type
        elif type == "number":
            self.type = "float"
        elif "|" in type:
            # Handle union types like "string|number|boolean|enum"
            types = type.split("|")
            if "enum" in types:
                self.type = "enum"
            elif "string" in types:
                self.type = "string"
            elif "number" in types or "float" in types:
                self.type = "float"
            elif "integer" in types:
                self.type = "integer"
            elif "boolean" in types:
                self.type = "boolean"
            elif "array" in types:
                self.type = "array"
            elif "object" in types:
                self.type = "object"
            else:
                self.type = "string"  # Default to string
        else:
            self.type = "string"  # Default to string

        self.required = required
        self.validation = validation or {}
        self.schema = schema or {}
        self.enum = enum or []
        self.description = description


class TestGenerator:
    """Generator for decorator unit tests."""

    def __init__(
        self, registry_dir: str, output_dir: str, template_dir: Optional[str] = None
    ):
        """Initialize the TestGenerator.

        Args:
            registry_dir: Path to the registry directory
            output_dir: Path to the output directory for generated tests
            template_dir: Optional path to the template directory
        """
        self.registry_dir = registry_dir
        self.output_dir = output_dir
        self.template_dir = template_dir

        # Get all decorator data
        self.scanner = RegistryScanner(registry_dir)
        self.decorators = self.scanner.scan()

        # Store unique tags
        self.tags: Set[str] = set()
        for decorator in self.decorators:
            if "tags" in decorator:
                for tag in decorator["tags"]:
                    self.tags.add(tag)

    def generate_all_tests(self) -> List[str]:
        """Generate test files for all decorators in the registry.

        Returns:
            List of paths to the generated test files
        """
        generated_files = []

        # Create the output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

        # Generate the conftest.py file
        conftest_path = os.path.join(self.output_dir, "conftest.py")
        with open(conftest_path, "w") as f:
            f.write(self.generate_conftest())
            # Ensure file ends with a newline
            if not self.generate_conftest().endswith("\n"):
                f.write("\n")

        generated_files.append(conftest_path)

        # Generate test files for each decorator
        for decorator_file in glob.glob(
            os.path.join(self.registry_dir, "**/*.json"), recursive=True
        ):
            # Skip the template file
            if os.path.basename(decorator_file) == "decorator-template.json":
                logging.info(f"Skipping template file: {decorator_file}")
                continue

            try:
                with open(decorator_file, "r") as f:
                    decorator_data = json.load(f)

                # Skip if the decorator is marked as skipTest
                if decorator_data.get("skipTest", False):
                    continue

                # Generate the test file content
                test_content = self.generate_decorator_test(decorator_data)
                if not test_content:
                    continue

                # Save the test file
                decorator_name = decorator_data.get("decoratorName", "")
                snake_case_name = self._convert_to_snake_case(decorator_name)
                test_file_name = f"test_{snake_case_name}.py"
                test_file_path = os.path.join(self.output_dir, test_file_name)

                with open(test_file_path, "w") as f:
                    f.write(test_content)
                    # Ensure file ends with a newline
                    if not test_content.endswith("\n"):
                        f.write("\n")

                generated_files.append(test_file_path)
            except Exception as e:
                logging.error(f"Error generating tests for {decorator_file}: {e}")

        # Generate the test discovery file
        discovery_path = os.path.join(self.output_dir, "__init__.py")
        with open(discovery_path, "w") as f:
            discovery_content = self.generate_test_discovery()
            f.write(discovery_content)
            # Ensure file ends with a newline
            if not discovery_content.endswith("\n"):
                f.write("\n")

        generated_files.append(discovery_path)

        return generated_files

    def generate_conftest(self) -> str:
        """Generate the conftest.py file for pytest.

        Returns:
            The conftest.py file content as a string
        """
        conftest_content = [
            '"""Pytest configuration for decorator tests."""',
            "",
            "import pytest",
            "import importlib",
            "from typing import Optional, Type",
            "",
            "from prompt_decorators.core.base import BaseDecorator",
            "",
            "@pytest.fixture",
            "def load_decorator():",
            '    """Fixture to load a decorator class by name."""',
            "    def _load_decorator(decorator_name: str) -> Optional[Type[BaseDecorator]]:",
            "        try:",
            "            module = importlib.import_module(f'prompt_decorators.decorators.generated.decorators.{decorator_name.lower()}')",
            "            return getattr(module, decorator_name)",
            "        except (ImportError, AttributeError):",
            "            return None",
            "    return _load_decorator",
            "",
        ]

        return "\n".join(conftest_content)

    def generate_decorator_test(self, decorator_data: Dict[str, Any]) -> Optional[str]:
        """Generate a test file for a decorator.

        Args:
            decorator_data: The decorator data to generate a test file for

        Returns:
            The test file content as a string, or None if the decorator should be skipped
        """
        # Skip if the decorator is marked as skipTest
        if decorator_data.get("skipTest", False):
            return None

        # Get the decorator name
        decorator_name = decorator_data.get("decoratorName", "")
        if not decorator_name:
            return None

        # Create a dictionary with the decorator data
        self.decorator_data = {
            "name": decorator_name,
            "description": decorator_data.get("description", ""),
            "category": decorator_data.get("category", "unknown"),
            "version": decorator_data.get("version", "1.0.0"),
            "parameters": [
                {
                    "name": param["name"],
                    "type": param.get("type", "string"),
                    "required": param.get("required", False),
                    "validation": param.get("validation", {}),
                    "schema": param.get("schema", {}),
                    "enum": param.get("enum", []),
                    "description": param.get("description", ""),
                }
                for param in decorator_data.get("parameters", [])
            ],
            "examples": decorator_data.get("examples", []),
            "tags": decorator_data.get("tags", []),
        }

        # Generate the file header
        header = self._generate_file_header(decorator_name)

        # Generate the test content
        content = self._generate_test_content(decorator_data)

        # Combine the header and content
        return header + content

    def _generate_test_content(self, decorator_data: Dict[str, Any]) -> str:
        """Generate the test content for a decorator.

        Args:
            decorator_data: The decorator data to generate test content for

        Returns:
            The test content as a string
        """
        # Generate the test class
        test_class_lines = self._generate_test_class(decorator_data)

        # Join the lines with newlines
        return "\n".join(test_class_lines)

    def _generate_file_header(self, decorator_name: str) -> str:
        """Generate the file header for a test file.

        Args:
            decorator_name: The name of the decorator

        Returns:
            The file header as a string
        """
        snake_case_name = self._convert_to_snake_case(decorator_name)

        header = [
            '"""Tests for the {0} decorator."""'.format(decorator_name),
            "",
            "import unittest",
            "from prompt_decorators.core.base import ValidationError",
            "from prompt_decorators.decorators.generated.decorators.{0} import {1}".format(
                snake_case_name, decorator_name
            ),
            "",
            "",
        ]

        return "\n".join(header)

    def _generate_test_class(self, decorator_data: Dict[str, Any]) -> List[str]:
        """Generate the test class for a decorator.

        Args:
            decorator_data: The decorator data to generate a test class for

        Returns:
            List of code lines for the test class
        """
        decorator_name = decorator_data.get("decoratorName", "")
        description = decorator_data.get("description", "")

        # Start with the class definition and docstring
        class_lines = [
            f"class Test{decorator_name}(unittest.TestCase):",
            f'    """Tests for the {decorator_name} decorator.',
            "",
        ]

        # Add the description to the docstring if available
        if description:
            # Split the description into lines of 80 characters or less
            description_lines = []
            words = description.split()
            current_line = ""

            for word in words:
                if (
                    len(current_line) + len(word) + 1 <= 76
                ):  # 76 to account for indentation
                    if current_line:
                        current_line += " " + word
                    else:
                        current_line = word
                else:
                    description_lines.append(current_line)
                    current_line = word

            if current_line:
                description_lines.append(current_line)

            # Add the description lines to the docstring
            for line in description_lines:
                class_lines.append(f"    {line}")

            class_lines.append("")

        # Close the docstring
        class_lines.append('    """')

        # Add the _get_valid_params method
        valid_params_lines = self._generate_get_valid_params_method(decorator_data)
        class_lines.extend(valid_params_lines)

        # Add test methods
        test_methods = self._generate_test_methods(decorator_data)
        for method in test_methods:
            class_lines.append("")  # Add a blank line between methods
            class_lines.append(method)

        return class_lines

    def _generate_get_valid_params_method(
        self, decorator_data: Dict[str, Any]
    ) -> List[str]:
        """Generate the _get_valid_params method for testing.

        Args:
            decorator_data: The decorator data from the registry

        Returns:
            List of code lines for the method
        """
        decorator_name = decorator_data.get("decoratorName", "")
        parameters = decorator_data.get("parameters", [])

        code_lines = [
            "    def _get_valid_params(self):",
            '        """Get valid parameters for testing."""',
            "        return {",
        ]

        for param in parameters:
            param_name = param.get("name", "")
            param_type = param.get("type", "")
            default_value = param.get("default", None)
            enum_values = param.get("enum", [])
            validation = param.get("validation", {})

            # Determine a valid value for the parameter
            valid_value = None

            # First check for enum values
            if enum_values and len(enum_values) > 0:
                # For string enums, we need to quote the value
                if param_type == "string" or param_type == "enum":
                    valid_value = f'"{enum_values[0]}"'
                else:
                    # For non-string enums, convert to string representation
                    valid_value = str(enum_values[0])
            # Then check for default value
            elif default_value is not None:
                if param_type == "string" or param_type == "enum":
                    valid_value = f'"{default_value}"'
                elif param_type == "boolean":
                    # Ensure boolean values are properly formatted for Python
                    if isinstance(default_value, bool):
                        valid_value = str(default_value)
                    elif default_value == "true" or default_value == True:
                        valid_value = "True"
                    elif default_value == "false" or default_value == False:
                        valid_value = "False"
                    else:
                        valid_value = str(default_value)
                elif param_type == "array" and isinstance(default_value, list):
                    # Format array elements properly
                    elements = []
                    for element in default_value:
                        if isinstance(element, str):
                            elements.append(f'"{element}"')
                        else:
                            elements.append(str(element))
                    valid_value = f"[{', '.join(elements)}]"
                else:
                    valid_value = str(default_value)
            # Otherwise, generate a reasonable default based on type
            else:
                if param_type == "string" or param_type == "enum":
                    valid_value = '"example_value"'
                elif param_type == "integer":
                    # Use a value that satisfies minimum constraints if present
                    if validation and "minimum" in validation:
                        min_val = validation["minimum"]
                        # Use a value slightly above the minimum
                        valid_value = str(min_val + 1)
                    else:
                        valid_value = "1"
                elif param_type == "number":
                    # Use a value that satisfies minimum constraints if present
                    if validation and "minimum" in validation:
                        min_val = validation["minimum"]
                        # Use a value slightly above the minimum
                        valid_value = str(min_val + 1)
                    else:
                        valid_value = "1.0"
                elif param_type == "boolean":
                    valid_value = "True"
                elif param_type == "array":
                    valid_value = "[]"
                elif param_type == "object":
                    valid_value = "{}"
                else:
                    valid_value = "None"

            # Add the parameter to the code
            code_lines.append(f'            "{param_name}": {valid_value},')

        code_lines.append("        }")
        return code_lines

    def _generate_test_methods(self, decorator_data: Dict[str, Any]) -> List[str]:
        """Generate test methods for a decorator.

        Args:
            decorator_data: The decorator data to generate test methods for

        Returns:
            List of test methods as strings
        """
        decorator_name = decorator_data.get("decoratorName", "")
        params = decorator_data.get("parameters", [])
        examples = decorator_data.get("examples", [])

        all_methods = []

        # Generate tests for required parameters
        for param in params:
            if param.get("required", False):
                param_obj = Parameter(
                    name=param["name"],
                    type=param.get("type", "string"),
                    required=True,
                    validation=param.get("validation", {}),
                    schema=param.get("schema", {}),
                    enum=param.get("enum", []),
                )
                method_code = self._generate_required_param_test(
                    decorator_name, param_obj
                )
                all_methods.append(method_code)

        # Generate tests for parameter validation
        for param in params:
            param_obj = Parameter(
                name=param["name"],
                type=param.get("type", "string"),
                required=param.get("required", False),
                validation=param.get("validation", {}),
                schema=param.get("schema", {}),
                enum=param.get("enum", []),
            )
            method_code = self._generate_param_validation_test(
                decorator_name, param_obj
            )
            all_methods.append(method_code)

        # Generate tests for apply method using examples
        if examples:
            apply_test_lines = self._generate_apply_examples_test(decorator_data)
            # Make sure the apply_examples test is properly indented
            apply_test_method = "\n".join(apply_test_lines)
            # Fix indentation by adding 4 spaces to the beginning of each line
            apply_test_method = apply_test_method.replace(
                "def test_apply_examples(self):", "    def test_apply_examples(self):"
            )
            apply_test_method = apply_test_method.replace("\n    ", "\n        ")
            all_methods.append(apply_test_method)

        # Generate tests for serialization
        serialization_test = self._generate_serialization_tests(decorator_name)
        all_methods.append(serialization_test)

        # Return the list of methods
        return all_methods

    def _generate_required_param_test(
        self, decorator_name: str, param: Parameter
    ) -> str:
        """Generate test for a required parameter.

        This method creates test cases for required parameter validation,
        ensuring that initialization fails when required parameters are missing.

        Args:
            decorator_name: Name of the decorator being tested
            param: Parameter object containing validation rules

        Returns:
            str: Generated test code as string
        """
        return f"""
    def test_missing_required_param_{param.name}(self):
        \"\"\"Test that initialization fails when missing required parameter {param.name}.\"\"\"
        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "{param.name}" in params:
            del params["{param.name}"]

        # Should raise either ValidationError or TypeError when the required parameter is missing
        with self.assertRaises((ValidationError, TypeError)) as exc_info:
            {decorator_name}(**params)

        # Check that the error message contains the parameter name
        error_message = str(exc_info.exception)
        self.assertTrue(
            "{param.name}" in error_message or
            "required" in error_message.lower()
        )
"""

    def _generate_param_validation_test(
        self, decorator_name: str, param: Parameter
    ) -> str:
        """Generate a test method for parameter validation.

        Args:
            decorator_name: The name of the decorator
            param: The parameter to generate a test for

        Returns:
            The test method as a string
        """
        snake_case_name = self._convert_to_snake_case(decorator_name)
        param_name = param.name
        test_name = f"test_validate_{param_name}"

        test_lines = [
            f"    def {test_name}(self):",
            f'        """Test validation for the {param_name} parameter."""',
            "        # Get valid parameters",
            "        params = self._get_valid_params()",
            "",
        ]

        # Type validation
        if param.type == "string":
            test_lines.extend(
                [
                    "        # Test type validation",
                    "        params['{}'] = 123  # Not a string".format(param_name),
                    "        with self.assertRaises(ValidationError) as context:",
                    f"            {decorator_name}(**params)",
                    f"        self.assertIn('{param_name}', str(context.exception))",
                    "        self.assertIn('string', str(context.exception).lower())",
                    "",
                    "        # Restore valid parameters",
                    "        params = self._get_valid_params()",
                    "",
                ]
            )
        elif param.type == "integer":
            test_lines.extend(
                [
                    "        # Test type validation",
                    "        params['{}'] = 'not_an_integer'  # Not an integer".format(
                        param_name
                    ),
                    "        with self.assertRaises(ValidationError) as context:",
                    f"            {decorator_name}(**params)",
                    f"        self.assertIn('{param_name}', str(context.exception))",
                    "        self.assertIn('integer', str(context.exception).lower())",
                    "",
                    "        # Restore valid parameters",
                    "        params = self._get_valid_params()",
                    "",
                ]
            )
        elif param.type == "float":
            test_lines.extend(
                [
                    "        # Test type validation",
                    "        params['{}'] = 'not_a_number'  # Not a number".format(
                        param_name
                    ),
                    "        with self.assertRaises(ValidationError) as context:",
                    f"            {decorator_name}(**params)",
                    f"        self.assertIn('{param_name}', str(context.exception))",
                    "        self.assertIn('numeric', str(context.exception).lower())",
                    "",
                    "        # Restore valid parameters",
                    "        params = self._get_valid_params()",
                    "",
                ]
            )
        elif param.type == "boolean":
            test_lines.extend(
                [
                    "        # Test type validation",
                    "        params['{}'] = 'not_a_boolean'  # Not a boolean".format(
                        param_name
                    ),
                    "        with self.assertRaises(ValidationError) as context:",
                    f"            {decorator_name}(**params)",
                    f"        self.assertIn('{param_name}', str(context.exception))",
                    "        self.assertIn('boolean', str(context.exception).lower())",
                    "",
                    "        # Restore valid parameters",
                    "        params = self._get_valid_params()",
                    "",
                ]
            )
        elif param.type == "enum":
            if param.enum and len(param.enum) > 0:
                test_lines.extend(
                    [
                        "        # Test type validation",
                        "        params['{}'] = 123  # Not a string".format(param_name),
                        "        with self.assertRaises(ValidationError) as context:",
                        f"            {decorator_name}(**params)",
                        f"        self.assertIn('{param_name}', str(context.exception))",
                        "        self.assertIn('string', str(context.exception).lower())",
                        "",
                        "        # Restore valid parameters",
                        "        params = self._get_valid_params()",
                        "",
                        "        # Test invalid enum value",
                        "        params['{}'] = 'invalid_enum_value'  # Invalid enum value".format(
                            param_name
                        ),
                        "        with self.assertRaises(ValidationError) as context:",
                        f"            {decorator_name}(**params)",
                        f"        self.assertIn('{param_name}', str(context.exception))",
                        "        self.assertTrue('must be one of' in str(context.exception).lower() or 'valid options' in str(context.exception).lower() or 'enum' in str(context.exception).lower())",
                        "",
                        "        # Restore valid parameters",
                        "        params = self._get_valid_params()",
                        "",
                        "        # Test valid enum values",
                    ]
                )

                # Add tests for each valid enum value
                for enum_value in param.enum:
                    test_lines.extend(
                        [
                            f"        params['{param_name}'] = '{enum_value}'",
                            "        # This should not raise an exception",
                            f"        {decorator_name}(**params)",
                        ]
                    )
            else:
                # If there are no enum values defined, just add a comment
                test_lines.extend(
                    [
                        "        # Since no enum values are defined for this parameter,",
                        "        # we'll just verify that any string value is accepted",
                        "        params['{}'] = 'any_string_value'".format(param_name),
                        "        # This should not raise an exception",
                        f"        {decorator_name}(**params)",
                    ]
                )
        elif param.type == "array":
            test_lines.extend(
                [
                    "        # Test type validation",
                    "        params['{}'] = 'not_an_array'  # Not an array".format(
                        param_name
                    ),
                    "        with self.assertRaises(ValidationError) as context:",
                    f"            {decorator_name}(**params)",
                    f"        self.assertIn('{param_name}', str(context.exception))",
                    "        self.assertIn('array', str(context.exception).lower())",
                    "",
                    "        # Restore valid parameters",
                    "        params = self._get_valid_params()",
                    "",
                ]
            )
        elif param.type == "object":
            test_lines.extend(
                [
                    "        # Test type validation",
                    "        params['{}'] = 'not_an_object'  # Not an object".format(
                        param_name
                    ),
                    "        with self.assertRaises(ValidationError) as context:",
                    f"            {decorator_name}(**params)",
                    f"        self.assertIn('{param_name}', str(context.exception))",
                    "        self.assertIn('object', str(context.exception).lower())",
                    "",
                    "        # Restore valid parameters",
                    "        params = self._get_valid_params()",
                    "",
                ]
            )

        # Add validation for additional constraints
        if param.validation:
            if "pattern" in param.validation:
                pattern = param.validation["pattern"]
                test_lines.extend(
                    [
                        "        # Test pattern validation",
                        f"        params['{param_name}'] = 'invalid-pattern'  # Does not match pattern",
                        "        with self.assertRaises(ValidationError) as context:",
                        f"            {decorator_name}(**params)",
                        f"        self.assertIn('{param_name}', str(context.exception))",
                        "        self.assertIn('pattern', str(context.exception).lower())",
                        "",
                        "        # Restore valid parameters",
                        "        params = self._get_valid_params()",
                        "",
                    ]
                )

            if "minimum" in param.validation and param.type in ["integer", "float"]:
                minimum = param.validation["minimum"]
                test_lines.extend(
                    [
                        "        # Test minimum value validation",
                        f"        params['{param_name}'] = {minimum - 1}  # Below minimum",
                        "        with self.assertRaises(ValidationError) as context:",
                        f"            {decorator_name}(**params)",
                        f"        self.assertIn('{param_name}', str(context.exception))",
                        "        self.assertTrue('minimum' in str(context.exception).lower() or 'greater than' in str(context.exception).lower())",
                        "",
                        "        # Restore valid parameters",
                        "        params = self._get_valid_params()",
                        "",
                    ]
                )

            if "maximum" in param.validation and param.type in ["integer", "float"]:
                maximum = param.validation["maximum"]
                test_lines.extend(
                    [
                        "        # Test maximum value validation",
                        f"        params['{param_name}'] = {maximum + 1}  # Above maximum",
                        "        with self.assertRaises(ValidationError) as context:",
                        f"            {decorator_name}(**params)",
                        f"        self.assertIn('{param_name}', str(context.exception))",
                        "        self.assertTrue('maximum' in str(context.exception).lower() or 'less than' in str(context.exception).lower())",
                        "",
                        "        # Restore valid parameters",
                        "        params = self._get_valid_params()",
                        "",
                    ]
                )

            if "minLength" in param.validation and param.type == "string":
                min_length = param.validation["minLength"]
                test_lines.extend(
                    [
                        "        # Test minimum length validation",
                        f"        params['{param_name}'] = {'a' * (min_length - 1)}  # Too short",
                        "        with self.assertRaises(ValidationError) as context:",
                        f"            {decorator_name}(**params)",
                        f"        self.assertIn('{param_name}', str(context.exception))",
                        "        self.assertTrue('minimum length' in str(context.exception).lower() or 'too short' in str(context.exception).lower())",
                        "",
                        "        # Restore valid parameters",
                        "        params = self._get_valid_params()",
                        "",
                    ]
                )

            if "maxLength" in param.validation and param.type == "string":
                max_length = param.validation["maxLength"]
                test_lines.extend(
                    [
                        "        # Test maximum length validation",
                        f"        params['{param_name}'] = {'a' * (max_length + 1)}  # Too long",
                        "        with self.assertRaises(ValidationError) as context:",
                        f"            {decorator_name}(**params)",
                        f"        self.assertIn('{param_name}', str(context.exception))",
                        "        self.assertTrue('maximum length' in str(context.exception).lower() or 'too long' in str(context.exception).lower())",
                        "",
                        "        # Restore valid parameters",
                        "        params = self._get_valid_params()",
                        "",
                    ]
                )

            if "minItems" in param.validation and param.type == "array":
                min_items = param.validation["minItems"]
                test_lines.extend(
                    [
                        "        # Test minimum items validation",
                        f"        params['{param_name}'] = [1] * {min_items - 1}  # Too few items",
                        "        with self.assertRaises(ValidationError) as context:",
                        f"            {decorator_name}(**params)",
                        f"        self.assertIn('{param_name}', str(context.exception))",
                        "        self.assertTrue('minimum' in str(context.exception).lower() or 'too few' in str(context.exception).lower())",
                        "",
                        "        # Restore valid parameters",
                        "        params = self._get_valid_params()",
                        "",
                    ]
                )

            if "maxItems" in param.validation and param.type == "array":
                max_items = param.validation["maxItems"]
                test_lines.extend(
                    [
                        "        # Test maximum items validation",
                        f"        params['{param_name}'] = [1] * {max_items + 1}  # Too many items",
                        "        with self.assertRaises(ValidationError) as context:",
                        f"            {decorator_name}(**params)",
                        f"        self.assertIn('{param_name}', str(context.exception))",
                        "        self.assertTrue('maximum' in str(context.exception).lower() or 'too many' in str(context.exception).lower())",
                        "",
                        "        # Restore valid parameters",
                        "        params = self._get_valid_params()",
                        "",
                    ]
                )

        return "\n".join(test_lines)

    def _generate_apply_examples_test(
        self, decorator_data: Dict[str, Any]
    ) -> List[str]:
        """Generate the test_apply_examples method.

        Args:
            decorator_data: The decorator data from the registry

        Returns:
            List of code lines for the method
        """
        decorator_name = decorator_data.get("decoratorName", "")
        examples = decorator_data.get("examples", [])

        code_lines = [
            "def test_apply_examples(self):",
            '    """Test apply method with examples from the decorator definition."""',
        ]

        # If no examples are provided, create a simple test
        if not examples:
            code_lines.append(
                "    # Example of how to use this decorator with specific parameters"
            )
            code_lines.append("    params = self._get_valid_params()")
            code_lines.append(f"    decorator = {decorator_name}(**params)")
            code_lines.append(
                '    result = decorator.apply("Sample prompt for testing.")'
            )
            code_lines.append("    self.assertIsInstance(result, str)")
            # Don't check the exact output, just that it returns something
            code_lines.append("    self.assertTrue(len(result) > 0)")
        else:
            # Generate a test for each example
            for i, example in enumerate(examples):
                description = example.get("description", f"Example {i+1}")
                code_lines.append(f"    # {description}")
                code_lines.append("    params = self._get_valid_params()")

                # If the example specifies parameters, use those instead
                if "parameters" in example:
                    for param_name, param_value in example["parameters"].items():
                        if isinstance(param_value, str):
                            code_lines.append(
                                f"    params['{param_name}'] = '{param_value}'"
                            )
                        else:
                            code_lines.append(
                                f"    params['{param_name}'] = {param_value}"
                            )

                code_lines.append(f"    decorator = {decorator_name}(**params)")
                code_lines.append(
                    '    result = decorator.apply("Sample prompt for testing.")'
                )
                code_lines.append("    self.assertIsInstance(result, str)")

                # Don't check the exact output, just that it returns something
                code_lines.append("    self.assertTrue(len(result) > 0)")

        code_lines.append("")
        return code_lines

    def _generate_serialization_tests(self, decorator_name: str) -> str:
        """Generate tests for serialization.

        Args:
            decorator_name: The name of the decorator

        Returns:
            The test code as a string
        """
        test_lines = [
            "    def test_serialization(self):",
            '        """Test serialization and deserialization."""',
            "        # Create a decorator instance with valid parameters",
            "        params = self._get_valid_params()",
            f"        decorator = {decorator_name}(**params)",
            "",
            "        # Test to_dict() method",
            "        serialized = decorator.to_dict()",
            "        self.assertIsInstance(serialized, dict)",
            f'        self.assertEqual(serialized["name"], "{self._convert_to_snake_case(decorator_name)}")',
            '        self.assertIn("parameters", serialized)',
            '        self.assertIsInstance(serialized["parameters"], dict)',
            "",
            "        # Test that all parameters are included in the serialized output",
            "        for param_name, param_value in params.items():",
            '            self.assertIn(param_name, serialized["parameters"])',
            "",
            "        # Test from_dict() method",
            f"        deserialized = {decorator_name}.from_dict(serialized)",
            f"        self.assertIsInstance(deserialized, {decorator_name})",
            "",
            "        # Test that the deserialized decorator has the same parameters",
            "        deserialized_dict = deserialized.to_dict()",
            "        self.assertEqual(serialized, deserialized_dict)",
        ]

        return "\n".join(test_lines)

    def _format_params_for_test(self, params: Dict[str, Any]) -> str:
        """Format parameters for test code.

        Args:
            params: Dictionary of parameter names and values

        Returns:
            Formatted string representation of parameters
        """
        if not params:
            return "{}"

        formatted_params = {}

        for name, value in params.items():
            if value is None:
                formatted_params[name] = "None"
            elif isinstance(value, bool):
                formatted_params[name] = str(value)
            elif isinstance(value, (int, float)):
                formatted_params[name] = str(value)
            elif isinstance(value, str):
                # Check if this is a string representation of a Python value
                if (
                    value in ["True", "False", "None"]
                    or (value.startswith("[") and value.endswith("]"))
                    or (value.startswith("{") and value.endswith("}"))
                ):
                    formatted_params[name] = value
                else:
                    # Use double quotes if the string contains apostrophes
                    if "'" in value:
                        formatted_params[name] = f'"{value}"'
                    else:
                        formatted_params[name] = f"'{value}'"
            elif isinstance(value, list):
                # Format list elements properly
                formatted_elements = []
                for element in value:
                    if isinstance(element, str):
                        formatted_elements.append(f"'{element}'")
                    else:
                        formatted_elements.append(str(element))
                formatted_params[name] = f"[{', '.join(formatted_elements)}]"
            elif isinstance(value, dict):
                # Format dictionary properly
                formatted_dict = "{"
                for k, v in value.items():
                    if isinstance(v, str):
                        formatted_dict += f"'{k}': '{v}', "
                    else:
                        formatted_dict += f"'{k}': {v}, "
                formatted_dict = formatted_dict.rstrip(", ") + "}"
                formatted_params[name] = formatted_dict
            else:
                formatted_params[name] = f"'{value}'"

        # Convert the dictionary to a string representation
        return (
            "{" + ", ".join([f"'{k}': {v}" for k, v in formatted_params.items()]) + "}"
        )

    def generate_test_discovery(self) -> str:
        """Generate the __init__.py file for test discovery.

        Returns:
            The __init__.py file content as a string
        """
        init_content = [
            '"""Test package for auto-generated decorator tests."""',
            "",
            "# This file is intentionally empty.",
            "# It ensures that pytest recognizes this directory as a test package.",
            "",
        ]

        return "\n".join(init_content)

    def _convert_to_snake_case(self, name: str) -> str:
        """
        Convert a camelCase or PascalCase string to snake_case.

        Args:
            name: The string to convert

        Returns:
            The converted snake_case string
        """
        # Add underscore before uppercase letters
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        # Add underscore between lowercase and uppercase letters
        s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
        # Convert to lowercase
        return s2.lower()


def main():
    """Run the test generator as a standalone script."""
    import argparse
    import os
    import sys

    parser = argparse.ArgumentParser(description="Generate tests for prompt decorators")
    parser.add_argument(
        "--registry-dir",
        default="registry",
        help="Path to the registry directory (default: registry)",
    )
    parser.add_argument(
        "--output-dir",
        default="tests/auto",
        help="Path to the output directory for generated tests (default: tests/auto)",
    )
    parser.add_argument(
        "--template-dir",
        default=None,
        help="Path to the template directory (default: None)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )

    args = parser.parse_args()

    # Set up logging
    log_level = logging.INFO if args.verbose else logging.WARNING
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Generate the tests
    generator = TestGenerator(
        registry_dir=args.registry_dir,
        output_dir=args.output_dir,
        template_dir=args.template_dir,
    )

    try:
        generated_files = generator.generate_all_tests()
        logging.info(f"Generated {len(generated_files)} test files")
        for file_path in generated_files:
            logging.info(f"  - {file_path}")
        return 0
    except Exception as e:
        logging.error(f"Error generating tests: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

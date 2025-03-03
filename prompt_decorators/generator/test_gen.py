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

import os
import re
from typing import Any, Dict, List, Optional, Set

from prompt_decorators.core.base import Parameter
from prompt_decorators.generator.registry import RegistryScanner


class TestGenerator:
    """Generator for decorator unit tests."""

    def __init__(
        self, registry_dir: str, output_dir: str, template_dir: Optional[str] = None
    ):
        """Initialize the TestGenerator.

        Args:
            registry_dir: Directory containing the registry
            output_dir: Directory to write generated tests to
            template_dir: Optional directory containing templates
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
            List of generated file paths
        """
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

        # Generate the conftest file
        conftest_path = os.path.join(self.output_dir, "conftest.py")
        with open(conftest_path, "w") as f:
            f.write(self.generate_conftest())

        # Generate the test discovery file
        discovery_path = os.path.join(self.output_dir, "__init__.py")
        with open(discovery_path, "w") as f:
            f.write(self.generate_test_discovery())

        # Generate test files for each decorator
        test_files = [conftest_path, discovery_path]
        for decorator_data in self.decorators:
            test_file_path = self.generate_decorator_test(decorator_data)
            if test_file_path:
                test_files.append(test_file_path)

        return test_files

    def generate_conftest(self) -> str:
        """Generate a conftest.py file for pytest fixtures.

        Returns:
            The content of the conftest.py file
        """
        conftest_content = [
            "# Generated file - DO NOT EDIT BY HAND",
            "",
            "import pytest",
            "from prompt_decorators.decorators import *",
            "",
            "",
            "@pytest.fixture",
            "def decorator_registry():",
            '    """Fixture providing access to all registered decorators."""',
            "    from prompt_decorators.core.registry import get_registry",
            "    return get_registry()",
            "",
        ]

        return "\n".join(conftest_content)

    def generate_decorator_test(self, decorator_data: Dict[str, Any]) -> Optional[str]:
        """Generate a test file for a decorator.

        Args:
            decorator_data: The decorator data to generate tests for

        Returns:
            The path to the generated test file, or None if no tests were generated
        """
        # Extract decorator details
        decorator_name = decorator_data.get("decoratorName")
        if not decorator_name:
            return None

        # Generate the test content
        test_content = self._generate_test_content(decorator_data)
        if not test_content:
            return None

        # Make sure there's a directory to save the file
        os.makedirs(self.output_dir, exist_ok=True)

        # Save the test file
        snake_case_name = self._convert_to_snake_case(decorator_name)
        test_file_name = f"test_{snake_case_name}.py"
        test_file_path = os.path.join(self.output_dir, test_file_name)

        with open(test_file_path, "w") as f:
            f.write(test_content)

        return test_file_path

    def _generate_test_content(self, decorator_data: Dict[str, Any]) -> str:
        """Generate test content for a decorator.

        Args:
            decorator_data: The decorator data to generate tests for

        Returns:
            The content of the test file
        """
        decorator_name = decorator_data.get("decoratorName", "")
        if not decorator_name:
            return ""

        # Generate file header
        header = self._generate_file_header(decorator_name)

        # Generate test class
        test_class = self._generate_test_class(decorator_data)

        # Combine everything
        content = header + "\n".join(test_class)

        return content

    def _generate_file_header(self, decorator_name: str) -> str:
        """Generate the header for a test file.

        Args:
            decorator_name: The name of the decorator

        Returns:
            The header content
        """
        snake_case_name = self._convert_to_snake_case(decorator_name)

        header_lines = [
            "# Generated file - DO NOT EDIT BY HAND",
            "",
            "import pytest",
            "import json",
            "from prompt_decorators.core.base import ValidationError",
            f"from prompt_decorators.decorators import {decorator_name}",
            "",
            "",
            f"# Tests for the {decorator_name} decorator",
            f"# {'-' * len(f'Tests for the {decorator_name} decorator')}",
            "",
        ]

        return "\n".join(header_lines)

    def _generate_test_class(self, decorator_data: Dict[str, Any]) -> List[str]:
        """Generate a test class for a decorator.

        Args:
            decorator_data: The decorator data to generate tests for

        Returns:
            A list of code lines for the test class
        """
        decorator_name = decorator_data.get("decoratorName", "")
        test_methods = self._generate_test_methods(decorator_data)

        # Start with the class definition
        class_lines = [
            f"class Test{decorator_name}:",
            f'    """Tests for the {decorator_name} decorator."""',
            "",
        ]

        # Add helper method for valid parameters
        valid_params_method = self._generate_valid_params_method(decorator_data)
        class_lines.extend(valid_params_method)

        # Add all test methods
        class_lines.extend(test_methods)

        return class_lines

    def _generate_valid_params_method(
        self, decorator_data: Dict[str, Any]
    ) -> List[str]:
        """Generate the _get_valid_params helper method for the test class.

        Args:
            decorator_data: The decorator data to generate for

        Returns:
            List of code lines for the _get_valid_params method
        """
        params = decorator_data.get("parameters", [])

        code = [
            "    def _get_valid_params(self):",
            '        """Get valid parameters for testing."""',
            "        return {",
        ]

        for param in params:
            param_name = param["name"]
            param_type = param.get("type", "string")

            # Get a valid value for this parameter type
            if param_type == "string":
                if "enum" in param:
                    # Use the first enum value
                    value = f'"{param["enum"][0]}"'
                elif "default" in param:
                    value = f'"{param["default"]}"'
                else:
                    value = '"test_value"'
            elif param_type == "integer":
                if "default" in param:
                    value = str(param["default"])
                else:
                    value = "1"
            elif param_type == "number" or param_type == "float":
                if "default" in param:
                    value = str(param["default"])
                else:
                    value = "1.0"
            elif param_type == "boolean":
                if "default" in param:
                    value = str(param["default"]).lower()
                else:
                    value = "True"
            elif param_type == "array":
                if "default" in param:
                    value = str(param["default"])
                else:
                    value = "[]"
            elif param_type == "enum":
                if "enum" in param:
                    # Use the first enum value
                    value = f'"{param["enum"][0]}"'
                elif "default" in param:
                    value = f'"{param["default"]}"'
                else:
                    value = '""'
            else:
                value = '""'

            code.append(f'            "{param_name}": {value},')

        code.append("        }")
        code.append("")

        return code

    def _generate_test_methods(self, decorator_data: Dict[str, Any]) -> List[str]:
        """Generate test methods for a decorator.

        Args:
            decorator_data: Decorator data from registry

        Returns:
            List of code lines
        """
        name = decorator_data["decoratorName"]
        params = decorator_data.get("parameters", [])
        code = []

        # Check if there are any required parameters
        has_required_params = any(param.get("required", False) for param in params)

        # Test initialization with default parameters
        code.append("    def test_initialization_default_params(self, load_decorator):")
        code.append('        """Test initialization with default parameters."""')
        code.append(f'        decorator_class = load_decorator("{name}")')
        code.append("        assert decorator_class is not None")
        if has_required_params:
            code.append("        params = self._get_valid_params()")
            code.append("        decorator = decorator_class(**params)")
        else:
            code.append("        decorator = decorator_class()")
        code.append("        assert decorator is not None")
        code.append(f'        assert decorator.name == "{name}"')
        code.append("")

        # Test parameter validation
        for param in params:
            param_name = param["name"]
            param_type = param.get("type", "string")
            required = param.get("required", False)

            if required:
                # Test required parameter
                code.append(
                    f"    def test_{param_name}_required(self, load_decorator):"
                )
                code.append(f'        """Test that {param_name} is required."""')
                code.append(f'        decorator_class = load_decorator("{name}")')
                code.append("        assert decorator_class is not None")
                code.append("        params = self._get_valid_params()")
                code.append(f'        del params["{param_name}"]')
                code.append("        with pytest.raises(ValidationError):")
                code.append("            decorator_class(**params)")
                code.append("")

            # Test type validation
            code.append(
                f"    def test_{param_name}_type_validation(self, load_decorator):"
            )
            code.append(f'        """Test {param_name} type validation."""')
            code.append(f'        decorator_class = load_decorator("{name}")')
            code.append("        assert decorator_class is not None")
            code.append("        params = self._get_valid_params()")

            # Generate invalid value based on parameter type
            if param_type == "string":
                code.append(f"        params['{param_name}'] = 123")
            elif (
                param_type == "integer"
                or param_type == "number"
                or param_type == "float"
            ):
                code.append(f"        params['{param_name}'] = 'invalid'")
            elif param_type == "boolean":
                code.append(f"        params['{param_name}'] = 'invalid'")
            elif param_type == "array":
                code.append(f"        params['{param_name}'] = 'invalid'")
            elif param_type == "enum":
                code.append(f"        params['{param_name}'] = 'invalid_enum_value'")
            else:
                code.append(f"        params['{param_name}'] = None")

            code.append("        with pytest.raises(ValidationError) as exc_info:")
            code.append("            decorator_class(**params)")
            code.append(f'        assert "{param_name}" in str(exc_info.value)')

            if param_type == "enum":
                code.append('        assert "one of" in str(exc_info.value).lower()')
            else:
                code.append('        assert "type" in str(exc_info.value).lower()')

            code.append("")

            # Add enum validation test if applicable
            if param_type == "enum" and "enum" in param:
                code.append(
                    f"    def test_{param_name}_enum_validation(self, load_decorator):"
                )
                code.append(f'        """Test {param_name} enum value validation."""')
                code.append(f'        decorator_class = load_decorator("{name}")')
                code.append("        assert decorator_class is not None")
                code.append("        params = self._get_valid_params()")
                code.append(f"        params['{param_name}'] = 'invalid_enum_value'")
                code.append("        with pytest.raises(ValidationError) as exc_info:")
                code.append("            decorator_class(**params)")
                code.append(f'        assert "{param_name}" in str(exc_info.value)')
                code.append('        assert "one of" in str(exc_info.value).lower()')
                code.append("")

            # Add range validation tests if applicable
            if "validation" in param:
                validation = param["validation"]
                if "minimum" in validation:
                    code.append(
                        f"    def test_{param_name}_min_validation(self, load_decorator):"
                    )
                    code.append(
                        f'        """Test {param_name} minimum value validation."""'
                    )
                    code.append(f'        decorator_class = load_decorator("{name}")')
                    code.append("        assert decorator_class is not None")
                    code.append("        params = self._get_valid_params()")
                    if (
                        param_type == "integer"
                        or param_type == "number"
                        or param_type == "float"
                    ):
                        code.append(
                            f"        params['{param_name}'] = {validation['minimum'] - 1}"
                        )
                    code.append(
                        "        with pytest.raises(ValidationError) as exc_info:"
                    )
                    code.append("            decorator_class(**params)")
                    code.append(f'        assert "{param_name}" in str(exc_info.value)')
                    code.append(
                        '        assert "at least" in str(exc_info.value).lower()'
                    )
                    code.append("")

                if "maximum" in validation:
                    code.append(
                        f"    def test_{param_name}_max_validation(self, load_decorator):"
                    )
                    code.append(
                        f'        """Test {param_name} maximum value validation."""'
                    )
                    code.append(f'        decorator_class = load_decorator("{name}")')
                    code.append("        assert decorator_class is not None")
                    code.append("        params = self._get_valid_params()")
                    if (
                        param_type == "integer"
                        or param_type == "number"
                        or param_type == "float"
                    ):
                        code.append(
                            f"        params['{param_name}'] = {validation['maximum'] + 1}"
                        )
                    code.append(
                        "        with pytest.raises(ValidationError) as exc_info:"
                    )
                    code.append("            decorator_class(**params)")
                    code.append(f'        assert "{param_name}" in str(exc_info.value)')
                    code.append(
                        '        assert "at most" in str(exc_info.value).lower()'
                    )
                    code.append("")

        # Test apply method
        code.append("    def test_apply_basic(self, load_decorator, sample_prompt):")
        code.append('        """Test basic apply functionality."""')
        code.append(f'        decorator_class = load_decorator("{name}")')
        code.append("        assert decorator_class is not None")
        code.append("        params = self._get_valid_params()")
        code.append("        decorator = decorator_class(**params)")
        code.append("        result = decorator.apply(sample_prompt)")
        code.append("        assert isinstance(result, str)")
        code.append("")

        # Test serialization
        code.append("    def test_serialization(self, load_decorator):")
        code.append('        """Test decorator serialization."""')
        code.append(f'        decorator_class = load_decorator("{name}")')
        code.append("        assert decorator_class is not None")
        code.append("        params = self._get_valid_params()")
        code.append("        decorator = decorator_class(**params)")
        code.append("        serialized = decorator.to_dict()")
        code.append("        assert isinstance(serialized, dict)")
        code.append('        assert serialized["name"] == decorator.name')
        code.append('        assert "parameters" in serialized')
        code.append('        assert isinstance(serialized["parameters"], dict)')
        code.append("")

        # Test version compatibility
        code.append("    def test_version_compatibility(self, load_decorator):")
        code.append('        """Test version compatibility checks."""')
        code.append(f'        decorator_class = load_decorator("{name}")')
        code.append("        assert decorator_class is not None")
        code.append("")
        code.append("        # Test with current version")
        code.append("        current_version = decorator_class.version")
        code.append(
            "        assert decorator_class.is_compatible_with_version(current_version)"
        )
        code.append("")
        code.append("        # Test with incompatible version")
        code.append("        with pytest.raises(IncompatibleVersionError):")
        code.append(
            "            # Use a version lower than min_compatible_version to ensure incompatibility"
        )
        code.append('            decorator_class.is_compatible_with_version("0.0.1")')
        code.append("")
        code.append("        # Test instance method")
        code.append("        valid_params = self._get_valid_params()")
        code.append("        decorator = decorator_class(**valid_params)")
        code.append(
            "        assert decorator.is_compatible_with_version(current_version)"
        )
        code.append("        with pytest.raises(IncompatibleVersionError):")
        code.append(
            "            # Use a version lower than min_compatible_version to ensure incompatibility"
        )
        code.append('            decorator.is_compatible_with_version("0.0.1")')
        code.append("")

        # Test metadata
        code.append("    def test_metadata(self, load_decorator):")
        code.append('        """Test decorator metadata."""')
        code.append(f'        decorator_class = load_decorator("{name}")')
        code.append("        assert decorator_class is not None")
        code.append("        metadata = decorator_class.get_metadata()")
        code.append("        assert isinstance(metadata, dict)")
        code.append(f'        assert metadata["name"] == "{name}"')
        code.append('        assert "description" in metadata')
        code.append('        assert "category" in metadata')
        code.append('        assert "version" in metadata')
        code.append("")

        return code

    def _get_default_test_value(self, param: Dict[str, Any]) -> str:
        """Get a default test value for a parameter.

        Args:
            param: Parameter definition from registry

        Returns:
            String representation of default test value
        """
        param_type = param.get("type", "string")

        # If default is provided, use it
        if "default" in param:
            default_value = param["default"]
            if param_type == "string":
                return f'"{default_value}"'
            elif param_type == "enum" and "enum" in param:
                # Verify default value is in enum list
                enum_values = param["enum"]
                if default_value in enum_values:
                    return f'"{default_value}"'
                else:
                    # Use first enum value if default not in enum
                    return f'"{enum_values[0]}"'
            return str(default_value)

        # Otherwise generate appropriate test value based on type
        elif param_type == "string":
            return '"test_value"'
        elif param_type == "integer":
            return "42"
        elif param_type == "float" or param_type == "number":
            return "3.14"
        elif param_type == "boolean":
            return "False"
        elif param_type == "array":
            if "items" in param and "type" in param["items"]:
                item_type = param["items"]["type"]
                if item_type == "string":
                    return '["test1", "test2"]'
                elif item_type == "integer":
                    return "[1, 2, 3]"
                elif item_type == "boolean":
                    return "[True, False]"
            return '["test1", "test2"]'  # Default for arrays
        elif param_type == "enum" and "enum" in param:
            # Return the first enum value as a string literal
            enum_values = param.get("enum", [])
            if enum_values and len(enum_values) > 0:
                return f'"{enum_values[0]}"'
            return '"default_enum_value"'  # Fallback
        elif param_type == "object":
            return "{}"
        else:
            return "None"

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
    def test_missing_required_param_{param.name}(self, load_decorator):
        \"\"\"Test that initialization fails when missing required parameter {param.name}.\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        assert decorator_class is not None

        # Get valid parameters for all required fields except the one we're testing
        params = self._get_valid_params()

        # Remove the parameter we want to test as required
        if "{param.name}" in params:
            del params["{param.name}"]

        # Should raise ValidationError when the required parameter is missing
        with pytest.raises(ValidationError) as exc_info:
            decorator = decorator_class(**params)
        assert "{param.name}" in str(exc_info.value)
        assert "required" in str(exc_info.value).lower()
"""

    def _generate_param_validation_test(
        self, decorator_name: str, param: Parameter
    ) -> str:
        """Generate test for parameter validation.

        This method creates test cases for parameter validation, including:
        - Required field validation
        - Type checking
        - Pattern matching (for strings)
        - Range validation (for numbers)
        - Array validation
        - Enum value validation

        Args:
            decorator_name: Name of the decorator being tested
            param: Parameter object containing validation rules

        Returns:
            str: Generated test code as string
        """
        tests = []
        param_name = param.name
        param_type = param.type

        # Test required field validation if parameter is required
        if param.required:
            tests.append(
                f"""
    def test_{param_name}_required(self, load_decorator):
        \"\"\"Test that {param_name} is required.\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        assert decorator_class is not None

        params = self._get_valid_params()
        del params["{param_name}"]
        with pytest.raises(ValidationError) as exc_info:
            decorator_class(**params)
        assert "{param_name}" in str(exc_info.value)
        assert "required" in str(exc_info.value).lower()

"""
            )

        # Test type validation
        test_lines = []
        test_lines.append(
            f"    def test_{param_name}_type_validation(self, load_decorator):"
        )
        test_lines.append(f'        """Test {param_name} type validation."""')
        test_lines.append(
            f'        decorator_class = load_decorator("{decorator_name}")'
        )
        test_lines.append("        assert decorator_class is not None")
        test_lines.append("        params = self._get_valid_params()")

        # Generate invalid value based on parameter type
        if param_type == "string":
            invalid_value = "123"  # Number instead of string
        elif param_type in ["integer", "number", "float"]:
            invalid_value = "'invalid'"  # String instead of number
        elif param_type == "boolean":
            invalid_value = "'invalid'"  # String instead of boolean
        elif param_type == "array":
            invalid_value = "'invalid'"  # String instead of array
        elif param_type == "enum":
            invalid_value = "'invalid_enum_value'"  # Invalid enum value
        else:
            invalid_value = "None"

        # Replace the parameter with an invalid value
        test_lines.append(f"        params['{param_name}'] = {invalid_value}")

        test_lines.append("        with pytest.raises(ValidationError) as exc_info:")
        test_lines.append("            decorator_class(**params)")
        test_lines.append(f'        assert "{param_name}" in str(exc_info.value)')

        if param_type == "enum":
            test_lines.append(
                '        assert "one of" in str(exc_info.value).lower() or "enum" in str(exc_info.value).lower() or "valid" in str(exc_info.value).lower()'
            )
        else:
            test_lines.append(
                '        assert "type" in str(exc_info.value).lower() or "invalid" in str(exc_info.value).lower() or "must be" in str(exc_info.value).lower()'
            )

        test_lines.append("")

        tests.append("\n".join(test_lines))

        # Add enum validation test if applicable
        if param_type == "enum" and param.enum_values:
            enum_test_lines = []
            enum_test_lines.append(
                f"    def test_{param_name}_enum_validation(self, load_decorator):"
            )
            enum_test_lines.append(
                f'        """Test {param_name} enum value validation."""'
            )
            enum_test_lines.append(
                f'        decorator_class = load_decorator("{decorator_name}")'
            )
            enum_test_lines.append("        assert decorator_class is not None")
            enum_test_lines.append("        params = self._get_valid_params()")
            enum_test_lines.append(
                f"        params['{param_name}'] = 'invalid_enum_value'"
            )
            enum_test_lines.append(
                "        with pytest.raises(ValidationError) as exc_info:"
            )
            enum_test_lines.append("            decorator_class(**params)")
            enum_test_lines.append(
                f'        assert "{param_name}" in str(exc_info.value)'
            )
            enum_test_lines.append(
                '        assert "one of" in str(exc_info.value).lower() or "enum" in str(exc_info.value).lower() or "valid" in str(exc_info.value).lower()'
            )
            enum_test_lines.append("")

            tests.append("\n".join(enum_test_lines))

        return "\n".join(tests)

    def _generate_apply_tests(
        self, decorator_name: str, examples: List[Dict[str, Any]]
    ) -> str:
        """Generate tests for the apply method.

        This method creates test cases for the apply method using examples from
        the decorator definition. It tests both the basic functionality and
        parameter combinations.

        Args:
            decorator_name: Name of the decorator being tested
            examples: List of examples from the decorator definition

        Returns:
            str: Generated test code as string
        """
        if not examples:
            return ""

        formatted_tests = []
        for i, example in enumerate(examples):
            # Get the example data
            params = example.get("parameters", {})
            prompt = example.get("prompt", "Test prompt.")
            expected = example.get("expected", "")
            description = example.get("description", f"Example {i+1}")

            # Generate a test case name
            test_name = f"test_apply_example_{i+1}"

            # Format the test
            test_code = [
                f"    def {test_name}(self, load_decorator):",
                f'        """Test apply method with example {i+1}: {description}."""',
                f'        decorator_class = load_decorator("{decorator_name}")',
                "        assert decorator_class is not None",
                "",
                "        # Create the decorator with the example parameters",
                f"        params = {self._format_params_for_test(params)}",
                "        decorator = decorator_class(**params)",
                "",
                "        # Test prompt",
                f'        prompt = "{prompt}"',
                "",
                "        # Apply the decorator",
                "        result = decorator.apply(prompt)",
                "",
                "        # Assert the result contains expected elements",
                "        assert prompt in result  # Original prompt should be included",
            ]

            # Break long expected strings into multiple assertions to avoid line length issues
            if expected:
                if len(expected) > 40:  # If expected string is long
                    # Split it into chunks for multiple assertions
                    chunks = [expected[i : i + 40] for i in range(0, len(expected), 40)]
                    for chunk in chunks:
                        test_code.append(f'        assert "{chunk}" in result')
                else:
                    test_code.append(f'        assert "{expected}" in result')

            # Add additional assertions for parameters
            for param_name, param_value in params.items():
                if isinstance(param_value, str) and len(param_value) > 40:
                    # For long string values, just check if the parameter name is mentioned
                    test_code.append(f'        assert "{param_name}" in result')
                elif param_value is not None:
                    # For shorter values, can check for the actual value
                    test_code.append(
                        f'        assert str({param_value}) in result or "{param_name}" in result'
                    )

            # Join the test code lines
            formatted_tests.append("\n".join(test_code))

        # Join all test cases with blank lines between them
        return "\n\n".join(formatted_tests)

    def _format_params_for_test(self, params: Dict[str, Any]) -> str:
        """Format parameters for test cases.

        This method formats parameter dictionaries for test case generation,
        ensuring proper syntax and readability.

        Args:
            params: Dictionary of parameters and their values

        Returns:
            str: Formatted parameters as a string
        """
        if not params:
            return "{}"

        # Format each parameter
        formatted_params = []
        for name, value in params.items():
            if isinstance(value, str):
                # Escape quotes in strings
                escaped_value = value.replace('"', '\\"')
                if len(escaped_value) > 40:  # If string is too long
                    # Format as a shorter representation
                    short_value = escaped_value[:37] + "..."
                    formatted_params.append(f'    "{name}": "{short_value}"')
                else:
                    formatted_params.append(f'    "{name}": "{escaped_value}"')
            elif isinstance(value, bool):
                formatted_params.append(f'    "{name}": {str(value)}')
            elif isinstance(value, (int, float)):
                formatted_params.append(f'    "{name}": {value}')
            elif isinstance(value, list):
                # Format lists with proper indentation
                if len(str(value)) > 40:  # If list representation is too long
                    formatted_params.append(
                        f'    "{name}": [...]  # List of {len(value)} items'
                    )
                else:
                    formatted_params.append(f'    "{name}": {value}')
            elif value is None:
                formatted_params.append(f'    "{name}": None')
            else:
                formatted_params.append(f'    "{name}": {value}')

        # Join parameters and format as a dictionary
        return "{\n" + ",\n".join(formatted_params) + "\n}"

    def _generate_serialization_tests(self, decorator_name: str) -> str:
        """Generate tests for decorator serialization.

        This method creates test cases for serializing and deserializing decorators,
        ensuring that all parameters and metadata are preserved correctly.

        Args:
            decorator_name: Name of the decorator being tested

        Returns:
            str: Generated test code as string
        """
        return f"""
    def test_serialization(self, load_decorator):
        \"\"\"Test decorator serialization and deserialization.\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        assert decorator_class is not None

        # Create decorator with valid parameters
        valid_params = self._get_valid_params()
        decorator = decorator_class(**valid_params)

        # Test serialization
        serialized = decorator.to_dict()
        assert isinstance(serialized, dict)
        assert serialized["name"] == decorator.name
        assert "parameters" in serialized
        assert isinstance(serialized["parameters"], dict)

        # Test that all parameters are included in serialized form
        for param_name, param_value in valid_params.items():
            assert param_name in serialized["parameters"]

    def test_version_compatibility(self, load_decorator):
        \"\"\"Test version compatibility checks.\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        assert decorator_class is not None

        # Test with current version
        current_version = decorator_class.version
        assert decorator_class.is_compatible_with_version(current_version)

        # Test with incompatible version
        with pytest.raises(IncompatibleVersionError):
            decorator_class.is_compatible_with_version("999.0.0")

        # Test instance method
        valid_params = self._get_valid_params()
        decorator = decorator_class(**valid_params)
        assert decorator.is_compatible_with_version(current_version)
        with pytest.raises(IncompatibleVersionError):
            decorator.is_compatible_with_version("999.0.0")

    def test_metadata(self, load_decorator):
        \"\"\"Test decorator metadata.\"\"\"
        decorator_class = load_decorator("{decorator_name}")
        assert decorator_class is not None

        metadata = decorator_class.get_metadata()
        assert isinstance(metadata, dict)
        assert metadata["name"] == "{decorator_name}"
        assert "description" in metadata
        assert "category" in metadata
        assert "version" in metadata
"""

    def generate_test_discovery(self) -> str:
        """Generate a test discovery file.

        Returns:
            The content of the test discovery file
        """
        discovery_content = [
            "# Generated file - DO NOT EDIT BY HAND",
            "",
            "import pytest",
            "from prompt_decorators.decorators import *",
            "",
            "# This file ensures pytest discovers all tests in this directory",
            "",
        ]

        return "\n".join(discovery_content)

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
    """Main entry point for the test generator."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate tests for prompt decorators")
    parser.add_argument(
        "--registry-dir",
        "-r",
        default="registry",
        help="Path to the decorator registry directory",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        default="tests/auto",
        help="Path where test files will be generated",
    )
    parser.add_argument(
        "--template-dir",
        "-t",
        default=None,
        help="Optional path to test template directory",
    )

    args = parser.parse_args()

    generator = TestGenerator(
        registry_dir=args.registry_dir,
        output_dir=args.output_dir,
        template_dir=args.template_dir,
    )

    generated_files = generator.generate_all_tests()

    print(f"Generated {len(generated_files)} test files:")
    for file_path in generated_files:
        print(f"  - {file_path}")


if __name__ == "__main__":
    main()

"""Tests for enum handling in dynamic decorators.

This module contains tests specifically for the handling of enum parameters
in dynamic decorators, focusing on the ability to handle both 'enum' and
'enum_values' fields in parameter definitions.
"""

import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict

import pytest

# Add the parent directory to the path so we can import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from prompt_decorators.core.dynamic_decorator import DynamicDecorator, transform_prompt


# Create temporary decorator files for testing
@pytest.fixture
def enum_registry():
    """Create a temporary registry with test decorators for enum handling."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create registry structure
        registry_path = Path(temp_dir)
        core_path = registry_path / "core"
        core_path.mkdir()

        # Decorator with enum_values parameter
        with_enum_values = {
            "decoratorName": "WithEnumValues",
            "version": "1.0.0",
            "description": "Decorator with enum_values field",
            "category": "Testing",
            "parameters": [
                {
                    "name": "option",
                    "type": "enum",
                    "description": "An enum parameter with enum_values",
                    "default": "option1",
                    "required": False,
                    "enum_values": ["option1", "option2", "option3"],
                }
            ],
            "transform_function": """
selected_option = kwargs.get("option", "option1")
return f"Selected option: {selected_option}\\n{text}"
            """,
        }

        # Decorator with enum field (no enum_values)
        with_enum = {
            "decoratorName": "WithEnum",
            "version": "1.0.0",
            "description": "Decorator with enum field only",
            "category": "Testing",
            "parameters": [
                {
                    "name": "option",
                    "type": "enum",
                    "description": "An enum parameter with enum field only",
                    "default": "choice1",
                    "required": False,
                    "enum": ["choice1", "choice2", "choice3"],
                }
            ],
            "transform_function": """
selected_option = kwargs.get("option", "choice1")
return f"Selected option: {selected_option}\\n{text}"
            """,
        }

        # Decorator with both enum and enum_values fields
        with_both = {
            "decoratorName": "WithBoth",
            "version": "1.0.0",
            "description": "Decorator with both enum and enum_values fields",
            "category": "Testing",
            "parameters": [
                {
                    "name": "option",
                    "type": "enum",
                    "description": "An enum parameter with both fields",
                    "default": "value1",
                    "required": False,
                    "enum": ["old1", "old2", "old3"],
                    "enum_values": ["value1", "value2", "value3"],
                }
            ],
            "transform_function": """
selected_option = kwargs.get("option", "value1")
return f"Selected option: {selected_option}\\n{text}"
            """,
        }

        # Write files to temp registry
        with open(core_path / "WithEnumValues.json", "w") as f:
            json.dump(with_enum_values, f)

        with open(core_path / "WithEnum.json", "w") as f:
            json.dump(with_enum, f)

        with open(core_path / "WithBoth.json", "w") as f:
            json.dump(with_both, f)

        # Set environment variable to point to temp registry
        original_registry = os.environ.get("DECORATOR_REGISTRY_DIR")
        os.environ["DECORATOR_REGISTRY_DIR"] = str(registry_path)

        # Reset registry and load the new decorators
        DynamicDecorator._loaded = False
        DynamicDecorator._registry.clear()

        # Directly register the decorators for more reliable testing
        DynamicDecorator.register_decorator(with_enum_values)
        DynamicDecorator.register_decorator(with_enum)
        DynamicDecorator.register_decorator(with_both)

        yield registry_path

        # Reset environment
        if original_registry:
            os.environ["DECORATOR_REGISTRY_DIR"] = original_registry
        else:
            del os.environ["DECORATOR_REGISTRY_DIR"]

        # Reset the registry
        DynamicDecorator._loaded = False
        DynamicDecorator._registry.clear()


def test_enum_values_parameter(enum_registry):
    """Test parameter validation with enum_values field."""
    # Test with default value
    decorator = DynamicDecorator("WithEnumValues")
    assert decorator.parameters["option"].value == "option1"

    # Test with valid value
    decorator = DynamicDecorator("WithEnumValues", option="option2")
    assert decorator.parameters["option"].value == "option2"

    # Test with invalid value
    with pytest.raises(ValueError):
        DynamicDecorator("WithEnumValues", option="invalid")


def test_enum_field_parameter(enum_registry):
    """Test parameter validation with enum field (no enum_values)."""
    # Test with default value
    decorator = DynamicDecorator("WithEnum")
    assert decorator.parameters["option"].value == "choice1"

    # Test with valid value
    decorator = DynamicDecorator("WithEnum", option="choice2")
    assert decorator.parameters["option"].value == "choice2"

    # Test with invalid value
    with pytest.raises(ValueError):
        DynamicDecorator("WithEnum", option="invalid")


def test_both_enum_fields_parameter(enum_registry):
    """Test parameter validation with both enum and enum_values fields."""
    # Test with default value
    decorator = DynamicDecorator("WithBoth")
    assert decorator.parameters["option"].value == "value1"

    # Test with valid value from enum_values
    decorator = DynamicDecorator("WithBoth", option="value2")
    assert decorator.parameters["option"].value == "value2"

    # Test with valid value from enum field (which should be ignored)
    with pytest.raises(ValueError):
        DynamicDecorator("WithBoth", option="old1")

    # Test with invalid value
    with pytest.raises(ValueError):
        DynamicDecorator("WithBoth", option="invalid")


def test_transform_with_enum_parameters(enum_registry):
    """Test transforming prompts with enum parameters."""
    prompt = "Test prompt"

    # Test with enum_values parameter
    result = transform_prompt(prompt, ["+++WithEnumValues(option=option3)"])
    assert "Selected option: option3" in result

    # Test with enum field parameter
    result = transform_prompt(prompt, ["+++WithEnum(option=choice3)"])
    assert "Selected option: choice3" in result

    # Test with both fields parameter
    result = transform_prompt(prompt, ["+++WithBoth(option=value3)"])
    assert "Selected option: value3" in result


def test_dynamic_registration_of_enum_decorator():
    """Test dynamically registering a decorator with enum parameter."""
    # Create a test decorator definition
    test_decorator_def: Dict[str, Any] = {
        "decoratorName": "EnumTest",
        "version": "1.0.0",
        "description": "Test decorator for enum handling",
        "parameters": [
            {
                "name": "test_enum",
                "type": "enum",
                "description": "Test enum parameter",
                "enum": ["value1", "value2", "value3"],
                "default": "value1",
            }
        ],
        "transform_function": """
value = kwargs.get("test_enum", "value1")
return f"Using enum value: {value}\\n{text}"
        """,
    }

    # Save the original registry state
    original_registry = DynamicDecorator._registry.copy()
    original_loaded = DynamicDecorator._loaded

    try:
        # Ensure we're starting fresh
        DynamicDecorator._registry.clear()
        DynamicDecorator._loaded = True  # Prevent reloading

        # Register the decorator
        DynamicDecorator.register_decorator(test_decorator_def)

        # Check that the decorator was registered
        assert "EnumTest" in DynamicDecorator._registry

        # Verify the parameter definition has enum_values copied from enum
        param_def = next(
            param
            for param in DynamicDecorator._registry["EnumTest"]["parameters"]
            if param["name"] == "test_enum"
        )
        assert "enum_values" in param_def
        assert param_def["enum_values"] == ["value1", "value2", "value3"]

        # Create and test the decorator
        decorator = DynamicDecorator("EnumTest", test_enum="value2")
        result = decorator("Test text")
        assert "Using enum value: value2" in result

        # Test parameter validation
        with pytest.raises(ValueError):
            DynamicDecorator("EnumTest", test_enum="invalid_value")

    finally:
        # Restore the original registry
        DynamicDecorator._registry = original_registry
        DynamicDecorator._loaded = original_loaded

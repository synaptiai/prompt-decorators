"""Tests for enum handling in MCP integration.

This module tests the MCP integration with regards to enum parameter handling,
particularly ensuring that enum values are correctly passed and validated.
"""

import json
import os
import sys
from pathlib import Path

import pytest

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from prompt_decorators.core.dynamic_decorator import DynamicDecorator
from prompt_decorators.integrations.mcp import apply_decorators, get_decorator_details
from prompt_decorators.integrations.mcp.server import MCP_AVAILABLE

# Skip all tests in this module if MCP is not available
pytestmark = pytest.mark.skipif(
    not MCP_AVAILABLE, reason="MCP SDK not installed. Install with: pip install mcp"
)


@pytest.fixture
def setup_enum_decorators():
    """Set up test decorators with enum parameters."""
    # Save original registry state
    original_registry = DynamicDecorator._registry.copy()
    original_loaded = DynamicDecorator._loaded

    try:
        # Clear and setup test registry
        DynamicDecorator._registry.clear()
        DynamicDecorator._loaded = True  # Prevent automatic reloading

        # Define test decorators
        enum_only_decorator = {
            "decoratorName": "EnumOnly",
            "version": "1.0.0",
            "description": "Test decorator with enum field only",
            "category": "Test",
            "parameters": [
                {
                    "name": "option",
                    "type": "enum",
                    "description": "Test option",
                    "required": False,
                    "default": "option1",
                    "enum": ["option1", "option2", "option3"],
                }
            ],
            "transform_function": """
option = kwargs.get("option", "option1")
return f"EnumOnly decorator with option: {option}\\n{text}"
            """,
        }

        enum_values_decorator = {
            "decoratorName": "EnumValues",
            "version": "1.0.0",
            "description": "Test decorator with enum_values field",
            "category": "Test",
            "parameters": [
                {
                    "name": "option",
                    "type": "enum",
                    "description": "Test option",
                    "required": False,
                    "default": "value1",
                    "enum_values": ["value1", "value2", "value3"],
                }
            ],
            "transform_function": """
option = kwargs.get("option", "value1")
return f"EnumValues decorator with option: {option}\\n{text}"
            """,
        }

        # Register test decorators
        DynamicDecorator.register_decorator(enum_only_decorator)
        DynamicDecorator.register_decorator(enum_values_decorator)

        yield

    finally:
        # Restore original registry state
        DynamicDecorator._registry = original_registry
        DynamicDecorator._loaded = original_loaded


def test_get_decorator_details_enum_handling(setup_enum_decorators):
    """Test that get_decorator_details correctly handles enum parameters."""
    # Test decorator with enum field only
    enum_only_details = get_decorator_details("EnumOnly")

    # Check the response structure
    assert "decorator" in enum_only_details
    assert "content" in enum_only_details

    # Check decorator details
    decorator = enum_only_details["decorator"]
    assert decorator["name"] == "EnumOnly"

    # Verify parameters
    params = decorator["parameters"]
    assert len(params) == 1
    assert params[0]["name"] == "option"
    assert params[0]["type"] == "enum"
    assert params[0]["default"] == "option1"
    assert "enum_values" in params[0]
    assert set(params[0]["enum_values"]) == {"option1", "option2", "option3"}

    # Test decorator with enum_values field
    enum_values_details = get_decorator_details("EnumValues")

    # Check the response structure
    assert "decorator" in enum_values_details
    assert "content" in enum_values_details

    # Check decorator details
    decorator = enum_values_details["decorator"]
    assert decorator["name"] == "EnumValues"

    # Verify parameters
    params = decorator["parameters"]
    assert len(params) == 1
    assert params[0]["name"] == "option"
    assert params[0]["type"] == "enum"
    assert params[0]["default"] == "value1"
    assert "enum_values" in params[0]
    assert set(params[0]["enum_values"]) == {"value1", "value2", "value3"}


def test_apply_decorators_enum_handling(setup_enum_decorators, caplog):
    """Test that apply_decorators correctly handles enum parameters."""
    import logging

    caplog.set_level(logging.ERROR)
    test_prompt = "Test prompt"

    # Test with EnumOnly decorator
    result = apply_decorators(
        prompt=test_prompt,
        decorators=[{"name": "EnumOnly", "parameters": {"option": "option2"}}],
    )

    # Check for successful response
    assert "isError" not in result
    assert "content" in result
    assert isinstance(result["content"], list)
    assert len(result["content"]) > 0
    assert "text" in result["content"][0]

    # Check that the decorator was properly applied
    transformed_text = result["content"][0]["text"]
    assert "EnumOnly decorator with option: option2" in transformed_text

    # Test with EnumValues decorator
    result = apply_decorators(
        prompt=test_prompt,
        decorators=[{"name": "EnumValues", "parameters": {"option": "value3"}}],
    )

    # Check for successful response
    assert "isError" not in result
    assert "content" in result
    transformed_text = result["content"][0]["text"]
    assert "EnumValues decorator with option: value3" in transformed_text

    # Test with invalid enum value for EnumOnly
    # The error is caught and logged, but the original prompt is still returned
    result = apply_decorators(
        prompt=test_prompt,
        decorators=[{"name": "EnumOnly", "parameters": {"option": "invalid"}}],
    )

    # Check that the error was logged
    assert any("must be one of" in record.message for record in caplog.records)

    # Since errors are caught and the original prompt is returned:
    assert "content" in result
    assert result["content"][0]["text"] == test_prompt

    # Clear the log
    caplog.clear()

    # Test with invalid enum value for EnumValues
    result = apply_decorators(
        prompt=test_prompt,
        decorators=[{"name": "EnumValues", "parameters": {"option": "invalid"}}],
    )

    # Check that the error was logged
    assert any("must be one of" in record.message for record in caplog.records)

    # Since errors are caught and the original prompt is returned:
    assert "content" in result
    assert result["content"][0]["text"] == test_prompt


def test_combined_enum_handling(setup_enum_decorators):
    """Test combining multiple decorators with enum parameters."""
    test_prompt = "Test prompt"

    # Test with both decorators
    result = apply_decorators(
        prompt=test_prompt,
        decorators=[
            {"name": "EnumOnly", "parameters": {"option": "option3"}},
            {"name": "EnumValues", "parameters": {"option": "value2"}},
        ],
    )

    # Check for successful response
    assert "isError" not in result
    assert "content" in result
    assert isinstance(result["content"], list)
    assert len(result["content"]) > 0

    # Check that the decorator was properly applied
    transformed_text = result["content"][0]["text"]
    assert "EnumOnly decorator with option: option3" in transformed_text
    assert "EnumValues decorator with option: value2" in transformed_text

    # Check metadata
    assert "metadata" in result
    assert "applied_decorators" in result["metadata"]
    assert "EnumOnly" in result["metadata"]["applied_decorators"]
    assert "EnumValues" in result["metadata"]["applied_decorators"]

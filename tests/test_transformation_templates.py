"""Tests for transformation templates."""

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict

import pytest

from prompt_decorators.core.dynamic_decorator import (
    DynamicDecorator,
    create_transform_function_from_template,
)


def test_create_transform_function_from_template():
    """Test creating a transform function from a template."""
    # Basic template with just an instruction
    template = {"instruction": "Please explain in detail.", "placement": "prepend"}

    transform_function = create_transform_function_from_template(template)
    assert "def transform(text, **kwargs):" in transform_function
    assert "result = '''Please explain in detail.'''" in transform_function
    assert 'return result + "\\n\\n" + text' in transform_function

    # Execute the function to make sure it works
    namespace = {}
    exec(transform_function, namespace)
    transform = namespace["transform"]
    result = transform("What is quantum computing?")
    assert result == "Please explain in detail.\n\nWhat is quantum computing?"


def test_template_with_parameter_value_map():
    """Test a template with a parameter value map."""
    template = {
        "instruction": "Please explain this concept.",
        "parameterMapping": {
            "depth": {
                "valueMap": {
                    "basic": "Provide a basic overview with essential information.",
                    "comprehensive": "Give a comprehensive explanation with lots of details.",
                }
            }
        },
        "placement": "prepend",
    }

    transform_function = create_transform_function_from_template(template)
    namespace = {}
    exec(transform_function, namespace)
    transform = namespace["transform"]

    # Test with depth=basic
    result = transform("What is AI?", depth="basic")
    assert "Please explain this concept." in result
    assert "Provide a basic overview with essential information." in result

    # Test with depth=comprehensive
    result = transform("What is AI?", depth="comprehensive")
    assert "Please explain this concept." in result
    assert "Give a comprehensive explanation with lots of details." in result


def test_template_with_format_parameter():
    """Test a template with a format parameter."""
    template = {
        "instruction": "Please explain this concept.",
        "parameterMapping": {"count": {"format": "Provide exactly {value} examples."}},
        "placement": "prepend",
    }

    transform_function = create_transform_function_from_template(template)
    namespace = {}
    exec(transform_function, namespace)
    transform = namespace["transform"]

    # Test with count=3
    result = transform("What is machine learning?", count=3)
    assert "Please explain this concept." in result
    assert "Provide exactly 3 examples." in result


def test_decorator_with_dynamic_registration():
    """Test dynamically registering a decorator with a transformation template."""
    # Define a decorator with a transformation template
    decorator_def = {
        "decoratorName": "DynamicTest",
        "description": "A dynamically registered test decorator",
        "parameters": [
            {
                "name": "format",
                "type": "enum",
                "description": "Output format",
                "enum_values": ["text", "json", "markdown"],
                "default": "text",
            }
        ],
        "transformationTemplate": {
            "instruction": "Format the output as follows:",
            "parameterMapping": {
                "format": {
                    "valueMap": {
                        "text": "Plain text format with paragraphs.",
                        "json": "JSON format with proper structure.",
                        "markdown": "Markdown format with headings and lists.",
                    }
                }
            },
            "placement": "prepend",
        },
    }

    # Save the original registry state
    original_registry = DynamicDecorator._registry.copy()
    original_loaded = DynamicDecorator._loaded

    try:
        # Clear the registry and set loaded to True to prevent reloading
        DynamicDecorator._registry = {}
        DynamicDecorator._loaded = True

        # Register the decorator
        DynamicDecorator.register_decorator(decorator_def)

        # Create an instance and apply it
        decorator = DynamicDecorator("DynamicTest", format="markdown")
        result = decorator("Test content")

        # Check that the transformation was applied
        assert "Format the output as follows:" in result
        assert "Markdown format with headings and lists." in result
        assert "Test content" in result
    finally:
        # Restore the original registry state
        DynamicDecorator._registry = original_registry
        DynamicDecorator._loaded = original_loaded

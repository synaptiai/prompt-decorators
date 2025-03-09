"""Tests for the dynamic decorator module.

This module contains tests for the dynamic decorator module, which loads
decorator definitions from the registry at runtime.
"""

import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List

import pytest

# Add the parent directory to the path so we can import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from prompt_decorators.core.dynamic_decorator import (
    DynamicDecorator,
    extract_decorators,
    parse_decorator,
    transform_prompt,
)
from prompt_decorators.dynamic_decorators_module import (
    apply_dynamic_decorators,
    create_decorator_instance,
    get_available_decorators,
)


# Create temporary decorator files for testing
@pytest.fixture
def temp_registry():
    """Create a temporary registry with test decorator files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create registry structure
        registry_path = Path(temp_dir)
        core_path = registry_path / "core"
        core_path.mkdir()

        # Create a simple StepByStep decorator
        step_by_step = {
            "decoratorName": "StepByStep",
            "version": "1.0.0",
            "description": "Structures the response as a sequence of steps",
            "category": "Format",
            "parameters": [
                {
                    "name": "numbered",
                    "type": "boolean",
                    "description": "Whether to number the steps",
                    "default": True,
                    "required": False,
                }
            ],
            "transform_function": """
result = "Please break down your response into clear, sequential steps.\\n"
if kwargs.get("numbered", True):
    result += "Number each step sequentially (Step 1, Step 2, etc.).\\n"
else:
    result += "Use bullet points for each step instead of numbers.\\n"
return result + text
            """,
        }

        # Create a simple Tone decorator
        tone = {
            "decoratorName": "Tone",
            "version": "1.0.0",
            "description": "Adjusts the tone of the response",
            "category": "Style",
            "parameters": [
                {
                    "name": "style",
                    "type": "enum",
                    "description": "Tone style to use",
                    "default": "friendly",
                    "required": False,
                    "enum_values": [
                        "formal",
                        "casual",
                        "friendly",
                        "technical",
                        "humorous",
                    ],
                }
            ],
            "transform_function": """
result = "Please adjust your tone to be appropriate for this response.\\n"
style = kwargs.get("style", "friendly")
if style == "formal":
    result += "Use a formal, professional tone.\\n"
elif style == "casual":
    result += "Use a casual, conversational tone.\\n"
elif style == "friendly":
    result += "Use a friendly, approachable tone.\\n"
elif style == "technical":
    result += "Use technical language and terminology.\\n"
elif style == "humorous":
    result += "Use a light-hearted, humorous tone.\\n"
return result + text
            """,
        }

        # Create a decorator with required parameters and validations
        validation_test = {
            "decoratorName": "ValidationTest",
            "version": "1.0.0",
            "description": "Tests parameter validation",
            "category": "Testing",
            "parameters": [
                {
                    "name": "required_param",
                    "type": "string",
                    "description": "A required parameter",
                    "required": True,
                },
                {
                    "name": "min_max",
                    "type": "number",
                    "description": "A number with min/max validation",
                    "validation": {
                        "minimum": 1,
                        "maximum": 10,
                    },
                    "default": 5,
                    "required": False,
                },
            ],
            "transform_function": """
result = "This is a test for validation.\\n"
result += f"Required parameter is {kwargs.get('required_param')}.\\n"
if 'min_max' in kwargs:
    result += f"Min/max parameter is {kwargs.get('min_max')}.\\n"
return result + text
            """,
        }

        # Write files to temp registry
        with open(core_path / "StepByStep.json", "w") as f:
            json.dump(step_by_step, f)

        with open(core_path / "Tone.json", "w") as f:
            json.dump(tone, f)

        with open(core_path / "ValidationTest.json", "w") as f:
            json.dump(validation_test, f)

        # Set environment variable to point to temp registry
        original_registry = os.environ.get("DECORATOR_REGISTRY_DIR")
        os.environ["DECORATOR_REGISTRY_DIR"] = str(registry_path)

        # Directly register the decorators for more reliable testing
        DynamicDecorator._loaded = False  # Reset the loaded flag
        DynamicDecorator.register_decorator(step_by_step)
        DynamicDecorator.register_decorator(tone)
        DynamicDecorator.register_decorator(validation_test)

        yield registry_path

        # Reset environment
        if original_registry:
            os.environ["DECORATOR_REGISTRY_DIR"] = original_registry
        else:
            del os.environ["DECORATOR_REGISTRY_DIR"]

        # Reset the registry
        DynamicDecorator._loaded = False
        DynamicDecorator._registry.clear()


def test_dynamic_decorator_loading(temp_registry):
    """Test loading decorators from the registry."""
    # Test loading a decorator
    decorator = DynamicDecorator("StepByStep")
    assert decorator.name == "StepByStep"
    assert "parameters" in decorator.definition
    assert "numbered" in [p["name"] for p in decorator.definition["parameters"]]

    # Test loading a decorator with parameters
    decorator = DynamicDecorator("StepByStep", numbered=False)
    assert decorator.name == "StepByStep"
    assert "numbered" in decorator.parameters
    assert decorator.parameters["numbered"].value is False

    # Test loading a decorator with default parameters
    decorator = DynamicDecorator("Tone")
    assert decorator.name == "Tone"
    assert "style" in decorator.parameters
    assert decorator.parameters["style"].value == "friendly"

    # Test that loading a non-existent decorator raises an error
    with pytest.raises(ValueError):
        DynamicDecorator("NonExistentDecorator")


def test_parameter_validation(temp_registry):
    """Test parameter validation."""
    # Test required parameter
    with pytest.raises(ValueError):
        DynamicDecorator("ValidationTest")

    # Test valid required parameter
    decorator = DynamicDecorator("ValidationTest", required_param="test")
    assert decorator.parameters["required_param"].value == "test"

    # Test parameter with default value
    decorator = DynamicDecorator("ValidationTest", required_param="test")
    assert decorator.parameters["min_max"].value == 5

    # Test parameter validation for min value
    with pytest.raises(ValueError):
        DynamicDecorator("ValidationTest", required_param="test", min_max=0)

    # Test parameter validation for max value
    with pytest.raises(ValueError):
        DynamicDecorator("ValidationTest", required_param="test", min_max=11)


def test_transform_prompt(temp_registry):
    """Test transforming prompts with decorators."""
    # Test basic transformation
    decorator = DynamicDecorator("StepByStep")
    prompt = "How do I bake a cake?"
    transformed = decorator(prompt)

    assert (
        "Please break down your response into clear, sequential steps." in transformed
    )
    assert "Number each step sequentially" in transformed
    assert prompt in transformed

    # Test with parameters
    decorator = DynamicDecorator("StepByStep", numbered=False)
    transformed = decorator(prompt)

    assert (
        "Please break down your response into clear, sequential steps." in transformed
    )
    assert "Use bullet points for each step instead of numbers." in transformed
    assert prompt in transformed

    # Test with a different decorator
    decorator = DynamicDecorator("Tone", style="technical")
    transformed = decorator(prompt)

    assert "Please adjust your tone to be appropriate for this response." in transformed
    assert "Use technical language and terminology" in transformed
    assert prompt in transformed


def test_parse_decorator():
    """Test parsing decorator strings."""
    # Test basic parsing
    name, params = parse_decorator("+++StepByStep")
    assert name == "StepByStep"
    assert params == {}

    # Test with parameters
    name, params = parse_decorator("+++StepByStep(numbered=true)")
    assert name == "StepByStep"
    assert params == {"numbered": True}

    # Test with multiple parameters
    name, params = parse_decorator('+++Tone(style="technical", other=123)')
    assert name == "Tone"
    assert params == {"style": "technical", "other": 123}

    # Test with version
    name, params = parse_decorator("+++StepByStep:v2.0.0(numbered=false)")
    assert name == "StepByStep:v2.0.0"
    assert params == {"numbered": False}

    # Test with invalid syntax
    with pytest.raises(ValueError):
        parse_decorator("InvalidSyntax")


def test_extract_decorators(temp_registry):
    """Test extracting decorators from a prompt string."""
    # Test basic extraction
    prompt = "+++StepByStep\nHow do I bake a cake?"
    decorators, cleaned = extract_decorators(prompt)

    assert len(decorators) == 1
    assert isinstance(decorators[0], DynamicDecorator)
    assert decorators[0].name == "StepByStep"
    assert cleaned == "How do I bake a cake?"

    # Test with multiple decorators
    prompt = (
        "+++StepByStep(numbered=true)\n+++Tone(style=technical)\nHow do I bake a cake?"
    )
    decorators, cleaned = extract_decorators(prompt)

    assert len(decorators) == 2
    assert isinstance(decorators[0], DynamicDecorator)
    assert isinstance(decorators[1], DynamicDecorator)
    assert decorators[0].name == "StepByStep"
    assert decorators[1].name == "Tone"
    assert cleaned == "How do I bake a cake?"

    # Test decorators with no parameters
    prompt = "+++StepByStep"
    decorators, cleaned = extract_decorators(prompt)

    assert len(decorators) == 1
    assert decorators[0].name == "StepByStep"
    assert cleaned == ""


def test_transform_prompt_function(temp_registry):
    """Test the transform_prompt function."""
    # Test with a single decorator
    prompt = "How do I bake a cake?"
    transformed = apply_dynamic_decorators("+++StepByStep(numbered=true)\n" + prompt)

    assert (
        "Please break down your response into clear, sequential steps." in transformed
    )
    assert "Number each step sequentially" in transformed

    # Test with multiple decorators
    prompt = "How do I bake a cake?"
    transformed = apply_dynamic_decorators(
        "+++StepByStep(numbered=true)\n+++Tone(style=technical)\n" + prompt
    )

    assert (
        "Please break down your response into clear, sequential steps." in transformed
    )
    assert "Number each step sequentially" in transformed
    assert "Use technical language and terminology" in transformed


def test_create_decorator(temp_registry):
    """Test the create_decorator function."""
    # Test creating a decorator
    decorator = create_decorator_instance("StepByStep")
    assert isinstance(decorator, DynamicDecorator)
    assert decorator.name == "StepByStep"

    # Test creating a decorator with parameters
    decorator = create_decorator_instance("StepByStep", numbered=False)
    assert isinstance(decorator, DynamicDecorator)
    assert decorator.parameters["numbered"].value is False

    # Test transforming a prompt
    prompt = "How do I bake a cake?"
    transformed = decorator(prompt)

    assert (
        "Please break down your response into clear, sequential steps." in transformed
    )
    assert "Use bullet points for each step instead of numbers." in transformed
    assert prompt in transformed


def test_decorate_function(temp_registry):
    """Test the decorate function."""

    # Test as a decorator for a function
    def get_prompt():
        return "How do I bake a cake?"

    # Apply the decorator manually
    step_by_step = create_decorator_instance("StepByStep", numbered=True)
    result = step_by_step(get_prompt())

    assert "Please break down your response into clear, sequential steps." in result
    assert "Number each step sequentially" in result

    # Test with a string
    prompt = "How do I bake a cake?"
    result = create_decorator_instance("StepByStep", numbered=False)(prompt)

    assert "Please break down your response into clear, sequential steps." in result

    # Test with multiple decorators
    def get_complex_prompt():
        return "How do I bake a cake?"

    # Apply multiple decorators manually
    step_by_step = create_decorator_instance("StepByStep", numbered=True)
    tone = create_decorator_instance("Tone", style="technical")
    result = tone(step_by_step(get_complex_prompt()))

    assert "Please break down your response into clear, sequential steps." in result
    assert "Number each step sequentially" in result
    assert "Use technical language and terminology" in result


def test_list_available_decorators(temp_registry):
    """Test the list_available_decorators function."""
    decorators = get_available_decorators()
    decorator_names = [d.name for d in decorators]
    assert "StepByStep" in decorator_names
    assert "Tone" in decorator_names


def test_decorator_pattern(temp_registry):
    """Test using decorators as Python decorators."""
    # Test basic decorator pattern
    decorator = DynamicDecorator("StepByStep")

    @decorator
    def get_prompt():
        return "How do I bake a cake?"

    transformed = get_prompt()
    assert (
        "Please break down your response into clear, sequential steps." in transformed
    )
    assert "Number each step sequentially" in transformed
    assert "How do I bake a cake?" in transformed

    # Test with parameters
    decorator = DynamicDecorator("StepByStep", numbered=False)

    @decorator
    def get_prompt_with_params():
        return "How do I bake a cake?"

    transformed = get_prompt_with_params()
    assert (
        "Please break down your response into clear, sequential steps." in transformed
    )
    assert "Use bullet points for each step instead of numbers." in transformed
    assert "How do I bake a cake?" in transformed

    # Test with a different decorator
    decorator = DynamicDecorator("Tone", style="technical")

    @decorator
    def get_technical_prompt():
        return "How do I bake a cake?"

    transformed = get_technical_prompt()
    assert "Please adjust your tone to be appropriate for this response." in transformed
    assert "Use technical language and terminology" in transformed
    assert "How do I bake a cake?" in transformed


def test_decorator_chaining(temp_registry):
    """Test chaining multiple decorators."""
    # Test basic chaining
    step_by_step = DynamicDecorator("StepByStep")
    tone = DynamicDecorator("Tone", style="technical")

    prompt = "How do I bake a cake?"

    # Apply decorators in sequence
    transformed = step_by_step(tone(prompt))

    # Check that both decorators were applied
    assert (
        "Please break down your response into clear, sequential steps." in transformed
    )
    assert "Number each step sequentially" in transformed
    assert "Please adjust your tone to be appropriate for this response." in transformed
    assert "Use technical language and terminology" in transformed
    assert prompt in transformed

    # Test using decorator pattern
    @step_by_step
    @tone
    def get_prompt():
        return "How do I bake a cake?"

    transformed = get_prompt()

    # Check that both decorators were applied
    assert (
        "Please break down your response into clear, sequential steps." in transformed
    )
    assert "Number each step sequentially" in transformed
    assert "Please adjust your tone to be appropriate for this response." in transformed
    assert "Use technical language and terminology" in transformed
    assert "How do I bake a cake?" in transformed

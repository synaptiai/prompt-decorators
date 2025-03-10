"""Tests for the dynamic_decorators_module.py file."""

from unittest.mock import patch

import pytest

from prompt_decorators.dynamic_decorators_module import (
    DecoratorDefinition,
    apply_decorator,
    apply_dynamic_decorators,
    create_decorator,
    create_decorator_class,
    create_decorator_instance,
    extract_decorator_name,
    get_available_decorators,
    list_available_decorators,
    load_decorator_definitions,
    parse_decorator_text,
    register_decorator,
    transform_prompt,
)


def test_transform_prompt():
    """Test the transform_prompt function in dynamic_decorators_module.py."""
    # Mock the core transform_prompt function
    with patch(
        "prompt_decorators.core.dynamic_decorator.transform_prompt"
    ) as mock_transform:
        # Set the return value
        mock_transform.return_value = "Transformed prompt"

        # Call our function
        prompt = "Test prompt"
        decorators = ["+++StepByStep", "+++Reasoning"]
        result = transform_prompt(prompt, decorators)

        # Check the result
        assert result == "Transformed prompt"

        # Verify the mock was called with the correct arguments
        mock_transform.assert_called_once_with(prompt, decorators)

"""Example of automatically generated tests for the Reasoning decorator.

This shows what kind of tests would be generated by the test generator script.
"""


import pytest

from tests.utils.test_helpers import (
    LLMClient,
    ValidationError,
    check_expectation,
    validate_decorator_in_prompt,
)

# Initialize test client
llm_client = LLMClient(use_real_llm=False, use_cache=True)


# Tests for Reasoning decorator


# Parameter validation tests
def test_reasoning_depth_enum_values():
    """Test that depth accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Reasoning(depth=basic)\nTest prompt.")
    validate_decorator_in_prompt("+++Reasoning(depth=moderate)\nTest prompt.")
    validate_decorator_in_prompt("+++Reasoning(depth=comprehensive)\nTest prompt.")

    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Reasoning(depth=invalid_value)\nTest prompt.")


# Example-based tests
def test_reasoning_basic_reasoning_process():
    """Test Reasoning with example: Basic reasoning process with moderate depth."""
    response = llm_client.generate("+++Reasoning\nExplain why the sky appears blue.")

    # Check if response meets expectations
    check_expectation(
        response,
        "matches_description",
        description="Provides a logical explanation of why the sky appears blue, showing the reasoning process that leads to the conclusion",
    )


def test_reasoning_comprehensive_scientific_explanation():
    """

    Test Reasoning with example: Comprehensive scientific explanation with
            detailed reasoning.
    """
    response = llm_client.generate(
        "+++Reasoning(depth=comprehensive)\nDescribe how neural networks learn"
        "patterns in data."
    )

    # Check if response meets expectations
    check_expectation(
        response,
        "matches_description",
        description="Delivers a comprehensive explanation of neural network learning with detailed reasoning steps, including gradient descent, backpropagation, and the mathematics behind pattern recognition",
    )


# Compatibility tests
def test_reasoning_compatibility_with_step_by_step():
    """Test that Reasoning works with StepByStep decorator."""
    # Test with both decorators
    response = llm_client.generate(
        "+++Reasoning\n+++StepByStep\nExplain how photosynthesis works."
    )

    # Should contain both reasoning elements and numbered steps
    assert check_expectation(response, "contains_numbered_steps")
    assert (
        "reason" in response.lower()
        or "because" in response.lower()
        or "therefore" in response.lower()
    )


if __name__ == "__main__":
    # Run the tests
    pytest.main(["-v", __file__])

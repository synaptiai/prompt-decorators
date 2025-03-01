"""
Automatically generated tests for prompt decorators.
DO NOT EDIT MANUALLY. Changes will be overwritten.
"""

import pytest
import re
import json
from tests.utils.test_helpers import (
    validate_decorator_in_prompt,
    check_expectation,
    LLMClient,
    combine_decorators,
    ValidationError,
)

# Initialize test client
llm_client = LLMClient(use_real_llm=False, use_cache=True)


# Tests for Tone decorator

# Parameter validation tests

def test_tone_style_required():
    """Test that style is required for Tone decorator."""
    prompt = "+++Tone\nTest prompt."
    with pytest.raises(ValidationError, match="style"):
        validate_decorator_in_prompt(prompt)


def test_tone_style_enum_values():
    """Test that style accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Tone(style=formal)\nTest prompt."); validate_decorator_in_prompt("+++Tone(style=casual)\nTest prompt."); validate_decorator_in_prompt("+++Tone(style=friendly)\nTest prompt."); validate_decorator_in_prompt("+++Tone(style=technical)\nTest prompt."); validate_decorator_in_prompt("+++Tone(style=humorous)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Tone(style=invalid_value)\nTest prompt.")


# Example-based tests

def test_tone_technical_documentation_tone():
    """Test Tone with example: Technical documentation tone"""
    response = llm_client.generate("+++Tone(style=technical)\nExplain how garbage collection works in Python")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a technically precise explanation using appropriate terminology")


def test_tone_casual_explanation():
    """Test Tone with example: Casual explanation"""
    response = llm_client.generate("+++Tone(style=casual)\nWhy is the sky blue?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers a relaxed, conversational explanation of atmospheric optics")


# Compatibility tests

def test_tone_conflicts():
    """Test that Tone has expected conflicts."""
    conflicts = ["ELI5"]
    for conflict in conflicts:
        result = combine_decorators(["Tone", conflict])
        assert not result["compatible"], f"Tone should conflict with {conflict}"

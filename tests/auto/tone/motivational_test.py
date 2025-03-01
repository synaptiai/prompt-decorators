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


# Tests for Motivational decorator

# Parameter validation tests

def test_motivational_intensity_enum_values():
    """Test that intensity accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Motivational(intensity=mild)\nTest prompt."); validate_decorator_in_prompt("+++Motivational(intensity=moderate)\nTest prompt."); validate_decorator_in_prompt("+++Motivational(intensity=high)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Motivational(intensity=invalid_value)\nTest prompt.")


def test_motivational_focus_enum_values():
    """Test that focus accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Motivational(focus=achievement)\nTest prompt."); validate_decorator_in_prompt("+++Motivational(focus=growth)\nTest prompt."); validate_decorator_in_prompt("+++Motivational(focus=resilience)\nTest prompt."); validate_decorator_in_prompt("+++Motivational(focus=purpose)\nTest prompt."); validate_decorator_in_prompt("+++Motivational(focus=balanced)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Motivational(focus=invalid_value)\nTest prompt.")


def test_motivational_actionable_boolean_validation():
    """Test boolean validation for actionable parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Motivational(actionable=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Motivational(actionable=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Motivational(actionable=not_boolean)\nTest prompt.")


# Example-based tests

def test_motivational_basic_moderately_motivational_response():
    """Test Motivational with example: Basic moderately motivational response"""
    response = llm_client.generate("+++Motivational\nWhat are some strategies for building healthy habits?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides strategies for building healthy habits with moderate motivational language, encouraging tone, and confidence-building framing")


def test_motivational_high_intensity_resilience_focused_motivational_content():
    """Test Motivational with example: High-intensity resilience-focused motivational content"""
    response = llm_client.generate("+++Motivational(intensity=high, focus=resilience, actionable=true)\nHow can I overcome setbacks in my professional life?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers highly energetic and inspiring advice for professional resilience, emphasizing overcoming adversity with specific actionable steps, using powerful language and empowering framing")


# Compatibility tests

def test_motivational_conflicts():
    """Test that Motivational has expected conflicts."""
    conflicts = ["Academic"]
    for conflict in conflicts:
        result = combine_decorators(["Motivational", conflict])
        assert not result["compatible"], f"Motivational should conflict with {conflict}"

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


# Tests for Concise decorator

# Parameter validation tests

def test_concise_maxWords_number_validation():
    """Test number validation for maxWords parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Concise(maxWords=10)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Concise(maxWords=9)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Concise(maxWords=500)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Concise(maxWords=501)\nTest prompt.")
    

def test_concise_bulletPoints_boolean_validation():
    """Test boolean validation for bulletPoints parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Concise(bulletPoints=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Concise(bulletPoints=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Concise(bulletPoints=not_boolean)\nTest prompt.")


def test_concise_level_enum_values():
    """Test that level accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Concise(level=moderate)\nTest prompt."); validate_decorator_in_prompt("+++Concise(level=high)\nTest prompt."); validate_decorator_in_prompt("+++Concise(level=extreme)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Concise(level=invalid_value)\nTest prompt.")


# Example-based tests

def test_concise_basic_concise_explanation_of_a_complex_topic():
    """Test Concise with example: Basic concise explanation of a complex topic"""
    response = llm_client.generate("+++Concise\nExplain how blockchain technology works.")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


def test_concise_extremely_concise_bulleted_answer_with_word_limit():
    """Test Concise with example: Extremely concise bulleted answer with word limit"""
    response = llm_client.generate("+++Concise(maxWords=50, bulletPoints=true, level=extreme)\nWhat are the key factors in successful project management?")
    
    # Check if response meets expectations
    check_expectation(response, "contains_bullet_points")
    check_expectation(response, "is_concise")


# Compatibility tests

def test_concise_conflicts():
    """Test that Concise has expected conflicts."""
    conflicts = ["Detailed"]
    for conflict in conflicts:
        result = combine_decorators(["Concise", conflict])
        assert not result["compatible"], f"Concise should conflict with {conflict}"

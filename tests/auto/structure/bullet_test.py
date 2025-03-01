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


# Tests for Bullet decorator

# Parameter validation tests

def test_bullet_style_enum_values():
    """Test that style accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Bullet(style=dash)\nTest prompt."); validate_decorator_in_prompt("+++Bullet(style=dot)\nTest prompt."); validate_decorator_in_prompt("+++Bullet(style=arrow)\nTest prompt."); validate_decorator_in_prompt("+++Bullet(style=star)\nTest prompt."); validate_decorator_in_prompt("+++Bullet(style=plus)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Bullet(style=invalid_value)\nTest prompt.")


def test_bullet_indented_boolean_validation():
    """Test boolean validation for indented parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Bullet(indented=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Bullet(indented=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Bullet(indented=not_boolean)\nTest prompt.")


def test_bullet_compact_boolean_validation():
    """Test boolean validation for compact parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Bullet(compact=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Bullet(compact=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Bullet(compact=not_boolean)\nTest prompt.")


# Example-based tests

def test_bullet_basic_bulleted_list_of_key_points():
    """Test Bullet with example: Basic bulleted list of key points"""
    response = llm_client.generate("+++Bullet\nWhat are the main factors to consider when buying a laptop?")
    
    # Check if response meets expectations
    check_expectation(response, "contains_bullet_points")


def test_bullet_compact_star_bullets_with_nesting_disabled():
    """Test Bullet with example: Compact star bullets with nesting disabled"""
    response = llm_client.generate("+++Bullet(style=star, indented=false, compact=true)\nList the benefits of regular exercise.")
    
    # Check if response meets expectations
    check_expectation(response, "contains_bullet_points")
    check_expectation(response, "is_concise")


# Compatibility tests

def test_bullet_conflicts():
    """Test that Bullet has expected conflicts."""
    conflicts = ["OutputFormat"]
    for conflict in conflicts:
        result = combine_decorators(["Bullet", conflict])
        assert not result["compatible"], f"Bullet should conflict with {conflict}"

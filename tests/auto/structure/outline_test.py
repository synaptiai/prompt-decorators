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


# Tests for Outline decorator

# Parameter validation tests

def test_outline_depth_number_validation():
    """Test number validation for depth parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Outline(depth=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Outline(depth=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Outline(depth=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Outline(depth=6)\nTest prompt.")
    

def test_outline_style_enum_values():
    """Test that style accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Outline(style=numeric)\nTest prompt."); validate_decorator_in_prompt("+++Outline(style=bullet)\nTest prompt."); validate_decorator_in_prompt("+++Outline(style=roman)\nTest prompt."); validate_decorator_in_prompt("+++Outline(style=alpha)\nTest prompt."); validate_decorator_in_prompt("+++Outline(style=mixed)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Outline(style=invalid_value)\nTest prompt.")


def test_outline_detailed_boolean_validation():
    """Test boolean validation for detailed parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Outline(detailed=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Outline(detailed=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Outline(detailed=not_boolean)\nTest prompt.")


# Example-based tests

def test_outline_simple_numeric_outline_of_a_complex_topic():
    """Test Outline with example: Simple numeric outline of a complex topic"""
    response = llm_client.generate("+++Outline\nExplain the structure of the United States government.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents the US government structure as a numbered outline with up to 3 levels of hierarchy")


def test_outline_detailed_outline_with_mixed_notation_and_deep_hierarchy():
    """Test Outline with example: Detailed outline with mixed notation and deep hierarchy"""
    response = llm_client.generate("+++Outline(style=mixed, depth=5, detailed=true)\nProvide a comprehensive overview of machine learning techniques.")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


# Compatibility tests

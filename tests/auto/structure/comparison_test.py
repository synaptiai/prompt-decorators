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


# Tests for Comparison decorator

# Parameter validation tests

def test_comparison_format_enum_values():
    """Test that format accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Comparison(format=table)\nTest prompt."); validate_decorator_in_prompt("+++Comparison(format=prose)\nTest prompt."); validate_decorator_in_prompt("+++Comparison(format=bullets)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Comparison(format=invalid_value)\nTest prompt.")


def test_comparison_highlight_boolean_validation():
    """Test boolean validation for highlight parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Comparison(highlight=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Comparison(highlight=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Comparison(highlight=not_boolean)\nTest prompt.")


# Example-based tests

def test_comparison_basic_tabular_comparison_of_specific_aspects():
    """Test Comparison with example: Basic tabular comparison of specific aspects"""
    response = llm_client.generate("+++Comparison(aspects=[performance,cost,ease of use,ecosystem])\nCompare React, Angular, and Vue for front-end development.")
    
    # Check if response meets expectations
    check_expectation(response, "contains_table")
    check_expectation(response, "contains_comparison")


def test_comparison_prose_based_comparison_without_specific_aspects():
    """Test Comparison with example: Prose-based comparison without specific aspects"""
    response = llm_client.generate("+++Comparison(format=prose, highlight=false)\nCompare democracy and authoritarianism as political systems.")
    
    # Check if response meets expectations
    check_expectation(response, "contains_comparison")


# Compatibility tests

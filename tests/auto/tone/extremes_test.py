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


# Tests for Extremes decorator

# Parameter validation tests

def test_extremes_versions_enum_values():
    """Test that versions accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Extremes(versions=radical)\nTest prompt."); validate_decorator_in_prompt("+++Extremes(versions=minimal)\nTest prompt."); validate_decorator_in_prompt("+++Extremes(versions=both)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Extremes(versions=invalid_value)\nTest prompt.")


def test_extremes_compare_boolean_validation():
    """Test boolean validation for compare parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Extremes(compare=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Extremes(compare=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Extremes(compare=not_boolean)\nTest prompt.")


# Example-based tests

def test_extremes_basic_exploration_of_minimal_and_radical_approaches():
    """Test Extremes with example: Basic exploration of minimal and radical approaches"""
    response = llm_client.generate("+++Extremes\nDescribe a strategy for reducing carbon emissions.")
    
    # Check if response meets expectations
    check_expectation(response, "contains_comparison")


def test_extremes_only_radical_version_along_a_specific_dimension():
    """Test Extremes with example: Only radical version along a specific dimension"""
    response = llm_client.generate("+++Extremes(versions=radical, dimension=technological innovation, compare=false)\nOutline the future of transportation.")
    
    # Check if response meets expectations
    check_expectation(response, "contains_comparison")


# Compatibility tests

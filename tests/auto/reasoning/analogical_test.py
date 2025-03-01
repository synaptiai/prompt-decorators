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


# Tests for Analogical decorator

# Parameter validation tests

def test_analogical_count_number_validation():
    """Test number validation for count parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Analogical(count=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Analogical(count=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Analogical(count=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Analogical(count=6)\nTest prompt.")
    

def test_analogical_depth_enum_values():
    """Test that depth accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Analogical(depth=brief)\nTest prompt."); validate_decorator_in_prompt("+++Analogical(depth=moderate)\nTest prompt."); validate_decorator_in_prompt("+++Analogical(depth=extended)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Analogical(depth=invalid_value)\nTest prompt.")


# Example-based tests

def test_analogical_single_analogy_from_a_specific_domain():
    """Test Analogical with example: Single analogy from a specific domain"""
    response = llm_client.generate("+++Analogical(domain=sports)\nExplain how the immune system works.")
    
    # Check if response meets expectations
    check_expectation(response, "contains_comparison")


def test_analogical_multiple_brief_analogies_from_different_domains():
    """Test Analogical with example: Multiple brief analogies from different domains"""
    response = llm_client.generate("+++Analogical(count=3, depth=brief)\nDescribe how blockchain technology functions.")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


# Compatibility tests

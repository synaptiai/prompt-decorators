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


# Tests for Layered decorator

# Parameter validation tests

def test_layered_levels_enum_values():
    """Test that levels accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Layered(levels=sentence-paragraph-full)\nTest prompt."); validate_decorator_in_prompt("+++Layered(levels=basic-intermediate-advanced)\nTest prompt."); validate_decorator_in_prompt("+++Layered(levels=summary-detail-technical)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Layered(levels=invalid_value)\nTest prompt.")


def test_layered_count_number_validation():
    """Test number validation for count parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Layered(count=2)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Layered(count=1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Layered(count=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Layered(count=6)\nTest prompt.")
    

def test_layered_progression_enum_values():
    """Test that progression accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Layered(progression=separate)\nTest prompt."); validate_decorator_in_prompt("+++Layered(progression=nested)\nTest prompt."); validate_decorator_in_prompt("+++Layered(progression=incremental)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Layered(progression=invalid_value)\nTest prompt.")


# Example-based tests

def test_layered_basic_three_level_explanation_of_a_complex_concept():
    """Test Layered with example: Basic three-level explanation of a complex concept"""
    response = llm_client.generate("+++Layered\nExplain how blockchain technology works.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a summary-level explanation of blockchain, followed by a detailed explanation, and finally a technical deep dive with implementation details")


def test_layered_multi_layered_nested_progression_with_custom_levels():
    """Test Layered with example: Multi-layered nested progression with custom levels"""
    response = llm_client.generate("+++Layered(levels=basic-intermediate-advanced, count=4, progression=nested)\nDescribe the principles of quantum computing.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers a nested explanation of quantum computing with four progressive layers of understanding, each building on the previous and increasing in complexity from basic to advanced")


# Compatibility tests

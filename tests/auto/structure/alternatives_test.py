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


# Tests for Alternatives decorator

# Parameter validation tests

def test_alternatives_count_number_validation():
    """Test number validation for count parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Alternatives(count=2)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Alternatives(count=1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Alternatives(count=7)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Alternatives(count=8)\nTest prompt.")
    

def test_alternatives_diversity_enum_values():
    """Test that diversity accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Alternatives(diversity=low)\nTest prompt."); validate_decorator_in_prompt("+++Alternatives(diversity=medium)\nTest prompt."); validate_decorator_in_prompt("+++Alternatives(diversity=high)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Alternatives(diversity=invalid_value)\nTest prompt.")


def test_alternatives_comparison_boolean_validation():
    """Test boolean validation for comparison parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Alternatives(comparison=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Alternatives(comparison=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Alternatives(comparison=not_boolean)\nTest prompt.")


# Example-based tests

def test_alternatives_basic_alternative_approaches_to_a_problem():
    """Test Alternatives with example: Basic alternative approaches to a problem"""
    response = llm_client.generate("+++Alternatives\nHow can I improve my public speaking skills?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides three distinct approaches to improving public speaking skills, each with its own methodology and focus")


def test_alternatives_highly_diverse_alternatives_with_comparative_analysis():
    """Test Alternatives with example: Highly diverse alternatives with comparative analysis"""
    response = llm_client.generate("+++Alternatives(count=5, diversity=high, comparison=true)\nWhat are some ways to reduce carbon emissions in urban areas?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents five highly diverse approaches to reducing urban carbon emissions, followed by a comparative analysis of their effectiveness, cost, and implementation challenges")


# Compatibility tests

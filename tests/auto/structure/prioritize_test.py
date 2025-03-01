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


# Tests for Prioritize decorator

# Parameter validation tests

def test_prioritize_count_number_validation():
    """Test number validation for count parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Prioritize(count=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Prioritize(count=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Prioritize(count=10)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Prioritize(count=11)\nTest prompt.")
    

def test_prioritize_showRationale_boolean_validation():
    """Test boolean validation for showRationale parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Prioritize(showRationale=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Prioritize(showRationale=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Prioritize(showRationale=not_boolean)\nTest prompt.")


# Example-based tests

def test_prioritize_basic_prioritization_of_key_factors():
    """Test Prioritize with example: Basic prioritization of key factors"""
    response = llm_client.generate("+++Prioritize\nWhat factors should be considered when designing a mobile app?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents the top 5 factors for mobile app design, ranked by importance from most to least critical")


def test_prioritize_detailed_prioritization_with_custom_criteria_and_rationale():
    """Test Prioritize with example: Detailed prioritization with custom criteria and rationale"""
    response = llm_client.generate("+++Prioritize(criteria=ROI, count=7, showRationale=true)\nWhat marketing strategies should our startup focus on?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides 7 marketing strategies ranked by return on investment, with explanations for each ranking position")


# Compatibility tests

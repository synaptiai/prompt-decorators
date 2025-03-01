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


# Tests for Steelman decorator

# Parameter validation tests

def test_steelman_sides_number_validation():
    """Test number validation for sides parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Steelman(sides=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Steelman(sides=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Steelman(sides=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Steelman(sides=6)\nTest prompt.")
    

def test_steelman_critique_boolean_validation():
    """Test boolean validation for critique parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Steelman(critique=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Steelman(critique=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Steelman(critique=not_boolean)\nTest prompt.")


def test_steelman_separation_boolean_validation():
    """Test boolean validation for separation parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Steelman(separation=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Steelman(separation=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Steelman(separation=not_boolean)\nTest prompt.")


# Example-based tests

def test_steelman_steel_manning_both_sides_of_a_controversial_issue():
    """Test Steelman with example: Steel-manning both sides of a controversial issue"""
    response = llm_client.generate("+++Steelman\nIs universal basic income a good policy?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents the strongest possible cases both for and against universal basic income, with each position articulated in its most compelling form")


def test_steelman_steel_manning_one_position_with_subsequent_critique():
    """Test Steelman with example: Steel-manning one position with subsequent critique"""
    response = llm_client.generate("+++Steelman(sides=1, critique=true, separation=true)\nWhat is the strongest case for cryptocurrency as the future of finance?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides the most compelling possible argument for cryptocurrency as the future of finance, clearly separated from a subsequent balanced critique")


# Compatibility tests

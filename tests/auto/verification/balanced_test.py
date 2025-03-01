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


# Tests for Balanced decorator

# Parameter validation tests

def test_balanced_perspectives_number_validation():
    """Test number validation for perspectives parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Balanced(perspectives=2)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Balanced(perspectives=1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Balanced(perspectives=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Balanced(perspectives=6)\nTest prompt.")
    

def test_balanced_structure_enum_values():
    """Test that structure accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Balanced(structure=alternating)\nTest prompt."); validate_decorator_in_prompt("+++Balanced(structure=sequential)\nTest prompt."); validate_decorator_in_prompt("+++Balanced(structure=comparative)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Balanced(structure=invalid_value)\nTest prompt.")


def test_balanced_equal_boolean_validation():
    """Test boolean validation for equal parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Balanced(equal=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Balanced(equal=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Balanced(equal=not_boolean)\nTest prompt.")


# Example-based tests

def test_balanced_basic_balanced_view_of_a_controversial_topic():
    """Test Balanced with example: Basic balanced view of a controversial topic"""
    response = llm_client.generate("+++Balanced\nDiscuss the pros and cons of nuclear energy.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents the benefits and drawbacks of nuclear energy with equal attention and detail given to both perspectives")


def test_balanced_balanced_presentation_of_multiple_perspectives_in_comparative_structure():
    """Test Balanced with example: Balanced presentation of multiple perspectives in comparative structure"""
    response = llm_client.generate("+++Balanced(perspectives=4, structure=comparative, equal=true)\nWhat are the different views on artificial intelligence regulation?")
    
    # Check if response meets expectations
    check_expectation(response, "contains_comparison")


# Compatibility tests

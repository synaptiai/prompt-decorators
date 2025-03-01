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


# Tests for MECE decorator

# Parameter validation tests

def test_mece_dimensions_number_validation():
    """Test number validation for dimensions parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++MECE(dimensions=2)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++MECE(dimensions=1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++MECE(dimensions=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++MECE(dimensions=6)\nTest prompt.")
    

def test_mece_depth_number_validation():
    """Test number validation for depth parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++MECE(depth=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++MECE(depth=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++MECE(depth=3)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++MECE(depth=4)\nTest prompt.")
    

def test_mece_framework_enum_values():
    """Test that framework accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++MECE(framework=issue tree)\nTest prompt."); validate_decorator_in_prompt("+++MECE(framework=value chain)\nTest prompt."); validate_decorator_in_prompt("+++MECE(framework=business segments)\nTest prompt."); validate_decorator_in_prompt("+++MECE(framework=stakeholders)\nTest prompt."); validate_decorator_in_prompt("+++MECE(framework=custom)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++MECE(framework=invalid_value)\nTest prompt.")


# Example-based tests

def test_mece_basic_mece_analysis_of_a_business_problem():
    """Test MECE with example: Basic MECE analysis of a business problem"""
    response = llm_client.generate("+++MECE\nWhat factors should we consider when expanding to a new market?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Organizes market expansion factors into 3 mutually exclusive, collectively exhaustive categories with no overlaps and full coverage of all considerations")


def test_mece_detailed_mece_framework_with_stakeholder_focus():
    """Test MECE with example: Detailed MECE framework with stakeholder focus"""
    response = llm_client.generate("+++MECE(dimensions=4, depth=3, framework=stakeholders)\nAnalyze the implications of implementing a four-day work week.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a 4-dimension MECE analysis of a four-day work week using a stakeholder framework, with up to 3 levels of hierarchical breakdown within each stakeholder category")


# Compatibility tests

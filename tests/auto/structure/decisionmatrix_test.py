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


# Tests for DecisionMatrix decorator

# Parameter validation tests

def test_decisionmatrix_weighted_boolean_validation():
    """Test boolean validation for weighted parameter."""
    # Test true value
    validate_decorator_in_prompt("+++DecisionMatrix(weighted=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++DecisionMatrix(weighted=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++DecisionMatrix(weighted=not_boolean)\nTest prompt.")


def test_decisionmatrix_scale_enum_values():
    """Test that scale accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++DecisionMatrix(scale=1-5)\nTest prompt."); validate_decorator_in_prompt("+++DecisionMatrix(scale=1-10)\nTest prompt."); validate_decorator_in_prompt("+++DecisionMatrix(scale=qualitative)\nTest prompt."); validate_decorator_in_prompt("+++DecisionMatrix(scale=percentage)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++DecisionMatrix(scale=invalid_value)\nTest prompt.")


# Example-based tests

def test_decisionmatrix_simple_decision_matrix_for_comparing_options():
    """Test DecisionMatrix with example: Simple decision matrix for comparing options"""
    response = llm_client.generate("+++DecisionMatrix\nWhat smartphone should I buy?")
    
    # Check if response meets expectations
    check_expectation(response, "contains_comparison")


def test_decisionmatrix_weighted_decision_matrix_with_custom_options_and_criteria():
    """Test DecisionMatrix with example: Weighted decision matrix with custom options and criteria"""
    response = llm_client.generate("+++DecisionMatrix(options=[Python,JavaScript,Go,Rust], criteria=[learning curve,performance,ecosystem,job market], weighted=true, scale=1-10)\nWhich programming language should I learn next?")
    
    # Check if response meets expectations
    check_expectation(response, "contains_comparison")


# Compatibility tests

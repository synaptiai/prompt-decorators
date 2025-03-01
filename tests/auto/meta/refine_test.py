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


# Tests for Refine decorator

# Parameter validation tests

def test_refine_iterations_number_validation():
    """Test number validation for iterations parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Refine(iterations=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Refine(iterations=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Refine(iterations=3)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Refine(iterations=4)\nTest prompt.")
    

def test_refine_showProcess_boolean_validation():
    """Test boolean validation for showProcess parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Refine(showProcess=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Refine(showProcess=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Refine(showProcess=not_boolean)\nTest prompt.")


# Example-based tests

def test_refine_basic_refinement_of_a_complex_explanation():
    """Test Refine with example: Basic refinement of a complex explanation"""
    response = llm_client.generate("+++Refine\nExplain the implications of quantum computing for cybersecurity.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a refined explanation of quantum computing implications for cybersecurity, with two hidden iterations improving clarity and accuracy")


def test_refine_detailed_refinement_with_visible_iterations():
    """Test Refine with example: Detailed refinement with visible iterations"""
    response = llm_client.generate("+++Refine(iterations=3, focus=[clarity,evidence,conciseness], showProcess=true)\nAnalyze the economic impacts of artificial intelligence.")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


# Compatibility tests

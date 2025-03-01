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


# Tests for Debate decorator

# Parameter validation tests

def test_debate_perspectives_number_validation():
    """Test number validation for perspectives parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Debate(perspectives=2)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Debate(perspectives=1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Debate(perspectives=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Debate(perspectives=6)\nTest prompt.")
    

def test_debate_balanced_boolean_validation():
    """Test boolean validation for balanced parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Debate(balanced=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Debate(balanced=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Debate(balanced=not_boolean)\nTest prompt.")


# Example-based tests

def test_debate_two_perspective_debate_on_an_ethical_issue():
    """Test Debate with example: Two-perspective debate on an ethical issue"""
    response = llm_client.generate("+++Debate\nIs it ethical to use AI-generated content without disclosure?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents balanced arguments for and against disclosure of AI-generated content")


def test_debate_three_perspective_debate_on_a_policy_issue_with_balanced_representation():
    """Test Debate with example: Three-perspective debate on a policy issue with balanced representation"""
    response = llm_client.generate("+++Debate(perspectives=3, balanced=true)\nShould universal basic income be implemented nationally?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents three balanced perspectives on UBI in a debate format, ensuring equal representation of each viewpoint")


# Compatibility tests

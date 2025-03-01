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


# Tests for Abductive decorator

# Parameter validation tests

def test_abductive_hypotheses_number_validation():
    """Test number validation for hypotheses parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Abductive(hypotheses=2)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Abductive(hypotheses=1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Abductive(hypotheses=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Abductive(hypotheses=6)\nTest prompt.")
    

def test_abductive_rank_boolean_validation():
    """Test boolean validation for rank parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Abductive(rank=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Abductive(rank=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Abductive(rank=not_boolean)\nTest prompt.")


# Example-based tests

def test_abductive_basic_abductive_reasoning_with_multiple_hypotheses():
    """Test Abductive with example: Basic abductive reasoning with multiple hypotheses"""
    response = llm_client.generate("+++Abductive\nWhy have bee populations been declining globally?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents observed facts about bee population decline, generates three possible explanations, and identifies the most likely causes based on available evidence")


def test_abductive_detailed_abductive_reasoning_with_specific_evaluation_criteria():
    """Test Abductive with example: Detailed abductive reasoning with specific evaluation criteria"""
    response = llm_client.generate("+++Abductive(hypotheses=4, criteria=[comprehensiveness,simplicity,novelty,testability], rank=true)\nWhat might explain the Fermi Paradox?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Develops four hypotheses explaining the Fermi Paradox, evaluates each against the specified criteria, and ranks them from most to least likely explanation")


# Compatibility tests

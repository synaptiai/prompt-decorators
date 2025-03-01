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


# Tests for Socratic decorator

# Parameter validation tests

def test_socratic_iterations_number_validation():
    """Test number validation for iterations parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Socratic(iterations=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Socratic(iterations=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Socratic(iterations=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Socratic(iterations=6)\nTest prompt.")
    

# Example-based tests

def test_socratic_basic_socratic_exploration_of_a_philosophical_concept():
    """Test Socratic with example: Basic socratic exploration of a philosophical concept"""
    response = llm_client.generate("+++Socratic\nWhat is justice?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Explores the concept of justice through a series of guiding questions")


def test_socratic_deep_socratic_analysis_with_5_iterations():
    """Test Socratic with example: Deep socratic analysis with 5 iterations"""
    response = llm_client.generate("+++Socratic(iterations=5)\nHow do we know what we know?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an extended series of 5 question-answer cycles to explore epistemology")


# Compatibility tests

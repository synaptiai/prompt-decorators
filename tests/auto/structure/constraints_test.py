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


# Tests for Constraints decorator

# Parameter validation tests

def test_constraints_wordCount_number_validation():
    """Test number validation for wordCount parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Constraints(wordCount=10)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Constraints(wordCount=9)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Constraints(wordCount=1000)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Constraints(wordCount=1001)\nTest prompt.")
    

def test_constraints_vocabulary_enum_values():
    """Test that vocabulary accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Constraints(vocabulary=simple)\nTest prompt."); validate_decorator_in_prompt("+++Constraints(vocabulary=technical)\nTest prompt."); validate_decorator_in_prompt("+++Constraints(vocabulary=domain-specific)\nTest prompt."); validate_decorator_in_prompt("+++Constraints(vocabulary=creative)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Constraints(vocabulary=invalid_value)\nTest prompt.")


# Example-based tests

def test_constraints_word_count_constraint_for_a_complex_topic():
    """Test Constraints with example: Word count constraint for a complex topic"""
    response = llm_client.generate("+++Constraints(wordCount=100)\nExplain quantum computing principles.")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


def test_constraints_multiple_constraints_for_a_creative_response():
    """Test Constraints with example: Multiple constraints for a creative response"""
    response = llm_client.generate("+++Constraints(wordCount=200, vocabulary=creative, custom=each paragraph must contain exactly three sentences)\nDescribe a futuristic city.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers a 200-word description of a futuristic city using creative vocabulary, with each paragraph containing exactly three sentences")


# Compatibility tests

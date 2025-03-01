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


# Tests for Summary decorator

# Parameter validation tests

def test_summary_length_enum_values():
    """Test that length accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Summary(length=short)\nTest prompt."); validate_decorator_in_prompt("+++Summary(length=medium)\nTest prompt."); validate_decorator_in_prompt("+++Summary(length=long)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Summary(length=invalid_value)\nTest prompt.")


def test_summary_wordCount_number_validation():
    """Test number validation for wordCount parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Summary(wordCount=10)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Summary(wordCount=9)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Summary(wordCount=500)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Summary(wordCount=501)\nTest prompt.")
    

def test_summary_position_enum_values():
    """Test that position accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Summary(position=beginning)\nTest prompt."); validate_decorator_in_prompt("+++Summary(position=end)\nTest prompt."); validate_decorator_in_prompt("+++Summary(position=standalone)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Summary(position=invalid_value)\nTest prompt.")


# Example-based tests

def test_summary_short_standalone_summary_of_a_complex_topic():
    """Test Summary with example: Short standalone summary of a complex topic"""
    response = llm_client.generate("+++Summary(length=short)\nExplain quantum computing and its potential applications.")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


def test_summary_specific_word_count_summary_at_the_beginning_of_a_response():
    """Test Summary with example: Specific word count summary at the beginning of a response"""
    response = llm_client.generate("+++Summary(wordCount=100, position=beginning)\nDescribe the causes and effects of climate change.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Starts with a 100-word summary of climate change causes and effects, followed by more detailed information")


# Compatibility tests

def test_summary_conflicts():
    """Test that Summary has expected conflicts."""
    conflicts = ["Detailed"]
    for conflict in conflicts:
        result = combine_decorators(["Summary", conflict])
        assert not result["compatible"], f"Summary should conflict with {conflict}"

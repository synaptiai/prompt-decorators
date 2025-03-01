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


# Tests for Confidence decorator

# Parameter validation tests

def test_confidence_scale_enum_values():
    """Test that scale accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Confidence(scale=percent)\nTest prompt."); validate_decorator_in_prompt("+++Confidence(scale=qualitative)\nTest prompt."); validate_decorator_in_prompt("+++Confidence(scale=stars)\nTest prompt."); validate_decorator_in_prompt("+++Confidence(scale=numeric)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Confidence(scale=invalid_value)\nTest prompt.")


def test_confidence_threshold_number_validation():
    """Test number validation for threshold parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Confidence(threshold=0)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Confidence(threshold=-1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Confidence(threshold=100)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Confidence(threshold=101)\nTest prompt.")
    

def test_confidence_detailed_boolean_validation():
    """Test boolean validation for detailed parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Confidence(detailed=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Confidence(detailed=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Confidence(detailed=not_boolean)\nTest prompt.")


# Example-based tests

def test_confidence_qualitative_confidence_indicators_for_a_complex_topic():
    """Test Confidence with example: Qualitative confidence indicators for a complex topic"""
    response = llm_client.generate("+++Confidence\nExplain the current understanding of dark matter.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Explains dark matter theories with qualitative confidence indicators (high confidence, moderate confidence, etc.) for different claims")


def test_confidence_detailed_percentage_based_confidence_with_high_threshold():
    """Test Confidence with example: Detailed percentage-based confidence with high threshold"""
    response = llm_client.generate("+++Confidence(scale=percent, threshold=80, detailed=true)\nWhat are the most effective treatments for depression?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Discusses only high-confidence (80%+) depression treatments with percentage indicators and explanations for confidence assessments")


# Compatibility tests

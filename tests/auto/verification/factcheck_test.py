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


# Tests for FactCheck decorator

# Parameter validation tests

def test_factcheck_confidence_boolean_validation():
    """Test boolean validation for confidence parameter."""
    # Test true value
    validate_decorator_in_prompt("+++FactCheck(confidence=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++FactCheck(confidence=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++FactCheck(confidence=not_boolean)\nTest prompt.")


def test_factcheck_uncertain_enum_values():
    """Test that uncertain accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++FactCheck(uncertain=mark)\nTest prompt."); validate_decorator_in_prompt("+++FactCheck(uncertain=exclude)\nTest prompt."); validate_decorator_in_prompt("+++FactCheck(uncertain=qualify)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++FactCheck(uncertain=invalid_value)\nTest prompt.")


def test_factcheck_strictness_enum_values():
    """Test that strictness accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++FactCheck(strictness=low)\nTest prompt."); validate_decorator_in_prompt("+++FactCheck(strictness=moderate)\nTest prompt."); validate_decorator_in_prompt("+++FactCheck(strictness=high)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++FactCheck(strictness=invalid_value)\nTest prompt.")


# Example-based tests

def test_factcheck_basic_fact_checking_with_confidence_indicators():
    """Test FactCheck with example: Basic fact checking with confidence indicators"""
    response = llm_client.generate("+++FactCheck\nExplain the history and effectiveness of vaccines.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides information about vaccines with clear indications of confidence levels for different claims")


def test_factcheck_high_strictness_fact_checking_that_excludes_uncertain_information():
    """Test FactCheck with example: High-strictness fact checking that excludes uncertain information"""
    response = llm_client.generate("+++FactCheck(strictness=high, uncertain=exclude)\nDescribe what we know about dark matter.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents only well-established scientific facts about dark matter, excluding speculative or uncertain information")


# Compatibility tests

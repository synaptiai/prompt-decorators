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


# Tests for Audience decorator

# Parameter validation tests

def test_audience_level_enum_values():
    """Test that level accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Audience(level=beginner)\nTest prompt."); validate_decorator_in_prompt("+++Audience(level=intermediate)\nTest prompt."); validate_decorator_in_prompt("+++Audience(level=expert)\nTest prompt."); validate_decorator_in_prompt("+++Audience(level=technical)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Audience(level=invalid_value)\nTest prompt.")


def test_audience_examples_boolean_validation():
    """Test boolean validation for examples parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Audience(examples=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Audience(examples=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Audience(examples=not_boolean)\nTest prompt.")


# Example-based tests

def test_audience_technical_explanation_for_experts_in_a_specific_field():
    """Test Audience with example: Technical explanation for experts in a specific field"""
    response = llm_client.generate("+++Audience(level=technical, domain=cybersecurity)\nExplain zero-knowledge proofs.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an in-depth technical explanation of zero-knowledge proofs using cybersecurity-specific terminology and concepts")


def test_audience_beginner_friendly_explanation_with_examples():
    """Test Audience with example: Beginner-friendly explanation with examples"""
    response = llm_client.generate("+++Audience(level=beginner, examples=true)\nHow does machine learning work?")
    
    # Check if response meets expectations
    check_expectation(response, "contains_table")


# Compatibility tests

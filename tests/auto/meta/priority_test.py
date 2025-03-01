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


# Tests for Priority decorator

# Parameter validation tests

def test_priority_decorators_required():
    """Test that decorators is required for Priority decorator."""
    prompt = "+++Priority\nTest prompt."
    with pytest.raises(ValidationError, match="decorators"):
        validate_decorator_in_prompt(prompt)


def test_priority_explicit_boolean_validation():
    """Test boolean validation for explicit parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Priority(explicit=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Priority(explicit=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Priority(explicit=not_boolean)\nTest prompt.")


def test_priority_mode_enum_values():
    """Test that mode accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Priority(mode=override)\nTest prompt."); validate_decorator_in_prompt("+++Priority(mode=merge)\nTest prompt."); validate_decorator_in_prompt("+++Priority(mode=cascade)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Priority(mode=invalid_value)\nTest prompt.")


# Example-based tests

def test_priority_basic_priority_ordering_between_potentially_conflicting_decorators():
    """Test Priority with example: Basic priority ordering between potentially conflicting decorators"""
    response = llm_client.generate("+++Priority(decorators=[Concise,Detailed])\nExplain quantum computing.")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


def test_priority_complex_priority_with_explicit_conflict_resolution():
    """Test Priority with example: Complex priority with explicit conflict resolution"""
    response = llm_client.generate("+++Priority(decorators=[Academic,Creative,StepByStep], explicit=true, mode=cascade)\nExplain the water cycle.")
    
    # Check if response meets expectations
    check_expectation(response, "has_formal_language")


# Compatibility tests

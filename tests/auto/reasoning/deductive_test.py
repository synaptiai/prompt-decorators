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


# Tests for Deductive decorator

# Parameter validation tests

def test_deductive_premises_number_validation():
    """Test number validation for premises parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Deductive(premises=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Deductive(premises=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Deductive(premises=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Deductive(premises=6)\nTest prompt.")
    

def test_deductive_formal_boolean_validation():
    """Test boolean validation for formal parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Deductive(formal=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Deductive(formal=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Deductive(formal=not_boolean)\nTest prompt.")


def test_deductive_steps_number_validation():
    """Test number validation for steps parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Deductive(steps=2)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Deductive(steps=1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Deductive(steps=7)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Deductive(steps=8)\nTest prompt.")
    

# Example-based tests

def test_deductive_basic_deductive_reasoning_from_principles_to_specific_conclusions():
    """Test Deductive with example: Basic deductive reasoning from principles to specific conclusions"""
    response = llm_client.generate("+++Deductive\nShould social media companies be regulated like utilities?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Starts with general principles about utilities and regulation, establishes premises about social media characteristics, and deduces conclusions about appropriate regulatory approaches")


def test_deductive_formal_deductive_logic_with_multiple_steps():
    """Test Deductive with example: Formal deductive logic with multiple steps"""
    response = llm_client.generate("+++Deductive(formal=true, steps=5)\nIs artificial intelligence conscious?")
    
    # Check if response meets expectations
    check_expectation(response, "has_formal_language")


# Compatibility tests

def test_deductive_conflicts():
    """Test that Deductive has expected conflicts."""
    conflicts = ["Inductive"]
    for conflict in conflicts:
        result = combine_decorators(["Deductive", conflict])
        assert not result["compatible"], f"Deductive should conflict with {conflict}"

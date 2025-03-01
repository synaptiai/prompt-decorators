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


# Tests for Inductive decorator

# Parameter validation tests

def test_inductive_examples_number_validation():
    """Test number validation for examples parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Inductive(examples=2)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Inductive(examples=1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Inductive(examples=10)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Inductive(examples=11)\nTest prompt.")
    

def test_inductive_confidence_boolean_validation():
    """Test boolean validation for confidence parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Inductive(confidence=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Inductive(confidence=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Inductive(confidence=not_boolean)\nTest prompt.")


def test_inductive_structure_enum_values():
    """Test that structure accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Inductive(structure=generalization)\nTest prompt."); validate_decorator_in_prompt("+++Inductive(structure=causal)\nTest prompt."); validate_decorator_in_prompt("+++Inductive(structure=statistical)\nTest prompt."); validate_decorator_in_prompt("+++Inductive(structure=analogical)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Inductive(structure=invalid_value)\nTest prompt.")


# Example-based tests

def test_inductive_basic_inductive_reasoning_from_examples_to_general_principles():
    """Test Inductive with example: Basic inductive reasoning from examples to general principles"""
    response = llm_client.generate("+++Inductive\nWhat factors contribute to successful startups?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides specific examples of successful startups, identifies patterns across them, and derives general principles of startup success")


def test_inductive_causal_inductive_reasoning_with_confidence_levels():
    """Test Inductive with example: Causal inductive reasoning with confidence levels"""
    response = llm_client.generate("+++Inductive(examples=5, confidence=true, structure=causal)\nHow does screen time affect child development?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents 5 specific observations about screen time and child development, infers causal relationships, and generalizes with explicit confidence levels for each conclusion")


# Compatibility tests

def test_inductive_conflicts():
    """Test that Inductive has expected conflicts."""
    conflicts = ["Deductive"]
    for conflict in conflicts:
        result = combine_decorators(["Inductive", conflict])
        assert not result["compatible"], f"Inductive should conflict with {conflict}"

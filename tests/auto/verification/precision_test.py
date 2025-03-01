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


# Tests for Precision decorator

# Parameter validation tests

def test_precision_level_enum_values():
    """Test that level accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Precision(level=moderate)\nTest prompt."); validate_decorator_in_prompt("+++Precision(level=high)\nTest prompt."); validate_decorator_in_prompt("+++Precision(level=scientific)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Precision(level=invalid_value)\nTest prompt.")


def test_precision_units_boolean_validation():
    """Test boolean validation for units parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Precision(units=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Precision(units=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Precision(units=not_boolean)\nTest prompt.")


def test_precision_definitions_boolean_validation():
    """Test boolean validation for definitions parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Precision(definitions=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Precision(definitions=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Precision(definitions=not_boolean)\nTest prompt.")


# Example-based tests

def test_precision_basic_precise_explanation_of_a_scientific_concept():
    """Test Precision with example: Basic precise explanation of a scientific concept"""
    response = llm_client.generate("+++Precision\nExplain how vaccines work.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an explanation of vaccine mechanisms using precise terminology, specific examples, and accurate measurements where relevant")


def test_precision_highly_precise_response_with_scientific_rigor():
    """Test Precision with example: Highly precise response with scientific rigor"""
    response = llm_client.generate("+++Precision(level=scientific, units=true, definitions=true)\nDescribe the process of photosynthesis.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers a scientifically precise explanation of photosynthesis with exact units for all measurements, precise definitions for key terms, and specific chemical reactions")


# Compatibility tests

def test_precision_conflicts():
    """Test that Precision has expected conflicts."""
    conflicts = ["ELI5"]
    for conflict in conflicts:
        result = combine_decorators(["Precision", conflict])
        assert not result["compatible"], f"Precision should conflict with {conflict}"

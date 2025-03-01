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


# Tests for Detailed decorator

# Parameter validation tests

def test_detailed_depth_enum_values():
    """Test that depth accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Detailed(depth=moderate)\nTest prompt."); validate_decorator_in_prompt("+++Detailed(depth=comprehensive)\nTest prompt."); validate_decorator_in_prompt("+++Detailed(depth=exhaustive)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Detailed(depth=invalid_value)\nTest prompt.")


def test_detailed_examples_boolean_validation():
    """Test boolean validation for examples parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Detailed(examples=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Detailed(examples=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Detailed(examples=not_boolean)\nTest prompt.")


# Example-based tests

def test_detailed_comprehensive_detailed_explanation_of_a_concept():
    """Test Detailed with example: Comprehensive detailed explanation of a concept"""
    response = llm_client.generate("+++Detailed\nExplain how the human immune system works.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a thorough, in-depth explanation of the immune system covering all major components, processes, and functions with illustrative examples")


def test_detailed_exhaustive_detailed_analysis_of_specific_aspects():
    """Test Detailed with example: Exhaustive detailed analysis of specific aspects"""
    response = llm_client.generate("+++Detailed(depth=exhaustive, aspects=[economic,environmental,social,technological], examples=true)\nAnalyze the implications of transitioning to renewable energy.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers an extremely detailed analysis of renewable energy transition, exhaustively covering all four specified aspects with comprehensive examples")


# Compatibility tests

def test_detailed_conflicts():
    """Test that Detailed has expected conflicts."""
    conflicts = ["Concise", "Summary"]
    for conflict in conflicts:
        result = combine_decorators(["Detailed", conflict])
        assert not result["compatible"], f"Detailed should conflict with {conflict}"

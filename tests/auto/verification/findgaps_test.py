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


# Tests for FindGaps decorator

# Parameter validation tests

def test_findgaps_aspects_enum_values():
    """Test that aspects accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++FindGaps(aspects=questions)\nTest prompt."); validate_decorator_in_prompt("+++FindGaps(aspects=resources)\nTest prompt."); validate_decorator_in_prompt("+++FindGaps(aspects=stakeholders)\nTest prompt."); validate_decorator_in_prompt("+++FindGaps(aspects=risks)\nTest prompt."); validate_decorator_in_prompt("+++FindGaps(aspects=dependencies)\nTest prompt."); validate_decorator_in_prompt("+++FindGaps(aspects=comprehensive)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++FindGaps(aspects=invalid_value)\nTest prompt.")


def test_findgaps_depth_enum_values():
    """Test that depth accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++FindGaps(depth=basic)\nTest prompt."); validate_decorator_in_prompt("+++FindGaps(depth=thorough)\nTest prompt."); validate_decorator_in_prompt("+++FindGaps(depth=exhaustive)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++FindGaps(depth=invalid_value)\nTest prompt.")


def test_findgaps_solutions_boolean_validation():
    """Test boolean validation for solutions parameter."""
    # Test true value
    validate_decorator_in_prompt("+++FindGaps(solutions=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++FindGaps(solutions=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++FindGaps(solutions=not_boolean)\nTest prompt.")


# Example-based tests

def test_findgaps_basic_comprehensive_gap_analysis_of_a_business_plan():
    """Test FindGaps with example: Basic comprehensive gap analysis of a business plan"""
    response = llm_client.generate("+++FindGaps\nWe plan to launch our SaaS product with these features and marketing channels...")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="First identifies gaps across various aspects of the SaaS product launch plan, then suggests solutions for addressing each gap")


def test_findgaps_exhaustive_stakeholder_focused_gap_analysis_without_solutions():
    """Test FindGaps with example: Exhaustive stakeholder-focused gap analysis without solutions"""
    response = llm_client.generate("+++FindGaps(aspects=stakeholders, depth=exhaustive, solutions=false)\nHere's our urban redevelopment proposal...")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an exhaustive analysis of overlooked or inadequately considered stakeholders in the urban redevelopment proposal, without suggesting solutions")


# Compatibility tests

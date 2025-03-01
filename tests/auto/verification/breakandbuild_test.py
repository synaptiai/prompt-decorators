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


# Tests for BreakAndBuild decorator

# Parameter validation tests

def test_breakandbuild_breakdown_enum_values():
    """Test that breakdown accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++BreakAndBuild(breakdown=weaknesses)\nTest prompt."); validate_decorator_in_prompt("+++BreakAndBuild(breakdown=assumptions)\nTest prompt."); validate_decorator_in_prompt("+++BreakAndBuild(breakdown=risks)\nTest prompt."); validate_decorator_in_prompt("+++BreakAndBuild(breakdown=comprehensive)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++BreakAndBuild(breakdown=invalid_value)\nTest prompt.")


def test_breakandbuild_intensity_enum_values():
    """Test that intensity accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++BreakAndBuild(intensity=mild)\nTest prompt."); validate_decorator_in_prompt("+++BreakAndBuild(intensity=thorough)\nTest prompt."); validate_decorator_in_prompt("+++BreakAndBuild(intensity=intense)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++BreakAndBuild(intensity=invalid_value)\nTest prompt.")


def test_breakandbuild_buildRatio_number_validation():
    """Test number validation for buildRatio parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++BreakAndBuild(buildRatio=0.5)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++BreakAndBuild(buildRatio=-0.5)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++BreakAndBuild(buildRatio=3)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++BreakAndBuild(buildRatio=4)\nTest prompt.")
    

# Example-based tests

def test_breakandbuild_basic_break_and_build_analysis_of_a_business_concept():
    """Test BreakAndBuild with example: Basic break and build analysis of a business concept"""
    response = llm_client.generate("+++BreakAndBuild\nEvaluate this startup idea: a subscription service for plant care.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="First thoroughly critiques the plant care subscription concept by identifying weaknesses and risks, then reconstructs it with improvements and solutions of equal depth")


def test_breakandbuild_intense_breakdown_of_assumptions_with_substantial_rebuilding():
    """Test BreakAndBuild with example: Intense breakdown of assumptions with substantial rebuilding"""
    response = llm_client.generate("+++BreakAndBuild(breakdown=assumptions, intensity=intense, buildRatio=2)\nAnalyze this public policy proposal for reducing urban congestion.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers an intense critique focused specifically on the assumptions underlying the urban congestion proposal, followed by twice as much content reconstructing it with stronger foundations and improvements")


# Compatibility tests

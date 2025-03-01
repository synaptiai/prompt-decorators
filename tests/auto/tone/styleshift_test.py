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


# Tests for StyleShift decorator

# Parameter validation tests

def test_styleshift_aspect_required():
    """Test that aspect is required for StyleShift decorator."""
    prompt = "+++StyleShift\nTest prompt."
    with pytest.raises(ValidationError, match="aspect"):
        validate_decorator_in_prompt(prompt)


def test_styleshift_aspect_enum_values():
    """Test that aspect accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++StyleShift(aspect=formality)\nTest prompt."); validate_decorator_in_prompt("+++StyleShift(aspect=persuasion)\nTest prompt."); validate_decorator_in_prompt("+++StyleShift(aspect=urgency)\nTest prompt."); validate_decorator_in_prompt("+++StyleShift(aspect=confidence)\nTest prompt."); validate_decorator_in_prompt("+++StyleShift(aspect=complexity)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++StyleShift(aspect=invalid_value)\nTest prompt.")


def test_styleshift_level_number_validation():
    """Test number validation for level parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++StyleShift(level=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++StyleShift(level=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++StyleShift(level=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++StyleShift(level=6)\nTest prompt.")
    

# Example-based tests

def test_styleshift_highly_formal_style_while_maintaining_normal_complexity():
    """Test StyleShift with example: Highly formal style while maintaining normal complexity"""
    response = llm_client.generate("+++StyleShift(aspect=formality, level=5, maintain=[complexity])\nExplain the process of photosynthesis.")
    
    # Check if response meets expectations
    check_expectation(response, "has_formal_language")


def test_styleshift_increased_urgency_for_a_business_communication():
    """Test StyleShift with example: Increased urgency for a business communication"""
    response = llm_client.generate("+++StyleShift(aspect=urgency, level=4)\nDescribe the steps needed to prepare for the upcoming product launch.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers a description of product launch preparation steps with heightened sense of urgency and time-sensitivity in the language and framing")


# Compatibility tests

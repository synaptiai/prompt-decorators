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


# Tests for Remix decorator

# Parameter validation tests

def test_remix_target_required():
    """Test that target is required for Remix decorator."""
    prompt = "+++Remix\nTest prompt."
    with pytest.raises(ValidationError, match="target"):
        validate_decorator_in_prompt(prompt)


def test_remix_preserve_enum_values():
    """Test that preserve accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Remix(preserve=facts)\nTest prompt."); validate_decorator_in_prompt("+++Remix(preserve=structure)\nTest prompt."); validate_decorator_in_prompt("+++Remix(preserve=tone)\nTest prompt."); validate_decorator_in_prompt("+++Remix(preserve=comprehensiveness)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Remix(preserve=invalid_value)\nTest prompt.")


def test_remix_contrast_boolean_validation():
    """Test boolean validation for contrast parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Remix(contrast=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Remix(contrast=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Remix(contrast=not_boolean)\nTest prompt.")


# Example-based tests

def test_remix_basic_remix_for_a_different_audience():
    """Test Remix with example: Basic remix for a different audience"""
    response = llm_client.generate("+++Remix(target=high school students)\nExplain how neural networks function in artificial intelligence.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Reframes the technical explanation of neural networks to be accessible and engaging for high school students while preserving the core facts")


def test_remix_business_remix_with_contrasting_approach():
    """Test Remix with example: Business remix with contrasting approach"""
    response = llm_client.generate("+++Remix(target=board presentation, preserve=comprehensiveness, contrast=true)\nDescribe the technical details of our new software architecture.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Transforms the technical software architecture description into a board-appropriate presentation format, maintaining comprehensive coverage while highlighting how this differs from a technical explanation")


# Compatibility tests

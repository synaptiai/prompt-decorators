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


# Tests for Creative decorator

# Parameter validation tests

def test_creative_level_enum_values():
    """Test that level accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Creative(level=moderate)\nTest prompt."); validate_decorator_in_prompt("+++Creative(level=high)\nTest prompt."); validate_decorator_in_prompt("+++Creative(level=unconventional)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Creative(level=invalid_value)\nTest prompt.")


# Example-based tests

def test_creative_basic_creative_response_to_a_standard_question():
    """Test Creative with example: Basic creative response to a standard question"""
    response = llm_client.generate("+++Creative\nExplain how the internet works.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an imaginative explanation of the internet using unexpected metaphors and creative language while maintaining accuracy")


def test_creative_highly_creative_response_with_specific_elements():
    """Test Creative with example: Highly creative response with specific elements"""
    response = llm_client.generate("+++Creative(level=unconventional, elements=[metaphor,narrative,wordplay], constraints=[must reference nature])\nDescribe the principles of quantum computing.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers an unconventional explanation of quantum computing through an engaging narrative filled with nature metaphors and clever wordplay")


# Compatibility tests

def test_creative_conflicts():
    """Test that Creative has expected conflicts."""
    conflicts = ["Academic", "Professional"]
    for conflict in conflicts:
        result = combine_decorators(["Creative", conflict])
        assert not result["compatible"], f"Creative should conflict with {conflict}"

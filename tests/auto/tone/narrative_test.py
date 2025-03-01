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


# Tests for Narrative decorator

# Parameter validation tests

def test_narrative_structure_enum_values():
    """Test that structure accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Narrative(structure=classic)\nTest prompt."); validate_decorator_in_prompt("+++Narrative(structure=nonlinear)\nTest prompt."); validate_decorator_in_prompt("+++Narrative(structure=case-study)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Narrative(structure=invalid_value)\nTest prompt.")


def test_narrative_characters_boolean_validation():
    """Test boolean validation for characters parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Narrative(characters=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Narrative(characters=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Narrative(characters=not_boolean)\nTest prompt.")


def test_narrative_length_enum_values():
    """Test that length accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Narrative(length=brief)\nTest prompt."); validate_decorator_in_prompt("+++Narrative(length=moderate)\nTest prompt."); validate_decorator_in_prompt("+++Narrative(length=extended)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Narrative(length=invalid_value)\nTest prompt.")


# Example-based tests

def test_narrative_classic_narrative_structure_to_explain_a_concept():
    """Test Narrative with example: Classic narrative structure to explain a concept"""
    response = llm_client.generate("+++Narrative\nExplain how the stock market works.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Explains the stock market through a classic narrative structure, introducing character elements and following a traditional story arc")


def test_narrative_brief_case_study_without_character_elements():
    """Test Narrative with example: Brief case study without character elements"""
    response = llm_client.generate("+++Narrative(structure=case-study, characters=false, length=brief)\nDescribe the impact of social media on mental health.")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


# Compatibility tests

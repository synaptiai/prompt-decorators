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


# Tests for Limitations decorator

# Parameter validation tests

def test_limitations_detail_enum_values():
    """Test that detail accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Limitations(detail=brief)\nTest prompt."); validate_decorator_in_prompt("+++Limitations(detail=moderate)\nTest prompt."); validate_decorator_in_prompt("+++Limitations(detail=comprehensive)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Limitations(detail=invalid_value)\nTest prompt.")


def test_limitations_position_enum_values():
    """Test that position accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Limitations(position=beginning)\nTest prompt."); validate_decorator_in_prompt("+++Limitations(position=end)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Limitations(position=invalid_value)\nTest prompt.")


def test_limitations_focus_enum_values():
    """Test that focus accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Limitations(focus=knowledge)\nTest prompt."); validate_decorator_in_prompt("+++Limitations(focus=methodology)\nTest prompt."); validate_decorator_in_prompt("+++Limitations(focus=context)\nTest prompt."); validate_decorator_in_prompt("+++Limitations(focus=biases)\nTest prompt."); validate_decorator_in_prompt("+++Limitations(focus=all)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Limitations(focus=invalid_value)\nTest prompt.")


# Example-based tests

def test_limitations_brief_limitations_statement_at_the_end_focused_on_methodology():
    """Test Limitations with example: Brief limitations statement at the end focused on methodology"""
    response = llm_client.generate("+++Limitations(detail=brief, focus=methodology)\nExplain how personality tests predict career success.")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


def test_limitations_comprehensive_limitations_at_the_beginning_covering_all_aspects():
    """Test Limitations with example: Comprehensive limitations at the beginning covering all aspects"""
    response = llm_client.generate("+++Limitations(detail=comprehensive, position=beginning, focus=all)\nDescribe the current understanding of consciousness.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Begins with a thorough discussion of the limitations in our understanding of consciousness before presenting the current state of knowledge")


# Compatibility tests

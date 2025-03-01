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


# Tests for NegativeSpace decorator

# Parameter validation tests

def test_negativespace_focus_enum_values():
    """Test that focus accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++NegativeSpace(focus=implications)\nTest prompt."); validate_decorator_in_prompt("+++NegativeSpace(focus=missing)\nTest prompt."); validate_decorator_in_prompt("+++NegativeSpace(focus=unstated)\nTest prompt."); validate_decorator_in_prompt("+++NegativeSpace(focus=comprehensive)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++NegativeSpace(focus=invalid_value)\nTest prompt.")


def test_negativespace_depth_enum_values():
    """Test that depth accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++NegativeSpace(depth=surface)\nTest prompt."); validate_decorator_in_prompt("+++NegativeSpace(depth=moderate)\nTest prompt."); validate_decorator_in_prompt("+++NegativeSpace(depth=deep)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++NegativeSpace(depth=invalid_value)\nTest prompt.")


def test_negativespace_structure_enum_values():
    """Test that structure accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++NegativeSpace(structure=before)\nTest prompt."); validate_decorator_in_prompt("+++NegativeSpace(structure=after)\nTest prompt."); validate_decorator_in_prompt("+++NegativeSpace(structure=integrated)\nTest prompt."); validate_decorator_in_prompt("+++NegativeSpace(structure=separate)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++NegativeSpace(structure=invalid_value)\nTest prompt.")


# Example-based tests

def test_negativespace_basic_comprehensive_negative_space_analysis():
    """Test NegativeSpace with example: Basic comprehensive negative space analysis"""
    response = llm_client.generate("+++NegativeSpace\nDiscuss the impact of social media on society.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a discussion of social media's societal impact while integrating analysis of unstated assumptions, overlooked factors, and typically unaddressed implications")


def test_negativespace_deep_negative_space_analysis_focused_on_missing_elements():
    """Test NegativeSpace with example: Deep negative space analysis focused on missing elements"""
    response = llm_client.generate("+++NegativeSpace(focus=missing, depth=deep, structure=after)\nExplain the current approaches to artificial intelligence safety.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="First explains current AI safety approaches, then provides a separate deep analysis of missing elements in the discussion, such as unstudied risks, overlooked stakeholders, and neglected scenarios")


# Compatibility tests

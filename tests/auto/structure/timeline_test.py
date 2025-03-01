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


# Tests for Timeline decorator

# Parameter validation tests

def test_timeline_granularity_enum_values():
    """Test that granularity accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Timeline(granularity=day)\nTest prompt."); validate_decorator_in_prompt("+++Timeline(granularity=month)\nTest prompt."); validate_decorator_in_prompt("+++Timeline(granularity=year)\nTest prompt."); validate_decorator_in_prompt("+++Timeline(granularity=decade)\nTest prompt."); validate_decorator_in_prompt("+++Timeline(granularity=century)\nTest prompt."); validate_decorator_in_prompt("+++Timeline(granularity=era)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Timeline(granularity=invalid_value)\nTest prompt.")


def test_timeline_format_enum_values():
    """Test that format accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Timeline(format=list)\nTest prompt."); validate_decorator_in_prompt("+++Timeline(format=narrative)\nTest prompt."); validate_decorator_in_prompt("+++Timeline(format=table)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Timeline(format=invalid_value)\nTest prompt.")


def test_timeline_details_enum_values():
    """Test that details accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Timeline(details=minimal)\nTest prompt."); validate_decorator_in_prompt("+++Timeline(details=moderate)\nTest prompt."); validate_decorator_in_prompt("+++Timeline(details=comprehensive)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Timeline(details=invalid_value)\nTest prompt.")


# Example-based tests

def test_timeline_basic_chronological_timeline_of_major_events():
    """Test Timeline with example: Basic chronological timeline of major events"""
    response = llm_client.generate("+++Timeline\nDescribe the key developments in artificial intelligence.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents a year-by-year list of important AI milestones and breakthroughs from earliest developments to present day")


def test_timeline_detailed_narrative_timeline_with_specific_date_granularity():
    """Test Timeline with example: Detailed narrative timeline with specific date granularity"""
    response = llm_client.generate("+++Timeline(granularity=month, format=narrative, details=comprehensive)\nWhat were the major events of the Apollo 11 mission?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a flowing narrative account of the Apollo 11 mission with month/day dates and comprehensive details of each significant event")


# Compatibility tests

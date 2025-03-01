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


# Tests for BlindSpots decorator

# Parameter validation tests

def test_blindspots_depth_enum_values():
    """Test that depth accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++BlindSpots(depth=basic)\nTest prompt."); validate_decorator_in_prompt("+++BlindSpots(depth=thorough)\nTest prompt."); validate_decorator_in_prompt("+++BlindSpots(depth=comprehensive)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++BlindSpots(depth=invalid_value)\nTest prompt.")


def test_blindspots_position_enum_values():
    """Test that position accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++BlindSpots(position=after)\nTest prompt."); validate_decorator_in_prompt("+++BlindSpots(position=before)\nTest prompt."); validate_decorator_in_prompt("+++BlindSpots(position=integrated)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++BlindSpots(position=invalid_value)\nTest prompt.")


# Example-based tests

def test_blindspots_basic_blind_spots_analysis_after_a_response():
    """Test BlindSpots with example: Basic blind spots analysis after a response"""
    response = llm_client.generate("+++BlindSpots\nWhat factors drive economic growth?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an analysis of economic growth factors, followed by identification of unstated assumptions and potential blind spots in the analysis")


def test_blindspots_comprehensive_blind_spots_analysis_integrated_throughout():
    """Test BlindSpots with example: Comprehensive blind spots analysis integrated throughout"""
    response = llm_client.generate("+++BlindSpots(categories=[cultural,historical,methodological], depth=comprehensive, position=integrated)\nEvaluate the impact of social media on society.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers an evaluation of social media's societal impact with comprehensive blind spot analysis woven throughout, specifically addressing cultural, historical, and methodological blind spots")


# Compatibility tests

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


# Tests for CiteSources decorator

# Parameter validation tests

def test_citesources_style_enum_values():
    """Test that style accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++CiteSources(style=inline)\nTest prompt."); validate_decorator_in_prompt("+++CiteSources(style=footnote)\nTest prompt."); validate_decorator_in_prompt("+++CiteSources(style=endnote)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++CiteSources(style=invalid_value)\nTest prompt.")


def test_citesources_format_enum_values():
    """Test that format accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++CiteSources(format=APA)\nTest prompt."); validate_decorator_in_prompt("+++CiteSources(format=MLA)\nTest prompt."); validate_decorator_in_prompt("+++CiteSources(format=Chicago)\nTest prompt."); validate_decorator_in_prompt("+++CiteSources(format=Harvard)\nTest prompt."); validate_decorator_in_prompt("+++CiteSources(format=IEEE)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++CiteSources(format=invalid_value)\nTest prompt.")


def test_citesources_comprehensive_boolean_validation():
    """Test boolean validation for comprehensive parameter."""
    # Test true value
    validate_decorator_in_prompt("+++CiteSources(comprehensive=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++CiteSources(comprehensive=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++CiteSources(comprehensive=not_boolean)\nTest prompt.")


# Example-based tests

def test_citesources_basic_inline_citations_for_a_scientific_topic():
    """Test CiteSources with example: Basic inline citations for a scientific topic"""
    response = llm_client.generate("+++CiteSources\nExplain the evidence for climate change.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Explains climate change with inline citations to scientific sources in APA format")


def test_citesources_comprehensive_footnote_citations_in_chicago_style():
    """Test CiteSources with example: Comprehensive footnote citations in Chicago style"""
    response = llm_client.generate("+++CiteSources(style=footnote, format=Chicago, comprehensive=true)\nDescribe the major events of World War II.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers a detailed account of WWII with comprehensive footnote citations in Chicago style for all factual claims")


# Compatibility tests

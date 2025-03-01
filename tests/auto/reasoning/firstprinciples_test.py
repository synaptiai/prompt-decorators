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


# Tests for FirstPrinciples decorator

# Parameter validation tests

def test_firstprinciples_depth_number_validation():
    """Test number validation for depth parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++FirstPrinciples(depth=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++FirstPrinciples(depth=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++FirstPrinciples(depth=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++FirstPrinciples(depth=6)\nTest prompt.")
    

# Example-based tests

def test_firstprinciples_basic_first_principles_analysis_of_a_concept():
    """Test FirstPrinciples with example: Basic first principles analysis of a concept"""
    response = llm_client.generate("+++FirstPrinciples\nHow do electric vehicles work?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Breaks down electric vehicles into fundamental principles of electricity, motors, and energy storage before explaining the complete system")


def test_firstprinciples_deep_first_principles_analysis_with_maximum_depth():
    """Test FirstPrinciples with example: Deep first principles analysis with maximum depth"""
    response = llm_client.generate("+++FirstPrinciples(depth=5)\nWhat makes machine learning effective?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an extensive breakdown of machine learning starting from mathematical foundations and progressively building up to complex algorithms")


# Compatibility tests

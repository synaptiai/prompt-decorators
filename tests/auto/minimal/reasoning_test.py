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


# Tests for Reasoning decorator

# Parameter validation tests

def test_reasoning_depth_enum_values():
    """Test that depth accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Reasoning(depth=basic)\nTest prompt."); validate_decorator_in_prompt("+++Reasoning(depth=moderate)\nTest prompt."); validate_decorator_in_prompt("+++Reasoning(depth=comprehensive)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Reasoning(depth=invalid_value)\nTest prompt.")


# Example-based tests

def test_reasoning_basic_reasoning_for_a_simple_question():
    """Test Reasoning with example: Basic reasoning for a simple question"""
    response = llm_client.generate("+++Reasoning(depth=basic)\nWhat is the best programming language for beginners?")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


def test_reasoning_comprehensive_analysis_of_a_complex_topic():
    """Test Reasoning with example: Comprehensive analysis of a complex topic"""
    response = llm_client.generate("+++Reasoning(depth=comprehensive)\nWhat are the implications of quantum computing for cybersecurity?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers an in-depth analysis covering multiple aspects and their interconnections")


# Compatibility tests

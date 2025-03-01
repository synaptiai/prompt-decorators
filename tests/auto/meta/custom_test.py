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


# Tests for Custom decorator

# Parameter validation tests

def test_custom_rules_required():
    """Test that rules is required for Custom decorator."""
    prompt = "+++Custom\nTest prompt."
    with pytest.raises(ValidationError, match="rules"):
        validate_decorator_in_prompt(prompt)


def test_custom_priority_enum_values():
    """Test that priority accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Custom(priority=override)\nTest prompt."); validate_decorator_in_prompt("+++Custom(priority=supplement)\nTest prompt."); validate_decorator_in_prompt("+++Custom(priority=fallback)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Custom(priority=invalid_value)\nTest prompt.")


# Example-based tests

def test_custom_basic_custom_formatting_rule():
    """Test Custom with example: Basic custom formatting rule"""
    response = llm_client.generate("+++Custom(rules=every paragraph must start with a word that begins with the letter A)\nExplain how search engines work.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an explanation of search engines where every paragraph begins with a word starting with the letter A")


def test_custom_complex_custom_behavior_with_named_reference():
    """Test Custom with example: Complex custom behavior with named reference"""
    response = llm_client.generate("+++Custom(name=DualPerspective, rules=present two contrasting viewpoints on each main point, label them as 'Perspective A' and 'Perspective B', and then provide a synthesis, priority=supplement)\nAnalyze the impact of social media on politics.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Analyzes social media's impact on politics using dual contrasting perspectives for each point, labeled as specified, with synthesis after each point, while still respecting other decorators")


# Compatibility tests

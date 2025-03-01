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


# Tests for Contrarian decorator

# Parameter validation tests

def test_contrarian_approach_enum_values():
    """Test that approach accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Contrarian(approach=outsider)\nTest prompt."); validate_decorator_in_prompt("+++Contrarian(approach=skeptic)\nTest prompt."); validate_decorator_in_prompt("+++Contrarian(approach=devil's-advocate)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Contrarian(approach=invalid_value)\nTest prompt.")


def test_contrarian_maintain_boolean_validation():
    """Test boolean validation for maintain parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Contrarian(maintain=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Contrarian(maintain=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Contrarian(maintain=not_boolean)\nTest prompt.")


# Example-based tests

def test_contrarian_basic_devil_s_advocate_approach_with_balanced_conclusion():
    """Test Contrarian with example: Basic devil's advocate approach with balanced conclusion"""
    response = llm_client.generate("+++Contrarian\nWhy is renewable energy considered the future of power generation?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Challenges conventional thinking about renewable energy's dominance, presenting counterarguments and limitations, followed by a balanced perspective")


def test_contrarian_maintained_skeptical_contrarian_stance_focused_on_a_specific_aspect():
    """Test Contrarian with example: Maintained skeptical contrarian stance focused on a specific aspect"""
    response = llm_client.generate("+++Contrarian(approach=skeptic, maintain=true, focus=methodology)\nDiscuss the reliability of climate models in predicting future global temperatures.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a consistently skeptical analysis of climate model methodologies, questioning assumptions, limitations, and historical accuracy throughout the response")


# Compatibility tests

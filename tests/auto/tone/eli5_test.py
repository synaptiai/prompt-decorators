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


# Tests for ELI5 decorator

# Parameter validation tests

def test_eli5_strictness_boolean_validation():
    """Test boolean validation for strictness parameter."""
    # Test true value
    validate_decorator_in_prompt("+++ELI5(strictness=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++ELI5(strictness=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++ELI5(strictness=not_boolean)\nTest prompt.")


# Example-based tests

def test_eli5_basic_explanation_of_a_complex_scientific_concept():
    """Test ELI5 with example: Basic explanation of a complex scientific concept"""
    response = llm_client.generate("+++ELI5\nExplain how nuclear fusion works.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Explains nuclear fusion using simple language, analogies, and examples a child could understand")


def test_eli5_strict_simplified_explanation_of_a_technical_subject():
    """Test ELI5 with example: Strict simplified explanation of a technical subject"""
    response = llm_client.generate("+++ELI5(strictness=true)\nHow does the internet work?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an extremely simplified explanation of the internet using only basic vocabulary and concrete examples appropriate for young children")


# Compatibility tests

def test_eli5_conflicts():
    """Test that ELI5 has expected conflicts."""
    conflicts = ["Academic", "Professional", "AsExpert", "Precision", "Tone"]
    for conflict in conflicts:
        result = combine_decorators(["ELI5", conflict])
        assert not result["compatible"], f"ELI5 should conflict with {conflict}"

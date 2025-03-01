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


# Tests for Academic decorator

# Parameter validation tests

def test_academic_style_enum_values():
    """Test that style accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Academic(style=humanities)\nTest prompt."); validate_decorator_in_prompt("+++Academic(style=scientific)\nTest prompt."); validate_decorator_in_prompt("+++Academic(style=legal)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Academic(style=invalid_value)\nTest prompt.")


def test_academic_citationStyle_enum_values():
    """Test that citationStyle accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Academic(citationStyle=APA)\nTest prompt."); validate_decorator_in_prompt("+++Academic(citationStyle=MLA)\nTest prompt."); validate_decorator_in_prompt("+++Academic(citationStyle=Chicago)\nTest prompt."); validate_decorator_in_prompt("+++Academic(citationStyle=Harvard)\nTest prompt."); validate_decorator_in_prompt("+++Academic(citationStyle=IEEE)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Academic(citationStyle=invalid_value)\nTest prompt.")


# Example-based tests

def test_academic_scientific_academic_response_with_apa_citations():
    """Test Academic with example: Scientific academic response with APA citations"""
    response = llm_client.generate("+++Academic\nDiscuss the evidence for climate change.")
    
    # Check if response meets expectations
    check_expectation(response, "has_formal_language")


def test_academic_humanities_focused_academic_response_with_mla_citations():
    """Test Academic with example: Humanities-focused academic response with MLA citations"""
    response = llm_client.generate("+++Academic(style=humanities, citationStyle=MLA)\nAnalyze the themes in Shakespeare's Hamlet.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a literary analysis of Hamlet using humanities-appropriate terminology and MLA citation format")


# Compatibility tests

def test_academic_conflicts():
    """Test that Academic has expected conflicts."""
    conflicts = ["ELI5", "Creative", "Motivational"]
    for conflict in conflicts:
        result = combine_decorators(["Academic", conflict])
        assert not result["compatible"], f"Academic should conflict with {conflict}"

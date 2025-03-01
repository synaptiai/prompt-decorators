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


# Tests for ForcedAnalogy decorator

# Parameter validation tests

def test_forcedanalogy_source_required():
    """Test that source is required for ForcedAnalogy decorator."""
    prompt = "+++ForcedAnalogy\nTest prompt."
    with pytest.raises(ValidationError, match="source"):
        validate_decorator_in_prompt(prompt)


def test_forcedanalogy_comprehensiveness_enum_values():
    """Test that comprehensiveness accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++ForcedAnalogy(comprehensiveness=basic)\nTest prompt."); validate_decorator_in_prompt("+++ForcedAnalogy(comprehensiveness=comprehensive)\nTest prompt."); validate_decorator_in_prompt("+++ForcedAnalogy(comprehensiveness=detailed)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++ForcedAnalogy(comprehensiveness=invalid_value)\nTest prompt.")


def test_forcedanalogy_mappings_number_validation():
    """Test number validation for mappings parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++ForcedAnalogy(mappings=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++ForcedAnalogy(mappings=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++ForcedAnalogy(mappings=7)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++ForcedAnalogy(mappings=8)\nTest prompt.")
    

# Example-based tests

def test_forcedanalogy_explaining_a_technical_concept_using_sports_analogies():
    """Test ForcedAnalogy with example: Explaining a technical concept using sports analogies"""
    response = llm_client.generate("+++ForcedAnalogy(source=sports)\nExplain how blockchain technology works.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Explains blockchain technology by mapping concepts to sports analogies (e.g., ledger as scoreboard, miners as referees, consensus as rulebook)")


def test_forcedanalogy_detailed_cooking_analogy_for_complex_scientific_process():
    """Test ForcedAnalogy with example: Detailed cooking analogy for complex scientific process"""
    response = llm_client.generate("+++ForcedAnalogy(source=cooking, comprehensiveness=detailed, mappings=5)\nDescribe how CRISPR gene editing works.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a detailed explanation of CRISPR through cooking analogies, with 5 distinct concept mappings (e.g., DNA as recipe, Cas9 as kitchen knife, guide RNA as cooking instructions)")


# Compatibility tests

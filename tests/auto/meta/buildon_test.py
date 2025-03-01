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


# Tests for BuildOn decorator

# Parameter validation tests

def test_buildon_reference_enum_values():
    """Test that reference accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++BuildOn(reference=last)\nTest prompt."); validate_decorator_in_prompt("+++BuildOn(reference=specific)\nTest prompt."); validate_decorator_in_prompt("+++BuildOn(reference=all)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++BuildOn(reference=invalid_value)\nTest prompt.")


def test_buildon_approach_enum_values():
    """Test that approach accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++BuildOn(approach=extend)\nTest prompt."); validate_decorator_in_prompt("+++BuildOn(approach=refine)\nTest prompt."); validate_decorator_in_prompt("+++BuildOn(approach=contrast)\nTest prompt."); validate_decorator_in_prompt("+++BuildOn(approach=synthesize)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++BuildOn(approach=invalid_value)\nTest prompt.")


def test_buildon_preserveStructure_boolean_validation():
    """Test boolean validation for preserveStructure parameter."""
    # Test true value
    validate_decorator_in_prompt("+++BuildOn(preserveStructure=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++BuildOn(preserveStructure=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++BuildOn(preserveStructure=not_boolean)\nTest prompt.")


# Example-based tests

def test_buildon_basic_extension_of_the_previous_response():
    """Test BuildOn with example: Basic extension of the previous response"""
    response = llm_client.generate("+++BuildOn\nAdd more detail about implementation challenges.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Extends the previous response by adding more detailed information about implementation challenges while maintaining continuity")


def test_buildon_specific_refinement_with_structural_changes():
    """Test BuildOn with example: Specific refinement with structural changes"""
    response = llm_client.generate("+++BuildOn(reference=specific, approach=refine, preserveStructure=false)\nImprove the section on risk analysis with more quantitative measures.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Refines specifically the risk analysis section from the previous content with more quantitative measures, potentially restructuring it")


# Compatibility tests

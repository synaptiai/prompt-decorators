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


# Tests for Professional decorator

# Parameter validation tests

def test_professional_formality_enum_values():
    """Test that formality accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Professional(formality=standard)\nTest prompt."); validate_decorator_in_prompt("+++Professional(formality=high)\nTest prompt."); validate_decorator_in_prompt("+++Professional(formality=executive)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Professional(formality=invalid_value)\nTest prompt.")


# Example-based tests

def test_professional_standard_professional_business_communication():
    """Test Professional with example: Standard professional business communication"""
    response = llm_client.generate("+++Professional\nExplain the benefits of implementing a CRM system.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers a clear, professional explanation of CRM benefits using business-appropriate language and structure")


def test_professional_industry_specific_executive_level_communication():
    """Test Professional with example: Industry-specific executive-level communication"""
    response = llm_client.generate("+++Professional(industry=healthcare, formality=executive)\nSummarize the impact of telehealth adoption on patient outcomes.")
    
    # Check if response meets expectations
    check_expectation(response, "has_formal_language")


# Compatibility tests

def test_professional_conflicts():
    """Test that Professional has expected conflicts."""
    conflicts = ["ELI5", "Creative"]
    for conflict in conflicts:
        result = combine_decorators(["Professional", conflict])
        assert not result["compatible"], f"Professional should conflict with {conflict}"

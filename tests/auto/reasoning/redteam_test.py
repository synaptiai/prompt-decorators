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


# Tests for RedTeam decorator

# Parameter validation tests

def test_redteam_strength_enum_values():
    """Test that strength accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++RedTeam(strength=moderate)\nTest prompt."); validate_decorator_in_prompt("+++RedTeam(strength=aggressive)\nTest prompt."); validate_decorator_in_prompt("+++RedTeam(strength=steelman)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++RedTeam(strength=invalid_value)\nTest prompt.")


def test_redteam_constructive_boolean_validation():
    """Test boolean validation for constructive parameter."""
    # Test true value
    validate_decorator_in_prompt("+++RedTeam(constructive=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++RedTeam(constructive=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++RedTeam(constructive=not_boolean)\nTest prompt.")


# Example-based tests

def test_redteam_basic_red_team_analysis_of_a_business_proposal():
    """Test RedTeam with example: Basic red team analysis of a business proposal"""
    response = llm_client.generate("+++RedTeam\nHere's our plan to launch a new subscription service...")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Analyzes the subscription service plan from an adversarial perspective, identifying potential weaknesses, oversights, and challenges")


def test_redteam_aggressive_red_team_analysis_with_specific_focus_areas():
    """Test RedTeam with example: Aggressive red team analysis with specific focus areas"""
    response = llm_client.generate("+++RedTeam(strength=aggressive, focus=[security,scalability,market-fit], constructive=true)\nReview our new authentication system design.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Aggressively challenges the authentication system design, specifically targeting security, scalability, and market-fit concerns, followed by constructive improvement suggestions")


# Compatibility tests

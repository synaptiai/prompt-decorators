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


# Tests for Persona decorator

# Parameter validation tests

def test_persona_role_required():
    """Test that role is required for Persona decorator."""
    prompt = "+++Persona\nTest prompt."
    with pytest.raises(ValidationError, match="role"):
        validate_decorator_in_prompt(prompt)


# Example-based tests

def test_persona_response_from_the_perspective_of_a_specific_stakeholder():
    """Test Persona with example: Response from the perspective of a specific stakeholder"""
    response = llm_client.generate("+++Persona(role=customer)\nWhat are the implications of implementing a new subscription model?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Analyzes the subscription model from a customer's perspective, focusing on value, convenience, and potential concerns")


def test_persona_detailed_persona_with_specific_traits_and_goals():
    """Test Persona with example: Detailed persona with specific traits and goals"""
    response = llm_client.generate("+++Persona(role=senior software engineer, traits=[pragmatic,detail-oriented,experienced], goals=[code quality,maintainability,efficiency])\nEvaluate the proposal to switch from monolith to microservices.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides a detailed analysis of the monolith-to-microservices transition from the perspective of a pragmatic, detail-oriented senior engineer who prioritizes code quality and maintainability")


# Compatibility tests

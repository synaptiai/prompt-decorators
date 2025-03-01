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


# Tests for AsExpert decorator

# Parameter validation tests

def test_asexpert_domain_required():
    """Test that domain is required for AsExpert decorator."""
    prompt = "+++AsExpert\nTest prompt."
    with pytest.raises(ValidationError, match="domain"):
        validate_decorator_in_prompt(prompt)


def test_asexpert_experience_enum_values():
    """Test that experience accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++AsExpert(experience=junior)\nTest prompt."); validate_decorator_in_prompt("+++AsExpert(experience=senior)\nTest prompt."); validate_decorator_in_prompt("+++AsExpert(experience=leading)\nTest prompt."); validate_decorator_in_prompt("+++AsExpert(experience=pioneering)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++AsExpert(experience=invalid_value)\nTest prompt.")


def test_asexpert_technical_boolean_validation():
    """Test boolean validation for technical parameter."""
    # Test true value
    validate_decorator_in_prompt("+++AsExpert(technical=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++AsExpert(technical=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++AsExpert(technical=not_boolean)\nTest prompt.")


# Example-based tests

def test_asexpert_basic_response_as_a_domain_expert():
    """Test AsExpert with example: Basic response as a domain expert"""
    response = llm_client.generate("+++AsExpert(domain=neuroscience)\nExplain how memories are formed in the brain.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an explanation of memory formation from the perspective of a senior neuroscientist, using appropriate terminology and references to relevant research")


def test_asexpert_highly_technical_response_as_pioneering_expert():
    """Test AsExpert with example: Highly technical response as pioneering expert"""
    response = llm_client.generate("+++AsExpert(domain=cryptography, experience=pioneering, technical=true)\nAssess the security implications of quantum computing for current encryption standards.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers a technically sophisticated assessment of quantum computing's encryption impacts from the perspective of a pioneering cryptography expert, using advanced terminology and nuanced analysis")


# Compatibility tests

def test_asexpert_conflicts():
    """Test that AsExpert has expected conflicts."""
    conflicts = ["ELI5"]
    for conflict in conflicts:
        result = combine_decorators(["AsExpert", conflict])
        assert not result["compatible"], f"AsExpert should conflict with {conflict}"

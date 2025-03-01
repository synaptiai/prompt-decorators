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


# Tests for Context decorator

# Parameter validation tests

def test_context_domain_required():
    """Test that domain is required for Context decorator."""
    prompt = "+++Context\nTest prompt."
    with pytest.raises(ValidationError, match="domain"):
        validate_decorator_in_prompt(prompt)


def test_context_scope_enum_values():
    """Test that scope accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Context(scope=terminology)\nTest prompt."); validate_decorator_in_prompt("+++Context(scope=examples)\nTest prompt."); validate_decorator_in_prompt("+++Context(scope=structure)\nTest prompt."); validate_decorator_in_prompt("+++Context(scope=all)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Context(scope=invalid_value)\nTest prompt.")


def test_context_level_enum_values():
    """Test that level accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Context(level=beginner)\nTest prompt."); validate_decorator_in_prompt("+++Context(level=intermediate)\nTest prompt."); validate_decorator_in_prompt("+++Context(level=expert)\nTest prompt."); validate_decorator_in_prompt("+++Context(level=mixed)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Context(level=invalid_value)\nTest prompt.")


# Example-based tests

def test_context_basic_domain_specific_adaptation_of_decorators():
    """Test Context with example: Basic domain-specific adaptation of decorators"""
    response = llm_client.generate("+++Context(domain=medicine)\n+++StepByStep\n+++Detailed\nExplain how vaccines are developed.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Applies the StepByStep and Detailed decorators with medical context-awareness, using appropriate medical terminology, examples, and structures for explaining vaccine development")


def test_context_targeted_contextualization_for_specific_expertise_level():
    """Test Context with example: Targeted contextualization for specific expertise level"""
    response = llm_client.generate("+++Context(domain=programming, scope=examples, level=beginner)\n+++Reasoning\n+++ELI5\nExplain how databases work.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Uses the Reasoning and ELI5 decorators with programming-appropriate examples specifically tailored for beginners, while keeping general terminology and structure accessible")


# Compatibility tests

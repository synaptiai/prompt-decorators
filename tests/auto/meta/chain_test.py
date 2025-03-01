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


# Tests for Chain decorator

# Parameter validation tests

def test_chain_decorators_required():
    """Test that decorators is required for Chain decorator."""
    prompt = "+++Chain\nTest prompt."
    with pytest.raises(ValidationError, match="decorators"):
        validate_decorator_in_prompt(prompt)


def test_chain_showSteps_boolean_validation():
    """Test boolean validation for showSteps parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Chain(showSteps=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Chain(showSteps=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Chain(showSteps=not_boolean)\nTest prompt.")


def test_chain_stopOnFailure_boolean_validation():
    """Test boolean validation for stopOnFailure parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Chain(stopOnFailure=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Chain(stopOnFailure=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Chain(stopOnFailure=not_boolean)\nTest prompt.")


# Example-based tests

def test_chain_basic_sequential_application_of_decorators():
    """Test Chain with example: Basic sequential application of decorators"""
    response = llm_client.generate("+++Chain(decorators=[StepByStep,Concise])\nExplain how neural networks learn.")
    
    # Check if response meets expectations
    check_expectation(response, "is_concise")


def test_chain_complex_decorator_chain_with_visible_intermediate_steps():
    """Test Chain with example: Complex decorator chain with visible intermediate steps"""
    response = llm_client.generate("+++Chain(decorators=[Socratic,Academic,TreeOfThought], showSteps=true, stopOnFailure=false)\nDiscuss the ethics of autonomous weapons.")
    
    # Check if response meets expectations
    check_expectation(response, "has_formal_language")


# Compatibility tests

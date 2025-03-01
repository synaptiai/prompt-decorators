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


# Tests for Conditional decorator

# Parameter validation tests

def test_conditional_if_required():
    """Test that if is required for Conditional decorator."""
    prompt = "+++Conditional\nTest prompt."
    with pytest.raises(ValidationError, match="if"):
        validate_decorator_in_prompt(prompt)


def test_conditional_then_required():
    """Test that then is required for Conditional decorator."""
    prompt = "+++Conditional\nTest prompt."
    with pytest.raises(ValidationError, match="then"):
        validate_decorator_in_prompt(prompt)


# Example-based tests

def test_conditional_basic_conditional_application_based_on_content_complexity():
    """Test Conditional with example: Basic conditional application based on content complexity"""
    response = llm_client.generate("+++Conditional(if=complex, then=StepByStep, else=Concise)\nExplain how quantum computing works.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Evaluates if the topic is complex, which quantum computing is, so it applies the StepByStep decorator")


def test_conditional_conditional_application_with_parameterized_decorators():
    """Test Conditional with example: Conditional application with parameterized decorators"""
    response = llm_client.generate("+++Conditional(if=controversial, then=Debate(perspectives=3), else=Reasoning(depth=moderate))\nDiscuss the ethical implications of gene editing in humans.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Determines that gene editing ethics is controversial, so it applies the Debate decorator with 3 perspectives rather than the Reasoning decorator")


# Compatibility tests

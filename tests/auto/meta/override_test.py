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


# Tests for Override decorator

# Parameter validation tests

def test_override_decorator_required():
    """Test that decorator is required for Override decorator."""
    prompt = "+++Override\nTest prompt."
    with pytest.raises(ValidationError, match="decorator"):
        validate_decorator_in_prompt(prompt)


# Example-based tests

def test_override_basic_parameter_override_for_a_standard_decorator():
    """Test Override with example: Basic parameter override for a standard decorator"""
    response = llm_client.generate("+++Override(decorator=StepByStep, parameters={\"numbered\": true, \"steps\": 7})\nExplain how to bake bread.")
    
    # Check if response meets expectations
    check_expectation(response, "contains_numbered_steps")


def test_override_complex_behavior_override_with_custom_instructions():
    """Test Override with example: Complex behavior override with custom instructions"""
    response = llm_client.generate("+++Override(decorator=Debate, parameters={\"perspectives\": 2}, behavior=instead of presenting neutral perspectives, adopt strongly opposing viewpoints with clear advocacy for each position)\nDiscuss the ethics of gene editing.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Uses the Debate decorator structure for discussing gene editing ethics, but modifies its standard neutral approach to present strongly advocated opposing positions")


# Compatibility tests

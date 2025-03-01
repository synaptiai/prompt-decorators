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


# Tests for StepByStep decorator

# Parameter validation tests

def test_stepbystep_numbered_boolean_validation():
    """Test boolean validation for numbered parameter."""
    # Test true value
    validate_decorator_in_prompt("+++StepByStep(numbered=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++StepByStep(numbered=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++StepByStep(numbered=not_boolean)\nTest prompt.")


# Example-based tests

def test_stepbystep_numbered_steps_for_a_technical_process():
    """Test StepByStep with example: Numbered steps for a technical process"""
    response = llm_client.generate("+++StepByStep(numbered=true)\nHow do I set up a Python virtual environment?")
    
    # Check if response meets expectations
    check_expectation(response, "contains_numbered_steps")


def test_stepbystep_bullet_point_steps_for_a_creative_process():
    """Test StepByStep with example: Bullet-point steps for a creative process"""
    response = llm_client.generate("+++StepByStep(numbered=false)\nHow do I brainstorm effectively?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers bullet-pointed steps for conducting a brainstorming session")


# Compatibility tests

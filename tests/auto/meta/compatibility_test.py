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


# Tests for Compatibility decorator

# Parameter validation tests

def test_compatibility_models_required():
    """Test that models is required for Compatibility decorator."""
    prompt = "+++Compatibility\nTest prompt."
    with pytest.raises(ValidationError, match="models"):
        validate_decorator_in_prompt(prompt)


# Example-based tests

def test_compatibility_basic_model_specific_adaptation():
    """Test Compatibility with example: Basic model-specific adaptation"""
    response = llm_client.generate("+++Compatibility(models=[gpt-4], fallback=StepByStep)\n+++TreeOfThought(branches=3, depth=3)\nSolve this complex optimization problem.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="If using GPT-4, applies the TreeOfThought decorator with full functionality; if using any other model, falls back to the simpler StepByStep decorator")


def test_compatibility_detailed_model_specific_behavior_adaptations():
    """Test Compatibility with example: Detailed model-specific behavior adaptations"""
    response = llm_client.generate("+++Compatibility(models=[gpt-4,gpt-3.5-turbo], behaviors={\"gpt-4\":\"use full mathematical notation and derivations\", \"gpt-3.5-turbo\":\"use simplified equations and more intuitive explanations\"})\n+++Academic(style=scientific)\nExplain quantum field theory.")
    
    # Check if response meets expectations
    check_expectation(response, "has_formal_language")


# Compatibility tests

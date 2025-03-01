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


# Tests for Uncertainty decorator

# Parameter validation tests

def test_uncertainty_format_enum_values():
    """Test that format accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Uncertainty(format=inline)\nTest prompt."); validate_decorator_in_prompt("+++Uncertainty(format=section)\nTest prompt."); validate_decorator_in_prompt("+++Uncertainty(format=confidence)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Uncertainty(format=invalid_value)\nTest prompt.")


def test_uncertainty_threshold_enum_values():
    """Test that threshold accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Uncertainty(threshold=low)\nTest prompt."); validate_decorator_in_prompt("+++Uncertainty(threshold=medium)\nTest prompt."); validate_decorator_in_prompt("+++Uncertainty(threshold=high)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Uncertainty(threshold=invalid_value)\nTest prompt.")


def test_uncertainty_reason_boolean_validation():
    """Test boolean validation for reason parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Uncertainty(reason=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Uncertainty(reason=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Uncertainty(reason=not_boolean)\nTest prompt.")


# Example-based tests

def test_uncertainty_inline_uncertainty_markers_in_a_technical_explanation():
    """Test Uncertainty with example: Inline uncertainty markers in a technical explanation"""
    response = llm_client.generate("+++Uncertainty\nExplain the potential timeline for achieving artificial general intelligence.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Explains AGI timelines with inline uncertainty markers highlighting speculative predictions, areas of expert disagreement, and knowledge gaps")


def test_uncertainty_dedicated_uncertainty_section_with_detailed_reasoning():
    """Test Uncertainty with example: Dedicated uncertainty section with detailed reasoning"""
    response = llm_client.generate("+++Uncertainty(format=section, reason=true, threshold=low)\nWhat are the environmental impacts of fusion energy?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides information about fusion energy's environmental impacts followed by a dedicated section discussing all points of uncertainty with explanations for why each point is uncertain")


# Compatibility tests

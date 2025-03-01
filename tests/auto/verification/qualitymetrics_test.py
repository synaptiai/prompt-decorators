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


# Tests for QualityMetrics decorator

# Parameter validation tests

def test_qualitymetrics_scale_enum_values():
    """Test that scale accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++QualityMetrics(scale=1-5)\nTest prompt."); validate_decorator_in_prompt("+++QualityMetrics(scale=1-10)\nTest prompt."); validate_decorator_in_prompt("+++QualityMetrics(scale=percentage)\nTest prompt."); validate_decorator_in_prompt("+++QualityMetrics(scale=qualitative)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++QualityMetrics(scale=invalid_value)\nTest prompt.")


def test_qualitymetrics_explanation_boolean_validation():
    """Test boolean validation for explanation parameter."""
    # Test true value
    validate_decorator_in_prompt("+++QualityMetrics(explanation=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++QualityMetrics(explanation=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++QualityMetrics(explanation=not_boolean)\nTest prompt.")


# Example-based tests

def test_qualitymetrics_basic_quality_assessment_of_an_analysis():
    """Test QualityMetrics with example: Basic quality assessment of an analysis"""
    response = llm_client.generate("+++QualityMetrics\nMy analysis of the financial market trends is as follows...")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides the analysis of financial market trends, followed by 1-5 ratings across standard quality metrics with explanations for each score")


def test_qualitymetrics_specific_custom_metrics_with_detailed_qualitative_assessment():
    """Test QualityMetrics with example: Specific custom metrics with detailed qualitative assessment"""
    response = llm_client.generate("+++QualityMetrics(metrics=[factual accuracy,predictive value,consideration of alternatives,logical flow], scale=qualitative, explanation=true)\nHere's my policy proposal for urban housing...")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers the policy proposal, followed by qualitative assessments (poor/fair/good/excellent) of the four specified metrics, with detailed explanations for each evaluation")


# Compatibility tests

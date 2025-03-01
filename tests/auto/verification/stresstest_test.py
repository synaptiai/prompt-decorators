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


# Tests for StressTest decorator

# Parameter validation tests

def test_stresstest_scenarios_number_validation():
    """Test number validation for scenarios parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++StressTest(scenarios=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++StressTest(scenarios=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++StressTest(scenarios=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++StressTest(scenarios=6)\nTest prompt.")
    

def test_stresstest_severity_enum_values():
    """Test that severity accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++StressTest(severity=moderate)\nTest prompt."); validate_decorator_in_prompt("+++StressTest(severity=severe)\nTest prompt."); validate_decorator_in_prompt("+++StressTest(severity=extreme)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++StressTest(severity=invalid_value)\nTest prompt.")


# Example-based tests

def test_stresstest_basic_stress_test_of_a_business_model():
    """Test StressTest with example: Basic stress test of a business model"""
    response = llm_client.generate("+++StressTest\nEvaluate this subscription-based SaaS business model.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an analysis of the business model followed by three severe stress test scenarios that challenge its core assumptions and viability")


def test_stresstest_extreme_stress_test_focused_on_a_specific_domain():
    """Test StressTest with example: Extreme stress test focused on a specific domain"""
    response = llm_client.generate("+++StressTest(scenarios=5, severity=extreme, domain=security)\nAssess our new authentication protocol design.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers an assessment of the authentication protocol followed by five extreme security-focused stress test scenarios that identify potential vulnerabilities and breaking points")


# Compatibility tests

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


# Tests for RootCause decorator

# Parameter validation tests

def test_rootcause_method_enum_values():
    """Test that method accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++RootCause(method=5whys)\nTest prompt."); validate_decorator_in_prompt("+++RootCause(method=fishbone)\nTest prompt."); validate_decorator_in_prompt("+++RootCause(method=pareto)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++RootCause(method=invalid_value)\nTest prompt.")


def test_rootcause_depth_number_validation():
    """Test number validation for depth parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++RootCause(depth=3)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++RootCause(depth=2)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++RootCause(depth=7)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++RootCause(depth=8)\nTest prompt.")
    

# Example-based tests

def test_rootcause_basic_5_whys_analysis_of_a_business_problem():
    """Test RootCause with example: Basic 5 Whys analysis of a business problem"""
    response = llm_client.generate("+++RootCause\nWhy is our website's bounce rate increasing?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Performs a systematic 5 Whys analysis to trace the increasing bounce rate back to its fundamental causes")


def test_rootcause_fishbone_diagram_approach_to_a_technical_issue():
    """Test RootCause with example: Fishbone diagram approach to a technical issue"""
    response = llm_client.generate("+++RootCause(method=fishbone)\nWhy do our application servers crash under moderate load?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Analyzes the server crashes using the fishbone (Ishikawa) methodology, categorizing potential causes into major categories like People, Process, Equipment, etc.")


def test_rootcause_pareto_analysis_with_deeper_investigation():
    """Test RootCause with example: Pareto analysis with deeper investigation"""
    response = llm_client.generate("+++RootCause(method=pareto, depth=7)\nWhat factors are causing our manufacturing defects?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Uses Pareto principle to identify the vital few causes responsible for most manufacturing defects, with an exceptionally thorough analysis")


# Compatibility tests

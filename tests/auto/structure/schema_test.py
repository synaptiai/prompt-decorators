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


# Tests for Schema decorator

# Parameter validation tests

def test_schema_schema_required():
    """Test that schema is required for Schema decorator."""
    prompt = "+++Schema\nTest prompt."
    with pytest.raises(ValidationError, match="schema"):
        validate_decorator_in_prompt(prompt)


def test_schema_strict_boolean_validation():
    """Test boolean validation for strict parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Schema(strict=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Schema(strict=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Schema(strict=not_boolean)\nTest prompt.")


# Example-based tests

def test_schema_basic_schema_for_a_person_s_information():
    """Test Schema with example: Basic schema for a person's information"""
    response = llm_client.generate("+++Schema(schema={\"type\":\"object\",\"properties\":{\"name\":{\"type\":\"string\"},\"age\":{\"type\":\"number\"},\"interests\":{\"type\":\"array\",\"items\":{\"type\":\"string\"}}}})\nDescribe a fictional character.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Returns information about a fictional character structured according to the specified schema with name, age, and interests")


def test_schema_strict_schema_for_product_information():
    """Test Schema with example: Strict schema for product information"""
    response = llm_client.generate("+++Schema(schema={\"type\":\"object\",\"required\":[\"productName\",\"price\",\"features\"],\"properties\":{\"productName\":{\"type\":\"string\"},\"price\":{\"type\":\"number\"},\"features\":{\"type\":\"array\"},\"availability\":{\"type\":\"boolean\"}}}, strict=true)\nDescribe a smartphone.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Returns smartphone information strictly following the specified schema with all required fields and proper data types")


# Compatibility tests

def test_schema_conflicts():
    """Test that Schema has expected conflicts."""
    conflicts = ["OutputFormat"]
    for conflict in conflicts:
        result = combine_decorators(["Schema", conflict])
        assert not result["compatible"], f"Schema should conflict with {conflict}"

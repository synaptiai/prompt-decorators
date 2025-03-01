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


# Tests for TableFormat decorator

# Parameter validation tests

def test_tableformat_columns_required():
    """Test that columns is required for TableFormat decorator."""
    prompt = "+++TableFormat\nTest prompt."
    with pytest.raises(ValidationError, match="columns"):
        validate_decorator_in_prompt(prompt)


def test_tableformat_format_enum_values():
    """Test that format accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++TableFormat(format=markdown)\nTest prompt."); validate_decorator_in_prompt("+++TableFormat(format=ascii)\nTest prompt."); validate_decorator_in_prompt("+++TableFormat(format=csv)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++TableFormat(format=invalid_value)\nTest prompt.")


def test_tableformat_alignment_enum_values():
    """Test that alignment accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++TableFormat(alignment=left)\nTest prompt."); validate_decorator_in_prompt("+++TableFormat(alignment=center)\nTest prompt."); validate_decorator_in_prompt("+++TableFormat(alignment=right)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++TableFormat(alignment=invalid_value)\nTest prompt.")


# Example-based tests

def test_tableformat_simple_comparison_table_in_markdown_format():
    """Test TableFormat with example: Simple comparison table in markdown format"""
    response = llm_client.generate("+++TableFormat(columns=[Feature, TypeScript, JavaScript])\nCompare TypeScript and JavaScript features.")
    
    # Check if response meets expectations
    check_expectation(response, "contains_table")
    check_expectation(response, "is_valid_markdown")
    check_expectation(response, "contains_comparison")


def test_tableformat_detailed_csv_table_with_specific_columns():
    """Test TableFormat with example: Detailed CSV table with specific columns"""
    response = llm_client.generate("+++TableFormat(columns=[Planet, Diameter, Distance from Sun, Orbital Period, Number of Moons], format=csv)\nList the planets in our solar system with their key characteristics.")
    
    # Check if response meets expectations
    check_expectation(response, "contains_table")


# Compatibility tests

def test_tableformat_conflicts():
    """Test that TableFormat has expected conflicts."""
    conflicts = ["OutputFormat"]
    for conflict in conflicts:
        result = combine_decorators(["TableFormat", conflict])
        assert not result["compatible"], f"TableFormat should conflict with {conflict}"

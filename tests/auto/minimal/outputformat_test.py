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


# Tests for OutputFormat decorator

# Parameter validation tests

def test_outputformat_format_required():
    """Test that format is required for OutputFormat decorator."""
    prompt = "+++OutputFormat\nTest prompt."
    with pytest.raises(ValidationError, match="format"):
        validate_decorator_in_prompt(prompt)


def test_outputformat_format_enum_values():
    """Test that format accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++OutputFormat(format=json)\nTest prompt."); validate_decorator_in_prompt("+++OutputFormat(format=markdown)\nTest prompt."); validate_decorator_in_prompt("+++OutputFormat(format=yaml)\nTest prompt."); validate_decorator_in_prompt("+++OutputFormat(format=xml)\nTest prompt."); validate_decorator_in_prompt("+++OutputFormat(format=plaintext)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++OutputFormat(format=invalid_value)\nTest prompt.")


# Example-based tests

def test_outputformat_json_output_for_structured_data():
    """Test OutputFormat with example: JSON output for structured data"""
    response = llm_client.generate("+++OutputFormat(format=json)\nList the top 5 programming languages and their key features.")
    
    # Check if response meets expectations
    check_expectation(response, "is_valid_json")


def test_outputformat_markdown_output_for_formatted_text():
    """Test OutputFormat with example: Markdown output for formatted text"""
    response = llm_client.generate("+++OutputFormat(format=markdown)\nWrite a tutorial on setting up a React project.")
    
    # Check if response meets expectations
    check_expectation(response, "is_valid_markdown")


# Compatibility tests

def test_outputformat_conflicts():
    """Test that OutputFormat has expected conflicts."""
    conflicts = ["Schema", "TableFormat", "Bullet"]
    for conflict in conflicts:
        result = combine_decorators(["OutputFormat", conflict])
        assert not result["compatible"], f"OutputFormat should conflict with {conflict}"

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


# Tests for Version decorator

# Parameter validation tests

def test_version_standard_required():
    """Test that standard is required for Version decorator."""
    prompt = "+++Version\nTest prompt."
    with pytest.raises(ValidationError, match="standard"):
        validate_decorator_in_prompt(prompt)


# Example-based tests

def test_version_specify_standard_version_for_compatibility():
    """Test Version with example: Specify standard version for compatibility"""
    response = llm_client.generate("+++Version(standard=1.0.0)\n+++Reasoning(depth=comprehensive)\nExplain quantum entanglement")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Ensures decorators are interpreted according to version 1.0.0 of the standard")


# Compatibility tests

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


# Tests for Extension decorator

# Parameter validation tests

def test_extension_source_required():
    """Test that source is required for Extension decorator."""
    prompt = "+++Extension\nTest prompt."
    with pytest.raises(ValidationError, match="source"):
        validate_decorator_in_prompt(prompt)


# Example-based tests

def test_extension_basic_loading_of_an_extension_package():
    """Test Extension with example: Basic loading of an extension package"""
    response = llm_client.generate("+++Extension(source=https://decorator-registry.ai/scientific-pack.json)\n+++ScientificReasoning(discipline=physics)\nExplain dark matter.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Loads decorators from the scientific-pack extension and then applies the ScientificReasoning decorator (defined in that pack) with physics discipline to explain dark matter")


def test_extension_loading_specific_decorators_from_a_versioned_extension():
    """Test Extension with example: Loading specific decorators from a versioned extension"""
    response = llm_client.generate("+++Extension(source=medical-decorators, version=2.1.0, decorators=[ClinicalCase,EvidenceBased])\n+++ClinicalCase(format=SOAP)\nDescribe the treatment approach for Type 2 diabetes.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Loads only the ClinicalCase and EvidenceBased decorators from version 2.1.0 of the medical-decorators package, then applies the ClinicalCase decorator with SOAP format to describe diabetes treatment")


# Compatibility tests

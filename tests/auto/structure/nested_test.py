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


# Tests for Nested decorator

# Parameter validation tests

def test_nested_depth_number_validation():
    """Test number validation for depth parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++Nested(depth=2)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Nested(depth=1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++Nested(depth=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Nested(depth=6)\nTest prompt.")
    

def test_nested_style_enum_values():
    """Test that style accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Nested(style=bullet)\nTest prompt."); validate_decorator_in_prompt("+++Nested(style=numbered)\nTest prompt."); validate_decorator_in_prompt("+++Nested(style=mixed)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Nested(style=invalid_value)\nTest prompt.")


def test_nested_collapsible_boolean_validation():
    """Test boolean validation for collapsible parameter."""
    # Test true value
    validate_decorator_in_prompt("+++Nested(collapsible=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++Nested(collapsible=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Nested(collapsible=not_boolean)\nTest prompt.")


# Example-based tests

def test_nested_deep_hierarchical_organization_of_a_complex_domain():
    """Test Nested with example: Deep hierarchical organization of a complex domain"""
    response = llm_client.generate("+++Nested\nExplain the classification of living organisms.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Presents taxonomy in a nested hierarchy with domains, kingdoms, phyla, etc., using mixed notation styles for different levels")


def test_nested_maximum_depth_collapsible_structure_for_reference_material():
    """Test Nested with example: Maximum depth collapsible structure for reference material"""
    response = llm_client.generate("+++Nested(depth=5, style=bullet, collapsible=true)\nProvide a comprehensive overview of programming paradigms.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Creates a 5-level deep bullet-point hierarchy of programming paradigms, designed to be rendered as collapsible sections")


# Compatibility tests

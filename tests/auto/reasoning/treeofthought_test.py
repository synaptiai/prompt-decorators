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


# Tests for TreeOfThought decorator

# Parameter validation tests

def test_treeofthought_branches_number_validation():
    """Test number validation for branches parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++TreeOfThought(branches=2)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++TreeOfThought(branches=1)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++TreeOfThought(branches=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++TreeOfThought(branches=6)\nTest prompt.")
    

def test_treeofthought_depth_number_validation():
    """Test number validation for depth parameter."""
    
    # Valid minimum value
    validate_decorator_in_prompt("+++TreeOfThought(depth=1)\nTest prompt.")
    
    # Invalid below minimum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++TreeOfThought(depth=0)\nTest prompt.")
    
    # Valid maximum value
    validate_decorator_in_prompt("+++TreeOfThought(depth=5)\nTest prompt.")
    
    # Invalid above maximum
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++TreeOfThought(depth=6)\nTest prompt.")
    

def test_treeofthought_pruning_boolean_validation():
    """Test boolean validation for pruning parameter."""
    # Test true value
    validate_decorator_in_prompt("+++TreeOfThought(pruning=true)\nTest prompt.")
    
    # Test false value
    validate_decorator_in_prompt("+++TreeOfThought(pruning=false)\nTest prompt.")
    
    # Test invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++TreeOfThought(pruning=not_boolean)\nTest prompt.")


# Example-based tests

def test_treeofthought_multi_branch_problem_solving_for_a_complex_question():
    """Test TreeOfThought with example: Multi-branch problem solving for a complex question"""
    response = llm_client.generate("+++TreeOfThought\nWhat might explain the Fermi Paradox?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Explores three different reasoning branches about potential explanations for the Fermi Paradox, developing each path to moderate depth")


def test_treeofthought_deep__focused_exploration_with_pruning():
    """Test TreeOfThought with example: Deep, focused exploration with pruning"""
    response = llm_client.generate("+++TreeOfThought(branches=5, depth=5, pruning=true)\nHow might we solve the climate change crisis?")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Starts with five different approaches to climate change, explores each in depth, and eliminates less promising branches to focus on the most viable solutions")


# Compatibility tests

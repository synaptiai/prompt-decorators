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


# Tests for PeerReview decorator

# Parameter validation tests

def test_peerreview_criteria_enum_values():
    """Test that criteria accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++PeerReview(criteria=accuracy)\nTest prompt."); validate_decorator_in_prompt("+++PeerReview(criteria=methodology)\nTest prompt."); validate_decorator_in_prompt("+++PeerReview(criteria=limitations)\nTest prompt."); validate_decorator_in_prompt("+++PeerReview(criteria=completeness)\nTest prompt."); validate_decorator_in_prompt("+++PeerReview(criteria=all)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++PeerReview(criteria=invalid_value)\nTest prompt.")


def test_peerreview_style_enum_values():
    """Test that style accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++PeerReview(style=constructive)\nTest prompt."); validate_decorator_in_prompt("+++PeerReview(style=critical)\nTest prompt."); validate_decorator_in_prompt("+++PeerReview(style=balanced)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++PeerReview(style=invalid_value)\nTest prompt.")


def test_peerreview_position_enum_values():
    """Test that position accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++PeerReview(position=after)\nTest prompt."); validate_decorator_in_prompt("+++PeerReview(position=before)\nTest prompt."); validate_decorator_in_prompt("+++PeerReview(position=alongside)\nTest prompt.")
    
    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++PeerReview(position=invalid_value)\nTest prompt.")


# Example-based tests

def test_peerreview_basic_peer_review_of_content_accuracy():
    """Test PeerReview with example: Basic peer review of content accuracy"""
    response = llm_client.generate("+++PeerReview(criteria=accuracy)\nExplain the current understanding of dark matter in astrophysics.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Provides an explanation of dark matter, followed by a balanced peer review focusing on the accuracy of the information presented")


def test_peerreview_critical_peer_review_of_multiple_aspects__shown_alongside_content():
    """Test PeerReview with example: Critical peer review of multiple aspects, shown alongside content"""
    response = llm_client.generate("+++PeerReview(criteria=all, style=critical, position=alongside)\nAnalyze the methodology used in Stanford's prison experiment.")
    
    # Check if response meets expectations
    check_expectation(response, "matches_description", description="Delivers an analysis of the Stanford prison experiment methodology with a parallel critical peer review addressing accuracy, methodology, limitations, and completeness")


# Compatibility tests

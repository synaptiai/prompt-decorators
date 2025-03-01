"""
Tests for the decorator classes.
"""

import pytest
from prompt_decorators_core.decorators import (
    Reasoning,
    ReasoningDepth,
    StepByStep,
    OutputFormat,
    OutputFormatType,
    Tone,
    ToneStyle,
    Version,
)


def test_reasoning_decorator():
    """Test the Reasoning decorator."""
    # Test with default parameters
    decorator = Reasoning()
    assert decorator.name == "Reasoning"
    assert decorator.version == "1.0.0"
    assert decorator.parameters == {"depth": ReasoningDepth.MODERATE}
    assert decorator.metadata == {"category": "core"}
    
    # Test with custom parameters
    decorator = Reasoning(depth=ReasoningDepth.COMPREHENSIVE)
    assert decorator.parameters == {"depth": ReasoningDepth.COMPREHENSIVE}
    
    # Test to_dict method
    decorator_dict = decorator.to_dict()
    assert decorator_dict["name"] == "Reasoning"
    assert decorator_dict["version"] == "1.0.0"
    assert decorator_dict["parameters"]["depth"] == ReasoningDepth.COMPREHENSIVE
    
    # Test to_string method
    decorator_str = decorator.to_string()
    assert decorator_str == '+++Reasoning(depth="comprehensive")'


def test_step_by_step_decorator():
    """Test the StepByStep decorator."""
    # Test with default parameters
    decorator = StepByStep()
    assert decorator.name == "StepByStep"
    assert decorator.parameters == {"numbered": True}
    
    # Test with custom parameters
    decorator = StepByStep(numbered=False)
    assert decorator.parameters == {"numbered": False}
    
    # Test to_string method
    decorator_str = decorator.to_string()
    assert decorator_str == "+++StepByStep(numbered=false)"


def test_output_format_decorator():
    """Test the OutputFormat decorator."""
    # Test with default parameters
    decorator = OutputFormat()
    assert decorator.name == "OutputFormat"
    assert decorator.parameters == {"format": OutputFormatType.PLAINTEXT}
    
    # Test with custom parameters
    decorator = OutputFormat(format=OutputFormatType.MARKDOWN)
    assert decorator.parameters == {"format": OutputFormatType.MARKDOWN}
    
    # Test to_string method
    decorator_str = decorator.to_string()
    assert decorator_str == '+++OutputFormat(format="markdown")'


def test_tone_decorator():
    """Test the Tone decorator."""
    # Test with default parameters
    decorator = Tone()
    assert decorator.name == "Tone"
    assert decorator.parameters == {"style": ToneStyle.FORMAL}
    
    # Test with custom parameters
    decorator = Tone(style=ToneStyle.TECHNICAL)
    assert decorator.parameters == {"style": ToneStyle.TECHNICAL}
    
    # Test to_string method
    decorator_str = decorator.to_string()
    assert decorator_str == '+++Tone(style="technical")'


def test_version_decorator():
    """Test the Version decorator."""
    # Test with default parameters
    decorator = Version()
    assert decorator.name == "Version"
    assert decorator.parameters == {"standard": "1.0.0"}
    
    # Test with custom parameters
    decorator = Version(standard="1.1.0")
    assert decorator.parameters == {"standard": "1.1.0"}
    
    # Test to_string method
    decorator_str = decorator.to_string()
    assert decorator_str == '+++Version(standard="1.1.0")' 
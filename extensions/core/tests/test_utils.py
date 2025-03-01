"""
Tests for the utility functions.
"""

import pytest
from prompt_decorators_core.utils import (
    format_parameter_value,
    parse_decorated_prompt,
    generate_system_instructions,
)
from prompt_decorators_core.decorators import (
    ReasoningDepth,
    OutputFormatType,
    ToneStyle,
)


def test_format_parameter_value():
    """Test format_parameter_value function."""
    # Test with boolean values
    assert format_parameter_value(True) == "true"
    assert format_parameter_value(False) == "false"
    
    # Test with enum values
    assert format_parameter_value(ReasoningDepth.BASIC) == '"basic"'
    assert format_parameter_value(OutputFormatType.MARKDOWN) == '"markdown"'
    assert format_parameter_value(ToneStyle.TECHNICAL) == '"technical"'
    
    # Test with string values
    assert format_parameter_value("test") == '"test"'
    assert format_parameter_value("") == '""'
    
    # Test with numeric values
    assert format_parameter_value(42) == "42"
    assert format_parameter_value(3.14) == "3.14"


def test_parse_decorated_prompt():
    """Test parse_decorated_prompt function."""
    # Test with a simple decorated prompt
    decorated_prompt = '+++Version(standard="1.0.0")Test prompt'
    decorators, prompt = parse_decorated_prompt(decorated_prompt)
    
    assert len(decorators) == 1
    assert decorators[0]["name"] == "Version"
    assert decorators[0]["parameters"]["standard"] == "1.0.0"
    assert prompt == "Test prompt"
    
    # Test with multiple decorators
    decorated_prompt = (
        '+++Version(standard="1.0.0")'
        '+++Reasoning(depth="comprehensive")'
        '+++StepByStep(numbered=true)'
        'Test prompt'
    )
    decorators, prompt = parse_decorated_prompt(decorated_prompt)
    
    assert len(decorators) == 3
    assert decorators[0]["name"] == "Version"
    assert decorators[1]["name"] == "Reasoning"
    assert decorators[2]["name"] == "StepByStep"
    assert decorators[1]["parameters"]["depth"] == "comprehensive"
    assert decorators[2]["parameters"]["numbered"] is True
    assert prompt == "Test prompt"
    
    # Test with no decorators
    decorated_prompt = "Test prompt"
    decorators, prompt = parse_decorated_prompt(decorated_prompt)
    
    assert len(decorators) == 0
    assert prompt == "Test prompt"
    
    # Test with empty parameters
    decorated_prompt = '+++Version()Test prompt'
    decorators, prompt = parse_decorated_prompt(decorated_prompt)
    
    assert len(decorators) == 1
    assert decorators[0]["name"] == "Version"
    assert decorators[0]["parameters"] == {}
    assert prompt == "Test prompt"


def test_generate_system_instructions():
    """Test generate_system_instructions function."""
    # Test with Reasoning decorator
    decorators = [
        {
            "name": "Reasoning",
            "version": "1.0.0",
            "parameters": {"depth": "basic"},
            "metadata": {"category": "core"}
        }
    ]
    instructions = generate_system_instructions(decorators)
    assert "basic reasoning" in instructions.lower()
    
    # Test with StepByStep decorator
    decorators = [
        {
            "name": "StepByStep",
            "version": "1.0.0",
            "parameters": {"numbered": True},
            "metadata": {"category": "core"}
        }
    ]
    instructions = generate_system_instructions(decorators)
    assert "numbered steps" in instructions.lower()
    
    # Test with OutputFormat decorator
    decorators = [
        {
            "name": "OutputFormat",
            "version": "1.0.0",
            "parameters": {"format": "markdown"},
            "metadata": {"category": "core"}
        }
    ]
    instructions = generate_system_instructions(decorators)
    assert "markdown" in instructions.lower()
    
    # Test with Tone decorator
    decorators = [
        {
            "name": "Tone",
            "version": "1.0.0",
            "parameters": {"style": "technical"},
            "metadata": {"category": "core"}
        }
    ]
    instructions = generate_system_instructions(decorators)
    assert "technical" in instructions.lower()
    
    # Test with multiple decorators
    decorators = [
        {
            "name": "Reasoning",
            "version": "1.0.0",
            "parameters": {"depth": "comprehensive"},
            "metadata": {"category": "core"}
        },
        {
            "name": "StepByStep",
            "version": "1.0.0",
            "parameters": {"numbered": True},
            "metadata": {"category": "core"}
        },
        {
            "name": "OutputFormat",
            "version": "1.0.0",
            "parameters": {"format": "markdown"},
            "metadata": {"category": "core"}
        },
        {
            "name": "Tone",
            "version": "1.0.0",
            "parameters": {"style": "technical"},
            "metadata": {"category": "core"}
        }
    ]
    instructions = generate_system_instructions(decorators)
    assert "comprehensive reasoning" in instructions.lower()
    assert "numbered steps" in instructions.lower()
    assert "markdown" in instructions.lower()
    assert "technical" in instructions.lower() 
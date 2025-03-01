"""
Tests for the API request class.
"""

import json
import pytest
from prompt_decorators_core.api import APIRequest
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


def test_api_request_init():
    """Test APIRequest initialization."""
    # Test with minimal parameters
    request = APIRequest(
        model="gpt-4",
        prompt="Test prompt",
    )
    assert request.model == "gpt-4"
    assert request.prompt == "Test prompt"
    assert request.decorators == []
    assert request.temperature == 0.7
    assert request.max_tokens is None
    
    # Test with all parameters
    decorators = [
        Reasoning(depth=ReasoningDepth.COMPREHENSIVE),
        StepByStep(numbered=True),
    ]
    request = APIRequest(
        model="gpt-4",
        prompt="Test prompt",
        decorators=decorators,
        temperature=0.5,
        max_tokens=100,
    )
    assert request.model == "gpt-4"
    assert request.prompt == "Test prompt"
    assert request.decorators == decorators
    assert request.temperature == 0.5
    assert request.max_tokens == 100


def test_api_request_to_dict():
    """Test APIRequest to_dict method."""
    decorators = [
        Reasoning(depth=ReasoningDepth.COMPREHENSIVE),
        StepByStep(numbered=True),
    ]
    request = APIRequest(
        model="gpt-4",
        prompt="Test prompt",
        decorators=decorators,
        temperature=0.5,
        max_tokens=100,
    )
    
    request_dict = request.to_dict()
    assert request_dict["model"] == "gpt-4"
    assert request_dict["prompt"] == "Test prompt"
    assert request_dict["temperature"] == 0.5
    assert request_dict["max_tokens"] == 100
    assert len(request_dict["decorators"]) == 2
    assert request_dict["decorators"][0]["name"] == "Reasoning"
    assert request_dict["decorators"][1]["name"] == "StepByStep"


def test_api_request_to_json():
    """Test APIRequest to_json method."""
    decorators = [
        Reasoning(depth=ReasoningDepth.COMPREHENSIVE),
        StepByStep(numbered=True),
    ]
    request = APIRequest(
        model="gpt-4",
        prompt="Test prompt",
        decorators=decorators,
    )
    
    request_json = request.to_json()
    request_dict = json.loads(request_json)
    assert request_dict["model"] == "gpt-4"
    assert request_dict["prompt"] == "Test prompt"
    assert len(request_dict["decorators"]) == 2


def test_api_request_get_system_instructions():
    """Test APIRequest get_system_instructions method."""
    decorators = [
        Reasoning(depth=ReasoningDepth.COMPREHENSIVE),
        StepByStep(numbered=True),
        OutputFormat(format=OutputFormatType.MARKDOWN),
        Tone(style=ToneStyle.TECHNICAL),
    ]
    request = APIRequest(
        model="gpt-4",
        prompt="Test prompt",
        decorators=decorators,
    )
    
    instructions = request.get_system_instructions()
    assert "comprehensive reasoning" in instructions.lower()
    assert "numbered steps" in instructions.lower()
    assert "markdown" in instructions.lower()
    assert "technical" in instructions.lower()


def test_api_request_get_decorated_prompt():
    """Test APIRequest get_decorated_prompt method."""
    decorators = [
        Version(standard="1.0.0"),
        Reasoning(depth=ReasoningDepth.COMPREHENSIVE),
        StepByStep(numbered=True),
    ]
    request = APIRequest(
        model="gpt-4",
        prompt="Test prompt",
        decorators=decorators,
    )
    
    decorated_prompt = request.get_decorated_prompt()
    assert '+++Version(standard="1.0.0")' in decorated_prompt
    assert '+++Reasoning(depth="comprehensive")' in decorated_prompt
    assert "+++StepByStep(numbered=true)" in decorated_prompt
    assert decorated_prompt.endswith("Test prompt")


def test_api_request_from_decorated_prompt():
    """Test APIRequest from_decorated_prompt method."""
    decorated_prompt = (
        '+++Version(standard="1.0.0")'
        '+++Reasoning(depth="comprehensive")'
        '+++StepByStep(numbered=true)'
        '+++OutputFormat(format="markdown")'
        '+++Tone(style="technical")'
        'Explain how nuclear fusion works.'
    )
    
    request = APIRequest.from_decorated_prompt(
        model="gpt-4",
        decorated_prompt=decorated_prompt,
    )
    
    assert request.model == "gpt-4"
    assert request.prompt == "Explain how nuclear fusion works."
    assert hasattr(request, "_parsed_decorators")
    assert len(request._parsed_decorators) == 5
    
    # Check that the decorators were parsed correctly
    names = [d["name"] for d in request._parsed_decorators]
    assert "Version" in names
    assert "Reasoning" in names
    assert "StepByStep" in names
    assert "OutputFormat" in names
    assert "Tone" in names
    
    # Check parameters
    for decorator in request._parsed_decorators:
        if decorator["name"] == "Reasoning":
            assert decorator["parameters"]["depth"] == "comprehensive"
        elif decorator["name"] == "StepByStep":
            assert decorator["parameters"]["numbered"] is True
        elif decorator["name"] == "OutputFormat":
            assert decorator["parameters"]["format"] == "markdown"
        elif decorator["name"] == "Tone":
            assert decorator["parameters"]["style"] == "technical"
        elif decorator["name"] == "Version":
            assert decorator["parameters"]["standard"] == "1.0.0" 
"""Tests for the Prompt Decorators implementation."""

import pytest
from pathlib import Path

from prompt_decorators.models import (
    APIRequest,
    ReasoningDecorator,
    StepByStepDecorator,
    OutputFormatDecorator,
    ToneDecorator,
    VersionDecorator,
    OutputFormat,
    ToneStyle,
)
from prompt_decorators.validator import DecoratorValidator


@pytest.fixture
def schemas_dir() -> Path:
    """Return path to schemas directory."""
    return Path(__file__).parent.parent.parent.parent / "schemas"


@pytest.fixture
def validator(schemas_dir: Path) -> DecoratorValidator:
    """Return initialized validator."""
    return DecoratorValidator(schemas_dir)


def test_reasoning_decorator():
    """Test ReasoningDecorator validation."""
    # Test valid decorator
    decorator = ReasoningDecorator(
        version="1.0.0",
        parameters={"depth": "comprehensive"}
    )
    assert decorator.name == "Reasoning"
    assert decorator.parameters["depth"] == "comprehensive"

    # Test invalid version format
    with pytest.raises(ValueError):
        ReasoningDecorator(version="1.0")


def test_step_by_step_decorator():
    """Test StepByStepDecorator validation."""
    # Test valid decorator
    decorator = StepByStepDecorator(
        version="1.0.0",
        parameters={"numbered": True}
    )
    assert decorator.name == "StepByStep"
    assert decorator.parameters["numbered"] is True

    # Test default parameters
    decorator = StepByStepDecorator(version="1.0.0")
    assert decorator.parameters["numbered"] is True


def test_output_format_decorator():
    """Test OutputFormatDecorator validation."""
    # Test valid decorator
    decorator = OutputFormatDecorator(
        version="1.0.0",
        parameters={"format": OutputFormat.JSON}
    )
    assert decorator.name == "OutputFormat"
    assert decorator.parameters["format"] == "json"

    # Test missing required parameters
    with pytest.raises(ValueError):
        OutputFormatDecorator(version="1.0.0")


def test_tone_decorator():
    """Test ToneDecorator validation."""
    # Test valid decorator
    decorator = ToneDecorator(
        version="1.0.0",
        parameters={"style": ToneStyle.PROFESSIONAL}
    )
    assert decorator.name == "Tone"
    assert decorator.parameters["style"] == "professional"

    # Test missing required parameters
    with pytest.raises(ValueError):
        ToneDecorator(version="1.0.0")


def test_version_decorator():
    """Test VersionDecorator validation."""
    # Test valid decorator
    decorator = VersionDecorator(
        version="1.0.0",
        parameters={"standard": "1.0.0"}
    )
    assert decorator.name == "Version"
    assert decorator.parameters["standard"] == "1.0.0"

    # Test missing required parameters
    with pytest.raises(ValueError):
        VersionDecorator(version="1.0.0")


def test_api_request_validation(validator: DecoratorValidator):
    """Test APIRequest validation."""
    # Test valid request
    request = APIRequest(
        prompt="Explain how nuclear fusion works",
        decorators=[
            ReasoningDecorator(
                version="1.0.0",
                parameters={"depth": "comprehensive"}
            ),
            StepByStepDecorator(
                version="1.0.0",
                parameters={"numbered": True}
            ),
            OutputFormatDecorator(
                version="1.0.0",
                parameters={"format": OutputFormat.MARKDOWN}
            )
        ],
        metadata={
            "model": "gpt-4",
            "temperature": 0.7
        }
    )
    
    errors = validator.validate_api_request(request)
    assert not errors, f"Validation errors found: {errors}"

    # Test invalid request (missing prompt)
    with pytest.raises(ValueError):
        APIRequest(
            decorators=[],
            metadata={}
        )


def test_decorator_validation(validator: DecoratorValidator):
    """Test individual decorator validation."""
    # Test valid decorator
    decorator = ReasoningDecorator(
        version="1.0.0",
        parameters={"depth": "comprehensive"}
    )
    errors = validator.validate_decorator(decorator)
    assert not errors, f"Validation errors found: {errors}"

    # Test invalid decorator (wrong version format)
    with pytest.raises(ValueError):
        ReasoningDecorator(version="1.0") 
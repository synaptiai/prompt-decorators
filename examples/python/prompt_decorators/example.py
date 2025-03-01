"""Example usage of the Prompt Decorators implementation."""

import json
from pathlib import Path
from typing import List, Optional, Any

from rich import print as rprint
from rich.panel import Panel

from .models import (
    APIRequest,
    ReasoningDecorator,
    StepByStepDecorator,
    OutputFormatDecorator,
    ToneDecorator,
    OutputFormat,
    ToneStyle,
)
from .validator import DecoratorValidator


def format_parameter_value(value: Any) -> str:
    """Format a parameter value for string representation.
    
    Args:
        value: The parameter value to format
        
    Returns:
        Formatted string representation
    """
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (OutputFormat, ToneStyle)):
        return value.value
    return str(value)


def create_example_request() -> APIRequest:
    """Create an example API request with decorators.

    Returns:
        APIRequest: The example request
    """
    return APIRequest(
        prompt="Explain how nuclear fusion works and its potential for clean energy",
        decorators=[
            ReasoningDecorator(
                version="1.0.0",
                parameters={"depth": "comprehensive"},
                metadata={
                    "description": "Provides detailed reasoning process",
                    "category": "reasoning"
                }
            ),
            StepByStepDecorator(
                version="1.0.0",
                parameters={"numbered": True},
                metadata={
                    "description": "Structures response as numbered steps",
                    "category": "output"
                }
            ),
            OutputFormatDecorator(
                version="1.0.0",
                parameters={"format": OutputFormat.MARKDOWN},
                metadata={
                    "description": "Formats output as markdown",
                    "category": "output"
                }
            ),
            ToneDecorator(
                version="1.0.0",
                parameters={"style": ToneStyle.ACADEMIC},
                metadata={
                    "description": "Sets academic tone for response",
                    "category": "tone"
                }
            )
        ],
        metadata={
            "model": "gpt-4",
            "temperature": 0.7,
            "max_tokens": 1000
        }
    )


def validate_and_print_request(
    request: APIRequest,
    validator: Optional[DecoratorValidator] = None
) -> List[str]:
    """Validate and pretty print an API request.

    Args:
        request: The API request to validate and print
        validator: Optional validator instance

    Returns:
        List of validation error messages
    """
    # Pretty print the request
    rprint(Panel.fit(
        json.dumps(request.model_dump(), indent=2),
        title="API Request",
        border_style="blue"
    ))

    # Validate if validator is provided
    errors = []
    if validator:
        errors = validator.validate_api_request(request)
        if errors:
            rprint(Panel.fit(
                "\n".join(errors),
                title="Validation Errors",
                border_style="red"
            ))
        else:
            rprint(Panel.fit(
                "Request validation successful!",
                title="Validation Result",
                border_style="green"
            ))

    return errors


def main() -> None:
    """Run the example script."""
    # Create example request
    request = create_example_request()

    # Initialize validator
    schemas_dir = Path(__file__).parent.parent.parent.parent / "schemas"
    validator = DecoratorValidator(schemas_dir)

    # Validate and print request
    errors = validate_and_print_request(request, validator)

    # Print decorator string format
    decorator_str = "\n".join([
        f"+++{d.name}"
        f"({','.join(f'{k}={format_parameter_value(v)}' for k, v in d.parameters.items())})"
        for d in request.decorators
    ])
    
    rprint(Panel.fit(
        f"{decorator_str}\n\n{request.prompt}",
        title="Decorator String Format",
        border_style="yellow"
    ))


if __name__ == "__main__":
    main() 
"""
Example usage of the Prompt Decorators Core extension package.
"""

import json
from typing import List

from .decorators import (
    Reasoning,
    ReasoningDepth,
    StepByStep,
    OutputFormat,
    OutputFormatType,
    Tone,
    ToneStyle,
    Version,
    BaseDecorator,
)
from .api import APIRequest


def example_with_decorator_objects() -> None:
    """Example using decorator objects."""
    print("\n=== Example with Decorator Objects ===\n")
    
    # Create decorators
    decorators = [
        Version(standard="1.0.0"),
        Reasoning(depth=ReasoningDepth.COMPREHENSIVE),
        StepByStep(numbered=True),
        OutputFormat(format=OutputFormatType.MARKDOWN),
        Tone(style=ToneStyle.TECHNICAL),
    ]
    
    # Create API request
    request = APIRequest(
        model="gpt-4",
        prompt="Explain how nuclear fusion works and its potential as an energy source.",
        decorators=decorators,
        temperature=0.7,
    )
    
    # Print decorated prompt
    print("Decorated Prompt:")
    print(request.get_decorated_prompt())
    print()
    
    # Print JSON representation
    print("JSON Representation:")
    print(request.to_json())
    print()
    
    # Print system instructions
    print("System Instructions:")
    print(request.get_system_instructions())
    print()


def example_with_decorated_prompt() -> None:
    """Example using a decorated prompt string."""
    print("\n=== Example with Decorated Prompt String ===\n")
    
    # Create decorated prompt
    decorated_prompt = (
        '+++Version(standard="1.0.0")'
        '+++Reasoning(depth="comprehensive")'
        '+++StepByStep(numbered=true)'
        '+++OutputFormat(format="markdown")'
        '+++Tone(style="technical")'
        'Explain how nuclear fusion works and its potential as an energy source.'
    )
    
    # Create API request from decorated prompt
    request = APIRequest.from_decorated_prompt(
        model="gpt-4",
        decorated_prompt=decorated_prompt,
        temperature=0.7,
    )
    
    # Print parsed prompt
    print("Parsed Prompt:")
    print(request.prompt)
    print()
    
    # Print parsed decorators
    print("Parsed Decorators:")
    if hasattr(request, "_parsed_decorators"):
        for decorator in request._parsed_decorators:
            print(f"- {decorator['name']}: {decorator['parameters']}")
    print()
    
    # Print system instructions
    print("System Instructions:")
    print(request.get_system_instructions())
    print()
    
    # Print JSON representation
    print("JSON Representation:")
    print(request.to_json())
    print()


def main() -> None:
    """Run the examples."""
    print("Prompt Decorators Core Extension - Examples")
    print("==========================================")
    
    example_with_decorator_objects()
    example_with_decorated_prompt()


if __name__ == "__main__":
    main() 
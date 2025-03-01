#!/usr/bin/env python3
"""
Prompt Decorators Demo

This script demonstrates how to use prompt decorators to modify and enhance prompts.
"""

import json
import sys
import os
from typing import List

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prompt_decorators.decorators import Reasoning, OutputFormat
from prompt_decorators.decorators.reasoning import ReasoningStyle
from prompt_decorators.decorators.format import FormatType
from prompt_decorators.utils import get_compatibility_checker, CompatibilityIssue
from prompt_decorators.core.request import DecoratedRequest


def print_section(title: str):
    """Print a section title."""
    print(f"\n{'=' * 80}")
    print(f"{title.center(80)}")
    print(f"{'=' * 80}\n")


def demonstrate_decorator_creation():
    """Demonstrate creating and using decorators."""
    print_section("Creating and Using Decorators")
    
    # Create a Reasoning decorator
    reasoning = Reasoning(
        style=ReasoningStyle.DETAILED.value,
        show_working=True,
        consider_alternatives=True,
        depth=4
    )
    
    # Display information about the decorator
    print(f"Decorator: {reasoning.name} (v{reasoning.version})")
    print(f"Parameters: {json.dumps(reasoning.parameters, indent=2)}")
    
    # Create an OutputFormat decorator
    output_format = OutputFormat(
        format_type=FormatType.MARKDOWN.value,
        pretty_print=True
    )
    
    # Display information about the decorator
    print(f"\nDecorator: {output_format.name} (v{output_format.version})")
    print(f"Parameters: {json.dumps(output_format.parameters, indent=2)}")


def demonstrate_decorator_validation():
    """Demonstrate decorator parameter validation."""
    print_section("Decorator Parameter Validation")
    
    # Try to create a decorator with invalid parameters
    try:
        reasoning = Reasoning(depth=10)  # Invalid: depth should be 1-5
        print("Created decorator:", reasoning)
    except Exception as e:
        print(f"Validation error (as expected): {e}")
    
    # Try to create a decorator with invalid parameters
    try:
        output_format = OutputFormat(format_type="invalid-format")  # Invalid format type
        print("Created decorator:", output_format)
    except Exception as e:
        print(f"Validation error (as expected): {e}")
    
    # Create with valid parameters
    reasoning = Reasoning(depth=5)  # Valid: depth is within range
    print(f"\nValid decorator: {reasoning}")


def demonstrate_serialization():
    """Demonstrate decorator serialization and deserialization."""
    print_section("Serialization and Deserialization")
    
    # Create a decorator
    reasoning = Reasoning(
        style=ReasoningStyle.SOCRATIC.value,
        consider_alternatives=True
    )
    
    # Serialize to JSON
    json_str = reasoning.to_json(indent=2)
    print(f"Serialized decorator:\n{json_str}")
    
    # Deserialize from JSON
    new_reasoning = Reasoning.from_json(json_str)
    print(f"\nDeserialized decorator: {new_reasoning}")
    print(f"Parameters match: {reasoning.parameters == new_reasoning.parameters}")


def demonstrate_applying_decorators():
    """Demonstrate applying decorators to prompts."""
    print_section("Applying Decorators to Prompts")
    
    # Original prompt
    original_prompt = "Explain the concept of quantum entanglement."
    print(f"Original prompt: {original_prompt}\n")
    
    # Apply Reasoning decorator
    reasoning = Reasoning(style=ReasoningStyle.DETAILED.value)
    modified_prompt1 = reasoning.apply(original_prompt)
    print(f"After Reasoning decorator:\n{modified_prompt1}\n")
    
    # Apply OutputFormat decorator
    output_format = OutputFormat(format_type=FormatType.MARKDOWN.value)
    modified_prompt2 = output_format.apply(modified_prompt1)
    print(f"After OutputFormat decorator:\n{modified_prompt2}")


def demonstrate_compatibility_checking():
    """Demonstrate compatibility checking between decorators."""
    print_section("Decorator Compatibility Checking")
    
    # Get compatibility checker
    checker = get_compatibility_checker()
    
    # Check compatibility between compatible decorators
    reasoning = Reasoning()
    output_format = OutputFormat(format_type=FormatType.MARKDOWN.value)
    
    issues = checker.check_compatibility(reasoning, output_format)
    print(f"Checking compatibility between {reasoning.name} and {output_format.name}:")
    if issues:
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("  No compatibility issues found.")
    
    # Since we don't have a Summary decorator yet, we'll check compatibility using strings
    issues = checker.check_compatibility("Reasoning", "Summary")
    print(f"\nChecking compatibility between Reasoning and Summary:")
    if issues:
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("  No compatibility issues found.")


def demonstrate_decorated_request():
    """Demonstrate using decorated requests."""
    print_section("Using Decorated Requests")
    
    # Create decorators
    reasoning = Reasoning(style=ReasoningStyle.DETAILED.value)
    output_format = OutputFormat(format_type=FormatType.MARKDOWN.value)
    
    # Create a decorated request
    request = DecoratedRequest(
        prompt="Explain the relationship between quantum mechanics and general relativity.",
        decorators=[reasoning, output_format],
        model="gpt-4",
        api_params={"temperature": 0.7, "max_tokens": 1000}
    )
    
    # Display the request
    print(f"Decorated Request:")
    print(f"  Prompt: {request.prompt}")
    print(f"  Decorators: {', '.join(d.name for d in request.decorators)}")
    print(f"  Model: {request.model}")
    print(f"  API Parameters: {request.api_params}")
    
    # Apply decorators
    decorated_prompt = request.apply_decorators()
    print(f"\nDecorated prompt:")
    print(f"  {decorated_prompt}")
    
    # Convert to dictionary and back
    request_dict = request.to_dict()
    print(f"\nSerialized request (preview):")
    print(f"  {json.dumps(request_dict, indent=2)[:200]}...")
    
    # Create from dictionary
    new_request = DecoratedRequest.from_dict(request_dict)
    print(f"\nDeserialized request:")
    print(f"  Model: {new_request.model}")
    print(f"  Decorators: {', '.join(d.name for d in new_request.decorators)}")
    print(f"  Number of decorators: {len(new_request.decorators)}")
    
    # Check decorator types
    for i, decorator in enumerate(new_request.decorators):
        print(f"  Decorator {i+1}: {decorator.name} (type: {type(decorator).__name__})")
        
    # Verify that the deserialized request produces the same decorated prompt
    new_decorated_prompt = new_request.apply_decorators()
    print(f"\nDecorated prompt from deserialized request:")
    print(f"  {new_decorated_prompt}")
    print(f"  Prompts match: {decorated_prompt == new_decorated_prompt}")


def main():
    """Run the demonstration."""
    print_section("Prompt Decorators Demo")
    print("This script demonstrates the prompt decorators framework functionality.\n")
    
    demonstrate_decorator_creation()
    demonstrate_decorator_validation()
    demonstrate_serialization()
    demonstrate_applying_decorators()
    demonstrate_compatibility_checking()
    demonstrate_decorated_request()
    
    print_section("End of Demo")


if __name__ == "__main__":
    main() 
#!/usr/bin/env python
"""Example script demonstrating usage of the dynamic prompt decorators module.

This script shows how to use the dynamic prompt decorators module to
transform prompts using decorator definitions from the registry.

Usage:
    python examples/dynamic_decorators_example.py
"""

import logging
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the dynamic decorators module
from prompt_decorators.dynamic_decorators_module import (
    apply_dynamic_decorators,
    create_decorator_instance,
    get_available_decorators,
)


def setup_logging():
    """Configure logging for the example."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )


def example_basic_usage():
    """Example of basic usage of apply_dynamic_decorators with decorator strings."""
    print("\n=== Basic Usage Example ===")

    prompt = """+++StepByStep(numbered=true)
What is quantum computing?"""

    transformed = apply_dynamic_decorators(prompt)

    print("\nOriginal prompt:")
    print(f"  {prompt}")
    print("\nTransformed prompt:")
    print(f"  {transformed}")


def example_decorator_objects():
    """Example of using decorator objects directly."""
    print("\n=== Decorator Objects Example ===")

    prompt = "Explain the principles of machine learning."

    # Create decorator objects
    step_by_step = create_decorator_instance("StepByStep", numbered=True)

    # Apply decorators
    transformed = step_by_step(prompt)

    print("\nOriginal prompt:")
    print(f"  {prompt}")
    print("\nDecorator objects:")
    print("  StepByStep(numbered=True)")
    print("\nTransformed prompt:")
    print(f"  {transformed}")


def example_decorator_syntax():
    """Example of using the decorator syntax."""
    print("\n=== Decorator Syntax Example ===")

    # Create decorator functions
    step_by_step = create_decorator_instance("StepByStep", numbered=True)

    # Define a function that returns a prompt
    def get_prompt():
        return "Describe the process of photosynthesis."

    # Apply decorators to the function's result
    def decorated_get_prompt():
        result = get_prompt()
        result = step_by_step(result)
        return result

    transformed = decorated_get_prompt()

    print("\nDecorator syntax:")
    print("  step_by_step = create_decorator_instance('StepByStep', numbered=True)")
    print("  def decorated_get_prompt():")
    print("      result = get_prompt()")
    print("      result = step_by_step(result)")
    print("      return result")
    print("\nTransformed prompt:")
    print(f"  {transformed}")


def example_inline_decorators():
    """Example of using inline decorators in the prompt."""
    print("\n=== Inline Decorators Example ===")

    prompt = """+++StepByStep(numbered=true)
Explain how to make a sourdough starter."""

    transformed = apply_dynamic_decorators(prompt)

    print("\nOriginal prompt with inline decorators:")
    print(f"  {prompt}")
    print("\nTransformed prompt:")
    print(f"  {transformed}")


def example_list_decorators():
    """Example of listing available decorators."""
    print("\n=== Available Decorators Example ===")

    decorators = get_available_decorators()

    print("\nAvailable decorators in the registry:")
    print(f"  Found {len(decorators)} decorators")

    # Print first 10 decorators as an example
    for i, decorator in enumerate(sorted(decorators, key=lambda d: d.name)[:10]):
        print(f"  - {decorator.name}: {decorator.description[:50]}...")


def main():
    """Run all examples."""
    setup_logging()

    print("\n" + "=" * 80)
    print("Dynamic Prompt Decorators Module - Usage Examples")
    print("=" * 80)

    # Run examples
    example_basic_usage()
    example_decorator_objects()
    example_decorator_syntax()
    example_inline_decorators()
    example_list_decorators()

    print("\n" + "=" * 80)
    print("End of Examples")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()

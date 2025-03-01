#!/usr/bin/env python3
"""
Test Generated Decorators

This script tests the generated decorators to ensure they work correctly.
"""

import sys
import os
from pathlib import Path
import importlib
import inspect

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prompt_decorators.decorators import *
from prompt_decorators.core.base import BaseDecorator


def print_section(title):
    """Print a section title."""
    print(f"\n{'=' * 80}")
    print(f"{title.center(80)}")
    print(f"{'=' * 80}\n")


def test_decorator_import():
    """Test that all decorators are imported correctly."""
    print_section("Testing Decorator Imports")
    
    # Get all decorators from the module
    from prompt_decorators import decorators
    
    # Count decorators
    decorator_count = 0
    
    # Print all available decorators
    print("Available decorators:")
    for name in dir(decorators):
        obj = getattr(decorators, name)
        if inspect.isclass(obj) and issubclass(obj, BaseDecorator) and obj != BaseDecorator:
            print(f"  - {name}")
            decorator_count += 1
    
    print(f"\nTotal decorators: {decorator_count}")


def test_decorator_instantiation():
    """Test that decorators can be instantiated."""
    print_section("Testing Decorator Instantiation")
    
    # Test a few decorators from different categories
    decorators_to_test = [
        # Core decorators
        Reasoning,
        StepByStep,
        OutputFormat,
        Tone,
        Version,
        
        # Reasoning decorators
        Socratic,
        Debate,
        TreeOfThought,
        
        # Structure decorators
        Summary,
        Outline,
        TableFormat,
        
        # Tone decorators
        Academic,
        Professional,
        Creative,
        
        # Verification decorators
        FactCheck,
        CiteSources,
        Limitations,
        
        # Meta decorators
        Refine,
        Chain,
        Context
    ]
    
    for decorator_class in decorators_to_test:
        try:
            # Create parameters for required arguments
            required_params = {}
            if decorator_class.__name__ == "OutputFormat":
                required_params["format"] = "markdown"
            elif decorator_class.__name__ == "Tone":
                required_params["style"] = "formal"
            elif decorator_class.__name__ == "Version":
                required_params["standard"] = "1.0.0"
            elif decorator_class.__name__ == "TableFormat":
                required_params["columns"] = ["Column1", "Column2"]
            elif decorator_class.__name__ == "Chain":
                required_params["decorators"] = ["Reasoning", "StepByStep"]
            elif decorator_class.__name__ == "Context":
                required_params["domain"] = "general"
            
            # Create an instance with default parameters
            decorator = decorator_class(**required_params)
            print(f"Successfully instantiated: {decorator.name} (v{decorator.version})")
            
            # Test parameter access
            print(f"  Parameters: {', '.join(decorator.parameters.keys())}")
            
            # Test to_dict and to_json
            decorator_dict = decorator.to_dict()
            decorator_json = decorator.to_json()
            print(f"  Serialization: ✓")
            
        except Exception as e:
            print(f"Error instantiating {decorator_class.__name__}: {e}")


def test_decorator_application():
    """Test applying decorators to prompts."""
    print_section("Testing Decorator Application")
    
    # Test prompt
    prompt = "Explain the concept of quantum computing."
    
    # Create decorators with correct parameters
    decorators_to_test = []
    
    # Reasoning
    decorators_to_test.append(Reasoning())
    
    # StepByStep
    decorators_to_test.append(StepByStep(numbered=True))
    
    # OutputFormat
    decorators_to_test.append(OutputFormat(format="markdown"))
    
    # ELI5
    decorators_to_test.append(ELI5())
    
    # Socratic
    decorators_to_test.append(Socratic(iterations=2))
    
    # Summary
    decorators_to_test.append(Summary(length="short"))
    
    for decorator in decorators_to_test:
        try:
            # Apply the decorator to the prompt
            decorated_prompt = decorator.apply(prompt)
            
            print(f"Applied {decorator.name}:")
            print(f"  Original: {prompt}")
            print(f"  Decorated: {decorated_prompt[:100]}..." if len(decorated_prompt) > 100 else f"  Decorated: {decorated_prompt}")
            print()
            
        except Exception as e:
            print(f"Error applying {decorator.name}: {e}")


def main():
    """Run the tests."""
    print_section("Testing Generated Decorators")
    
    test_decorator_import()
    test_decorator_instantiation()
    test_decorator_application()
    
    print_section("Tests Completed")


if __name__ == "__main__":
    main() 
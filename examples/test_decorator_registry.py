#!/usr/bin/env python
"""
Test script for the DecoratorRegistry functionality.

This script demonstrates how to use the DecoratorRegistry to discover
and register decorators from various sources.
"""

import os
import sys
import importlib
import inspect
from pathlib import Path

# Add the parent directory to sys.path to import the prompt_decorators package
sys.path.insert(0, str(Path(__file__).parent.parent))

from prompt_decorators.utils.discovery import DecoratorRegistry
from prompt_decorators.core.base import BaseDecorator

def main():
    """Run the decorator registry test."""
    print("\n" + "=" * 80)
    print("Testing Decorator Registry".center(80))
    print("=" * 80 + "\n")
    
    # Get the singleton instance of the registry
    registry = DecoratorRegistry()
    
    # Clear any existing registrations
    registry.clear()
    print(f"Registry cleared. Current decorators: {len(registry.get_all_decorators())}")
    
    # Instead of using the registry's directory scanning, we'll manually import and register decorators
    base_dir = Path(__file__).parent.parent
    generated_dir = base_dir / "prompt_decorators" / "decorators" / "generated" / "decorators"
    
    print(f"\nManually registering decorators from: {generated_dir}")
    
    # Add the project root to sys.path
    sys.path.insert(0, str(base_dir))
    
    # List of decorators to test
    test_decorators = [
        "Reasoning",
        "StepByStep",
        "OutputFormat",
        "Summary",
        "ELI5"
    ]
    
    # Module name mapping (for decorators with different module names)
    module_name_map = {
        "StepByStep": "step_by_step",
        "OutputFormat": "output_format"
    }
    
    registered_count = 0
    registered_names = []
    
    # Import and register each decorator
    for decorator_name in test_decorators:
        try:
            # Import the module
            module_name = module_name_map.get(decorator_name, decorator_name.lower())
            module_path = f"prompt_decorators.decorators.generated.decorators.{module_name}"
            module = importlib.import_module(module_path)
            
            # Find the decorator class
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and 
                    issubclass(obj, BaseDecorator) and 
                    obj is not BaseDecorator):
                    # Register the decorator
                    registry.register(obj)
                    registered_count += 1
                    registered_names.append(obj.name or name)
                    print(f"  - Registered: {obj.name or name}")
                    break
        except Exception as e:
            print(f"  - Failed to register {decorator_name}: {e}")
    
    print(f"\nRegistered {registered_count} decorators:")
    for name in sorted(registered_names):
        print(f"  - {name}")
    
    # Get all registered decorators
    all_decorators = registry.get_all_decorators()
    print(f"\nTotal registered decorators: {len(all_decorators)}")
    
    # Test getting decorators by category
    categories = registry.get_categories()
    print(f"\nDecorator categories ({len(categories)}):")
    for category in sorted(categories):
        decorators = registry.get_decorators_by_category(category)
        print(f"  - {category}: {len(decorators)} decorators")
    
    # Test getting a specific decorator
    test_decorator_name = "Reasoning" if "Reasoning" in registered_names else (registered_names[0] if registered_names else None)
    
    if test_decorator_name:
        decorator_class = registry.get_decorator(test_decorator_name)
        
        if decorator_class:
            print(f"\nRetrieved decorator: {test_decorator_name}")
            print(f"  - Description: {decorator_class.description}")
            print(f"  - Category: {decorator_class.category}")
            print(f"  - Version: {decorator_class.version}")
            
            # Test instantiation
            try:
                # Get the required parameters for this decorator
                params = {}
                if test_decorator_name == "Reasoning":
                    from prompt_decorators.decorators.generated.decorators.enums import ReasoningDepthEnum
                    params = {"depth": ReasoningDepthEnum.MODERATE}
                elif test_decorator_name == "OutputFormat":
                    params = {"format": "markdown"}
                
                decorator = decorator_class(**params)
                print(f"  - Successfully instantiated")
                
                # Test serialization
                serialized = decorator.to_dict()
                print(f"  - Serialization: {serialized}")
                
                # Test application
                original_prompt = "Explain the concept of quantum computing."
                decorated = decorator.apply(original_prompt)
                print(f"\nApplied {test_decorator_name}:")
                print(f"  Original: {original_prompt}")
                print(f"  Decorated: {decorated[:100]}...")
            except Exception as e:
                print(f"  - Error instantiating: {e}")
        else:
            print(f"\nFailed to retrieve decorator: {test_decorator_name}")
    else:
        print("\nNo decorators were registered successfully.")
    
    print("\n" + "=" * 80)
    print("Registry Test Completed".center(80))
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main() 
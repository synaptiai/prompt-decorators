#!/usr/bin/env python
"""
Script to register all decorators from the generated directory.

This script:
1. Clears the DecoratorRegistry
2. Discovers all decorator classes in the generated decorators directory
3. Registers each decorator class with the registry
4. Prints a summary of the registered decorators
"""

import sys
import os
from pathlib import Path
import importlib
import inspect
import logging
from datetime import datetime

# Add the parent directory to the path so we can import the prompt_decorators package
parent_dir = str(Path(__file__).resolve().parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.utils.discovery import DecoratorRegistry

def register_decorators():
    """
    Register all decorators from the generated directory.
    
    This function:
    1. Clears the DecoratorRegistry
    2. Discovers decorator classes in the specified directory
    3. Registers each decorator class with the registry
    4. Prints a summary of the registered decorators
    """
    print("\n" + "=" * 80)
    print("=" * 26 + " Registering All Decorators " + "=" * 26)
    print("=" * 80 + "\n")
    
    # Clear the registry
    registry = DecoratorRegistry()
    registry.clear()
    print(f"Registry cleared. Current decorators: {len(registry.get_all_decorators())}\n")
    
    # Path to the decorators directory
    decorators_dir = os.path.join(parent_dir, "prompt_decorators", "decorators", "generated", "decorators")
    print(f"Registering decorators from: {decorators_dir}\n")
    
    # Count of registered decorators
    registered_count = 0
    
    # Iterate through all Python files in the decorators directory
    for filename in os.listdir(decorators_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]  # Remove .py extension
            module_path = f"prompt_decorators.decorators.generated.decorators.{module_name}"
            
            try:
                # Import the module
                module = importlib.import_module(module_path)
                
                # Find all classes in the module that are subclasses of BaseDecorator
                for name, obj in inspect.getmembers(module):
                    if (inspect.isclass(obj) and 
                        issubclass(obj, BaseDecorator) and 
                        obj != BaseDecorator):
                        
                        # Use the class name as the decorator name
                        decorator_name = obj.__name__
                        
                        # Register the decorator
                        registry.register(obj)
                        registered_count += 1
                        
                        # Print registration information
                        print(f"  - Registered: {decorator_name}")
            
            except Exception as e:
                print(f"Error registering decorators from {module_path}: {str(e)}")
    
    # Print summary
    print(f"\nRegistered {registered_count} decorators:\n")
    
    # Get all registered decorators
    decorators = registry.get_all_decorators()
    print(f"Total registered decorators: {len(decorators)}")
    
    # Get decorator categories
    categories = registry.get_categories()
    print(f"\nDecorator categories ({len(categories)}):")
    for category in categories:
        category_decorators = registry.get_decorators_by_category(category)
        print(f"  - {category}: {len(category_decorators)} decorators")
    
    print("\n" + "=" * 80)
    print("=" * 28 + " Registration Completed " + "=" * 28)
    print("=" * 80 + "\n")

if __name__ == "__main__":
    register_decorators() 
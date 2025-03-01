#!/usr/bin/env python
"""
Example script demonstrating how to use registered decorators from the DecoratorRegistry.

This script shows how to:
1. Access the DecoratorRegistry
2. Retrieve decorators by name, category, or list all decorators
3. Create decorator instances with parameters
4. Apply decorators to a prompt
5. Combine multiple decorators
"""

import sys
import os
from pathlib import Path
import random
import importlib
import inspect

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

def print_separator(title):
    """Print a separator with a title."""
    print("\n" + "=" * 80)
    print(f" {title} ".center(80, "="))
    print("=" * 80 + "\n")

def main():
    """
    Main function to demonstrate the use of registered decorators.
    """
    # Register all decorators
    register_decorators()
    
    # Get the registry
    registry = DecoratorRegistry()
    
    # Print available decorators
    print("\n" + "=" * 80)
    print("=" * 29 + " Available Decorators " + "=" * 29)
    print("=" * 80 + "\n")
    
    decorators = registry.get_all_decorators()
    print(f"Total decorators available: {len(decorators)}")
    
    # Print a sample of decorators
    sample_size = min(5, len(decorators))
    for i in range(sample_size):
        decorator = decorators[i]
        # Get the version from the decorator class
        version = decorator.version
        print(f"- {decorator.__name__} (Latest version: {version})")
    
    # Use a specific decorator
    print("\n" + "=" * 80)
    print("=" * 26 + " Using a Specific Decorator " + "=" * 26)
    print("=" * 80 + "\n")
    
    # Get the Concise decorator
    concise_decorator = registry.get_decorator("Concise")
    if concise_decorator:
        # Create an instance of the decorator
        concise = concise_decorator(
            maxWords=None,
            bulletPoints=False,
            level=2
        )
        
        print(f"Created {concise.name} decorator (v{concise.version})")
        print(f"Parameters: {concise.to_dict()}")
        
        # Apply the decorator to a prompt
        original_prompt = "Explain the concept of quantum computing in detail, covering its history, principles, and potential applications in various fields."
        decorated_prompt = concise.apply(original_prompt)
        
        print(f"\nOriginal prompt:\n'{original_prompt}'\n")
        print(f"Decorated prompt:\n'{decorated_prompt}'")
    
    # Combine multiple decorators
    print("\n" + "=" * 80)
    print("=" * 25 + " Combining Multiple Decorators " + "=" * 25)
    print("=" * 80 + "\n")
    
    # Get the ELI5 decorator
    eli5_decorator = registry.get_decorator("ELI5")
    professional_decorator = registry.get_decorator("Professional")
    
    if eli5_decorator and professional_decorator:
        # Create instances
        eli5 = eli5_decorator(strictness=False)
        professional = professional_decorator()
        
        # Original prompt
        original_prompt = "Explain how neural networks work."
        
        # Apply ELI5 decorator
        eli5_prompt = eli5.apply(original_prompt)
        
        # Apply both decorators
        combined_prompt = professional.apply(eli5_prompt)
        
        print(f"\nOriginal prompt:\n'{original_prompt}'\n")
        print(f"With ELI5 decorator:\n'{eli5_prompt}'\n")
        print(f"With ELI5 + Professional decorators:\n'{combined_prompt}'")
    
    # Find decorators by category
    print("\n" + "=" * 80)
    print("=" * 25 + " Finding Decorators by Category " + "=" * 25)
    print("=" * 80 + "\n")
    
    categories = registry.get_categories()
    print(f"Available categories: {categories}")
    
    # Print decorators in a specific category
    if categories:
        category = categories[0]  # Use the first category
        category_decorators = registry.get_decorators_by_category(category)
        
        print(f"\nDecorators in category '{category}':")
        for decorator in category_decorators:
            print(f"- {decorator.__name__}")

if __name__ == "__main__":
    main() 
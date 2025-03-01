#!/usr/bin/env python
"""
Dynamic Decorator Example

This script demonstrates dynamic loading of decorators from JSON definitions.
"""

import os
import sys
import json
from pathlib import Path
import argparse

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from prompt_decorators.utils import (
    DecoratorRegistry, 
    DecoratorFactory, 
    JSONLoader,
    get_registry
)


# Example JSON decorator definition
EXAMPLE_JSON_DECORATOR = """
{
  "decoratorName": "DynamicExample",
  "version": "1.0.0",
  "description": "A dynamically created decorator example",
  "category": "demo",
  "parameters": [
    {
      "name": "style",
      "type": "enum",
      "description": "Style of the dynamically created decorator",
      "enum": ["simple", "detailed", "creative"],
      "default": "simple"
    },
    {
      "name": "intensity",
      "type": "number",
      "description": "Intensity level",
      "min": 1,
      "max": 10,
      "default": 5
    },
    {
      "name": "include_examples",
      "type": "boolean",
      "description": "Whether to include examples",
      "default": true
    }
  ]
}
"""


def demonstrate_json_string():
    """Demonstrate loading a decorator from a JSON string."""
    print("\n=== Loading Decorator from JSON String ===")
    
    # Create a registry
    registry = get_registry()
    registry.clear()
    
    # Register a decorator from a JSON string
    decorator_class = registry.register_from_json_string(EXAMPLE_JSON_DECORATOR)
    
    if decorator_class:
        print(f"Successfully registered decorator: {decorator_class.name}")
        
        # Create an instance
        decorator = decorator_class(
            style="detailed", 
            intensity=8, 
            include_examples=True
        )
        
        # Apply to a prompt
        prompt = "Explain the concept of virtual reality."
        decorated_prompt = decorator.apply(prompt)
        
        print(f"\nOriginal prompt: {prompt}")
        print(f"\nDecorated prompt:\n{decorated_prompt}")
    else:
        print("Failed to register decorator from JSON string.")


def demonstrate_json_file(file_path=None):
    """
    Demonstrate loading a decorator from a JSON file.
    
    Args:
        file_path: Path to a JSON file, or None to create a temporary file
    """
    # If no file path was provided, create a temporary file
    if not file_path:
        temp_dir = Path(project_root) / "examples" / "temp"
        temp_dir.mkdir(exist_ok=True)
        file_path = temp_dir / "dynamic_decorator.json"
        
        # Write the example JSON to the file
        with open(file_path, "w") as f:
            f.write(EXAMPLE_JSON_DECORATOR)
    
    print(f"\n=== Loading Decorator from JSON File: {file_path} ===")
    
    # Create a factory
    factory = DecoratorFactory()
    
    # Load from file
    decorator = factory.create_from_file(str(file_path))
    
    if decorator:
        print(f"Successfully loaded decorator: {decorator.name}")
        
        # Apply to a prompt
        prompt = "Explain the concept of quantum computing."
        decorated_prompt = decorator.apply(prompt)
        
        print(f"\nOriginal prompt: {prompt}")
        print(f"\nDecorated prompt:\n{decorated_prompt}")
    else:
        print(f"Failed to load decorator from file: {file_path}")


def demonstrate_json_directory(dir_path=None):
    """
    Demonstrate loading all decorators from a directory of JSON files.
    
    Args:
        dir_path: Path to a directory with JSON files, or None to use the registry dir
    """
    # If no directory path was provided, use the registry/demo directory or create it
    if not dir_path:
        dir_path = Path(project_root) / "registry" / "demo"
        dir_path.mkdir(exist_ok=True, parents=True)
        
        # Create some sample JSON decorator files if the directory is empty
        if not any(dir_path.iterdir()):
            # Create a few variations of our example decorator
            for i in range(1, 4):
                data = json.loads(EXAMPLE_JSON_DECORATOR)
                data["decoratorName"] = f"DynamicExample{i}"
                data["description"] = f"Dynamic example decorator #{i}"
                
                # Write to file
                with open(dir_path / f"dynamic_example{i}.json", "w") as f:
                    json.dump(data, f, indent=2)
    
    print(f"\n=== Loading Decorators from Directory: {dir_path} ===")
    
    # Load all decorators from the directory
    registry = get_registry()
    registry.clear()
    count = registry.register_all_from_json_directory(str(dir_path))
    
    print(f"Loaded {count} decorators from directory.")
    
    # Show all loaded decorators
    all_decorators = registry.get_all_decorators()
    print(f"\nAvailable decorators:")
    for name, decorator_class in all_decorators.items():
        print(f"  - {name} (v{decorator_class.version})")
    
    # Create and use a decorator if any were loaded
    if all_decorators:
        # Get the first decorator
        name = next(iter(all_decorators.keys()))
        decorator = registry.create_decorator(name)
        
        if decorator:
            # Apply to a prompt
            prompt = "Explain the concept of machine learning."
            decorated_prompt = decorator.apply(prompt)
            
            print(f"\nUsing decorator: {decorator.name}")
            print(f"Original prompt: {prompt}")
            print(f"\nDecorated prompt:\n{decorated_prompt}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demonstrate dynamic decorators")
    parser.add_argument(
        "--json-file", "-f",
        help="Path to a JSON file for the file-based example"
    )
    parser.add_argument(
        "--json-dir", "-d",
        help="Path to a directory of JSON files for the directory-based example"
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Run all demonstrations"
    )
    
    args = parser.parse_args()
    
    # If no specific examples were requested, run everything
    if not args.json_file and not args.json_dir and not args.all:
        args.all = True
    
    if args.all or not args.json_file and not args.json_dir:
        demonstrate_json_string()
        demonstrate_json_file()
        demonstrate_json_directory()
    else:
        if args.json_file:
            demonstrate_json_file(args.json_file)
        if args.json_dir:
            demonstrate_json_directory(args.json_dir) 
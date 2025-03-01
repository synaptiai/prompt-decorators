#!/usr/bin/env python
"""
Sample test generation script for a single decorator.

This script demonstrates how to use the TestGenerator to create
a test for a specific decorator.
"""

import os
import json
import sys
from pathlib import Path

# Add the project directory to the path for imports
sys.path.append(str(Path(__file__).resolve().parent))

from prompt_decorators.generator.test_gen import TestGenerator

def generate_sample_test():
    """Generate a sample test for the Detailed decorator."""
    
    # Path to the decorator JSON file
    decorator_file = Path("registry/core/tone/detailed.json")
    
    # Ensure the decorator file exists
    if not decorator_file.exists():
        print(f"Error: Decorator file not found: {decorator_file}")
        return False
    
    # Create output directory
    output_dir = Path("tests/auto/sample")
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the decorator data
    with open(decorator_file, "r") as f:
        decorator_data = json.load(f)
    
    # Create the test generator
    generator = TestGenerator(
        registry_dir="registry",
        output_dir=str(output_dir),
        template_dir=None
    )
    
    # Generate the conftest.py file
    conftest_path = generator.generate_conftest()
    print(f"Generated conftest.py: {conftest_path}")
    
    # Generate a test for the decorator
    test_file_path = generator.generate_decorator_test(decorator_data)
    print(f"Generated test file: {test_file_path}")
    
    # Generate the test discovery file
    discovery_path = generator.generate_test_discovery()
    print(f"Generated test discovery file: {discovery_path}")
    
    print("\nTest generation completed successfully!")
    return True

if __name__ == "__main__":
    if generate_sample_test():
        print("\nTo run the generated test, install pytest and run:")
        print("  python -m pytest tests/auto/sample -v")
    else:
        print("\nTest generation failed. See the error message above.")
        sys.exit(1) 
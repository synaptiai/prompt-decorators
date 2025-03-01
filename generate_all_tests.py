#!/usr/bin/env python
"""
Test Generator Script for Prompt Decorators

This script generates comprehensive unit tests for all decorators defined in the registry.
"""

import os
import sys
from pathlib import Path

# Add the project directory to the path for imports
sys.path.append(str(Path(__file__).resolve().parent))

from prompt_decorators.generator.test_gen import TestGenerator

def generate_all_tests():
    """Generate tests for all decorators in the registry."""
    
    # Create the test generator
    generator = TestGenerator(
        registry_dir="registry",
        output_dir="tests/auto",
        template_dir=None
    )
    
    # Generate tests
    print("Generating decorator tests...")
    generated_files = generator.generate_all_tests()
    
    print(f"Generated {len(generated_files)} test files:")
    for file_path in generated_files:
        print(f"  - {file_path}")
    
    print("\nTest generation completed successfully!")
    print("\nTo run the generated tests, install pytest and run:")
    print("  python -m pytest tests/auto -v")

if __name__ == "__main__":
    generate_all_tests() 
#!/usr/bin/env python3
"""
Prompt Decorators Generator Script

This script generates Python code from the decorator registry.
"""

import sys
from pathlib import Path
from prompt_decorators.generator.cli import main

if __name__ == "__main__":
    # Add the current directory to the Python path
    sys.path.insert(0, str(Path(__file__).parent))
    sys.exit(main()) 
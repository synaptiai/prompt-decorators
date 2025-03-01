#!/usr/bin/env python3
"""Installation script for the Prompt Decorators Core extension package."""

import json
import os
import shutil
import sys
from pathlib import Path
import argparse

def main():
    """Install the Prompt Decorators Core extension package."""
    parser = argparse.ArgumentParser(description="Install the Prompt Decorators Core extension package")
    parser.add_argument("--dest", default="~/.prompt-decorators/extensions",
                        help="Destination directory for the extension package")
    args = parser.parse_args()
    
    # Expand user directory
    dest_dir = Path(os.path.expanduser(args.dest)) / "core"
    
    # Get the source directory
    src_dir = Path(__file__).parent
    
    # Create the destination directory if it doesn't exist
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy the package.json file
    shutil.copy2(src_dir / "package.json", dest_dir / "package.json")
    
    # Copy the README.md file
    shutil.copy2(src_dir / "README.md", dest_dir / "README.md")
    
    # Create the examples directory
    examples_dir = dest_dir / "examples"
    examples_dir.mkdir(exist_ok=True)
    
    # Copy the example files
    for example_file in (src_dir / "examples").glob("*.md"):
        shutil.copy2(example_file, examples_dir / example_file.name)
    
    print(f"Installed Prompt Decorators Core extension package to {dest_dir}")
    print("You can now use the core decorators in your applications.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 
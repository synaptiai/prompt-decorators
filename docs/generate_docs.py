#!/usr/bin/env python
"""Documentation Generator CLI.

This module provides a command-line interface for generating API documentation
from the prompt-decorators package. It extracts information from docstrings and
the decorator registry to create comprehensive documentation.

This script can generate documentation in markdown or HTML format and supports
various command-line options for customization.

Example:
    Generate markdown documentation for the prompt_decorators package:

    $ python docs/generate_docs.py --format markdown

Returns:
    None: This script doesn't return anything but writes documentation files.
"""

import argparse
import logging
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from prompt_decorators.utils.doc_gen import DocGenerator

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    """Run the documentation generator CLI."""
    parser = argparse.ArgumentParser(description="Generate API documentation")
    parser.add_argument(
        "--package",
        "-p",
        default="prompt_decorators",
        help="Name of the package to document",
    )
    parser.add_argument(
        "--registry", "-r", default="registry", help="Path to the registry directory"
    )
    parser.add_argument(
        "--output",
        "-o",
        default="docs/api",
        help="Directory where documentation should be written",
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["markdown", "html", "both"],
        default="markdown",
        help="Output format for documentation",
    )

    args = parser.parse_args()

    # Create the documentation generator
    generator = DocGenerator(
        package_path=args.package, registry_path=args.registry, output_dir=args.output
    )

    # Extract documentation
    generator.extract_package_docs(args.package)

    # Load registry data
    generator.load_registry_data()

    # Generate documentation
    if args.format == "markdown" or args.format == "both":
        generator.generate_markdown_docs()

    if args.format == "html" or args.format == "both":
        generator.generate_html_docs()

    logger.info("Documentation generation complete")


if __name__ == "__main__":
    main()

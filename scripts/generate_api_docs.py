#!/usr/bin/env python3
"""API Documentation Generator.

DEPRECATED: This script is deprecated in favor of docs/generate_docs.py.
Please use docs/generate_docs.py instead, which provides the same functionality.

This module generates API documentation for the prompt-decorators project by
extracting information from docstrings and type annotations. It provides
a flexible command-line interface with various options for customization.

The generator creates a comprehensive documentation set covering all modules,
classes, and functions in the package, formatted according to the chosen output
format (markdown, HTML, or both).

Example:
    Generate markdown documentation with a clean output directory:

    $ python scripts/generate_api_docs.py --format markdown --clean

Returns:
    None: This script doesn't return anything but writes documentation files.
"""

import argparse
import logging
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_doc_generator(package_path, registry_path, output_dir):
    """
    Create a documentation generator instance.

    Args:
        package_path: Path to the package to document
        registry_path: Path to the registry directory
        output_dir: Directory where documentation should be written

    Returns:
        A documentation generator instance
    """
    try:
        from prompt_decorators.utils.doc_gen import DocumentationGenerator

        return DocumentationGenerator(
            package_path=package_path,
            registry_path=registry_path,
            output_dir=output_dir,
        )
    except ImportError:
        logger.error(
            "Could not import DocumentationGenerator. Make sure prompt-decorators is installed."
        )
        sys.exit(1)


def main():
    """
    Run the API documentation generator.

    Returns:
        None
    """
    logger.warning(
        "DEPRECATED: This script is deprecated in favor of docs/generate_docs.py. "
        "Please use docs/generate_docs.py instead, which provides the same functionality."
    )

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
    parser.add_argument(
        "--clean",
        "-c",
        action="store_true",
        help="Clean the output directory before generating documentation",
    )

    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Clean the output directory if requested
    if args.clean:
        logger.info(f"Cleaning output directory: {output_dir}")
        for file in output_dir.glob("**/*"):
            if file.is_file():
                file.unlink()

    # Create the documentation generator
    generator = get_doc_generator(
        package_path=args.package,
        registry_path=args.registry,
        output_dir=str(output_dir),
    )

    # Extract documentation
    generator.extract_package_docs(args.package)

    # Load registry data
    generator.load_registry_data()

    # Merge code and registry documentation
    merged_docs = generator.merge_code_and_registry_docs()

    # Generate documentation
    if args.format == "markdown" or args.format == "both":
        generator.generate_markdown_docs()
        logger.info(f"Generated Markdown documentation in {output_dir}")

    if args.format == "html" or args.format == "both":
        generator.generate_html_docs()
        logger.info(f"Generated HTML documentation in {output_dir}")

    logger.info("Documentation generation complete")
    logger.warning(
        "DEPRECATED: This script is deprecated in favor of docs/generate_docs.py. "
        "Please use docs/generate_docs.py instead, which provides the same functionality."
    )


if __name__ == "__main__":
    main()

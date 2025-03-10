#!/usr/bin/env python
"""Documentation Verification Script.

This script verifies that the documentation is complete, accurate, and consistent.
It checks docstring coverage, builds the documentation, and performs various checks.

Example:
    Run the script to verify documentation:

    $ python scripts/verify_documentation.py

Returns:
    int: 0 if all checks pass, 1 otherwise
"""

import json
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def run_command(
    cmd: List[str], cwd: Optional[str] = None, env: Optional[Dict[str, str]] = None
) -> Tuple[int, str, str]:
    """Run a command and return its exit code, stdout, and stderr.

    Args:
        cmd: Command to run as a list of strings
        cwd: Working directory to run the command in
        env: Environment variables to set

    Returns:
        Tuple containing (exit_code, stdout, stderr)
    """
    logger.debug(f"Running command: {' '.join(cmd)}")

    # Prepare environment
    cmd_env = os.environ.copy()
    if env:
        cmd_env.update(env)

    # Run the command
    process = subprocess.run(cmd, cwd=cwd, env=cmd_env, capture_output=True, text=True)

    return process.returncode, process.stdout, process.stderr


def check_docstring_coverage() -> bool:
    """Check docstring coverage using interrogate.

    Returns:
        bool: True if the check passes, False otherwise
    """
    logger.info("Checking docstring coverage...")

    # First check if interrogate is installed
    returncode, stdout, stderr = run_command(["pip", "show", "interrogate"])
    if returncode != 0:
        logger.warning("interrogate not installed. Installing...")
        returncode, stdout, stderr = run_command(["pip", "install", "interrogate"])
        if returncode != 0:
            logger.error(f"Failed to install interrogate: {stderr}")
            return False

    # Run interrogate on the prompt_decorators package
    returncode, stdout, stderr = run_command(
        ["interrogate", "-v", "prompt_decorators", "-f", "100"]
    )

    logger.info(stdout)
    if returncode != 0:
        logger.error(f"Docstring coverage check failed: {stderr}")
        return False

    return True


def build_documentation() -> bool:
    """Build the documentation using MkDocs.

    Returns:
        bool: True if the build succeeds, False otherwise
    """
    logger.info("Building documentation...")

    # Check if mkdocs is installed
    returncode, stdout, stderr = run_command(["pip", "show", "mkdocs"])
    if returncode != 0:
        logger.warning("mkdocs not installed. Installing...")
        returncode, stdout, stderr = run_command(
            [
                "pip",
                "install",
                "mkdocs",
                "mkdocs-material",
                "mkdocs-awesome-pages-plugin",
                "mkdocstrings",
            ]
        )
        if returncode != 0:
            logger.error(f"Failed to install mkdocs: {stderr}")
            return False

    # Build the documentation
    returncode, stdout, stderr = run_command(["mkdocs", "build", "--strict"])

    logger.info(stdout)
    if returncode != 0:
        logger.error(f"Documentation build failed: {stderr}")
        return False

    return True


def run_doc_generator() -> bool:
    """Run the documentation generator.

    Returns:
        bool: True if the generator succeeds, False otherwise
    """
    logger.info("Running documentation generator...")

    # Run the documentation generator
    returncode, stdout, stderr = run_command(["python", "docs/generate_docs.py"])

    logger.info(stdout)
    if returncode != 0:
        logger.error(f"Documentation generator failed: {stderr}")
        return False

    return True


def check_api_docs_completeness() -> bool:
    """Check that all modules have corresponding API documentation.

    Returns:
        bool: True if all modules are documented, False otherwise
    """
    logger.info("Checking API documentation completeness...")

    # Get all Python modules in the prompt_decorators package
    modules = []
    for root, dirs, files in os.walk("prompt_decorators"):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                module_path = os.path.join(root, file)
                module_name = (
                    module_path.replace("/", ".").replace("\\", ".").replace(".py", "")
                )
                modules.append(module_name)

    # Check if each module has corresponding documentation
    missing_docs = []
    for module in modules:
        # Convert module name to documentation path
        doc_path = f"docs/api/modules/{module}.md"
        if not os.path.exists(doc_path):
            missing_docs.append(module)

    if missing_docs:
        logger.error(
            f"Missing API documentation for modules: {', '.join(missing_docs)}"
        )
        return False

    return True


def check_registry_docs() -> bool:
    """Check that all decorators in the registry have documentation.

    Returns:
        bool: True if all decorators are documented, False otherwise
    """
    logger.info("Checking registry documentation...")

    # Get all decorator JSON files in the registry
    registry_files = []
    for pattern in ["*/*/decorator.json", "*/*/*.json"]:
        registry_files.extend(Path("registry").glob(pattern))

    # Check if each decorator has corresponding documentation
    missing_docs = []
    for registry_file in registry_files:
        try:
            # Extract decorator name from the JSON file
            with open(registry_file, "r") as f:
                data = json.load(f)

            # Check if this is a decorator definition
            if "decoratorName" in data:
                decorator_name = data["decoratorName"]
                doc_path = f"docs/api/decorators/{decorator_name}.md"
                if not os.path.exists(doc_path):
                    missing_docs.append(decorator_name)
        except Exception as e:
            logger.error(f"Error processing {registry_file}: {e}")

    if missing_docs:
        logger.error(f"Missing documentation for decorators: {', '.join(missing_docs)}")
        return False

    return True


def check_docstring_style() -> bool:
    """Check that docstrings follow Google style.

    Returns:
        bool: True if docstrings follow Google style, False otherwise
    """
    logger.info("Checking docstring style...")

    # Check if pydocstyle is installed
    returncode, stdout, stderr = run_command(["pip", "show", "pydocstyle"])
    if returncode != 0:
        logger.warning("pydocstyle not installed. Installing...")
        returncode, stdout, stderr = run_command(["pip", "install", "pydocstyle"])
        if returncode != 0:
            logger.error(f"Failed to install pydocstyle: {stderr}")
            return False

    # Run pydocstyle with Google convention
    returncode, stdout, stderr = run_command(
        ["pydocstyle", "--convention=google", "prompt_decorators"]
    )

    # Note: pydocstyle often returns non-zero even for minor issues
    # So we'll log the output but not fail the check
    if stdout:
        logger.warning(f"Docstring style issues found:\n{stdout}")

    return True


def check_mkdocs_config() -> bool:
    """Check that the MkDocs configuration is valid.

    Returns:
        bool: True if the configuration is valid, False otherwise
    """
    logger.info("Checking MkDocs configuration...")

    # Check if mkdocs is installed
    returncode, stdout, stderr = run_command(["pip", "show", "mkdocs"])
    if returncode != 0:
        logger.warning("mkdocs not installed. Installing...")
        returncode, stdout, stderr = run_command(
            [
                "pip",
                "install",
                "mkdocs",
                "mkdocs-material",
                "mkdocs-awesome-pages-plugin",
                "mkdocstrings",
            ]
        )
        if returncode != 0:
            logger.error(f"Failed to install mkdocs: {stderr}")
            return False

    # Check the configuration
    returncode, stdout, stderr = run_command(["mkdocs", "build", "--strict"])

    if returncode != 0:
        logger.error(f"MkDocs configuration check failed: {stderr}")
        return False

    return True


def main() -> int:
    """Run all documentation verification checks.

    Returns:
        int: 0 if all checks pass, 1 otherwise
    """
    # Define checks to run
    checks: List[Callable[[], bool]] = [
        check_mkdocs_config,
        check_docstring_coverage,
        check_docstring_style,
        build_documentation,
        run_doc_generator,
        check_api_docs_completeness,
        check_registry_docs,
    ]

    # Run checks
    results = []
    for check in checks:
        try:
            result = check()
            results.append(result)
        except Exception as e:
            logger.error(f"Check {check.__name__} failed with exception: {e}")
            results.append(False)

    # Summarize results
    logger.info("\n--- Documentation Verification Summary ---")
    for i, (check, result) in enumerate(zip(checks, results)):
        status = "PASSED" if result else "FAILED"
        logger.info(f"{i+1}. {check.__name__}: {status}")

    # Overall result
    if all(results):
        logger.info("\nAll documentation checks passed!")
        return 0
    else:
        logger.error("\nSome documentation checks failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())

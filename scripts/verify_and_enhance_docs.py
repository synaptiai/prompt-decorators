#!/usr/bin/env python
"""Documentation Verification and Enhancement Script.

This script runs all the documentation verification and enhancement steps.
It enhances the DocGenerator class, generates documentation, and verifies
that the documentation is complete and accurate.

Example:
    Run the script to verify and enhance documentation:

    $ python scripts/verify_and_enhance_docs.py

Returns:
    int: 0 if all steps succeed, 1 otherwise
"""

import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


def run_command(cmd: List[str], cwd: str = None) -> Tuple[int, str, str]:
    """Run a command and return its exit code, stdout, and stderr.

    Args:
        cmd: Command to run as a list of strings
        cwd: Working directory to run the command in

    Returns:
        Tuple containing (exit_code, stdout, stderr)
    """
    logger.info(f"Running command: {' '.join(cmd)}")

    process = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)

    return process.returncode, process.stdout, process.stderr


def enhance_doc_generator() -> bool:
    """Enhance the DocGenerator class.

    Returns:
        bool: True if the enhancement succeeds, False otherwise
    """
    logger.info("Enhancing DocGenerator class...")

    returncode, stdout, stderr = run_command(
        ["python", "scripts/enhance_doc_generator.py"]
    )

    logger.info(stdout)
    if returncode != 0:
        logger.error(f"DocGenerator enhancement failed: {stderr}")
        return False

    return True


def generate_documentation() -> bool:
    """Generate documentation using the enhanced DocGenerator.

    Returns:
        bool: True if the generation succeeds, False otherwise
    """
    logger.info("Generating documentation...")

    returncode, stdout, stderr = run_command(
        ["python", "docs/generate_docs.py", "--format", "markdown"]
    )

    logger.info(stdout)
    if returncode != 0:
        logger.error(f"Documentation generation failed: {stderr}")
        return False

    return True


def verify_documentation() -> bool:
    """Verify the generated documentation.

    Returns:
        bool: True if the verification succeeds, False otherwise
    """
    logger.info("Verifying documentation...")

    returncode, stdout, stderr = run_command(
        ["python", "scripts/verify_documentation.py"]
    )

    logger.info(stdout)
    if returncode != 0:
        logger.error(f"Documentation verification failed: {stderr}")
        return False

    return True


def build_documentation() -> bool:
    """Build the documentation using MkDocs.

    Returns:
        bool: True if the build succeeds, False otherwise
    """
    logger.info("Building documentation...")

    returncode, stdout, stderr = run_command(["mkdocs", "build", "--strict"])

    logger.info(stdout)
    if returncode != 0:
        logger.error(f"Documentation build failed: {stderr}")
        return False

    return True


def main() -> int:
    """Run all documentation verification and enhancement steps.

    Returns:
        int: 0 if all steps succeed, 1 otherwise
    """
    steps = [
        ("Enhancing DocGenerator", enhance_doc_generator),
        ("Generating documentation", generate_documentation),
        ("Verifying documentation", verify_documentation),
        ("Building documentation", build_documentation),
    ]

    results = []
    for step_name, step_func in steps:
        logger.info(f"\n--- {step_name} ---")
        try:
            result = step_func()
            results.append(result)
            if not result:
                logger.error(f"{step_name} failed")
        except Exception as e:
            logger.error(f"{step_name} failed with exception: {e}")
            results.append(False)

    # Summarize results
    logger.info("\n--- Documentation Verification and Enhancement Summary ---")
    for i, (step_name, _) in enumerate(steps):
        status = "PASSED" if results[i] else "FAILED"
        logger.info(f"{i+1}. {step_name}: {status}")

    # Overall result
    if all(results):
        logger.info("\nAll documentation verification and enhancement steps passed!")
        return 0
    else:
        logger.error("\nSome documentation verification and enhancement steps failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())

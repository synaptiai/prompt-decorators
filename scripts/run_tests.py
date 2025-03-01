#!/usr/bin/env python3
"""
Test Runner for Prompt Decorators

This script generates tests from decorator JSON files and runs them,
providing a summary of the results.
"""

import os
import sys
import argparse
import subprocess
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Paths
SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
TESTS_DIR = PROJECT_ROOT / "tests"
AUTO_TESTS_DIR = TESTS_DIR / "auto"


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Generate and run decorator tests.")
    parser.add_argument(
        "--use-real-llm", 
        action="store_true",
        help="Use real LLM API for tests (requires API keys)"
    )
    parser.add_argument(
        "--no-cache", 
        action="store_true",
        help="Disable response caching (slower, but ensures fresh results)"
    )
    parser.add_argument(
        "--no-generate", 
        action="store_true",
        help="Skip test generation (use existing tests only)"
    )
    parser.add_argument(
        "--category", 
        type=str,
        choices=["reasoning", "structure", "tone", "verification", "meta", "minimal", "misc", "all"],
        default="all",
        help="Test only a specific decorator category"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )
    return parser.parse_args()


def generate_tests():
    """Generate tests from decorator definitions."""
    logger.info("Generating tests from decorator definitions...")
    
    generator_script = SCRIPTS_DIR / "generate_tests.py"
    
    if not generator_script.exists():
        logger.error(f"Test generator script not found: {generator_script}")
        sys.exit(1)
    
    try:
        result = subprocess.run(
            [sys.executable, str(generator_script)],
            check=True,
            capture_output=True,
            text=True
        )
        # Check if there is any output before trying to access the last line
        if result.stdout and result.stdout.splitlines():
            logger.info(f"Test generation completed: {result.stdout.splitlines()[-1]}")
        else:
            logger.info("Test generation completed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Test generation failed: {e.stderr}")
        sys.exit(1)


def run_tests(category="all", use_real_llm=False, use_cache=True, verbose=False):
    """Run the tests."""
    logger.info(f"Running tests for category: {category}")
    
    # Prepare environment variables
    env = os.environ.copy()
    env["USE_REAL_LLM"] = "true" if use_real_llm else "false"
    env["USE_RESPONSE_CACHE"] = "true" if use_cache else "false"
    
    # Prepare the test path
    if category == "all":
        test_path = str(AUTO_TESTS_DIR)
    else:
        test_path = str(AUTO_TESTS_DIR / category)
    
    # Prepare pytest arguments
    pytest_args = ["-v"] if verbose else []
    
    try:
        # Run the tests
        result = subprocess.run(
            [sys.executable, "-m", "pytest", test_path] + pytest_args,
            env=env,
            check=False  # Don't exit if tests fail
        )
        
        if result.returncode != 0:
            logger.warning(f"Some tests failed. Exit code: {result.returncode}")
        else:
            logger.info("All tests passed successfully.")
            
        return result.returncode
    except Exception as e:
        logger.error(f"Error running tests: {e}")
        return 1


def main():
    """Main entry point."""
    args = parse_arguments()
    
    # Make sure directories exist
    os.makedirs(AUTO_TESTS_DIR, exist_ok=True)
    
    # Generate tests if required
    if not args.no_generate:
        generate_tests()
    else:
        logger.info("Skipping test generation as requested.")
    
    # Run the tests
    exit_code = run_tests(
        category=args.category,
        use_real_llm=args.use_real_llm,
        use_cache=not args.no_cache,
        verbose=args.verbose
    )
    
    # Exit with the appropriate code
    sys.exit(exit_code)


if __name__ == "__main__":
    main() 
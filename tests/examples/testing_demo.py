#!/usr/bin/env python3
"""
Testing Framework Demo

This script demonstrates how to use the testing framework with specific decorators.
It shows both manual testing and how to interact with the auto-generated tests.
"""

import os
import sys
import argparse
from pathlib import Path

# Add parent directory to path so we can import helpers
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.test_helpers import (
    LLMClient, 
    check_expectation,
    validate_decorator_in_prompt,
    combine_decorators
)

# Initialize the client
llm_client = LLMClient(
    use_real_llm=os.getenv("USE_REAL_LLM", "false").lower() == "true",
    use_cache=os.getenv("USE_RESPONSE_CACHE", "true").lower() == "true"
)


def demo_manual_testing():
    """Demonstrate manual testing of decorators."""
    print("\n=== Demo: Manual Testing ===\n")
    
    # 1. Test a simple Bullet decorator
    prompt = "+++Bullet\nList the benefits of exercise."
    print(f"Testing prompt: {prompt}")
    
    response = llm_client.generate(prompt)
    print("\nResponse:")
    print(response)
    
    # Check if the response contains bullet points
    has_bullets = check_expectation(response, "contains_bullet_points")
    print(f"\nContains bullet points: {has_bullets}")
    
    # 2. Test a more complex combination
    prompt = "+++Reasoning\n+++StepByStep\nExplain how to implement a binary search algorithm."
    print(f"\nTesting prompt: {prompt}")
    
    response = llm_client.generate(prompt)
    print("\nResponse (truncated):")
    print("\n".join(response.split("\n")[:10]) + "\n...")
    
    # Check specific expectations
    has_steps = check_expectation(response, "contains_numbered_steps")
    has_reasoning = "because" in response.lower() or "therefore" in response.lower()
    
    print(f"\nContains numbered steps: {has_steps}")
    print(f"Contains reasoning elements: {has_reasoning}")
    
    # 3. Test parameter validation
    print("\nTesting parameter validation:")
    
    try:
        validate_decorator_in_prompt("+++Reasoning(depth=invalid)\nTest prompt.")
        print("❌ Validation should have failed but didn't")
    except Exception as e:
        print(f"✅ Validation correctly failed: {e}")


def demo_compatibility_testing():
    """Demonstrate compatibility testing between decorators."""
    print("\n=== Demo: Compatibility Testing ===\n")
    
    # Test compatible decorators
    compatible_pairs = [
        ("Reasoning", "StepByStep"),
        ("Academic", "CiteSources"),
        ("Bullet", "Concise")
    ]
    
    print("Testing compatible decorator pairs:")
    for pair in compatible_pairs:
        result = combine_decorators(pair)
        status = "✅ Compatible" if result["compatible"] else f"❌ Incompatible: {result['message']}"
        print(f"  {pair[0]} + {pair[1]}: {status}")
    
    # Test incompatible decorators
    incompatible_pairs = [
        ("Concise", "Detailed"),
        ("ELI5", "Academic"),
        ("Bullet", "OutputFormat")
    ]
    
    print("\nTesting incompatible decorator pairs:")
    for pair in incompatible_pairs:
        result = combine_decorators(pair)
        status = "❌ Correctly identified as incompatible" if not result["compatible"] else "❓ Incorrectly identified as compatible"
        print(f"  {pair[0]} + {pair[1]}: {status}")


def demo_expectations_checking():
    """Demonstrate checking different types of expectations."""
    print("\n=== Demo: Expectations Checking ===\n")
    
    expectations = [
        ("contains_bullet_points", "- This is a bullet point\n- This is another bullet point"),
        ("contains_numbered_steps", "1. First step\n2. Second step\n3. Third step"),
        ("is_concise", "This is a short response."),
        ("has_formal_language", "The research indicates that these findings are significant. Furthermore, the methodology demonstrates robust experimental design."),
        ("is_valid_json", '{"name": "John", "age": 30, "city": "New York"}'),
        ("contains_comparison", "X is better than Y in terms of efficiency, but Y outperforms X in reliability."),
        ("contains_pros_and_cons", "Pros: Easy to use, affordable, reliable. Cons: Limited features, slow performance.")
    ]
    
    print("Testing different expectation types:")
    
    for expectation_type, test_text in expectations:
        result = check_expectation(test_text, expectation_type)
        status = "✅ Correctly matched" if result else "❌ Did not match"
        print(f"  {expectation_type}: {status}")
        print(f"    Text: {test_text[:50]}{'...' if len(test_text) > 50 else ''}\n")


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Demonstrate the testing framework")
    parser.add_argument(
        "--use-real-llm", 
        action="store_true",
        help="Use real LLM API for demos (requires API keys)"
    )
    parser.add_argument(
        "--no-cache", 
        action="store_true",
        help="Disable response caching"
    )
    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_arguments()
    
    # Set environment variables for the helpers
    if args.use_real_llm:
        os.environ["USE_REAL_LLM"] = "true"
    
    if args.no_cache:
        os.environ["USE_RESPONSE_CACHE"] = "false"
    
    # Run the demos
    print("\n=== PROMPT DECORATORS TESTING FRAMEWORK DEMO ===\n")
    print(f"Using real LLM: {os.getenv('USE_REAL_LLM', 'false')}")
    print(f"Using response cache: {os.getenv('USE_RESPONSE_CACHE', 'true')}")
    
    demo_manual_testing()
    demo_compatibility_testing()
    demo_expectations_checking()
    
    print("\n=== Demo Complete ===\n")
    
    print("Next Steps:")
    print("1. Generate tests: python scripts/generate_tests.py")
    print("2. Run tests: python scripts/run_tests.py")
    print("3. Explore test files in: tests/auto/")


if __name__ == "__main__":
    main() 
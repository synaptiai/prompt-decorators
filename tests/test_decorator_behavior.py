#!/usr/bin/env python
"""
Decorator Behavior Test Script

This script tests prompt decorators with actual AI models to verify their behavior.
It requires an API key for the model service being tested.
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Try to import OpenAI and other optional dependencies
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

# --- Configuration ---

# Add the prompt-decorators directory to the path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Base prompt for testing
DEFAULT_TEST_PROMPT = "Explain quantum computing in simple terms."

# --- Helper Functions ---

def load_decorator(decorator_path):
    """Load a decorator from a JSON file"""
    with open(decorator_path, 'r') as f:
        return json.load(f)

def format_decorator(decorator_data, parameter_values=None):
    """Format a decorator with optional parameter values"""
    name = decorator_data["decoratorName"]
    params = parameter_values or {}
    
    # Use default values for missing parameters
    for param in decorator_data.get("parameters", []):
        if param["name"] not in params and "default" in param:
            params[param["name"]] = param["default"]
    
    # Format parameters string if any parameters are provided
    params_str = ""
    if params:
        params_str = "(" + ", ".join(f"{k}={v}" for k, v in params.items()) + ")"
    
    return f"+++{name}{params_str}"

def run_test_with_openai(prompt, model="gpt-3.5-turbo"):
    """Run a test with OpenAI's API"""
    if not OPENAI_AVAILABLE:
        print("OpenAI package not installed. Run: pip install openai")
        return None
    
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        return None
        
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that follows prompt decorators."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def run_test_with_anthropic(prompt, model="claude-3-opus-20240229"):
    """Run a test with Anthropic's API"""
    if not ANTHROPIC_AVAILABLE:
        print("Anthropic package not installed. Run: pip install anthropic")
        return None
    
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        return None
        
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=model,
        system="You are a helpful assistant that follows prompt decorators.",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.content[0].text

def main():
    parser = argparse.ArgumentParser(description="Test prompt decorators with AI models")
    parser.add_argument("decorator_path", help="Path to the decorator JSON file")
    parser.add_argument("--prompt", help="Test prompt to use", default=DEFAULT_TEST_PROMPT)
    parser.add_argument("--provider", choices=["openai", "anthropic"], default="openai",
                        help="AI provider to use for testing (default: openai)")
    parser.add_argument("--model", help="Model to use for testing")
    parser.add_argument("--param", action="append", nargs=2, metavar=("NAME", "VALUE"),
                        help="Parameter value to use (can be specified multiple times)")
    args = parser.parse_args()
    
    # Load the decorator
    try:
        decorator_data = load_decorator(args.decorator_path)
        print(f"Testing decorator: {decorator_data['decoratorName']}")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading decorator: {e}")
        return 1
    
    # Format parameters
    params = {}
    if args.param:
        for name, value in args.param:
            # Try to convert string values to appropriate types
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            elif value.isdigit():
                value = int(value)
            elif value.replace(".", "", 1).isdigit():
                value = float(value)
            params[name] = value
    
    # Format the decorator and prompt
    decorator_str = format_decorator(decorator_data, params)
    test_prompt = f"{decorator_str}\n{args.prompt}"
    
    print("\n--- Test Prompt ---")
    print(test_prompt)
    print("-------------------\n")
    
    # Select the provider and model
    provider = args.provider
    model = args.model
    
    if provider == "openai":
        if not model:
            model = "gpt-3.5-turbo"
        print(f"Testing with OpenAI: {model}")
        result = run_test_with_openai(test_prompt, model)
    elif provider == "anthropic":
        if not model:
            model = "claude-3-opus-20240229"
        print(f"Testing with Anthropic: {model}")
        result = run_test_with_anthropic(test_prompt, model)
    else:
        print(f"Unsupported provider: {provider}")
        return 1
    
    if result:
        print("\n--- Result ---")
        print(result)
        print("-------------\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 
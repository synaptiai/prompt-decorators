#!/usr/bin/env python
"""
TreeOfThought Decorator Example

This script demonstrates the use of the TreeOfThought decorator with various parameters
and shows how it affects the output of different AI models.
"""

import os
import sys
import json
from pathlib import Path

# Add the parent directory to the path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

try:
    import openai
except ImportError:
    print("OpenAI package not installed. Run: pip install openai")
    sys.exit(1)

# Load the TreeOfThought decorator definition
DECORATOR_FILE = Path(__file__).resolve().parent.parent.parent / "registry/core/reasoning/tree-of-thought.json"
with open(DECORATOR_FILE, 'r') as f:
    TREE_OF_THOUGHT = json.load(f)

# Example prompts to test the decorator with
TEST_PROMPTS = [
    "What strategies might help address climate change?",
    "How could we design a more effective educational system?",
    "What are different approaches to reducing traffic congestion in cities?"
]

def format_decorator(params=None):
    """Format the TreeOfThought decorator with optional parameters"""
    params = params or {}
    
    # Use default values for missing parameters
    for param in TREE_OF_THOUGHT.get("parameters", []):
        if param["name"] not in params and "default" in param:
            params[param["name"]] = param["default"]
    
    # Format parameters string if any parameters are provided
    params_str = ""
    if params:
        params_str = "(" + ", ".join(f"{k}={v}" for k, v in params.items()) + ")"
    
    return f"+++{TREE_OF_THOUGHT['decoratorName']}{params_str}"

def generate_response(prompt, model="gpt-3.5-turbo", params=None):
    """Generate a response using the TreeOfThought decorator"""
    # Format the decorator
    decorator = format_decorator(params)
    
    # Create the prompt with the decorator
    decorated_prompt = f"{decorator}\n{prompt}"
    
    print(f"\n--- Prompt with {decorator} ---")
    print(decorated_prompt)
    print("----------------------------")
    
    # Generate the response
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that follows prompt decorators."},
                {"role": "user", "content": decorated_prompt}
            ],
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {e}"

def run_tests():
    """Run a series of tests with different parameters and prompts"""
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        return

    models = ["gpt-3.5-turbo"]
    if os.environ.get("USE_GPT4") == "true":
        models.append("gpt-4")
    
    test_configurations = [
        {"params": {}, "description": "Default parameters (3 branches, depth 3, no pruning)"},
        {"params": {"branches": 2, "depth": 2}, "description": "Minimal branching (2 branches, depth 2)"},
        {"params": {"branches": 5, "depth": 5, "pruning": True}, "description": "Maximum branching with pruning"}
    ]
    
    for model in models:
        print(f"\n\n{'='*50}")
        print(f"Testing with model: {model}")
        print(f"{'='*50}")
        
        for prompt in TEST_PROMPTS:
            print(f"\n\n{'*'*50}")
            print(f"Testing prompt: {prompt}")
            print(f"{'*'*50}")
            
            for config in test_configurations:
                print(f"\n\n{'-'*50}")
                print(f"Configuration: {config['description']}")
                print(f"{'-'*50}")
                
                response = generate_response(prompt, model, config["params"])
                print("\n--- Response ---")
                print(response)
                print("-----------------")
                
                # Add a pause between requests to avoid rate limits
                input("\nPress Enter to continue to the next test...")

if __name__ == "__main__":
    print(f"Testing TreeOfThought decorator defined in: {DECORATOR_FILE}")
    run_tests() 
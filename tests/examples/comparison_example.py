#!/usr/bin/env python
"""Comparison Decorator Example.

This script demonstrates the use of the Comparison decorator with various parameters
and shows how it affects the output of different AI models when comparing items.
"""

import json
import os
import sys
from pathlib import Path

# Add the parent directory to the path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

try:
    import openai
except ImportError:
    print("OpenAI package not installed. Run: pip install openai")
    sys.exit(1)

# Load the Comparison decorator definition
DECORATOR_FILE = (
    Path(__file__).resolve().parent.parent.parent
    / "registry/core/structure/comparison.json"
)
with open(DECORATOR_FILE, "r") as f:
    COMPARISON = json.load(f)

# Example prompts to test the decorator with
TEST_PROMPTS = [
    "Compare Python, JavaScript, and Java as programming languages for beginners.",
    "Compare electric, hybrid, and gas vehicles in terms of cost, environmental impact, and performance.",
    "Compare different approaches to remote work: fully remote, hybrid, and fully in-office.",
]


def format_decorator(params=None):
    """Format the Comparison decorator with optional parameters."""
    params = params or {}

    # Use default values for missing parameters
    for param in COMPARISON.get("parameters", []):
        if param["name"] not in params and "default" in param:
            params[param["name"]] = param["default"]

    # Format parameters string if any parameters are provided
    params_str = ""
    if params:
        # Special handling for arrays
        formatted_params = []
        for k, v in params.items():
            if isinstance(v, list):
                v_str = f"[{','.join(v)}]"
                formatted_params.append(f"{k}={v_str}")
            else:
                formatted_params.append(f"{k}={v}")

        params_str = "(" + ", ".join(formatted_params) + ")"

    return f"+++{COMPARISON['decoratorName']}{params_str}"


def generate_response(prompt, model="gpt-4-turbo", params=None):
    """Generate a response using the Comparison decorator."""
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
                {
                    "role": "system",
                    "content": "You are a helpful assistant that follows prompt decorators.",
                },
                {"role": "user", "content": decorated_prompt},
            ],
            max_tokens=1000,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {e}"


def run_tests():
    """Run a series of tests with different parameters and prompts."""
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        return

    models = ["gpt-4-turbo"]
    if os.environ.get("USE_GPT4") == "true":
        models.append("gpt-4o")

    test_configurations = [
        {
            "params": {},
            "description": "Default parameters (table format with highlighting)",
        },
        {
            "params": {"format": "prose", "highlight": False},
            "description": "Prose format without highlighting",
        },
        {
            "params": {
                "aspects": [
                    "learning curve",
                    "job market",
                    "community support",
                    "performance",
                ],
                "format": "bullets",
            },
            "description": "Bullets with specific aspects",
        },
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
    print(f"Testing Comparison decorator defined in: {DECORATOR_FILE}")
    run_tests()

"""
OpenAI Prompt Decorator Demo with Dynamic Decorators

This module provides the core functionality for demonstrating prompt decorators
with the OpenAI API, using dynamic decorators instead of the generated ones.
It includes functionality for applying decorators to prompts, making API calls,
and handling responses.
"""

import json
import os
import re
from dataclasses import dataclass
from typing import Any, Collection, Dict, List, Optional, Tuple, Union

import typer
from openai import OpenAI

# Import utility modules
from demo.utils.config import load_config, load_config_value, validate_config
from demo.utils.logging import log_decorated_prompt, log_error, log_info, log_response

# Import the dynamic decorators module
from prompt_decorators.dynamic_decorators_module import (
    create_decorator,
    list_available_decorators,
    transform_prompt,
)

# Define regex patterns for decorator parsing
DECORATOR_PATTERN = re.compile(
    r"(?P<prefix>\+{3})?(?P<n>[A-Za-z0-9_]+)(?:\((?P<params>.*?)\))?$"
)
PARAM_PATTERN = re.compile(
    r"(?P<n>[A-Za-z0-9_]+)\s*=\s*(?P<value>\".*?\"|\'.*?\'|[^,]+)"
)

# Default prompt used when none is provided
DEFAULT_PROMPT = "Tell me about the future of artificial intelligence."

# Example configurations for different decorators
EXAMPLES = {
    "step_by_step": {
        "prompt": "How do I build a website?",
        "decorators": ["+++StepByStep(numbered=true)"],
        "description": "Break down complex tasks into clear, numbered steps",
    },
    "technical": {
        "prompt": "Explain how machine learning works",
        "decorators": ["+++Tone(style=technical)"],
        "description": "Use a technical tone suitable for experts",
    },
    "eli5": {
        "prompt": "How does quantum computing work?",
        "decorators": ["+++ELI5"],
        "description": "Explain Like I'm 5 - simple explanations for complex topics",
    },
    "coding": {
        "prompt": "Write a Python function to find prime numbers",
        "decorators": [
            "+++CodeStandards(standard=pep8)",
            "+++BestPractices(for=python)",
        ],
        "description": "Generate code that follows best practices and coding standards",
    },
    "creative": {
        "prompt": "Write a short story about AI",
        "decorators": ["+++Creative", "+++Tone(style=narrative)"],
        "description": "Enhance creativity and use a narrative tone",
    },
    "analysis": {
        "prompt": "Analyze the pros and cons of remote work",
        "decorators": [
            "+++Tradeoffs(axes=productivity,wellbeing,collaboration)",
            "+++BalancedView",
        ],
        "description": "Create a balanced analysis with multiple perspectives",
    },
}

app = typer.Typer(
    help="OpenAI Prompt Decorator Demo - Showcase dynamic prompt decorators with OpenAI"
)


@dataclass
class Args:
    prompt: Optional[str] = None
    decorators: Optional[List[str]] = None
    model: Optional[str] = None
    example: Optional[str] = None
    decorator: Optional[str] = None


def initialize_openai_client() -> OpenAI:
    """
    Initialize the OpenAI client with API key from environment or config.

    Returns:
        OpenAI: Initialized OpenAI client
    """
    # Load configuration
    config = load_config()

    # Get API key from environment or config
    api_key = os.getenv("OPENAI_API_KEY") or config.get("openai", {}).get("api_key")
    if not api_key:
        raise ValueError(
            "OpenAI API key not found. Please set it in .env file or config.json"
        )

    # Initialize client
    return OpenAI(api_key=api_key)


def parse_decorator_string(decorator_str: str) -> Tuple[Optional[str], Dict[str, Any]]:
    """
    Parse a decorator string into name and parameters.

    Args:
        decorator_str: String representation of a decorator (e.g., "+++StepByStep(numbered=true)")

    Returns:
        Tuple[Optional[str], Dict[str, Any]]: (decorator_name, parameters) or (None, {}) if parsing fails
    """
    decorator_match = DECORATOR_PATTERN.match(decorator_str)
    if not decorator_match:
        log_error(f"Invalid decorator format: {decorator_str}")
        return None, {}

    name = decorator_match.group("n")
    params_str = decorator_match.group("params") or ""

    # Parse parameters
    params = {}
    if params_str:
        # Handle simple key=value params
        param_matches = re.finditer(PARAM_PATTERN, params_str)
        for param_match in param_matches:
            param_name = param_match.group("n")
            param_value = param_match.group("value").strip("\"'")

            # Convert string representations of booleans to actual boolean values
            if param_value.lower() == "true":
                param_value = True
            elif param_value.lower() == "false":
                param_value = False
            # Convert string representations of numeric values to actual numeric values
            elif param_value.replace(".", "", 1).isdigit():
                # Check if it's a float (contains a decimal point)
                if "." in param_value:
                    param_value = float(param_value)
                else:
                    param_value = int(param_value)

            params[param_name] = param_value

    return name, params


def apply_dynamic_decorators(
    prompt: str, decorator_strings: Union[List[str], Collection[str]]
) -> str:
    """
    Apply a list of decorators to a prompt using the dynamic decorator implementation.

    Args:
        prompt: The original prompt to decorate
        decorator_strings: List of decorator strings (e.g., ["+++StepByStep(numbered=true)"])

    Returns:
        str: The decorated prompt
    """
    try:
        log_info(
            f"Applying {len(decorator_strings)} decorators using dynamic implementation"
        )

        # Track original prompt for logging
        original_prompt = prompt

        # Apply each decorator individually for better logging
        for decorator_string in decorator_strings:
            # Extract decorator name and parameters
            name, params = parse_decorator_string(decorator_string)
            if not name:
                continue

            # For logging only - store current state before applying this decorator
            prompt_before = prompt

            try:
                # Create and apply a single decorator
                decorator = create_decorator(name, **params)
                prompt = decorator(prompt)

                # Log the transformation
                log_info(f"Applied {name} decorator")
                log_decorated_prompt(prompt_before, decorator_string, prompt)
            except Exception as e:
                log_error(f"Error applying decorator {name}: {str(e)}")

        return prompt
    except Exception as e:
        log_error(f"Error applying decorators: {str(e)}")
        return prompt


def query_with_decorators(
    prompt: str,
    decorators: Union[List[str], Collection[str]],
    model: Optional[str] = None,
) -> str:
    """
    Send a prompt with applied decorators to OpenAI and return the response.

    Args:
        prompt: The prompt to send
        decorators: List of decorator strings to apply
        model: OpenAI model to use

    Returns:
        str: The response from OpenAI
    """
    try:
        # Load configuration
        config = load_config()
        validate_config(config)

        # Apply decorators to the prompt
        decorated_prompt = apply_dynamic_decorators(prompt, decorators)

        # Initialize OpenAI client
        client = initialize_openai_client()

        # Set model and temperature from config if not provided
        if not model:
            # Use the default model from config
            model = config.get("openai", {}).get("default_model", "gpt-4o")

        # Get temperature from config
        temperature = float(config.get("openai", {}).get("temperature", 0.7))

        # Log the API call details
        log_info(f"Sending API request to OpenAI")
        log_info(f"Model: {model}")
        log_info(f"Temperature: {temperature}")

        # Make the API call
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": decorated_prompt},
            ],
        )

        # Extract and return the response content
        if response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content
            log_response(content)
            return content
        else:
            log_error("No response received from OpenAI")
            return "Error: No response received"

    except Exception as e:
        log_error(f"Error querying OpenAI: {str(e)}")
        return f"Error: {str(e)}"


@app.command()
def run_custom_prompt(
    prompt: str = typer.Option(..., help="The prompt to send to OpenAI"),
    decorator: List[str] = typer.Option(
        [], help="Decorator to apply (can be used multiple times)"
    ),
    model: Optional[str] = typer.Option(
        None, help="OpenAI model to use (defaults to value from config)"
    ),
    temperature: float = typer.Option(
        None, help="Sampling temperature (0.0-2.0) (defaults to value from config)"
    ),
) -> None:
    """
    Run a custom prompt with specified decorators.
    """
    # Update config with temperature if provided
    if temperature is not None:
        config = load_config()
        config["temperature"] = temperature
        with open("config.json", "w") as f:
            json.dump(config, f, indent=2)

    response = query_with_decorators(prompt, decorator, model)
    log_info("Response received from OpenAI")


@app.callback(invoke_without_command=True)
def main(
    prompt: Optional[str] = typer.Option(
        None, "--prompt", "-p", help="The prompt to send to OpenAI"
    ),
    decorators: Optional[List[str]] = typer.Option(
        None,
        "--decorator",
        "-d",
        help="Decorator to apply (can be used multiple times)",
    ),
    model: Optional[str] = typer.Option(
        None, "--model", "-m", help="OpenAI model to use"
    ),
    list_examples: bool = typer.Option(
        False, "--list-examples", "-l", help="List available decorator examples"
    ),
    example: Optional[str] = typer.Option(
        None, "--example", "-e", help="Run a specific decorator example"
    ),
    list_decorators: bool = typer.Option(
        False, "--list-decorators", help="List all available decorators"
    ),
) -> None:
    """
    OpenAI Prompt Decorator Demo - Showcase dynamic prompt decorators with OpenAI.

    This application demonstrates how to use dynamic prompt decorators with the OpenAI API
    to enhance LLM outputs across various use cases.
    """
    try:
        # Create Args object to store command arguments
        args = Args(
            prompt=prompt,
            decorators=decorators,
            model=model,
            example=example,
        )

        # Handle --list-examples flag
        if list_examples:
            log_info("Available examples:")
            for name, example_data in EXAMPLES.items():
                log_info(f"  - {name}: {example_data['description']}")
                log_info(f"    Prompt: {example_data['prompt']}")
                log_info(f"    Decorators: {', '.join(example_data['decorators'])}")
                log_info("")
            return

        # Handle --list-decorators flag
        if list_decorators:
            log_info("Available dynamic decorators:")
            available = list_available_decorators()
            for decorator_name in sorted(available):
                log_info(f"  - {decorator_name}")
            return

        # Handle --example flag
        if example:
            run_example(args)
            return

        # Handle prompt and decorators
        if prompt or decorators:
            handle_prompt_and_decorators(args)
    except Exception as e:
        log_error(f"Error: {str(e)}")


def run_example(args: Args) -> None:
    """
    Run a specific example from the predefined examples.

    Args:
        args: Command arguments
    """
    example_name = args.example
    if not example_name:
        log_error("No example name provided")
        return

    # Check if the example exists
    if example_name not in EXAMPLES:
        log_error(f"Example '{example_name}' not found")
        log_info("Available examples:")
        for name in EXAMPLES:
            log_info(f"  - {name}")
        return

    # Get the example data
    example_data = EXAMPLES[example_name]
    prompt = example_data["prompt"]
    decorators = example_data["decorators"]

    log_info(f"Running example: {example_name}")
    log_info(f"Description: {example_data['description']}")
    log_info(f"Prompt: {prompt}")
    log_info(f"Decorators: {', '.join(decorators)}")

    # Run the example
    response = query_with_decorators(prompt, decorators, args.model)
    log_info("Response received from OpenAI")


def handle_prompt_and_decorators(args: Args) -> None:
    """
    Handle prompt and decorators provided in the command arguments.

    Args:
        args: Command arguments
    """
    # Use default prompt if none provided
    prompt = args.prompt or DEFAULT_PROMPT
    decorators = args.decorators or []

    if not decorators:
        log_info("No decorators specified, using undecorated prompt")
        log_info(f"Prompt: {prompt}")
    else:
        log_info(f"Using {len(decorators)} decorators")
        log_info(f"Prompt: {prompt}")
        log_info(f"Decorators: {', '.join(decorators)}")

    # Run the query
    response = query_with_decorators(prompt, decorators, args.model)
    log_info("Response received from OpenAI")


if __name__ == "__main__":
    app()

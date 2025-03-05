"""
OpenAI Prompt Decorator Demo

This module provides the core functionality for demonstrating prompt decorators
with the OpenAI API. It includes functionality for applying decorators to prompts,
making API calls, and handling responses.
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Collection, Dict, List, Optional, Tuple, Union, cast

import typer
from openai import OpenAI

from demo.utils import logging as logger

# Import utility modules
from demo.utils.config import load_config, load_config_value, validate_config
from demo.utils.logging import log_decorated_prompt, log_error, log_info, log_response

# Import base classes
from prompt_decorators.core.base import BaseDecorator

# Import decorators
# Either import from auto/format/audience directories or from generated.decorators, not both
from prompt_decorators.decorators.generated.decorators import (  # Basic decorators; Format-related decorators; Advanced reasoning decorators; Critical thinking decorators; Comparison and decision decorators; Expert and role-based decorators; Quality and verification decorators; Creativity and style decorators; Collaborative and iterative decorators; Uncertainty and debate decorators; Specialized decorators; Custom decorator
    ELI5,
    MECE,
    Abductive,
    Academic,
    Alternatives,
    Analogical,
    AsExpert,
    Audience,
    Balanced,
    BlindSpots,
    BreakAndBuild,
    BuildOn,
    Bullet,
    Chain,
    CiteSources,
    Comparison,
    Compatibility,
    Concise,
    Conditional,
    Confidence,
    Constraints,
    Context,
    Contrarian,
    Creative,
    Custom,
    Debate,
    DecisionMatrix,
    Deductive,
    Detailed,
    Extension,
    Extremes,
    FactCheck,
    FindGaps,
    FirstPrinciples,
    ForcedAnalogy,
    Inductive,
    Layered,
    Limitations,
    Motivational,
    Narrative,
    NegativeSpace,
    Nested,
    Outline,
    OutputFormat,
    Override,
    PeerReview,
    Persona,
    Precision,
    Prioritize,
    Priority,
    Professional,
    QualityMetrics,
    Reasoning,
    RedTeam,
    Refine,
    Remix,
    RootCause,
    Schema,
    Socratic,
    Steelman,
    StepByStep,
    StressTest,
    StyleShift,
    Summary,
    TableFormat,
    Timeline,
    Tone,
    TreeOfThought,
    Uncertainty,
    Version,
)

# Define regex patterns for decorator parsing
DECORATOR_PATTERN = re.compile(
    r"(?P<prefix>\+{3})?(?P<name>[A-Za-z0-9_]+)(?:\((?P<params>.*?)\))?$"
)
PARAM_PATTERN = re.compile(
    r"(?P<name>[A-Za-z0-9_]+)\s*=\s*(?P<value>\".*?\"|\'.*?\'|[^,]+)"
)

# Default prompt used when none is provided
DEFAULT_PROMPT = "Tell me about the future of artificial intelligence."

# Example configurations for different decorators
EXAMPLES = {
    "Reasoning": {
        "prompt": "What are the ethical implications of AI?",
        "params": {"depth": "comprehensive"},
    },
    "StepByStep": {"prompt": "How do I learn to play the piano?", "params": {}},
    "NegativeSpace": {
        "prompt": "What are the risks of autonomous vehicles?",
        "params": {"focus": "blindspots", "depth": "comprehensive"},
    },
    "OutputFormat": {
        "prompt": "Compare Python, JavaScript, and Rust",
        "params": {"format": "markdown"},
    },
    "Tone": {
        "prompt": "Explain quantum computing",
        "params": {"style": "enthusiastic"},
    },
    "Audience": {
        "prompt": "Explain neural networks",
        "params": {"expertise": "beginner"},
    },
}

# Initialize Typer app
app = typer.Typer()

from dataclasses import dataclass


# Define Args class at module level for type checking
@dataclass
class Args:
    prompt: Optional[str] = None
    decorators: Optional[List[str]] = None
    model: Optional[str] = None
    example: Optional[str] = None
    decorator: Optional[str] = None


def initialize_openai_client() -> OpenAI:
    """
    Initialize and return an OpenAI client with the API key from config.

    Returns:
        OpenAI: Configured OpenAI client instance

    Raises:
        ValueError: If the OpenAI API key is missing or invalid
    """
    config = load_config()
    validate_config(config)

    return OpenAI(api_key=config.get("OPENAI_API_KEY"))


def parse_decorator_string(decorator_str: str) -> Tuple[Optional[str], Dict[str, Any]]:
    """
    Parse a decorator string into name and parameters.

    Args:
        decorator_str: Decorator string (e.g., "+++Reasoning(depth=comprehensive)")

    Returns:
        Tuple of (decorator_name, params_dict)
    """
    # Extract decorator name and parameters
    decorator_match = DECORATOR_PATTERN.match(decorator_str)
    if not decorator_match:
        logger.log_error(f"Invalid decorator format: {decorator_str}")
        return None, {}

    name = decorator_match.group("name")
    params_str = decorator_match.group("params") or ""

    # Parse parameters
    params = {}
    if params_str:
        # Handle simple key=value params
        param_matches = re.finditer(PARAM_PATTERN, params_str)
        for param_match in param_matches:
            param_name = param_match.group("name")
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


# Dictionary of available decorators
available_decorators = {
    "Reasoning": Reasoning,
    "StepByStep": StepByStep,
    "NegativeSpace": NegativeSpace,
    "OutputFormat": OutputFormat,
    "Tone": Tone,
    "Audience": Audience,
    "TreeOfThought": TreeOfThought,
    "Detailed": Detailed,
    "Concise": Concise,
    "Summary": Summary,
    "Context": Context,
    "TableFormat": TableFormat,
    "Bullet": Bullet,
    "Outline": Outline,
    "Socratic": Socratic,
    "FirstPrinciples": FirstPrinciples,
    "Deductive": Deductive,
    "Inductive": Inductive,
    "Abductive": Abductive,
    "Analogical": Analogical,
    "Contrarian": Contrarian,
    "RedTeam": RedTeam,
    "Steelman": Steelman,
    "FindGaps": FindGaps,
    "Limitations": Limitations,
    "BlindSpots": BlindSpots,
    "ForcedAnalogy": ForcedAnalogy,
    "Comparison": Comparison,
    "DecisionMatrix": DecisionMatrix,
    "Alternatives": Alternatives,
    "BreakAndBuild": BreakAndBuild,
    "RootCause": RootCause,
    "Prioritize": Prioritize,
    "AsExpert": AsExpert,
    "Persona": Persona,
    "Academic": Academic,
    "Professional": Professional,
    "ELI5": ELI5,
    "Layered": Layered,
}


def create_decorator_instance(
    class_name: str, params: Dict[str, Any]
) -> Optional[BaseDecorator]:
    """
    Create an instance of a decorator class with the given parameters.

    Args:
        class_name: Name of the decorator class to instantiate
        params: Dictionary of parameters to pass to the constructor

    Returns:
        BaseDecorator: Instance of the decorator class, or None if it could not be created
    """
    # Create a case-insensitive dictionary lookup
    available_decorators_insensitive = {
        k.lower(): v for k, v in available_decorators.items()
    }

    # Check if the decorator exists (case-insensitive)
    if class_name.lower() not in available_decorators_insensitive:
        logger.log_error(f"Decorator '{class_name}' not found in available decorators")
        return None

    # Get the correct case for the class name
    for original_name, decorator_class in available_decorators.items():
        if original_name.lower() == class_name.lower():
            class_name = original_name
            break

    # Get the decorator class
    decorator_class = available_decorators_insensitive[class_name.lower()]

    try:
        # Create and return an instance of the decorator
        decorator_instance: BaseDecorator = decorator_class(**params)
        return decorator_instance
    except Exception as e:
        logger.log_error(f"Error creating decorator '{class_name}': {str(e)}")
        return None


def apply_decorators(
    prompt: str, decorator_strings: Union[list[str], Collection[str]]
) -> tuple[str, list[BaseDecorator]]:
    """
    Apply a list of decorators to a prompt.

    Args:
        prompt: The original prompt to decorate
        decorator_strings: List of decorator strings (e.g., ["+++Reasoning(depth=comprehensive)"])

    Returns:
        tuple: (decorated_prompt, list of applied decorators)
    """
    original_prompt = prompt
    applied_decorators = []

    # Store the applied decorator strings for logging
    applied_decorator_strings = []

    for decorator_string in decorator_strings:
        try:
            # Extract decorator name and parameters
            decorator_match = DECORATOR_PATTERN.match(decorator_string)
            if not decorator_match:
                logger.log_error(f"Invalid decorator format: {decorator_string}")
                continue

            prefix = decorator_match.group("prefix")
            name = decorator_match.group("name")
            params_str = decorator_match.group("params") or ""

            # Parse parameters
            params = {}
            if params_str:
                # Handle simple key=value params
                param_matches = re.finditer(PARAM_PATTERN, params_str)
                for param_match in param_matches:
                    param_name = param_match.group("name")
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

            # Create the decorator instance
            decorator = create_decorator_instance(name, params)
            if decorator:
                # Store the applied decorator string for logging
                applied_decorator_strings.append(decorator_string)

                # Apply the decorator's transformation to the prompt
                original_prompt_for_log = prompt  # Store current prompt for logging
                prompt = decorator.apply_to_prompt(prompt)

                logger.log_info(f"Applied {name} decorator")

                # Log comparison for each transformation step
                logger.log_decorated_prompt(
                    original_prompt_for_log, decorator_string, prompt
                )

                applied_decorators.append(decorator)
            else:
                logger.log_error(f"Decorator {name} not found or could not be created")
        except Exception as e:
            logger.log_error(f"Error applying decorator {decorator_string}: {str(e)}")

    return prompt, applied_decorators


def query_with_decorators(
    prompt: str,
    decorators: Union[List[str], Collection[str]],
    model: Optional[str] = None,
) -> str:
    """
    Query OpenAI with a prompt decorated with the specified decorators.

    Args:
        prompt: The original prompt to be decorated
        decorators: List of decorator strings
        model: Optional model override

    Returns:
        str: The model's response
    """
    try:
        # Initialize the OpenAI client
        client = OpenAI(
            api_key=load_config_value("OPENAI_API_KEY", "openai_api_key"),
        )

        # Apply decorators to the prompt
        decorated_prompt, applied_decorators = apply_decorators(
            prompt, list(decorators)
        )

        # Get model from config or use provided override
        model_name = model or load_config_value("DEFAULT_MODEL", "default_model")

        # Log the final prompt being sent to OpenAI
        logger.log_info(f"Querying OpenAI with model: {model_name}")

        # Print the actual prompt that will be sent to OpenAI
        logger.log_final_prompt(decorated_prompt)

        # Make the API call
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": decorated_prompt}],
            temperature=0.7,
        )

        # Extract and return the response text
        response_text = response.choices[0].message.content
        if response_text is None:
            response_text = ""  # Convert None to empty string

        # Apply any response transformations from decorators
        for decorator in applied_decorators:
            if hasattr(decorator, "transform_response") and callable(
                decorator.transform_response
            ):
                try:
                    # Ensure response_text is str, not None
                    response_text = decorator.transform_response(response_text)
                except Exception as e:
                    logger.log_error(
                        f"Error transforming response with {decorator.__class__.__name__}: {str(e)}"
                    )

        # Create a descriptive title for the response
        decorator_names = [d.__class__.__name__ for d in applied_decorators]
        response_title = "Model Response"

        # Log the response with a descriptive title
        logger.log_response(response_text, title=response_title)

        return response_text

    except Exception as e:
        logger.log_error(f"Error querying OpenAI: {str(e)}")
        return str(f"Error: {str(e)}")


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
    log_info(f"Running custom prompt with {len(decorator)} decorators")

    response = query_with_decorators(prompt=prompt, decorators=decorator, model=model)

    log_response(response, title="Custom Prompt Response")


@app.callback()
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
) -> None:
    """
    OpenAI Prompt Decorator Demo Application

    This demo allows you to test and experiment with prompt decorators. You can:

    1. Apply decorators to a custom prompt
    2. Run pre-defined examples
    3. List available examples

    Examples:

    python main.py --prompt "How do neural networks work?" --decorator "StepByStep"
    python main.py --example "Reasoning"
    python main.py --list-examples
    """
    try:
        # Load and validate configuration
        config = load_config()
        validate_config(config)

        # Create an instance of Args
        args = Args(prompt=prompt, decorators=decorators, model=model, example=example)

        # Handle list examples request
        if list_examples:
            logger.log_info("Available decorator examples:")
            examples_dict = list_decorator_examples()
            for name, example_data in examples_dict.items():
                params_dict = (
                    example_data.get("params", {})
                    if isinstance(example_data, dict)
                    else {}
                )
                params_str = ", ".join([f"{k}={v}" for k, v in params_dict.items()])
                params_display = f"({params_str})" if params_str else ""
                prompt_text = (
                    example_data.get("prompt", "")
                    if isinstance(example_data, dict)
                    else ""
                )
                logger.log_info(f"  - {name}{params_display}: {prompt_text}")
            return

        # Handle example request
        if example:
            args.decorator = example
            run_example(args)
            return

        # Handle prompt and decorators
        handle_prompt_and_decorators(args)

    except Exception as e:
        logger.log_error(f"Error: {str(e)}")
        sys.exit(1)


def run_example(args: Args) -> None:
    """Run a specific decorator example."""
    # Get the decorator name from args
    decorator_name = args.decorator

    if decorator_name not in EXAMPLES:
        logger.log_error(f"No examples found for decorator '{decorator_name}'")
        logger.log_info(f"Available examples: {', '.join(EXAMPLES.keys())}")
        return

    # Get the example prompt and params
    example = EXAMPLES[decorator_name]
    prompt = example.get("prompt", DEFAULT_PROMPT)
    params: Dict[str, Any] = {}
    if "params" in example and isinstance(example["params"], dict):
        params = example["params"]

    # Format the decorator string
    param_str = ""
    if params:
        param_str = "(" + ", ".join([f"{k}={v}" for k, v in params.items()]) + ")"

    decorator_str = f"+++{decorator_name}{param_str}"

    logger.log_info(f"Running example for decorator: {decorator_name}")

    # Query with the decorator and explicitly ignore the return value
    if isinstance(prompt, str):
        _ = query_with_decorators(prompt, cast(List[str], [decorator_str]), args.model)
    else:
        # Convert prompt to string if it's not already
        _ = query_with_decorators(
            str(prompt), cast(List[str], [decorator_str]), args.model
        )


def handle_prompt_and_decorators(args: Args) -> None:
    """
    Handle the prompt and decorators provided by the user.

    Args:
        args: The command line arguments
    """
    # Get the prompt from args or use default
    prompt = args.prompt or DEFAULT_PROMPT

    # Get the decorators from args or use empty list
    decorator_list: List[str] = []
    if args.decorators is not None:
        decorator_list = list(args.decorators)

    if not decorator_list:
        logger.log_info(
            "No decorators specified. Run with --decorator to add decorators."
        )

    logger.log_info(f"Running with {len(decorator_list)} decorators")
    logger.log_info(f"Prompt: {prompt}")

    # Query with decorators and explicitly ignore the return value
    if isinstance(prompt, str):
        _ = query_with_decorators(prompt, decorator_list, args.model)
    else:
        logger.log_error("Prompt must be a string")
        return


def list_decorator_examples() -> Dict[str, Dict[str, Any]]:
    """
    List all available decorator examples.

    Returns:
        Dict[str, Dict[str, Any]]: Dictionary of example configurations
    """
    config = load_config()
    validate_config(config)

    return EXAMPLES


if __name__ == "__main__":
    typer.run(main)

"""
MCP Server for Prompt Decorators.

This module provides integration between Prompt Decorators and the Model Context Protocol (MCP),
exposing prompt decorators as MCP tools that can be used by any MCP client.

Implementation follows the official MCP SDK patterns and best practices.
"""

import copy
import logging
import sys
from typing import Any, Callable, Dict, List, Optional, cast

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print(
        "ERROR: MCP SDK not installed. Please install with: pip install mcp",
        file=sys.stderr,
    )
    sys.exit(1)

from prompt_decorators.dynamic_decorators_module import (
    apply_dynamic_decorators,
    get_available_decorators,
    load_decorator_definitions,
)

# Configure logging to stderr
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger("prompt-decorators-mcp")

# Make sure decorators are loaded
load_decorator_definitions()

# Create the MCP server
mcp = FastMCP("Prompt Decorators")


@mcp.tool()
def list_decorators() -> Dict[str, Any]:
    """
    Lists all available prompt decorators.

    Returns:
        A dictionary containing information about all available decorators.
    """
    logger.info("Listing all decorators")
    decorators = get_available_decorators()

    result = {}
    for decorator in decorators:
        result[decorator.name] = {
            "name": decorator.name,
            "description": decorator.description or "No description available",
            "category": decorator.category,
            "parameters": decorator.parameters,
        }

    return {"decorators": result}


@mcp.tool()
def get_decorator_details(name: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific decorator.

    Args:
        name: The name of the decorator to get details for.

    Returns:
        A dictionary containing detailed information about the decorator.
    """
    logger.info(f"Getting details for decorator: {name}")
    decorators = get_available_decorators()

    for decorator in decorators:
        if decorator.name == name:
            return {
                "name": decorator.name,
                "description": decorator.description or "No description available",
                "category": decorator.category,
                "parameters": decorator.parameters,
                "version": decorator.version,
            }

    return {
        "error": f"Decorator '{name}' not found",
        "available_decorators": [d.name for d in decorators],
    }


@mcp.tool()
def apply_decorators(prompt: str, decorators: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Apply decorators to a prompt using the +++ syntax.

    Args:
        prompt: The prompt text to decorate.
        decorators: List of decorators to apply, each with name and parameters.

    Returns:
        The decorated prompt with decorators applied.
    """
    logger.info(f"Applying {len(decorators)} decorators to prompt")

    # Format the prompt with +++ decorators syntax
    decorator_strings = []
    for decorator in decorators:
        name = decorator.get("name")
        params = decorator.get("parameters", {})

        param_str = ""
        if params:
            param_parts = []
            for key, value in params.items():
                param_parts.append(f"{key}={value}")
            param_str = " " + " ".join(param_parts)

        decorator_strings.append(f"+++{name}{param_str}")

    decorated_prompt = "\n".join(decorator_strings) + "\n\n" + prompt

    # Apply the decorators
    result = apply_dynamic_decorators(decorated_prompt)

    return {
        "original_prompt": prompt,
        "decorated_prompt": result,
        "applied_decorators": [d.get("name") for d in decorators],
    }


@mcp.tool()
def create_decorated_prompt(
    template_name: str, content: str, parameters: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Create a decorated prompt using a predefined template.

    Args:
        template_name: The name of the template to use.
        content: The content to include in the prompt.
        parameters: Optional parameters for customizing the template.

    Returns:
        The decorated prompt created from the template.
    """
    logger.info(f"Creating decorated prompt using template: {template_name}")

    # Define available templates
    templates = {
        "detailed-reasoning": {
            "description": "Enhanced critical thinking template with structured reasoning",
            "decorators": [
                {
                    "name": "SystemMessage",
                    "parameters": {
                        "message": "Analyze this problem step-by-step with detailed reasoning."
                    },
                },
                {"name": "Reasoning", "parameters": {"depth": "deep"}},
                {"name": "Structured", "parameters": {"format": "markdown"}},
            ],
        },
        "academic-analysis": {
            "description": "Academic style analysis with citations and formal tone",
            "decorators": [
                {"name": "Academic", "parameters": {"level": "advanced"}},
                {"name": "Citation", "parameters": {"style": "apa"}},
                {"name": "Formal", "parameters": {}},
            ],
        },
        "explain-simply": {
            "description": "Simplify complex topics for broader understanding",
            "decorators": [
                {
                    "name": "SystemMessage",
                    "parameters": {"message": "Explain this topic in simple terms."},
                },
                {"name": "Simplify", "parameters": {"level": "beginner"}},
                {"name": "Examples", "parameters": {"count": 2}},
            ],
        },
        "creative-storytelling": {
            "description": "Creative writing with storytelling elements",
            "decorators": [
                {"name": "Creative", "parameters": {"style": "narrative"}},
                {"name": "Engaging", "parameters": {}},
                {"name": "Vivid", "parameters": {"level": "high"}},
            ],
        },
        "problem-solving": {
            "description": "Structured approach to solving problems",
            "decorators": [
                {
                    "name": "SystemMessage",
                    "parameters": {"message": "Solve this problem methodically."},
                },
                {"name": "ProblemSolver", "parameters": {}},
                {"name": "StepByStep", "parameters": {}},
            ],
        },
    }

    if template_name not in templates:
        return {
            "error": f"Template '{template_name}' not found",
            "available_templates": list(templates.keys()),
        }

    template = templates[template_name]

    # Manual deep copy of decorator list to avoid type issues
    template_decorators: List[Dict[str, Any]] = []
    for decorator in template["decorators"]:  # type: ignore[index]
        new_decorator: Dict[str, Any] = {"name": "", "parameters": {}}

        # Copy name
        if "name" in decorator:
            new_decorator["name"] = decorator["name"]  # type: ignore[index]

        # Copy parameters if present
        if "parameters" in decorator:  # type: ignore[index]
            params = decorator["parameters"]  # type: ignore[index]
            for param_key in params.keys():
                new_decorator["parameters"][param_key] = params[param_key]

        template_decorators.append(new_decorator)

    # Apply template parameters if provided
    if parameters:
        for decorator in template_decorators:
            decorator_params = decorator.get("parameters", {})
            for key, value in parameters.items():
                if key in decorator_params:
                    decorator_params[key] = value

    # Create the decorated prompt
    decorators_result = apply_decorators(content, template_decorators)

    return {
        "template_name": template_name,
        "template_description": template["description"],  # type: ignore[index]
        "original_content": content,
        "decorated_prompt": decorators_result["decorated_prompt"],
        "applied_decorators": template_decorators,
    }


def run_server(verbose: bool = False) -> None:
    """
    Run the MCP server.

    Args:
        verbose: Whether to enable verbose logging.

    Returns:
        None
    """
    # Set logging level based on verbose flag
    if verbose:
        logger.setLevel(logging.DEBUG)
        logging.getLogger().setLevel(logging.DEBUG)

    logger.info("Starting Prompt Decorators MCP server")

    try:
        # Log available decorators
        decorators = get_available_decorators()
        logger.info(f"Available decorators: {len(decorators)}")
        logger.debug(f"Decorator names: {[d.name for d in decorators]}")

        # Run the server
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server shutdown requested")
    except Exception as e:
        logger.error(f"Error running server: {e}", exc_info=True)
    finally:
        logger.info("Server shutdown complete")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the Prompt Decorators MCP server")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()
    run_server(verbose=args.verbose)

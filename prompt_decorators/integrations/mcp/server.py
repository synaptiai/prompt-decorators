"""
MCP Server for Prompt Decorators.

This module provides integration between Prompt Decorators and the Model Context Protocol (MCP),
exposing prompt decorators as MCP tools that can be used by any MCP client.

Implementation follows the official MCP SDK patterns and best practices.
"""

import copy
import logging
import sys
from typing import Any, Callable, Dict, List, Optional, TypeVar, cast

# Set up logging before imports
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger("prompt-decorators-mcp")

# Global flag to track if MCP is available
MCP_AVAILABLE = False

# Define types for function decorators
F = TypeVar("F", bound=Callable[..., Any])

# Try to import the real FastMCP, or define a dummy one
try:
    from mcp.server.fastmcp import FastMCP as RealFastMCP

    FastMCP = RealFastMCP  # Use the real FastMCP
    MCP_AVAILABLE = True
except ImportError:
    logger.error("MCP SDK not installed. Please install with: pip install mcp")

    # Define a dummy FastMCP class for type checking
    class FastMCP:  # type: ignore[no-redef]
        """Dummy FastMCP class for when MCP is not installed."""

        def __init__(self, name: str) -> None:
            """
            Initialize the dummy FastMCP class.

            Args:
                name: The name of the MCP server.

            Returns:
                None
            """
            self.name = name

        def tool(self, *args: Any, **kwargs: Any) -> Callable[[F], F]:
            """
            Dummy tool decorator for registering functions as MCP tools.

            Args:
                *args: Positional arguments (ignored).
                **kwargs: Keyword arguments (ignored).

            Returns:
                A function decorator that returns the input function unchanged.
            """

            def decorator(func: F) -> F:
                """
                Inner decorator function that returns the input function unchanged.

                Args:
                    func: The function to decorate.

                Returns:
                    The input function unchanged.
                """
                return func

            return decorator

        def run(self, **kwargs: Any) -> None:
            """
            Dummy run method that raises an ImportError.

            Args:
                **kwargs: Keyword arguments (ignored).

            Returns:
                None

            Raises:
                ImportError: Always raised as MCP is not available.
            """
            raise ImportError(
                "MCP SDK not installed. Please install with: pip install mcp"
            )


# Only import decorator modules if MCP is available
if MCP_AVAILABLE:
    from prompt_decorators.dynamic_decorators_module import (
        apply_dynamic_decorators,
        get_available_decorators,
        load_decorator_definitions,
    )

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
    def apply_decorators(
        prompt: str, decorators: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
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
                        "parameters": {
                            "message": "Explain this topic in simple terms."
                        },
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
            "applied_decorators": decorators_result["applied_decorators"],
        }

    def run_server(host: str = "0.0.0.0", port: int = 5000) -> None:
        """
        Run the MCP server.

        Args:
            host: The host to listen on.
            port: The port to listen on.

        Returns:
            None
        """
        logger.info(f"Starting MCP server on {host}:{port}")
        # Since we can't directly set host and port attributes on FastMCP,
        # we'll use a try-except block to handle different FastMCP implementations
        try:
            # Try to use the run method with host and port parameters
            # This works with newer versions of the MCP SDK
            mcp.run(host=host, port=port)  # type: ignore[call-arg]
        except TypeError:
            # If that fails, try to use the run method without parameters
            # This works with older versions of the MCP SDK
            logger.warning(
                "FastMCP.run() doesn't support host/port parameters, using defaults"
            )
            mcp.run()

else:
    # Stub implementations for when MCP is not available
    def list_decorators() -> Dict[str, Any]:
        """
        Stub implementation for when MCP is not available.

        Returns:
            A dictionary with an error message.
        """
        logger.error("MCP is not available. Cannot list decorators.")
        return {"error": "MCP is not available"}

    def get_decorator_details(name: str) -> Dict[str, Any]:
        """
        Stub implementation for when MCP is not available.

        Args:
            name: The name of the decorator to get details for (ignored).

        Returns:
            A dictionary with an error message.
        """
        logger.error("MCP is not available. Cannot get decorator details.")
        return {"error": "MCP is not available"}

    def apply_decorators(
        prompt: str, decorators: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Stub implementation for when MCP is not available.

        Args:
            prompt: The prompt text to decorate (ignored).
            decorators: List of decorators to apply (ignored).

        Returns:
            A dictionary with an error message.
        """
        logger.error("MCP is not available. Cannot apply decorators.")
        return {"error": "MCP is not available"}

    def create_decorated_prompt(
        template_name: str, content: str, parameters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Stub implementation for when MCP is not available.

        Args:
            template_name: The name of the template to use (ignored).
            content: The content to include in the prompt (ignored).
            parameters: Optional parameters for customizing the template (ignored).

        Returns:
            A dictionary with an error message.
        """
        logger.error("MCP is not available. Cannot create decorated prompt.")
        return {"error": "MCP is not available"}

    def run_server(host: str = "0.0.0.0", port: int = 5000) -> None:
        """
        Stub implementation for when MCP is not available.

        Args:
            host: The host to listen on (ignored).
            port: The port to listen on (ignored).

        Returns:
            None

        Raises:
            ImportError: Always raised as MCP is not available.
        """
        logger.error("MCP is not available. Cannot run MCP server.")
        raise ImportError("MCP SDK not installed. Please install with: pip install mcp")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the Prompt Decorators MCP server")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=5000, help="Port to listen on")

    args = parser.parse_args()

    # Configure logging level based on verbose flag
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    run_server(host=args.host, port=args.port)

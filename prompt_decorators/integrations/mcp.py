"""
Model Context Protocol (MCP) integration for Prompt Decorators.

This module provides integration between Prompt Decorators and the Model Context Protocol (MCP),
allowing users to apply decorators through MCP tools and predefined templates.

Usage:
    # Run as a standalone MCP server
    python -m prompt_decorators.integrations.mcp

    # Or import and use in your own MCP server
    from prompt_decorators.integrations.mcp import create_mcp_server

    mcp_server = create_mcp_server("my-decorator-server")
    mcp_server.run()
"""

import asyncio
import importlib
import inspect
import json
import logging
import sys
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Type, Union, cast

# Set up a global variable to track if MCP is available
MCP_AVAILABLE = False


# Define a FastMCP type that will be either the real FastMCP or our placeholder
class DummyFastMCP:
    """Placeholder class for FastMCP when MCP is not installed."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize a dummy instance that does nothing.

        Args:
            *args: Positional arguments (ignored)
            **kwargs: Keyword arguments (ignored)

        Returns:
            None
        """
        pass

    def tool(self, *args: Any, **kwargs: Any) -> Callable:
        """Dummy tool decorator that returns the function unchanged.

        Args:
            *args: Positional arguments (ignored)
            **kwargs: Keyword arguments (ignored)

        Returns:
            A function that returns its input unchanged
        """

        def decorator(func: Callable) -> Callable:
            """Inner decorator function that returns the function unchanged.

            Args:
                func: The function to decorate

            Returns:
                The original function unchanged
            """
            return func

        return decorator

    def prompt(self, *args: Any, **kwargs: Any) -> Callable:
        """Dummy prompt decorator that returns the function unchanged.

        Args:
            *args: Positional arguments (ignored)
            **kwargs: Keyword arguments (ignored)

        Returns:
            A function that returns its input unchanged
        """

        def decorator(func: Callable) -> Callable:
            """Inner decorator function that returns the function unchanged.

            Args:
                func: The function to decorate

            Returns:
                The original function unchanged
            """
            return func

        return decorator

    def prompts_list_handler(self, *args: Any, **kwargs: Any) -> Callable:
        """Dummy prompts_list_handler decorator that returns the function unchanged.

        Args:
            *args: Positional arguments (ignored)
            **kwargs: Keyword arguments (ignored)

        Returns:
            A function that returns its input unchanged
        """

        def decorator(func: Callable) -> Callable:
            """Inner decorator function that returns the function unchanged.

            Args:
                func: The function to decorate

            Returns:
                The original function unchanged
            """
            return func

        return decorator

    def prompts_get_handler(self, *args: Any, **kwargs: Any) -> Callable:
        """Dummy prompts_get_handler decorator that returns the function unchanged.

        Args:
            *args: Positional arguments (ignored)
            **kwargs: Keyword arguments (ignored)

        Returns:
            A function that returns its input unchanged
        """

        def decorator(func: Callable) -> Callable:
            """Inner decorator function that returns the function unchanged.

            Args:
                func: The function to decorate

            Returns:
                The original function unchanged
            """
            return func

        return decorator

    async def run_stdio_async(self) -> None:
        """Dummy async run method that does nothing.

        This is a placeholder for the FastMCP.run_stdio_async method.
        """
        pass

    def run(self) -> None:
        """Dummy run method that does nothing.

        This is a placeholder for the FastMCP.run method.

        Args:
            None

        Returns:
            None
        """
        pass


# Try to import the real FastMCP
try:
    from mcp.server.fastmcp import FastMCP

    MCP_AVAILABLE = True
except ImportError:
    # If not available, use our dummy implementation
    FastMCP = DummyFastMCP  # type: ignore

from prompt_decorators.core import BaseDecorator
from prompt_decorators.core.parser import DecoratorParser
from prompt_decorators.core.registry import DecoratorRegistry
from prompt_decorators.core.request import DecoratedRequest

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("prompt-decorators-mcp")

# Global registry for decorators
DECORATOR_REGISTRY = DecoratorRegistry()


@dataclass
class DecoratorTemplate:
    """Configuration for a predefined decorator template."""

    description: str
    decorators: List[BaseDecorator]
    arguments: List[Dict[str, Any]] = field(default_factory=list)
    example: str = ""

    def __post_init__(self) -> None:
        """Ensure arguments list includes the prompt argument."""
        has_prompt_arg = any(arg.get("name") == "prompt" for arg in self.arguments)
        if not has_prompt_arg:
            self.arguments.append(
                {
                    "name": "prompt",
                    "description": "User prompt to decorate",
                    "required": True,
                }
            )


def load_decorator_classes() -> Dict[str, Type[BaseDecorator]]:
    """
    Dynamically load all decorator classes from the generated decorators module.

    Returns:
        Dictionary mapping decorator names to decorator classes
    """
    try:
        # Import the decorators module
        decorators_module = importlib.import_module(
            "prompt_decorators.decorators.generated.decorators"
        )

        # Get all decorator classes
        decorator_classes = {}

        for name, obj in inspect.getmembers(decorators_module):
            if (
                inspect.isclass(obj)
                and issubclass(obj, BaseDecorator)
                and obj != BaseDecorator
            ):
                decorator_classes[name] = obj
                # Register the decorator class with the global registry
                DECORATOR_REGISTRY.register(
                    obj, category=getattr(obj, "category", "Uncategorized")
                )

        logger.info(f"Loaded {len(decorator_classes)} decorator classes")
        return decorator_classes
    except ImportError as e:
        logger.error(f"Error loading decorator classes: {str(e)}")
        return {}


def create_default_templates() -> Dict[str, DecoratorTemplate]:
    """
    Create default templates using the available decorators.

    Returns:
        Dictionary of default templates
    """
    # Load all decorator classes
    decorator_classes = load_decorator_classes()

    # Create default templates
    templates = {
        "detailed-reasoning": DecoratorTemplate(
            description="Transform prompt for detailed reasoning and step-by-step analysis",
            decorators=[
                decorator_classes["Reasoning"](depth="comprehensive"),
                decorator_classes["StepByStep"](numbered=True),
            ],
            example="Explain how quantum computing works.",
        ),
        "academic-analysis": DecoratorTemplate(
            description="Transform prompt for scholarly academic analysis with citations",
            decorators=[
                decorator_classes["Reasoning"](depth="comprehensive"),
                decorator_classes["CiteSources"](style="inline", format="APA"),
                decorator_classes["OutputFormat"](format="markdown"),
            ],
            example="Analyze the impact of climate change on marine ecosystems.",
        ),
        "explain-simply": DecoratorTemplate(
            description="Explain a complex topic in simple, accessible terms",
            decorators=[
                decorator_classes["ELI5"](),
                decorator_classes["StepByStep"](numbered=True),
            ],
            example="Explain how nuclear fusion works.",
        ),
        "creative-storytelling": DecoratorTemplate(
            description="Generate creative narrative content",
            decorators=[
                decorator_classes["Creative"](level="high"),
                decorator_classes["OutputFormat"](format="markdown"),
            ],
            arguments=[
                {"name": "genre", "description": "Story genre", "required": False}
            ],
            example="Write a short story about a traveler discovering a hidden world.",
        ),
        "problem-solving": DecoratorTemplate(
            description="Structured approach to solving complex problems",
            decorators=[
                decorator_classes["StepByStep"](numbered=True),
                decorator_classes["TreeOfThought"](branches=3),
                decorator_classes["Limitations"](position="end"),
            ],
            example="How can we reduce plastic waste in the oceans?",
        ),
        "balanced-viewpoint": DecoratorTemplate(
            description="Present multiple perspectives on a contentious topic",
            decorators=[
                decorator_classes["Balanced"](),
                decorator_classes["PeerReview"](criteria="all"),
                decorator_classes["Steelman"](),
            ],
            example="Discuss the pros and cons of implementing universal basic income.",
        ),
        "technical-documentation": DecoratorTemplate(
            description="Generate clear technical documentation with code examples",
            decorators=[
                decorator_classes["OutputFormat"](format="markdown"),
                decorator_classes["Audience"](level="technical"),
                decorator_classes["StepByStep"](numbered=True),
            ],
            arguments=[
                {
                    "name": "language",
                    "description": "Programming language",
                    "required": False,
                }
            ],
            example="Create documentation for a REST API.",
        ),
        "data-analysis": DecoratorTemplate(
            description="Analyze data with structured insights and visualizations",
            decorators=[
                decorator_classes["TableFormat"](
                    columns=["Category", "Value", "Trend", "Insight"]
                ),
                decorator_classes["Reasoning"](depth="comprehensive"),
                decorator_classes["Prioritize"](criteria="impact"),
            ],
            example="Analyze the trends in this sales data.",
        ),
    }

    return templates


# Create default templates
DEFAULT_TEMPLATES = create_default_templates()


def create_mcp_server(
    name: str = "prompt-decorators-suite",
    templates: Optional[Dict[str, DecoratorTemplate]] = None,
) -> Any:
    """
    Create an MCP server with prompt decorator integration.

    Args:
        name: Name of the MCP server
        templates: Optional custom templates to use instead of defaults

    Returns:
        Configured FastMCP server instance

    Raises:
        ImportError: If the MCP package is not installed but is required for this function
    """
    # Check if MCP is available
    if not MCP_AVAILABLE:
        raise ImportError(
            "MCP integration requires the 'mcp' package to be installed. "
            "Install it with 'pip install \"mcp[cli]\"'"
        )

    # Initialize FastMCP server (we know FastMCP is available at this point)
    mcp = FastMCP(name)

    # Use provided templates or defaults
    prompt_templates = templates or DEFAULT_TEMPLATES

    # Load all decorator classes
    decorator_classes = load_decorator_classes()

    @mcp.tool()
    async def apply_decorators(prompt: str) -> Dict[str, Any]:
        """Apply decorators to a prompt.

        Args:
            prompt: The prompt to apply decorators to.

        Returns:
            A dictionary containing the transformed prompt and the list of decorators applied.
        """
        logger.info(f"Applying decorators to prompt: {prompt}...")

        try:
            # Parse the prompt to extract decorators
            parser = DecoratorParser()
            decorators, clean_prompt = parser.extract_decorators(prompt)

            if not decorators:
                logger.info("No decorators found in prompt")
                return {
                    "transformed_prompt": prompt,
                    "decorators_applied": [],
                    "original_prompt": prompt,
                }

            # Log the decorators found
            decorator_names = [d.__class__.__name__ for d in decorators]
            logger.info(f"Found decorators: {decorator_names}")

            # Apply each decorator to the prompt
            transformed_prompt = clean_prompt
            for decorator in decorators:
                logger.info(f"Applying decorator: {decorator.__class__.__name__}")
                try:
                    transformed_prompt = decorator.apply_to_prompt(transformed_prompt)
                    logger.info(
                        f"Prompt after applying {decorator.__class__.__name__}: {transformed_prompt[:50]}..."
                    )
                except Exception as e:
                    logger.error(
                        f"Error applying decorator {decorator.__class__.__name__}: {str(e)}"
                    )
                    logger.error(f"Decorator details: {decorator.__dict__}")
                    import traceback

                    logger.error(f"Traceback: {traceback.format_exc()}")

            return {
                "transformed_prompt": transformed_prompt,
                "decorators_applied": decorator_names,
                "original_prompt": prompt,
            }
        except Exception as e:
            logger.error(f"Error in apply_decorators: {str(e)}")
            import traceback

            logger.error(f"Traceback: {traceback.format_exc()}")
            return {
                "transformed_prompt": prompt,
                "decorators_applied": [],
                "original_prompt": prompt,
                "error": str(e),
            }

    @mcp.tool()
    async def list_decorators() -> List[Dict[str, Any]]:
        """Retrieve a list of available decorators.

        Returns:
            List[Dict[str, Any]]: A list of decorator information dictionaries.
        """
        logger.info("Retrieving list of available decorators")

        # Get the registry
        registry = DecoratorRegistry()

        # Log registry information for debugging
        decorators_dict = registry.decorators
        logger.info(f"Registry contains {len(decorators_dict)} decorators")
        logger.info(f"Registry type: {type(decorators_dict)}")

        if decorators_dict:
            first_key = next(iter(decorators_dict.keys()))
            first_value = decorators_dict[first_key]
            logger.info(f"First key type: {type(first_key)}, value: {first_key}")
            logger.info(
                f"First value type: {type(first_value)}, name: {first_value.__name__}"
            )

        # Process all decorators
        decorators = []
        for name, decorator_class in decorators_dict.items():
            logger.info(f"Processing decorator: {decorator_class.__name__}")

            # Get description from the class
            description = "Base decorator class"
            if hasattr(decorator_class, "description"):
                description = decorator_class.description

            # Get category from the class
            category = "Uncategorized"
            if hasattr(decorator_class, "category"):
                category = decorator_class.category

            # Get parameters from the class
            parameters = {}
            if hasattr(decorator_class, "parameters"):
                parameters = decorator_class.parameters

            decorators.append(
                {
                    "name": decorator_class.__name__,
                    "description": description,
                    "category": category,
                    "parameters": parameters,
                }
            )

        logger.info(f"Returning {len(decorators)} decorators")
        return decorators

    @mcp.tool()
    async def get_decorator_details(decorator_name: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific decorator.

        Args:
            decorator_name: Name of the decorator to get details for

        Returns:
            Dictionary containing decorator details
        """
        logger.info(f"Retrieving details for decorator: {decorator_name}")

        try:
            # Try to get the decorator class from the global registry
            decorator_class = DECORATOR_REGISTRY.get(decorator_name)

            # If not found, try converting from PascalCase to snake_case
            if decorator_class is None:
                # Convert PascalCase to snake_case (e.g., StepByStep -> step_by_step)
                snake_case_name = "".join(
                    ["_" + c.lower() if c.isupper() else c for c in decorator_name]
                ).lstrip("_")
                decorator_class = DECORATOR_REGISTRY.get(snake_case_name)

                # If still not found, try looking up by class name in the registry
                if decorator_class is None:
                    # Try to find a class with a matching name (case-insensitive)
                    for name, cls in DECORATOR_REGISTRY.decorators.items():
                        if cls.__name__.lower() == decorator_name.lower():
                            decorator_class = cls
                            break

            if decorator_class is None:
                return {"error": f"Decorator not found: {decorator_name}"}

            # Extract metadata from the decorator class
            metadata = {}

            # Get description
            if hasattr(decorator_class, "description"):
                metadata["description"] = decorator_class.description

            # Get category
            if hasattr(decorator_class, "category"):
                metadata["category"] = decorator_class.category

            # Get parameters
            if hasattr(decorator_class, "parameters"):
                parameters = decorator_class.parameters
                metadata["parameters"] = parameters  # type: ignore

            # Get examples
            if hasattr(decorator_class, "examples"):
                metadata["examples"] = decorator_class.examples

            # Get version and author if available
            version = "1.0.0"
            author = "Unknown"

            # Try to get metadata from get_metadata method if it exists
            if hasattr(decorator_class, "get_metadata") and callable(
                getattr(decorator_class, "get_metadata")
            ):
                try:
                    # Create an instance to call the method
                    instance = decorator_class()
                    full_metadata = instance.get_metadata()  # type: ignore
                    if "version" in full_metadata:
                        version = full_metadata["version"]
                    if "author" in full_metadata:
                        author = full_metadata["author"]
                except Exception as e:
                    logger.error(f"Error getting metadata from decorator: {str(e)}")

            return {
                "name": decorator_name,
                "description": metadata.get("description", "No description available"),
                "category": metadata.get("category", "Uncategorized"),
                "parameters": metadata.get("parameters", {}),
                "usage_examples": metadata.get("examples", []),
                "version": version,
                "author": author,
            }
        except Exception as e:
            logger.error(f"Error retrieving decorator details: {str(e)}")
            return {"error": str(e)}

    @mcp.tool()
    async def create_decorated_prompt(
        template_name: str,
        prompt: str,
        additional_params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Apply a predefined decorator template to a prompt.

        Args:
            template_name: The name of the template to apply
            prompt: The prompt text to decorate
            additional_params: Optional additional parameters for the template

        Returns:
            A dictionary containing the transformed prompt and metadata
        """
        logger.info(f"Creating decorated prompt using template: {template_name}")

        try:
            if template_name not in prompt_templates:
                error_msg = f"Template not found: {template_name}"
                available_templates_list = list(prompt_templates.keys())
                return {
                    "error": error_msg,
                    "available_templates": available_templates_list,
                }

            template = prompt_templates[template_name]
            decorated_prompt = prompt

            # Apply the decorators in sequence
            for decorator in template.decorators:
                decorated_prompt = decorator.apply_to_prompt(decorated_prompt)

            # Handle additional template-specific processing
            if template_name == "creative-storytelling" and additional_params:
                genre = additional_params.get("genre")
                if genre:
                    decorated_prompt = f"Write in the {genre} genre. {decorated_prompt}"

            elif template_name == "technical-documentation" and additional_params:
                language = additional_params.get("language")
                if language:
                    decorated_prompt = (
                        f"Create documentation for {language} code. {decorated_prompt}"
                    )

            return {
                "transformed_prompt": decorated_prompt,
                "template_used": template_name,
                "original_prompt": prompt,
            }
        except Exception as e:
            logger.error(f"Error creating decorated prompt: {str(e)}")
            return {"error": str(e)}

    # Register prompt templates as MCP prompts
    for name, template in prompt_templates.items():

        @mcp.prompt(name=name)
        async def prompt_handler(prompt: str, **kwargs: Any) -> str:
            """Handle prompt template requests."""
            decorated_prompt = prompt

            # Get the template based on the prompt name
            template_name = kwargs.get("__prompt_name__", name)
            template = prompt_templates[template_name]

            # Apply the decorators in sequence
            for decorator in template.decorators:
                decorated_prompt = decorator.apply_to_prompt(decorated_prompt)

            # Handle additional template-specific processing
            if template_name == "creative-storytelling" and "genre" in kwargs:
                genre = kwargs.get("genre")
                if genre:
                    decorated_prompt = f"Write in the {genre} genre. {decorated_prompt}"

            elif template_name == "technical-documentation" and "language" in kwargs:
                language = kwargs.get("language")
                if language:
                    decorated_prompt = (
                        f"Create documentation for {language} code. {decorated_prompt}"
                    )

            return decorated_prompt

    # Check if the MCP version supports prompts_list_handler
    if hasattr(mcp, "prompts_list_handler"):

        @mcp.prompts_list_handler()
        async def list_prompts() -> Dict[str, List[Dict[str, Any]]]:
            """List all available prompt templates.

            Returns:
                Dict containing a list of prompt templates with their details.
            """
            logger.info("Listing available prompt templates")

            prompts: List[Dict[str, Any]] = []
            for template_name, template_obj in prompt_templates.items():
                prompts.append(
                    {
                        "name": template_name,
                        "description": template_obj.description,
                        "arguments": template_obj.arguments,
                        "example": template_obj.example,
                    }
                )

            return {"prompts": prompts}

    # Check if the MCP version supports prompts_get_handler
    if hasattr(mcp, "prompts_get_handler"):

        @mcp.prompts_get_handler()
        async def get_prompt(request: Any) -> Dict[str, Any]:
            """Get a specific prompt template and apply it to the provided arguments.

            Args:
                request: The request object containing the prompt name and arguments.

            Returns:
                Dict containing either the error information or the prompt messages.
            """
            logger.info(f"Getting prompt template: {request.params}")

            name = request.params.get("name")
            arguments = request.params.get("arguments", {})

            if name not in prompt_templates:
                error_msg = f"Template not found: {name}"
                available_templates_list = list(prompt_templates.keys())
                return {
                    "error": error_msg,
                    "available_templates": available_templates_list,
                }

            template = prompt_templates[name]
            prompt = arguments.get("prompt", "")

            # Apply the decorators in sequence
            decorated_prompt = prompt
            for decorator in template.decorators:
                decorated_prompt = decorator.apply_to_prompt(decorated_prompt)

            # Handle additional template-specific processing
            if name == "creative-storytelling" and "genre" in arguments:
                genre = arguments.get("genre")
                if genre:
                    decorated_prompt = f"Write in the {genre} genre. {decorated_prompt}"

            elif name == "technical-documentation" and "language" in arguments:
                language = arguments.get("language")
                if language:
                    decorated_prompt = (
                        f"Create documentation for {language} code. {decorated_prompt}"
                    )

            return {
                "messages": [
                    {
                        "role": "user",
                        "content": {
                            "type": "text",
                            "text": decorated_prompt,
                        },
                    }
                ]
            }

    async def run_async() -> None:
        """Run the MCP server asynchronously."""
        # Use an event to keep the server running
        stop_event = asyncio.Event()

        # Start the server in background
        server_task = asyncio.create_task(mcp.run_stdio_async())

        # Wait for the stop event or ctrl+c
        try:
            await stop_event.wait()
        except asyncio.CancelledError:
            logger.info("Server task cancelled")
        finally:
            # Clean up
            if not server_task.done():
                server_task.cancel()
                try:
                    await server_task
                except asyncio.CancelledError:
                    pass

    # Add the method to the server instance
    setattr(mcp, "run_async", run_async)

    # Return the server instance
    return mcp


def main() -> None:
    """Run the MCP server as a standalone application."""
    # Check if MCP is available
    if not MCP_AVAILABLE:
        logger.error(
            "MCP package is not installed. Cannot run MCP server. "
            "Install it with 'pip install \"mcp[cli]\"'"
        )
        sys.exit(1)

    logger.info("Starting Prompt Decorators MCP Server")

    # Create the server
    mcp_server = create_mcp_server()

    # Run the server
    mcp_server.run()


if __name__ == "__main__":
    main()

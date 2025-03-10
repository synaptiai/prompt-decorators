"""MCP Server for Prompt Decorators.

This module provides integration between Prompt Decorators and the Model Context Protocol (MCP),
exposing prompt decorators as MCP tools that can be used by any MCP client.

Implementation follows the official MCP SDK patterns and best practices.
"""

import copy
import json
import logging
import sys
from typing import (
    Any,
    Callable,
    Dict,
    List,
    MutableMapping,
    MutableSequence,
    Optional,
    TypeVar,
    cast,
)

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
            """Initialize the dummy FastMCP class.

            Args:
                name: The name of the MCP server.

            Returns:
                None
            """
            self.name = name

        def tool(self, *args: Any, **kwargs: Any) -> Callable[[F], F]:
            """Dummy tool decorator for registering functions as MCP tools.

            Args:
                *args: Positional arguments (ignored).
                **kwargs: Keyword arguments (ignored).

            Returns:
                A function decorator that returns the input function unchanged.
            """

            def decorator(func: F) -> F:
                """Inner decorator function that returns the input function unchanged.

                Args:
                    func: The function to decorate.

                Returns:
                    The input function unchanged.
                """
                return func

            return decorator

        def run(self, **kwargs: Any) -> None:
            """Dummy run method that raises an ImportError.

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


# Create the MCP server instance regardless of MCP availability
# When MCP is not available, this will be a dummy instance
mcp = FastMCP("Prompt Decorators")

# Only import decorator modules if MCP is available
if MCP_AVAILABLE:
    from prompt_decorators.core.dynamic_decorator import (
        transform_prompt as core_transform_prompt,
    )
    from prompt_decorators.dynamic_decorators_module import (
        apply_dynamic_decorators,
        get_available_decorators,
        load_decorator_definitions,
    )

    # Make sure decorators are loaded
    load_decorator_definitions()

    @mcp.tool()
    def list_decorators() -> Dict[str, Any]:
        """Lists all available prompt decorators.

        Returns:
            A dictionary containing information about all available decorators.
        """
        logger.info("Listing all decorators")
        decorators = get_available_decorators()

        result = []
        for decorator in decorators:
            # Create proper tool definition with JSON Schema
            tool_schema: Dict[str, Any] = {
                "name": decorator.name if hasattr(decorator, "name") else "Unknown",
                "description": decorator.description
                if hasattr(decorator, "description")
                else f"Apply the {decorator.name if hasattr(decorator, 'name') else 'Unknown'} decorator to your prompt",
                "version": decorator.version
                if hasattr(decorator, "version")
                else "1.0.0",
                "category": decorator.category
                if hasattr(decorator, "category")
                else "General",
                "inputSchema": {"type": "object", "properties": {}, "required": []},
            }

            # Add each parameter to the schema properties
            properties = tool_schema["inputSchema"][
                "properties"
            ]  # type: Dict[str, Any]
            required = tool_schema["inputSchema"]["required"]  # type: List[str]

            # Add a prompt field to properties
            properties["prompt"] = {
                "type": "string",
                "description": "The prompt text to decorate",
            }
            required.append("prompt")

            for param in decorator.parameters:
                # Convert parameter type to JSON Schema type
                if hasattr(param, "type"):
                    param_type = param.type
                elif hasattr(param, "type_"):
                    param_type = param.type_
                else:
                    param_type = (
                        "string"  # Default to string type if no type attribute found
                    )

                param_description = (
                    param.description
                    if hasattr(param, "description")
                    else "No description available"
                )

                if param_type == "string":
                    param_schema = {"type": "string", "description": param_description}
                    # Add string-specific validations
                    if hasattr(param, "min_length") and param.min_length is not None:
                        param_schema["minLength"] = param.min_length
                    if hasattr(param, "max_length") and param.max_length is not None:
                        param_schema["maxLength"] = param.max_length
                    if hasattr(param, "pattern") and param.pattern is not None:
                        param_schema["pattern"] = param.pattern

                elif param_type == "number":
                    param_schema = {"type": "number", "description": param_description}
                    # Add number-specific validations
                    if hasattr(param, "min_value") and param.min_value is not None:
                        param_schema["minimum"] = param.min_value
                    if hasattr(param, "max_value") and param.max_value is not None:
                        param_schema["maximum"] = param.max_value

                elif param_type == "boolean":
                    param_schema = {"type": "boolean", "description": param_description}

                elif param_type == "enum":
                    param_schema = {
                        "type": "string",
                        "description": param_description,
                        "enum": param.enum_values
                        if hasattr(param, "enum_values")
                        else [],
                    }

                else:
                    # Default to string type for unknown types
                    param_schema = {"type": "string", "description": param_description}

                # Add default value if available
                if hasattr(param, "default") and param.default is not None:
                    param_schema["default"] = param.default

                # Add to properties
                param_name = (
                    param.name if hasattr(param, "name") else f"param_{id(param)}"
                )
                properties[param_name] = param_schema

                # Add to required list if parameter is required
                if hasattr(param, "required") and param.required:
                    required.append(param_name)

            # Add compatibility summary
            if hasattr(decorator, "compatibility"):
                compatibility = decorator.compatibility
                tool_schema["compatibilitySummary"] = {
                    "requires": compatibility.get("requires", []),
                    "conflicts": compatibility.get("conflicts", []),
                    "supportedModels": compatibility.get("models", []),
                }

            # Add transformationTemplate if available
            if hasattr(decorator, "transformationTemplate"):
                template = decorator.transformationTemplate
                if isinstance(template, dict):
                    tool_schema["transformationTemplate"] = template

            # Add author information if available
            if hasattr(decorator, "author"):
                author = decorator.author
                if isinstance(author, dict):
                    tool_schema["author"] = author

            # Add sample usage if available
            if hasattr(decorator, "examples") and decorator.examples:
                # Add just the first example as a summary
                examples = decorator.examples
                if examples:
                    first_example = None
                    if isinstance(examples, list) and examples:
                        first_example = examples[0]
                    else:
                        first_example = examples

                    if isinstance(first_example, dict) and "usage" in first_example:
                        tool_schema["sampleUsage"] = first_example.get("usage")

            result.append(tool_schema)

        return {
            "content": [
                {"type": "text", "text": f"Found {len(result)} available decorators"}
            ],
            "tools": result,
        }

    @mcp.tool()
    def get_decorator_details(name: str) -> Dict[str, Any]:
        """Get detailed information about a specific decorator.

        Args:
            name: The name of the decorator to get details for.

        Returns:
            A dictionary containing detailed information about the decorator.
        """
        logger.info(f"Getting details for decorator: {name}")
        decorators = get_available_decorators()

        for decorator in decorators:
            if decorator.name == name:
                # Create detailed JSON Schema
                schema: Dict[str, Any] = {
                    "type": "object",
                    "properties": {},
                    "required": [],
                }

                # Get references to the schema properties and required fields
                schema_properties: Dict[str, Any] = schema["properties"]
                schema_required: List[str] = schema["required"]

                # Add each parameter to the schema
                for param in decorator.parameters:
                    # Get parameter type - handle both type and type_ attributes for compatibility
                    if hasattr(param, "type"):
                        param_type = param.type
                    elif hasattr(param, "type_"):
                        param_type = param.type_
                    else:
                        param_type = "string"  # Default to string type if no type attribute found

                    param_description = (
                        param.description
                        if hasattr(param, "description")
                        else "No description available"
                    )

                    # Convert parameter type to JSON Schema type
                    if param_type == "string":
                        param_schema: Dict[str, Any] = {
                            "type": "string",
                            "description": param_description,
                        }
                        # Add string-specific validations
                        if (
                            hasattr(param, "min_length")
                            and param.min_length is not None
                        ):
                            param_schema["minLength"] = param.min_length
                        if (
                            hasattr(param, "max_length")
                            and param.max_length is not None
                        ):
                            param_schema["maxLength"] = param.max_length
                        if hasattr(param, "pattern") and param.pattern is not None:
                            param_schema["pattern"] = param.pattern

                    elif param_type == "number":
                        param_schema = {
                            "type": "number",
                            "description": param_description,
                        }
                        # Add number-specific validations
                        if hasattr(param, "min_value") and param.min_value is not None:
                            param_schema["minimum"] = param.min_value
                        if hasattr(param, "max_value") and param.max_value is not None:
                            param_schema["maximum"] = param.max_value

                    elif param_type == "boolean":
                        param_schema = {
                            "type": "boolean",
                            "description": param_description,
                        }

                    elif param_type == "enum":
                        param_schema = {
                            "type": "string",
                            "description": param_description,
                            "enum": param.enum_values
                            if hasattr(param, "enum_values")
                            else [],
                        }

                    else:
                        # Default to string type for unknown types
                        param_schema = {
                            "type": "string",
                            "description": param_description,
                        }

                    # Add default value if available
                    if hasattr(param, "default") and param.default is not None:
                        param_schema["default"] = param.default

                    # Add to properties
                    param_name = (
                        param.name if hasattr(param, "name") else f"param_{id(param)}"
                    )
                    schema_properties[param_name] = param_schema

                    # Add to required list if parameter is required
                    if hasattr(param, "required") and param.required:
                        schema_required.append(param_name)

                # Add prompt field to schema
                schema_properties["prompt"] = {
                    "type": "string",
                    "description": "The prompt text to decorate",
                }
                schema_required.append("prompt")

                # Build the comprehensive response
                response = {
                    "name": decorator.name if hasattr(decorator, "name") else "Unknown",
                    "description": decorator.description
                    if hasattr(decorator, "description")
                    else "No description available",
                    "category": decorator.category
                    if hasattr(decorator, "category")
                    else "General",
                    "version": decorator.version
                    if hasattr(decorator, "version")
                    else "1.0.0",
                    "parameters": [
                        param.to_dict()
                        if hasattr(param, "to_dict")
                        else {
                            "name": param.name
                            if hasattr(param, "name")
                            else f"param_{id(param)}",
                            "description": param.description
                            if hasattr(param, "description")
                            else "No description available",
                            "type": param.type
                            if hasattr(param, "type")
                            else param.type_
                            if hasattr(param, "type_")
                            else "string",
                        }
                        for param in decorator.parameters
                    ],
                    "inputSchema": schema,
                }

                # Add transformation function information
                transform_function = None
                if hasattr(decorator, "transform_function"):
                    transform_function = decorator.transform_function
                    response["transformationSummary"] = {
                        "available": transform_function is not None
                    }

                # Add transformation template if available
                if hasattr(decorator, "transformationTemplate"):
                    template = decorator.transformationTemplate
                    if isinstance(template, dict):
                        response["transformationTemplate"] = template

                # Add author information if available
                if hasattr(decorator, "author"):
                    author = decorator.author
                    if isinstance(author, dict):
                        response["author"] = author

                # Add detailed compatibility information
                if hasattr(decorator, "compatibility"):
                    compatibility = decorator.compatibility
                    response["compatibility"] = {
                        "requires": compatibility.get("requires", []),
                        "conflicts": compatibility.get("conflicts", []),
                        "minStandardVersion": compatibility.get("minStandardVersion"),
                        "maxStandardVersion": compatibility.get("maxStandardVersion"),
                        "supportedModels": compatibility.get("models", []),
                    }

                # Add examples if available
                if hasattr(decorator, "examples") and decorator.examples:
                    examples = decorator.examples
                    if isinstance(examples, list):
                        response["examples"] = examples

                # Add implementation guidance if available
                if hasattr(decorator, "implementationGuidance"):
                    guidance = decorator.implementationGuidance
                    if isinstance(guidance, dict):
                        response["implementationGuidance"] = guidance

                return {
                    "content": [
                        {
                            "type": "text",
                            "text": f"Details for decorator: {decorator.name}",
                        }
                    ],
                    "decorator": response,
                }

        # Return error response if decorator not found
        return {
            "isError": True,
            "content": [{"type": "text", "text": f"Decorator '{name}' not found"}],
            "metadata": {"available_decorators": [d.name for d in decorators]},
        }

    @mcp.tool()
    def apply_decorators(
        prompt: str, decorators: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Apply decorators to a prompt using the +++ syntax.

        Args:
            prompt: The prompt text to decorate.
            decorators: List of decorators to apply, each with name and parameters.

        Returns:
            The decorated prompt with decorators applied, following MCP tool response format.
        """
        try:
            logger.info(f"Applying {len(decorators)} decorators to prompt")

            # Format the prompt with +++ decorators syntax
            decorator_strings = []
            applied_decorator_names = []

            for decorator in decorators:
                name = decorator.get("name")
                if not name:
                    continue

                applied_decorator_names.append(name)
                params = decorator.get("parameters", {})

                # Format parameters
                param_parts = []
                for key, value in params.items():
                    # Handle different parameter types appropriately
                    if isinstance(value, bool):
                        formatted_value = str(value).lower()
                    elif isinstance(value, (int, float)):
                        formatted_value = str(value)
                    elif isinstance(value, str):
                        # Quote string values with spaces or special characters
                        if " " in value or any(c in value for c in ",()="):
                            formatted_value = f'"{value}"'
                        else:
                            formatted_value = value
                    else:
                        # For other types, use JSON serialization
                        formatted_value = json.dumps(value)

                    param_parts.append(f"{key}={formatted_value}")

                # Build decorator string
                if param_parts:
                    decorator_str = f"+++{name}({', '.join(param_parts)})"
                else:
                    decorator_str = f"+++{name}"

                decorator_strings.append(decorator_str)

            # Create the decorated prompt
            if decorator_strings:
                transformed_prompt = core_transform_prompt(prompt, decorator_strings)
            else:
                transformed_prompt = prompt

            # Return in MCP tool response format with content array
            return {
                "content": [{"type": "text", "text": transformed_prompt}],
                "metadata": {
                    "original_prompt": prompt,
                    "applied_decorators": applied_decorator_names,
                    "decorator_strings": decorator_strings,
                },
            }

        except Exception as e:
            logger.error(f"Error applying decorators: {str(e)}")
            return {
                "isError": True,
                "content": [
                    {"type": "text", "text": f"Error applying decorators: {str(e)}"}
                ],
            }

    @mcp.tool()
    def create_decorated_prompt(
        template_name: str, content: str, parameters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create a decorated prompt using a predefined template.

        Args:
            template_name: The name of the template to use.
            content: The content to include in the prompt.
            parameters: Optional parameters for customizing the template.

        Returns:
            The decorated prompt created from the template, following MCP tool response format.
        """
        try:
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
                            "parameters": {
                                "message": "Solve this problem methodically."
                            },
                        },
                        {"name": "ProblemSolver", "parameters": {}},
                        {"name": "StepByStep", "parameters": {}},
                    ],
                },
            }

            if template_name not in templates:
                return {
                    "isError": True,
                    "content": [
                        {
                            "type": "text",
                            "text": f"Template '{template_name}' not found",
                        }
                    ],
                    "metadata": {"available_templates": list(templates.keys())},
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

            # Create the decorated prompt using the apply_decorators function
            result = apply_decorators(content, template_decorators)

            # Return successful response
            return {
                "content": result.get("content", []),
                "metadata": {
                    "template_name": template_name,
                    "template_description": template["description"],  # type: ignore[index]
                    "original_content": content,
                    "applied_decorators": result.get("metadata", {}).get(
                        "applied_decorators", []
                    ),
                },
            }
        except Exception as e:
            logger.error(f"Error creating decorated prompt: {str(e)}")
            return {
                "isError": True,
                "content": [
                    {
                        "type": "text",
                        "text": f"Error creating decorated prompt: {str(e)}",
                    }
                ],
            }

    @mcp.tool()
    def transform_prompt(prompt: str, decorator_strings: List[str]) -> Dict[str, Any]:
        """Transform a prompt using a list of decorator strings.

        This tool directly transforms a prompt using the raw decorator syntax strings
        (e.g., "+++StepByStep(numbered=true)"), which can be useful for clients
        that already have decorator strings rather than structured decorator objects.

        Args:
            prompt: The prompt text to transform.
            decorator_strings: List of decorator syntax strings to apply.

        Returns:
            The transformed prompt, following MCP tool response format.
        """
        try:
            logger.info(
                f"Transforming prompt with {len(decorator_strings)} decorator strings"
            )

            # Validate decorator strings
            valid_decorators = []
            invalid_decorators = []

            for dec_str in decorator_strings:
                # Clean up decorator string - remove any trailing +++ that might be present
                cleaned_dec_str = dec_str
                if cleaned_dec_str.endswith("+++"):
                    cleaned_dec_str = cleaned_dec_str[:-3]

                # Basic validation - ensure it has the +++ prefix
                if not cleaned_dec_str.startswith("+++"):
                    invalid_decorators.append(
                        {"string": dec_str, "error": "Decorator must start with +++"}
                    )
                    continue

                valid_decorators.append(cleaned_dec_str)

            # Create the decorated prompt
            if valid_decorators:
                transformed_prompt = core_transform_prompt(prompt, valid_decorators)
            else:
                transformed_prompt = prompt

            # Provide the original strings in the metadata for reference
            original_decorators = decorator_strings

            # Return in MCP tool response format
            response: Dict[str, Any] = {
                "content": [{"type": "text", "text": transformed_prompt}],
                "metadata": {
                    "original_prompt": prompt,
                    "applied_decorators": original_decorators,
                    "cleaned_decorators": valid_decorators,
                },
            }

            # Add warning if there were invalid decorators
            if invalid_decorators:
                metadata: Dict[str, Any] = response["metadata"]
                metadata["invalidDecorators"] = invalid_decorators
                metadata[
                    "warning"
                ] = f"{len(invalid_decorators)} invalid decorator(s) were skipped"

            return response

        except Exception as e:
            logger.error(f"Error transforming prompt: {str(e)}")
            return {
                "isError": True,
                "content": [
                    {"type": "text", "text": f"Error transforming prompt: {str(e)}"}
                ],
            }

    def run_server(host: str = "0.0.0.0", port: int = 5000) -> None:
        """Run the MCP server.

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
        """Stub implementation for when MCP is not available.

        Returns:
            A dictionary with an error message.
        """
        logger.error("MCP is not available. Cannot list decorators.")
        return {"error": "MCP is not available"}

    def get_decorator_details(name: str) -> Dict[str, Any]:
        """Stub implementation for when MCP is not available.

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
        """Stub implementation for when MCP is not available.

        Args:
            prompt: The prompt text to decorate (ignored).
            decorators: List of decorators to apply (ignored).

        Returns:
            A dictionary with an error message.
        """
        logger.error("MCP is not available. Cannot apply decorators.")
        return {"error": "MCP is not available"}

    def transform_prompt(prompt: str, decorator_strings: List[str]) -> Dict[str, Any]:
        """Stub implementation for when MCP is not available.

        Args:
            prompt: The prompt text to transform (ignored).
            decorator_strings: List of decorator strings to apply (ignored).

        Returns:
            A dictionary with an error message.
        """
        logger.error("MCP is not available. Cannot transform prompt.")
        return {"error": "MCP is not available"}

    def create_decorated_prompt(
        template_name: str, content: str, parameters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Stub implementation for when MCP is not available.

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
        """Stub implementation for when MCP is not available.

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

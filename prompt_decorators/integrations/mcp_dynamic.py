"""
Model Context Protocol (MCP) integration for Dynamic Prompt Decorators.

This module provides integration between Prompt Decorators and the Model Context Protocol (MCP),
allowing users to apply decorators through MCP tools using the dynamic decorator implementation.

Usage:
    # Run as a standalone MCP server
    python -m prompt_decorators.integrations.mcp_dynamic

    # Or import and use in your own MCP server
    from prompt_decorators.integrations.mcp_dynamic import create_mcp_server

    mcp_server = create_mcp_server("my-decorator-server")
    mcp_server.run()
"""

import asyncio
import json
import logging
import sys
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Union

# Import the dynamic decorator implementation
from prompt_decorators.core.base import DecoratorBase
from prompt_decorators.core.dynamic_decorator import (
    DynamicDecorator,
    extract_decorators,
    parse_decorator,
)
from prompt_decorators.dynamic_decorators_module import (
    apply_dynamic_decorators,
    create_decorator_instance,
    get_available_decorators,
)

# Set up a global variable to track if MCP is available
MCP_AVAILABLE = False

# Try to import MCP
try:
    import mcp
    from mcp.server.prompt_template import PromptTemplate
    from mcp.server.server import Server as MCPServer
    from mcp.server.stdio import stdio_server
    from mcp.server.tool import Tool
    from mcp.server.tool_call import ToolCall
    from mcp.server.tool_result import ToolResult

    MCP_AVAILABLE = True
except ImportError:
    # Create dummy classes for type hints if MCP is not available
    # Use different names to avoid redefinition issues
    class DummyMCPServer:
        """Dummy MCPServer class for type hints."""

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            """Initialize the dummy server."""
            pass

        def add_tool(self, *args: Any, **kwargs: Any) -> None:
            """Add a tool to the dummy server."""
            pass

        def add_prompt_template(self, *args: Any, **kwargs: Any) -> None:
            """Add a prompt template to the dummy server."""
            pass

        def run_stdio(self) -> None:
            """Run the dummy server."""
            print(
                "MCP is not available. Install it with 'pip install \"mcp[cli]\"' to use this functionality."
            )
            sys.exit(1)

        async def run_async(self) -> None:
            """Run the dummy server asynchronously."""
            print(
                "MCP is not available. Install it with 'pip install \"mcp[cli]\"' to use this functionality."
            )
            sys.exit(1)

    class DummyPromptTemplate:
        """Dummy PromptTemplate class for type hints."""

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            """Initialize the dummy prompt template."""
            pass

    class DummyTool:
        """Dummy Tool class for type hints."""

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            """Initialize the dummy tool."""
            pass

    class DummyToolCall:
        """Dummy ToolCall class for type hints."""

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            """Initialize the dummy tool call."""
            pass

    class DummyToolResult:
        """Dummy ToolResult class for type hints."""

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            """Initialize the dummy tool result."""
            pass

    # Assign the dummy classes to the expected names
    MCPServer = DummyMCPServer
    PromptTemplate = DummyPromptTemplate
    Tool = DummyTool
    ToolCall = DummyToolCall
    ToolResult = DummyToolResult


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class DecoratorInfo:
    """Information about a decorator."""

    name: str
    description: str
    category: str
    parameters: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class TemplateInfo:
    """Information about a prompt template."""

    name: str
    description: str
    decorators: List[Dict[str, Any]] = field(default_factory=list)


def create_mcp_server(name: str) -> MCPServer:
    """Create an MCP server with prompt decorator integration.

    Args:
        name: Name of the server

    Returns:
        An MCP server instance
    """
    if not MCP_AVAILABLE:
        logger.warning("MCP is not available. Using dummy implementation.")
        return MCPServer(name)

    # Create the MCP server
    server = MCPServer(name)

    # Add tools for working with decorators
    server.add_tool(
        Tool(
            name="list_decorators",
            description="List all available prompt decorators",
            handler=list_decorators_tool,
        )
    )

    server.add_tool(
        Tool(
            name="get_decorator_details",
            description="Get details about a specific decorator",
            handler=get_decorator_details_tool,
            parameter_schema={
                "type": "object",
                "properties": {
                    "decorator_name": {
                        "type": "string",
                        "description": "Name of the decorator to get details for",
                    }
                },
                "required": ["decorator_name"],
            },
        )
    )

    server.add_tool(
        Tool(
            name="apply_decorators",
            description="Apply decorators to a prompt using the +++ syntax",
            handler=apply_decorators_tool,
            parameter_schema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "Prompt text with decorator annotations",
                    }
                },
                "required": ["prompt"],
            },
        )
    )

    server.add_tool(
        Tool(
            name="create_decorated_prompt",
            description="Create a decorated prompt using a template",
            handler=create_decorated_prompt_tool,
            parameter_schema={
                "type": "object",
                "properties": {
                    "template_name": {
                        "type": "string",
                        "description": "Name of the template to use",
                    },
                    "prompt": {
                        "type": "string",
                        "description": "Prompt text to use with the template",
                    },
                    "parameters": {
                        "type": "object",
                        "description": "Additional parameters for the template",
                    },
                },
                "required": ["template_name", "prompt"],
            },
        )
    )

    # Add prompt templates
    templates = create_default_templates()
    for template in templates:
        server.add_prompt_template(template)

    return server


def list_decorators_tool(tool_call: ToolCall) -> ToolResult:
    """List all available decorators.

    Args:
        tool_call: The tool call

    Returns:
        A tool result containing the list of decorators
    """
    try:
        # Get all available decorators
        decorators = get_available_decorators()

        # Convert to a list of dictionaries
        result = []
        for decorator in decorators:
            # Convert parameters to dictionaries
            param_dicts = []
            for param in decorator.parameters:
                if hasattr(param, "to_dict"):
                    param_dicts.append(param.to_dict())
                else:
                    # If to_dict is not available, create a dictionary manually
                    param_dicts.append(
                        {
                            "name": param.name if hasattr(param, "name") else "unknown",
                            "description": param.description
                            if hasattr(param, "description")
                            else "",
                            "type": param.type_
                            if hasattr(param, "type_")
                            else "string",
                            "required": param.required
                            if hasattr(param, "required")
                            else False,
                            "default": param.default
                            if hasattr(param, "default")
                            else None,
                        }
                    )

            result.append(
                {
                    "name": decorator.name,
                    "description": decorator.description,
                    "category": decorator.category,
                    "parameters": param_dicts,
                }
            )

        return ToolResult(content=result)
    except Exception as e:
        logger.error(f"Error listing decorators: {e}")
        return ToolResult(error=str(e))


def get_decorator_details_tool(tool_call: ToolCall) -> ToolResult:
    """Get details about a specific decorator.

    Args:
        tool_call: The tool call

    Returns:
        A tool result containing the decorator details
    """
    try:
        # Get the decorator name from the arguments
        decorator_name = tool_call.arguments.get("decorator_name")
        if not decorator_name:
            return ToolResult(error="Decorator name is required")

        # Get all available decorators
        decorators = get_available_decorators()

        # Find the requested decorator
        for decorator in decorators:
            if decorator.name == decorator_name:
                # Convert parameters to dictionaries
                param_dicts = []
                for param in decorator.parameters:
                    if hasattr(param, "to_dict"):
                        param_dicts.append(param.to_dict())
                    else:
                        # If to_dict is not available, create a dictionary manually
                        param_dicts.append(
                            {
                                "name": param.name
                                if hasattr(param, "name")
                                else "unknown",
                                "description": param.description
                                if hasattr(param, "description")
                                else "",
                                "type": param.type_
                                if hasattr(param, "type_")
                                else "string",
                                "required": param.required
                                if hasattr(param, "required")
                                else False,
                                "default": param.default
                                if hasattr(param, "default")
                                else None,
                            }
                        )

                # Convert to a dictionary
                result = {
                    "name": decorator.name,
                    "description": decorator.description,
                    "category": decorator.category,
                    "parameters": param_dicts,
                    "version": decorator.version,
                }
                return ToolResult(content=result)

        return ToolResult(error=f"Decorator '{decorator_name}' not found")
    except Exception as e:
        logger.error(f"Error getting decorator details: {e}")
        return ToolResult(error=str(e))


def apply_decorators_tool(tool_call: ToolCall) -> ToolResult:
    """Apply decorators to a prompt.

    Args:
        tool_call: The tool call

    Returns:
        A tool result containing the transformed prompt
    """
    try:
        # Get the prompt from the arguments
        prompt = tool_call.arguments.get("prompt")
        if not prompt:
            return ToolResult(error="Prompt is required")

        # Extract decorators from the prompt
        decorators, clean_prompt = extract_decorators(prompt)

        # Apply decorators
        transformed_prompt = clean_prompt
        for decorator in decorators:
            transformed = decorator(transformed_prompt)
            if isinstance(transformed, str):
                transformed_prompt = transformed
            else:
                # This should not happen in normal usage, but handle it just in case
                transformed_prompt = str(transformed)

        # Create the result
        result = {
            "original_prompt": prompt,
            "transformed_prompt": transformed_prompt,
            "decorators_applied": [decorator.name for decorator in decorators],
        }

        return ToolResult(content=result)
    except Exception as e:
        logger.error(f"Error applying decorators: {e}")
        return ToolResult(error=str(e))


def create_decorated_prompt_tool(tool_call: ToolCall) -> ToolResult:
    """Create a decorated prompt using a template.

    Args:
        tool_call: The tool call

    Returns:
        A tool result containing the decorated prompt
    """
    try:
        # Get the template name and prompt from the arguments
        template_name = tool_call.arguments.get("template_name")
        prompt = tool_call.arguments.get("prompt")

        if not template_name:
            return ToolResult(error="Template name is required")
        if not prompt:
            return ToolResult(error="Prompt is required")

        # Get the template
        templates = create_default_templates()
        template = None
        for t in templates:
            if t.name == template_name:
                template = t
                break

        if not template:
            return ToolResult(error=f"Template '{template_name}' not found")

        # Apply the template
        decorator_strings = []
        for decorator_info in template.metadata.get("decorators", []):
            decorator_name = decorator_info.get("name")
            parameters = decorator_info.get("parameters", {})

            # Create the decorator string
            if parameters:
                param_str = ", ".join(
                    f"{k}='{v}'" if isinstance(v, str) else f"{k}={v}"
                    for k, v in parameters.items()
                )
                decorator_str = f"+++{decorator_name}({param_str})"
            else:
                decorator_str = f"+++{decorator_name}"

            decorator_strings.append(decorator_str)

        # Combine decorators with the prompt
        decorated_prompt = "\n".join(decorator_strings) + f"\n{prompt}"

        # Apply the decorators
        transformed_prompt = apply_dynamic_decorators(decorated_prompt)

        # Ensure transformed_prompt is a string
        if not isinstance(transformed_prompt, str):
            transformed_prompt = str(transformed_prompt)

        # Create the result
        result = {
            "original_prompt": prompt,
            "decorated_prompt": decorated_prompt,
            "transformed_prompt": transformed_prompt,
            "decorators_applied": [
                d.get("name") for d in template.metadata.get("decorators", [])
            ],
        }

        return ToolResult(content=result)
    except Exception as e:
        logger.error(f"Error creating decorated prompt: {e}")
        return ToolResult(error=str(e))


def create_default_templates() -> List[PromptTemplate]:
    """Create default prompt templates.

    Returns:
        A list of prompt templates
    """
    templates = []

    # Template 1: Detailed reasoning
    templates.append(
        PromptTemplate(
            name="detailed_reasoning",
            description="Detailed reasoning with step-by-step breakdown",
            template="{prompt}",
            metadata={
                "decorators": [
                    {"name": "Reasoning", "parameters": {"depth": "comprehensive"}},
                    {"name": "StepByStep", "parameters": {"numbered": True}},
                ],
            },
        )
    )

    # Template 2: Beginner explanation
    templates.append(
        PromptTemplate(
            name="beginner_explanation",
            description="Explain a concept to a beginner",
            template="{prompt}",
            metadata={
                "decorators": [
                    {"name": "Audience", "parameters": {"level": "beginner"}},
                    {"name": "Detailed", "parameters": {"examples": True}},
                ],
            },
        )
    )

    # Template 3: Technical documentation
    templates.append(
        PromptTemplate(
            name="technical_documentation",
            description="Generate technical documentation",
            template="{prompt}",
            metadata={
                "decorators": [
                    {"name": "Audience", "parameters": {"level": "expert"}},
                    {"name": "Format", "parameters": {"style": "markdown"}},
                    {"name": "Detailed", "parameters": {"examples": True}},
                ],
            },
        )
    )

    # Template 4: Creative writing
    templates.append(
        PromptTemplate(
            name="creative_writing",
            description="Generate creative content",
            template="{prompt}",
            metadata={
                "decorators": [
                    {"name": "Creative", "parameters": {"style": "narrative"}},
                    {"name": "Detailed", "parameters": {"imagery": True}},
                ],
            },
        )
    )

    # Template 5: Concise summary
    templates.append(
        PromptTemplate(
            name="concise_summary",
            description="Generate a concise summary",
            template="{prompt}",
            metadata={
                "decorators": [
                    {"name": "Concise", "parameters": {"max_words": 100}},
                    {"name": "Format", "parameters": {"style": "bullet_points"}},
                ],
            },
        )
    )

    # Template 6: Pros and cons analysis
    templates.append(
        PromptTemplate(
            name="pros_cons_analysis",
            description="Analyze pros and cons of a topic",
            template="{prompt}",
            metadata={
                "decorators": [
                    {"name": "ProsAndCons", "parameters": {}},
                    {"name": "Balanced", "parameters": {}},
                    {"name": "Format", "parameters": {"style": "table"}},
                ],
            },
        )
    )

    return templates


def main() -> None:
    """Run the MCP server."""
    # Create and run the server
    server = create_mcp_server("prompt-decorators")
    server.run_stdio()


if __name__ == "__main__":
    main()

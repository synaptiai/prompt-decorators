#!/usr/bin/env python3
"""
Example script for using the MCP client with Dynamic Prompt Decorators.

This script demonstrates how to connect to the prompt-decorators MCP server
that uses the dynamic implementation and use the various tools provided by the integration.

Requirements:
- prompt-decorators
- mcp[cli]

Usage:
    python prompt_decorators/integrations/mcp/examples/mcp_client_example.py
"""

import asyncio
import json
import logging
import os
import sys
from typing import Any, Dict, List, Optional

from mcp import ClientSession, StdioServerParameters, stdio_client
from mcp.types import TextContent

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("mcp-client-example")


async def test_list_decorators(client: ClientSession) -> None:
    """Test the list_decorators tool."""
    logger.info("Testing list_decorators tool")

    try:
        # Call the list_decorators tool
        result = await client.call_tool("list_decorators", arguments={})

        # Access the content property of the CallToolResult
        if hasattr(result, "content") and result.content is not None:
            # The content should be a list of decorators
            decorators = result.content

            logger.info(f"Content type: {type(decorators)}")

            if isinstance(decorators, list):
                logger.info(f"Found {len(decorators)} decorators")
                for i, decorator in enumerate(decorators[:5]):  # Show first 5
                    if isinstance(decorator, dict):
                        logger.info(f"  {i+1}. {decorator.get('name', 'Unknown')}")
                    else:
                        logger.info(f"  {i+1}. {decorator}")
            else:
                logger.error("No content returned from list_decorators")
    except Exception as e:
        logger.error(f"Error in list_decorators: {str(e)}")


async def test_get_decorator_details(
    client: ClientSession, decorator_name: str
) -> None:
    """Test the get_decorator_details tool.

    Args:
        client: The MCP client session
        decorator_name: The name of the decorator to get details for
    """
    logger.info(f"Testing get_decorator_details for {decorator_name}")

    try:
        # Call the get_decorator_details tool
        result = await client.call_tool(
            "get_decorator_details", arguments={"decorator_name": decorator_name}
        )

        # Access the content property of the CallToolResult
        if hasattr(result, "content") and result.content is not None:
            # The content should be a dictionary with decorator details
            details = result.content

            if isinstance(details, dict):
                logger.info(f"Decorator details: {json.dumps(details, indent=2)}")
            else:
                logger.error(f"Unexpected response type: {type(details)}")
        else:
            logger.error("No content returned from get_decorator_details")
    except Exception as e:
        logger.error(f"Error in get_decorator_details: {str(e)}")


async def test_apply_decorators(client: ClientSession, prompt: str) -> None:
    """Test the apply_decorators tool.

    Args:
        client: The MCP client session
        prompt: The prompt to apply decorators to
    """
    logger.info(f"Testing apply_decorators with prompt: {prompt}")

    try:
        # Call the apply_decorators tool
        result = await client.call_tool(
            "apply_decorators", arguments={"prompt": prompt}
        )

        # Access the content property of the CallToolResult
        if hasattr(result, "content") and result.content is not None:
            # The content should be a dictionary with the transformed prompt
            response = result.content

            if isinstance(response, dict):
                logger.info(f"Original prompt: {response.get('original_prompt', '')}")
                logger.info(
                    f"Transformed prompt: {response.get('transformed_prompt', '')[:100]}..."
                )
                logger.info(
                    f"Decorators applied: {response.get('decorators_applied', [])}"
                )
            else:
                logger.error(f"Unexpected response type: {type(response)}")
        else:
            logger.error("No content returned from apply_decorators")
    except Exception as e:
        logger.error(f"Error in apply_decorators: {str(e)}")


async def test_create_decorated_prompt(
    client: ClientSession,
    template_name: str,
    prompt: str,
    additional_params: Optional[Dict[str, Any]] = None,
) -> None:
    """Test the create_decorated_prompt tool.

    Args:
        client: The MCP client session
        template_name: The name of the template to use
        prompt: The prompt to decorate
        additional_params: Optional additional parameters for the template
    """
    logger.info(
        f"Testing create_decorated_prompt with template: {template_name}, prompt: {prompt}"
    )

    try:
        # Prepare arguments
        arguments: Dict[str, Any] = {
            "template_name": template_name,
            "prompt": prompt,
        }
        if additional_params:
            arguments["additional_params"] = additional_params

        # Call the create_decorated_prompt tool
        result = await client.call_tool("create_decorated_prompt", arguments=arguments)

        # Access the content property of the CallToolResult
        if hasattr(result, "content") and result.content is not None:
            # The content should be a dictionary with the decorated prompt
            response: Dict[str, Any] = {}

            # Convert the content to a dictionary if it's not already
            if isinstance(result.content, dict):
                response = result.content
            elif hasattr(result.content, "to_dict"):
                response = result.content.to_dict()
            elif isinstance(result.content, str):
                try:
                    response = json.loads(result.content)
                except json.JSONDecodeError:
                    response = {"text": result.content}
            else:
                response = {"content": str(result.content)}

            if isinstance(response, dict):
                logger.info(f"Original prompt: {response.get('original_prompt', '')}")
                logger.info(
                    f"Decorated prompt: {response.get('decorated_prompt', '')[:100]}..."
                )
                logger.info(f"Template used: {response.get('template_name', '')}")
                logger.info(
                    f"Decorators applied: {response.get('decorators_applied', [])}"
                )
            else:
                logger.error(f"Unexpected response type: {type(response)}")
        else:
            logger.error("No content returned from create_decorated_prompt")
    except Exception as e:
        logger.error(f"Error in create_decorated_prompt: {str(e)}")


async def main() -> None:
    """
    Run the main client example flow.
    """
    logger.info("Starting MCP client for Prompt Decorators (Dynamic Version)...")

    # Default server parameters for stdio connection
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "prompt_decorators.integrations.mcp_dynamic"],
        env={"PYTHONPATH": os.getcwd()},
    )

    # Connect to the MCP server
    async with stdio_client(server_params) as client:
        logger.info("Connected to MCP server")

        # 1. List available decorators
        await test_list_decorators(client)

        # 2. Get details for a specific decorator
        await test_get_decorator_details(client, "StepByStep")

        # 3. Apply decorators to a prompt
        await test_apply_decorators(
            client, "+++StepByStep(numbered=true)\nHow to build a website?"
        )

        # 4. Create a decorated prompt using a template
        await test_create_decorated_prompt(
            client, "beginner_explanation", "How does quantum computing work?"
        )

    logger.info("Example complete")


if __name__ == "__main__":
    asyncio.run(main())

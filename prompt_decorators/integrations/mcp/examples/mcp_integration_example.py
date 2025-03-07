#!/usr/bin/env python
"""
Example script demonstrating the MCP integration with Dynamic Prompt Decorators.

This script shows how to:
1. Start an MCP server with Dynamic Prompt Decorators integration
2. Connect to the server using an MCP client
3. Use the various tools provided by the integration

Requirements:
- prompt-decorators
- mcp[cli]
"""

import asyncio
import json
import logging
import os
import sys
from typing import Any, Dict, List

try:
    from mcp import ClientSession
    from mcp.client.stdio import StdioServerParameters, stdio_client
except ImportError:
    raise ImportError(
        "This example requires the 'mcp' package. "
        "Install it with 'pip install \"mcp[cli]\"'"
    )

from prompt_decorators.integrations.mcp_dynamic import create_mcp_server

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("mcp-example")


async def run_client() -> None:
    """
    Run an MCP client to interact with the server.
    """
    logger.info("Connecting to MCP server")

    # Create server parameters for stdio connection
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "prompt_decorators.integrations.mcp_dynamic"],
        env={"PYTHONPATH": os.getcwd()},
    )

    # Connect to the MCP server
    async with stdio_client(server_params) as client:
        logger.info("Connected to MCP server")

        # 1. List available decorators
        result = await client.call_tool("list_decorators", arguments={})
        if hasattr(result, "content") and result.content is not None:
            decorators = result.content
            if isinstance(decorators, list):
                logger.info(f"Found {len(decorators)} decorators")
                for i, decorator in enumerate(decorators[:5]):  # Show first 5
                    logger.info(f"  {i+1}. {decorator.get('name', 'Unknown')}")

        # 2. Get details for StepByStep decorator
        result = await client.call_tool(
            "get_decorator_details", arguments={"decorator_name": "StepByStep"}
        )
        if hasattr(result, "content") and result.content is not None:
            details = result.content
            if isinstance(details, dict):
                logger.info(f"StepByStep details: {json.dumps(details, indent=2)}")

        # 3. Apply decorators to a prompt
        result = await client.call_tool(
            "apply_decorators",
            arguments={
                "prompt": "+++StepByStep(numbered=true)\nHow to build a website?"
            },
        )
        if hasattr(result, "content") and result.content is not None:
            response = result.content
            if isinstance(response, dict):
                logger.info(f"Original prompt: {response.get('original_prompt', '')}")
                logger.info(
                    f"Transformed prompt: {response.get('transformed_prompt', '')[:100]}..."
                )
                logger.info(
                    f"Decorators applied: {response.get('decorators_applied', [])}"
                )

        # 4. Create a decorated prompt using a template
        result = await client.call_tool(
            "create_decorated_prompt",
            arguments={
                "template_name": "beginner_explanation",
                "prompt": "How does quantum computing work?",
            },
        )
        if hasattr(result, "content") and result.content is not None:
            response = result.content
            if isinstance(response, dict):
                logger.info(f"Original prompt: {response.get('original_prompt', '')}")
                logger.info(
                    f"Decorated prompt: {response.get('decorated_prompt', '')[:100]}..."
                )
                logger.info(f"Template used: {response.get('template_name', '')}")
                logger.info(
                    f"Decorators applied: {response.get('decorators_applied', [])}"
                )

        logger.info("Client interaction complete")


async def main() -> None:
    """
    Start the MCP server and run a client to interact with it.
    """
    logger.info("Starting MCP integration example for Dynamic Prompt Decorators...")

    # Create and start the MCP server
    server = create_mcp_server("prompt-decorators-example")

    # Start the client and server concurrently
    await asyncio.gather(
        server.run_async(),  # This will block indefinitely
        run_client(),  # This will complete after running the tests
    )


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(main())

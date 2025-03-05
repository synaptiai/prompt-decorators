#!/usr/bin/env python
"""
Example script demonstrating the MCP integration with Prompt Decorators.

This script shows how to:
1. Start an MCP server with Prompt Decorators integration
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
from typing import Any, Dict, List

try:
    from mcp import ClientSession
    from mcp.client.stdio import StdioServerParameters, stdio_client
except ImportError:
    raise ImportError(
        "This example requires the 'mcp' package. "
        "Install it with 'pip install \"mcp[cli]\"'"
    )

from prompt_decorators.integrations.mcp import create_mcp_server

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
        command=["python", "-m", "prompt_decorators.integrations.mcp"],
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as client:
            # Initialize the connection
            await client.initialize()

            # Example 1: Apply decorators using the +++ syntax
            logger.info("Example 1: Applying decorators using +++ syntax")
            decorated_result = await client.call_tool(
                "apply_decorators",
                arguments={
                    "prompt": "+++Reasoning(depth='comprehensive')\n+++StepByStep()\nExplain quantum computing."
                },
            )
            print("\n=== Example 1: Apply Decorators ===")
            print(f"Original prompt: {decorated_result['original_prompt']}")
            print(f"Transformed prompt: {decorated_result['transformed_prompt']}")
            print(
                f"Decorators applied: {json.dumps(decorated_result['decorators_applied'], indent=2)}"
            )

            # Example 2: List available decorators
            logger.info("Example 2: Listing available decorators")
            decorators = await client.call_tool("list_decorators", arguments={})
            print("\n=== Example 2: List Decorators ===")
            print(f"Found {len(decorators)} decorators")
            # Print first 3 decorators as example
            for decorator in decorators[:3]:
                print(f"- {decorator['name']}: {decorator['description']}")

            # Example 3: Get details for a specific decorator
            logger.info("Example 3: Getting details for a specific decorator")
            details = await client.call_tool(
                "get_decorator_details", arguments={"decorator_name": "Reasoning"}
            )
            print("\n=== Example 3: Decorator Details ===")
            print(f"Name: {details['name']}")
            print(f"Description: {details['description']}")
            print(f"Category: {details['category']}")
            print(f"Parameters: {json.dumps(details['parameters'], indent=2)}")

            # Example 4: Use a predefined template
            logger.info("Example 4: Using a predefined template")
            template_result = await client.call_tool(
                "create_decorated_prompt",
                arguments={
                    "template_name": "detailed-reasoning",
                    "prompt": "Explain how quantum computing works.",
                },
            )
            print("\n=== Example 4: Use Template ===")
            print(f"Original prompt: {template_result['original_prompt']}")
            print(f"Template used: {template_result['template_used']}")
            print(f"Transformed prompt: {template_result['transformed_prompt']}")

            # Example 5: List available prompt templates
            logger.info("Example 5: Listing available prompts")
            prompts = await client.list_prompts()
            print("\n=== Example 5: List Templates ===")
            print(f"Found {len(prompts)} templates")
            # Print first 3 templates as example
            for i, prompt in enumerate(prompts[:3]):
                print(f"- {prompt.name}: {prompt.description}")

            # Example 6: Use a template through the prompts API
            logger.info("Example 6: Using a template through the prompts API")
            prompt_result = await client.get_prompt(
                "explain-simply",
                arguments={"prompt": "Explain how nuclear fusion works."},
            )
            print("\n=== Example 6: Use Template via Prompts API ===")
            print(f"Generated prompt: {prompt_result}")


async def main() -> None:
    """Run the MCP server and client."""
    # Create and start the MCP server
    logger.info("Starting MCP server")
    server = create_mcp_server("prompt-decorators-example")

    # Start the server in a separate task
    server_task = asyncio.create_task(server.run_stdio_async())

    try:
        # Wait a moment for the server to start
        await asyncio.sleep(1)

        # Run the client
        await run_client()
    finally:
        # Stop the server
        logger.info("Stopping MCP server")
        server_task.cancel()
        try:
            await server_task
        except asyncio.CancelledError:
            pass


if __name__ == "__main__":
    asyncio.run(main())

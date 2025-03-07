"""
Example script demonstrating Claude Desktop integration with Prompt Decorators via MCP.

This script simulates how Claude Desktop might integrate with the Prompt Decorators
MCP server to apply decorators to prompts before sending them to the Claude API.

Requirements:
- prompt-decorators
- mcp[cli]

Usage:
    python prompt_decorators/integrations/mcp/examples/claude_desktop_example.py
"""

import asyncio
import json
import logging
import os
import sys
from typing import Any, Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("claude-desktop-example")


async def simulate_claude_desktop() -> None:
    """Simulate the Claude Desktop integration with the MCP server."""
    try:
        # Import the MCP client modules
        from mcp.client.session import ClientSession
        from mcp.client.stdio import StdioServerParameters, stdio_client

        # Set up server parameters
        server_params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "prompt_decorators.integrations.mcp_dynamic"],
            env={"PYTHONPATH": os.getcwd()},
        )

        # Connect to the server
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                logger.info("Connected to MCP server")

                # Simulate the Claude Desktop prompt with decorators
                test_prompt = "+++Reasoning(depth='comprehensive')\n+++StepByStep()\nExplain quantum computing"

                # Call the apply_decorators tool
                logger.info(f"Applying decorators to prompt: {test_prompt}")
                result = await session.call_tool(
                    "apply_decorators", {"prompt": test_prompt}
                )

                # Print the results
                print("\n=== Claude Desktop Prompt Decoration ===")
                print("Original prompt:", result.get("original_prompt"))
                print("\nTransformed prompt:", result.get("transformed_prompt"))

                # Print the decorators applied
                decorators = result.get("decorators_applied", [])
                print(f"\nDecorators applied ({len(decorators)}):")
                for i, decorator in enumerate(decorators, 1):
                    print(f"{i}. {decorator}")

                logger.info("Claude Desktop simulation completed successfully")

    except Exception as e:
        logger.error(f"Error in Claude Desktop simulation: {str(e)}")
        raise


async def main() -> None:
    """Run the Claude Desktop simulation."""
    await simulate_claude_desktop()


if __name__ == "__main__":
    asyncio.run(main())

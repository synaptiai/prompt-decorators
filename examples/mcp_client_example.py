#!/usr/bin/env python3
"""
Example script for using the MCP client with Prompt Decorators.

This script demonstrates how to connect to the prompt-decorators MCP server
and use the various tools provided by the integration.

Requirements:
- prompt-decorators
- mcp[cli]

Usage:
    python examples/mcp_client_example.py
"""

import asyncio
import json
import logging
import os
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

                # Print first 5 decorators as example
                for i, decorator in enumerate(decorators[:5]):
                    if (
                        isinstance(decorator, dict)
                        and "name" in decorator
                        and "description" in decorator
                    ):
                        logger.info(
                            f"{i+1}. {decorator['name']}: {decorator['description']}"
                        )
            else:
                logger.info(f"Content is not a list: {decorators}")
        else:
            logger.error("No content found in result")

        return result
    except Exception as e:
        logger.error(f"Error listing decorators: {str(e)}")
        return None


async def test_get_decorator_details(
    client: ClientSession, decorator_name: str
) -> None:
    """Test the get_decorator_details tool."""
    logger.info(f"Testing get_decorator_details tool for {decorator_name}")

    try:
        # Call the get_decorator_details tool
        result = await client.call_tool(
            "get_decorator_details", arguments={"decorator_name": decorator_name}
        )

        # Access the content property of the CallToolResult
        if hasattr(result, "content") and result.content is not None:
            # The content should be a dictionary with decorator details
            details = result.content

            logger.info(f"Content type: {type(details)}")

            if isinstance(details, dict):
                logger.info(f"Name: {details.get('name', 'N/A')}")
                logger.info(f"Description: {details.get('description', 'N/A')}")
                logger.info(f"Category: {details.get('category', 'N/A')}")
                logger.info(
                    f"Parameters: {json.dumps(details.get('parameters', {}), indent=2)}"
                )
            else:
                logger.info(f"Content is not a dictionary: {details}")
        else:
            logger.error("No content found in result")

        return result
    except Exception as e:
        logger.error(f"Error getting decorator details: {str(e)}")
        return None


async def test_apply_decorators(client: ClientSession, prompt: str) -> None:
    """Test the apply_decorators tool."""
    logger.info("Testing apply_decorators tool")

    try:
        # Call the apply_decorators tool
        result = await client.call_tool(
            "apply_decorators", arguments={"prompt": prompt}
        )

        # Access the content property of the CallToolResult
        if hasattr(result, "content") and result.content is not None:
            # The content should be a dictionary with transformation details
            data = result.content

            logger.info(f"Content type: {type(data)}")

            if isinstance(data, dict):
                logger.info(f"Original prompt: {data.get('original_prompt', 'N/A')}")
                logger.info(
                    f"Transformed prompt: {data.get('transformed_prompt', 'N/A')}"
                )
                logger.info(
                    f"Decorators applied: {json.dumps(data.get('decorators_applied', []), indent=2)}"
                )
            else:
                logger.info(f"Content is not a dictionary: {data}")
        else:
            logger.error("No content found in result")

        return result
    except Exception as e:
        logger.error(f"Error applying decorators: {str(e)}")
        return None


async def test_create_decorated_prompt(
    client: ClientSession,
    template_name: str,
    prompt: str,
    additional_params: Optional[Dict[str, Any]] = None,
) -> None:
    """Test the create_decorated_prompt tool."""
    logger.info(f"Testing create_decorated_prompt tool with template {template_name}")

    try:
        args = {"template_name": template_name, "prompt": prompt}

        if additional_params:
            args["additional_params"] = additional_params

        # Call the create_decorated_prompt tool
        result = await client.call_tool("create_decorated_prompt", arguments=args)

        # Access the content property of the CallToolResult
        if hasattr(result, "content") and result.content is not None:
            # The content should be a dictionary with template details
            data = result.content

            logger.info(f"Content type: {type(data)}")

            if isinstance(data, dict):
                logger.info(f"Original prompt: {data.get('original_prompt', 'N/A')}")
                logger.info(f"Template used: {data.get('template_used', 'N/A')}")
                logger.info(
                    f"Transformed prompt: {data.get('transformed_prompt', 'N/A')}"
                )
            else:
                logger.info(f"Content is not a dictionary: {data}")
        else:
            logger.error("No content found in result")

        return result
    except Exception as e:
        logger.error(f"Error creating decorated prompt: {str(e)}")
        return None


async def main():
    """Run the tests."""
    try:
        logger.info("Connecting to MCP server")

        # Initialize server parameters
        server_params = StdioServerParameters(
            command="/Users/danielbentes/.pyenv/versions/3.11.8/bin/python",
            args=["-m", "prompt_decorators.integrations.mcp"],
            cwd=os.getcwd(),
        )

        # Create client
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as client:
                # Initialize the client
                await client.initialize()

                # List available tools
                logger.info("Listing available tools")
                tools = await client.list_tools()
                logger.info(f"Available tools: {[tool.name for tool in tools.tools]}")

                # Test list_decorators
                logger.info("Getting all registered decorators")
                decorators = await client.call_tool("list_decorators")

                # Log information about the response
                logger.info(f"Decorators response type: {type(decorators)}")
                logger.info(f"Decorators response attributes: {dir(decorators)}")

                if hasattr(decorators, "content"):
                    logger.info(f"Content type: {type(decorators.content)}")

                    # Extract decorator names from TextContent objects
                    decorator_names = []
                    if isinstance(decorators.content, list):
                        for i, item in enumerate(decorators.content):
                            logger.info(f"Item {i} type: {type(item)}")
                            if hasattr(item, "text"):
                                logger.info(f"Item {i} text: {item.text}")
                                try:
                                    # Parse the JSON text to extract the decorator name
                                    decorator_data = json.loads(item.text)
                                    if "name" in decorator_data:
                                        decorator_names.append(decorator_data["name"])
                                except json.JSONDecodeError:
                                    logger.error(f"Failed to parse JSON from item {i}")

                    logger.info(
                        f"Extracted {len(decorator_names)} decorator names: {decorator_names[:5]}..."
                    )

                    if decorator_names:
                        # Test get_decorator_details with PascalCase
                        first_decorator = decorator_names[0]
                        logger.info(
                            f"Testing get_decorator_details with {first_decorator} (PascalCase)"
                        )
                        details_pascal = await client.call_tool(
                            "get_decorator_details", {"decorator_name": first_decorator}
                        )
                        logger.info(
                            f"Decorator details (PascalCase): {details_pascal.content}"
                        )

                        # Test get_decorator_details with snake_case
                        snake_case_name = "".join(
                            [
                                "_" + c.lower() if c.isupper() else c.lower()
                                for c in first_decorator
                            ]
                        ).lstrip("_")
                        logger.info(
                            f"Testing get_decorator_details with {snake_case_name} (snake_case)"
                        )
                        details_snake = await client.call_tool(
                            "get_decorator_details", {"decorator_name": snake_case_name}
                        )
                        logger.info(
                            f"Decorator details (snake_case): {details_snake.content}"
                        )

                        # Test apply_decorators with various decorators
                        known_decorators = [
                            "StepByStep",
                            "Concise",
                            "Balanced",
                            "Academic",
                            "Creative",
                        ]
                        for decorator in known_decorators:
                            logger.info(f"Testing apply_decorators with {decorator}")
                            prompt = (
                                f"This is a test prompt for the {decorator} decorator"
                            )
                            response = await client.call_tool(
                                "apply_decorators", {"prompt": prompt}
                            )
                            logger.info(f"Prompt: {prompt}")
                            logger.info(f"Response: {response}")

                        # Test apply_decorators with +++decorator syntax
                        logger.info("Testing apply_decorators with +++decorator syntax")
                        decorated_prompts = [
                            "+++StepByStep\nExplain how to make a sandwich",
                            "+++Concise\nDescribe the solar system",
                            "+++Balanced\nDiscuss the pros and cons of remote work",
                            "+++Academic\nExplain the theory of relativity",
                            "+++Creative\nWrite a short story about a robot",
                        ]

                        for prompt in decorated_prompts:
                            first_line = prompt.split("\n")[0]
                            logger.info(f"Testing prompt with decorator: {first_line}")
                            response = await client.call_tool(
                                "apply_decorators", {"prompt": prompt}
                            )
                            logger.info(f"Original prompt: {prompt}")

                            # Properly handle the response
                            if hasattr(response, "content") and response.content:
                                if (
                                    isinstance(response.content, list)
                                    and len(response.content) > 0
                                ):
                                    content_item = response.content[0]
                                    if hasattr(content_item, "text"):
                                        try:
                                            response_data = json.loads(
                                                content_item.text
                                            )
                                            logger.info(
                                                f"Transformed prompt: {response_data.get('transformed_prompt', 'N/A')}"
                                            )
                                            logger.info(
                                                f"Decorators applied: {response_data.get('decorators_applied', [])}"
                                            )
                                        except json.JSONDecodeError:
                                            logger.info(
                                                f"Response text (not JSON): {content_item.text}"
                                            )
                                    else:
                                        logger.info(
                                            f"Content item has no text attribute: {content_item}"
                                        )
                                else:
                                    logger.info(
                                        f"Response content is not a list or is empty: {response.content}"
                                    )
                            else:
                                logger.info("No content in response")

                        # Test get_decorator_details for the first known decorator
                        if known_decorators:
                            logger.info(
                                f"Testing get_decorator_details with {known_decorators[0]}"
                            )
                            details = await client.call_tool(
                                "get_decorator_details",
                                {"decorator_name": known_decorators[0]},
                            )
                            logger.info(f"Decorator details: {details.content}")

                        # Test create_decorated_prompt
                        logger.info("Testing create_decorated_prompt")
                        decorated_prompt = await client.call_tool(
                            "create_decorated_prompt",
                            {
                                "template_name": "detailed-reasoning",
                                "prompt": "This is a test prompt",
                            },
                        )
                        logger.info(f"Decorated prompt: {decorated_prompt.content}")

                logger.info("All tests completed successfully")
    except Exception as e:
        logger.error(f"Error: {e}")
        if hasattr(e, "__cause__") and e.__cause__:
            logger.error(f"Caused by: {e.__cause__}")


if __name__ == "__main__":
    asyncio.run(main())

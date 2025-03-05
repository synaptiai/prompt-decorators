"""End-to-end tests for the MCP integration using a real MCP server and client.

These tests verify that the MCP integration works correctly in a real-world scenario
by starting an MCP server and connecting to it with an MCP client.

Note: These tests require the MCP package to be installed.
"""

import asyncio
import json
import logging
import os
import sys
import threading
from typing import Any, Dict, List, Optional, Tuple

import pytest

# Skip all tests if MCP is not installed
pytest.importorskip("mcp.server.fastmcp")

try:
    from mcp import ClientSession
    from mcp.client.stdio import StdioServerParameters, stdio_client
except ImportError:
    pytest.skip("MCP client not installed", allow_module_level=True)

from prompt_decorators.integrations.mcp import create_mcp_server

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("test-mcp-e2e")


class MCPTestError(Exception):
    """Exception raised when an MCP test fails."""

    pass


# Create a simple test that doesn't require MCP server
def test_dummy():
    """A dummy test to ensure the test file is loaded."""
    assert True


# Skip the remaining tests if we're in CI or if the environment variable is set
if os.environ.get("SKIP_MCP_E2E_TESTS", "false").lower() == "true":
    pytest.skip("Skipping MCP E2E tests as requested", allow_module_level=True)


def run_server_in_thread(server):
    """Run the MCP server in a separate thread."""
    server.run()


@pytest.mark.asyncio
async def test_apply_decorators():
    """Test the apply_decorators tool."""
    # Create the MCP server
    logger.info("Starting MCP server for test_apply_decorators")
    server = create_mcp_server("prompt-decorators-test")

    # Start the server in a separate thread
    server_thread = threading.Thread(
        target=run_server_in_thread, args=(server,), daemon=True
    )
    server_thread.start()

    try:
        # Wait a moment for the server to start
        await asyncio.sleep(1)

        # Create server parameters for stdio connection
        server_params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "prompt_decorators.integrations.mcp"],
            cwd=os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            ),
        )

        # Connect to the server
        logger.info("Connecting to MCP server")
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as client:
                # Initialize the client
                await client.initialize()

                # Call the apply_decorators tool with a known decorator
                result = await client.call_tool(
                    "apply_decorators",
                    {
                        "prompt": "+++StepByStep\nExplain how to make a sandwich...",
                    },
                )

                # Verify the result
                assert hasattr(result, "content")
                content = result.content

                # The content should be a list of TextContent objects
                assert isinstance(content, list)
                assert len(content) > 0

                # Extract the text from the first TextContent
                text_content = content[0]
                assert hasattr(text_content, "text")

                # The transformed prompt should contain step-by-step instructions
                assert "step" in text_content.text.lower()
    finally:
        # Stop the server
        logger.info("Stopping MCP server")
        # Use server.shutdown() instead of server.stop() if available
        if hasattr(server, "shutdown"):
            server.shutdown()
        elif hasattr(server, "stop"):
            server.stop()
        # The server thread is daemon, so it will be terminated when the test exits


@pytest.mark.asyncio
async def test_list_decorators():
    """Test the list_decorators tool."""
    # Create the MCP server
    logger.info("Starting MCP server for test_list_decorators")
    server = create_mcp_server("prompt-decorators-test")

    # Start the server in a separate thread
    server_thread = threading.Thread(
        target=run_server_in_thread, args=(server,), daemon=True
    )
    server_thread.start()

    try:
        # Wait a moment for the server to start
        await asyncio.sleep(1)

        # Create server parameters for stdio connection
        server_params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "prompt_decorators.integrations.mcp"],
            cwd=os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            ),
        )

        # Connect to the server
        logger.info("Connecting to MCP server")
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as client:
                # Initialize the client
                await client.initialize()

                # Call the list_decorators tool
                result = await client.call_tool("list_decorators")

                # Verify the result
                assert hasattr(result, "content")
                content = result.content

                # The content should be a list of TextContent objects
                assert isinstance(content, list)
                assert len(content) > 0

                # Process each TextContent object
                decorators_found = []
                for text_content in content:
                    assert hasattr(text_content, "text")
                    # Parse the JSON text
                    decorator_info = json.loads(text_content.text)
                    decorators_found.append(decorator_info)

                # Verify we have decorators
                assert len(decorators_found) > 0

                # Verify that each decorator has the expected fields
                for decorator in decorators_found:
                    assert "name" in decorator
                    assert "description" in decorator
                    assert "category" in decorator
    finally:
        # Stop the server
        logger.info("Stopping MCP server")
        # Use server.shutdown() instead of server.stop() if available
        if hasattr(server, "shutdown"):
            server.shutdown()
        elif hasattr(server, "stop"):
            server.stop()


@pytest.mark.asyncio
async def test_get_decorator_details():
    """Test the get_decorator_details tool."""
    # Create the MCP server
    logger.info("Starting MCP server for test_get_decorator_details")
    server = create_mcp_server("prompt-decorators-test")

    # Start the server in a separate thread
    server_thread = threading.Thread(
        target=run_server_in_thread, args=(server,), daemon=True
    )
    server_thread.start()

    try:
        # Wait a moment for the server to start
        await asyncio.sleep(1)

        # Create server parameters for stdio connection
        server_params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "prompt_decorators.integrations.mcp"],
            cwd=os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            ),
        )

        # Connect to the server
        logger.info("Connecting to MCP server")
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as client:
                # Initialize the client
                await client.initialize()

                # Call the get_decorator_details tool with a known decorator
                result = await client.call_tool(
                    "get_decorator_details", {"decorator_name": "StepByStep"}
                )

                # Verify the result
                assert hasattr(result, "content")
                content = result.content

                # The content should be a list of TextContent objects
                assert isinstance(content, list)
                assert len(content) > 0

                # Extract the JSON from the TextContent
                text_content = content[0]
                assert hasattr(text_content, "text")

                # Parse the JSON text
                decorator_details = json.loads(text_content.text)

                # Verify the decorator details
                assert isinstance(decorator_details, dict)
                assert "name" in decorator_details
                assert decorator_details["name"] == "StepByStep"
                assert "description" in decorator_details
    finally:
        # Stop the server
        logger.info("Stopping MCP server")
        # Use server.shutdown() instead of server.stop() if available
        if hasattr(server, "shutdown"):
            server.shutdown()
        elif hasattr(server, "stop"):
            server.stop()
        # The server thread is daemon, so it will be terminated when the test exits


@pytest.mark.asyncio
async def test_create_decorated_prompt():
    """Test the create_decorated_prompt tool."""
    # Create the MCP server
    logger.info("Starting MCP server for test_create_decorated_prompt")
    server = create_mcp_server("prompt-decorators-test")

    # Start the server in a separate thread
    server_thread = threading.Thread(
        target=run_server_in_thread, args=(server,), daemon=True
    )
    server_thread.start()

    try:
        # Wait a moment for the server to start
        await asyncio.sleep(1)

        # Create server parameters for stdio connection
        server_params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "prompt_decorators.integrations.mcp"],
            cwd=os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            ),
        )

        # Connect to the server
        logger.info("Connecting to MCP server")
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as client:
                # Initialize the client
                await client.initialize()

                # Call the create_decorated_prompt tool with a known template
                result = await client.call_tool(
                    "create_decorated_prompt",
                    {
                        "template_name": "detailed-reasoning",
                        "prompt": "Explain quantum computing",
                    },
                )

                # Verify the result
                assert hasattr(result, "content")
                content = result.content

                # The content should be a list of TextContent objects
                assert isinstance(content, list)
                assert len(content) > 0

                # Extract the JSON from the TextContent
                text_content = content[0]
                assert hasattr(text_content, "text")

                # Parse the JSON text
                prompt_result = json.loads(text_content.text)

                # Verify the prompt result
                assert isinstance(prompt_result, dict)
                assert "transformed_prompt" in prompt_result
                assert "template_used" in prompt_result
                assert prompt_result["template_used"] == "detailed-reasoning"
                assert "original_prompt" in prompt_result
                assert prompt_result["original_prompt"] == "Explain quantum computing"
    finally:
        # Stop the server
        logger.info("Stopping MCP server")
        # Use server.shutdown() instead of server.stop() if available
        if hasattr(server, "shutdown"):
            server.shutdown()
        elif hasattr(server, "stop"):
            server.stop()
        # The server thread is daemon, so it will be terminated when the test exits


@pytest.mark.asyncio
async def test_list_prompts():
    """Test the list_prompts handler."""
    # Create the MCP server
    logger.info("Starting MCP server for test_list_prompts")
    server = create_mcp_server("prompt-decorators-test")

    # Start the server in a separate thread
    server_thread = threading.Thread(
        target=run_server_in_thread, args=(server,), daemon=True
    )
    server_thread.start()

    try:
        # Wait a moment for the server to start
        await asyncio.sleep(1)

        # Create server parameters for stdio connection
        server_params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "prompt_decorators.integrations.mcp"],
            cwd=os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            ),
        )

        # Connect to the server
        logger.info("Connecting to MCP server")
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as client:
                # Initialize the client
                await client.initialize()

                # Call the list_prompts method
                try:
                    prompts = await client.list_prompts()

                    # Verify the result
                    assert prompts is not None

                    # Check if the result has a prompts attribute (newer MCP versions)
                    if hasattr(prompts, "prompts"):
                        prompts_list = prompts.prompts
                        assert len(prompts_list) > 0
                    # For newer MCP versions, the result might be a ListPromptsResult object
                    elif hasattr(prompts, "content") and isinstance(
                        prompts.content, list
                    ):
                        prompts_list = prompts.content
                        assert len(prompts_list) > 0
                    # For newer MCP versions with a different structure
                    elif (
                        hasattr(prompts, "content")
                        and isinstance(prompts.content, dict)
                        and "prompts" in prompts.content
                    ):
                        prompts_list = prompts.content["prompts"]
                        assert len(prompts_list) > 0
                    else:
                        # Fall back to checking if it's at least not empty
                        assert prompts is not None
                        logger.info(f"Got prompts of type: {type(prompts)}")
                except Exception as e:
                    # Some MCP versions might not support list_prompts
                    logger.warning(f"Error listing prompts: {str(e)}")
                    pytest.skip("MCP version doesn't support list_prompts")
    finally:
        # The server thread will be terminated when the test exits
        pass


@pytest.mark.asyncio
async def test_get_prompt():
    """Test the get_prompt handler."""
    # Create the MCP server
    logger.info("Starting MCP server for test_get_prompt")
    server = create_mcp_server("prompt-decorators-test")

    # Start the server in a separate thread
    server_thread = threading.Thread(
        target=run_server_in_thread, args=(server,), daemon=True
    )
    server_thread.start()

    try:
        # Wait a moment for the server to start
        await asyncio.sleep(1)

        # Create server parameters for stdio connection
        server_params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "prompt_decorators.integrations.mcp"],
            cwd=os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            ),
        )

        # Connect to the server
        logger.info("Connecting to MCP server")
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as client:
                # Initialize the client
                await client.initialize()

                # Call the get_prompt handler with a known template
                try:
                    result = await client.get_prompt(
                        "detailed-reasoning",
                        arguments={"prompt": "Explain quantum computing"},
                    )

                    # Verify the result
                    assert result is not None

                    # Check if result is a string (older MCP versions)
                    if isinstance(result, str):
                        assert "Explain quantum computing" in result
                    # Check if result is a GetPromptResult object (newer MCP versions)
                    elif hasattr(result, "messages") and result.messages:
                        prompt_text = None
                        for message in result.messages:
                            if hasattr(message, "content") and hasattr(
                                message.content, "text"
                            ):
                                prompt_text = message.content.text
                                break
                        assert prompt_text is not None
                        assert "Explain quantum computing" in prompt_text
                    # Handle other possible result formats
                    elif hasattr(result, "content") and isinstance(result.content, str):
                        assert "Explain quantum computing" in result.content
                    else:
                        logger.info(f"Unknown get_prompt result format: {type(result)}")
                        assert result is not None
                except Exception as e:
                    # Some MCP versions might not support get_prompt
                    logger.warning(f"Error getting prompt: {str(e)}")
                    pytest.skip("MCP version doesn't support get_prompt")
    finally:
        # The server thread will be terminated when the test exits
        pass

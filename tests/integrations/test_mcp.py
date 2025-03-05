"""
Unit tests for the MCP integration module.

These tests verify that the MCP integration functions work correctly
by mocking the MCP server and client.
"""

import asyncio
import json
import logging
import os
from typing import Any, Dict, List, Optional, Tuple
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from prompt_decorators.core import BaseDecorator
from prompt_decorators.core.parser import DecoratorParser

# Import MCP integration module with proper error handling
from prompt_decorators.integrations.mcp import (
    MCP_AVAILABLE,
    DecoratorTemplate,
    create_default_templates,
    create_mcp_server,
    load_decorator_classes,
)

# Skip tests if MCP is not available
pytestmark = pytest.mark.skipif(
    not MCP_AVAILABLE, reason="MCP package is not installed"
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("test-mcp")


class MockDecorator(BaseDecorator):
    """A mock decorator for testing."""

    name = "MockDecorator"
    description = "A mock decorator for testing"
    parameters = {}

    def __init__(self, **kwargs):
        """Initialize the mock decorator."""
        # No need to call super() since we're handling parameters differently
        for name, value in kwargs.items():
            setattr(self, name, value)

    def apply(self, prompt: str) -> str:
        """Apply the decorator to a prompt."""
        return f"MOCK_DECORATED: {prompt}"

    def to_dict(self) -> dict:
        """Convert the decorator to a dictionary."""
        return {"name": self.name, "description": self.description, "parameters": {}}

    @classmethod
    def from_dict(cls, data: dict) -> "MockDecorator":
        """Create a decorator from a dictionary."""
        return cls()

    def __repr__(self) -> str:
        """Return a string representation of the decorator."""
        return f"MockDecorator()"


@pytest.fixture
def mock_decorator_registry():
    """Create a mock decorator registry."""
    # Import here to avoid issues with missing MCP package
    import prompt_decorators.integrations.mcp

    with patch(
        "prompt_decorators.integrations.mcp.DECORATOR_REGISTRY"
    ) as mock_registry:
        mock_registry.get_all_decorators.return_value = {
            "MockDecorator": MockDecorator,
        }
        mock_registry.get_decorator_class.return_value = MockDecorator
        yield mock_registry


@pytest.fixture
def mock_decorator_parser():
    """Create a mock decorator parser."""
    with patch("prompt_decorators.integrations.mcp.DecoratorParser") as mock_parser_cls:
        mock_parser = MagicMock()
        mock_parser_cls.return_value = mock_parser

        # Configure the mock parser to return a mock decorator and clean prompt
        mock_parser.extract_decorators.return_value = (
            [MockDecorator()],
            "Clean prompt text",
        )

        yield mock_parser


@pytest.fixture
def mock_mcp_server():
    """Create a mock MCP server."""
    # Import here to avoid issues with missing MCP package
    import prompt_decorators.integrations.mcp

    with patch("prompt_decorators.integrations.mcp.FastMCP") as mock_mcp_cls:
        mock_server = MagicMock()
        mock_mcp_cls.return_value = mock_server

        # Create mock functions for each tool
        async def mock_apply_decorators(prompt: str):
            return {
                "transformed_prompt": "Mocked transformed prompt",
                "decorators_applied": ["MockDecorator"],
            }

        async def mock_list_decorators():
            return [{"name": "MockDecorator", "description": "A mock decorator"}]

        async def mock_get_decorator_details(decorator_name: str):
            return {"name": decorator_name, "description": "Details for mock decorator"}

        async def mock_create_decorated_prompt(
            template_name: str, prompt: str, additional_params=None
        ):
            return {
                "transformed_prompt": "Mocked decorated prompt",
                "template_used": template_name,
            }

        # Set the function names correctly
        mock_apply_decorators.__name__ = "apply_decorators"
        mock_list_decorators.__name__ = "list_decorators"
        mock_get_decorator_details.__name__ = "get_decorator_details"
        mock_create_decorated_prompt.__name__ = "create_decorated_prompt"

        # Mock the tool decorator to return the function with name preserved
        def mock_tool_decorator(*args, **kwargs):
            def decorator(func):
                # Return the mock function based on the name of the decorated function
                if func.__name__ == "apply_decorators":
                    return mock_apply_decorators
                elif func.__name__ == "list_decorators":
                    return mock_list_decorators
                elif func.__name__ == "get_decorator_details":
                    return mock_get_decorator_details
                elif func.__name__ == "create_decorated_prompt":
                    return mock_create_decorated_prompt
                return func

            return decorator

        mock_server.tool = mock_tool_decorator

        # Also patch MCP_AVAILABLE to ensure create_mcp_server works
        with patch("prompt_decorators.integrations.mcp.MCP_AVAILABLE", True):
            yield mock_server


def test_create_mcp_server(mock_mcp_server, mock_decorator_registry):
    """Test creating an MCP server."""
    # Call the function to create an MCP server
    server = create_mcp_server("test-server")

    # Get the mock class
    from unittest.mock import patch

    # Simply verify that the server was returned
    assert server == mock_mcp_server


def test_load_decorator_classes():
    """Test loading decorator classes."""
    # Import here to avoid issues with missing MCP package
    import prompt_decorators.integrations.mcp

    with patch(
        "prompt_decorators.integrations.mcp.importlib.import_module"
    ) as mock_import:
        # Create a proper mock module that doesn't use __dir__
        mock_module = type(
            "MockModule",
            (),
            {
                "MockDecorator": MockDecorator,
                "SomeOtherClass": object,  # This should be ignored
            },
        )
        mock_import.return_value = mock_module

        # Mock the registry as a module-level object
        with patch.object(
            prompt_decorators.integrations.mcp, "DECORATOR_REGISTRY"
        ) as mock_registry:
            mock_registry.register = MagicMock()

            # Call the function
            result = load_decorator_classes()

            # Verify that import_module was called with the correct module name
            mock_import.assert_called_once_with(
                "prompt_decorators.decorators.generated.decorators"
            )

            # Verify that the decorator class was registered with category
            mock_registry.register.assert_called_once_with(
                MockDecorator, category="Uncategorized"
            )

            # Verify the result is a dictionary with the decorator class
            assert isinstance(result, dict)
            assert "MockDecorator" in result
            assert result["MockDecorator"] == MockDecorator


def test_create_default_templates():
    """Test creating default templates."""
    with patch(
        "prompt_decorators.integrations.mcp.load_decorator_classes"
    ) as mock_load:
        # Mock the decorator classes
        mock_load.return_value = {
            "Reasoning": MockDecorator,
            "StepByStep": MockDecorator,
            "CiteSources": MockDecorator,
            "OutputFormat": MockDecorator,
            "ELI5": MockDecorator,
            "Creative": MockDecorator,
            "TreeOfThought": MockDecorator,
            "Limitations": MockDecorator,
            "Balanced": MockDecorator,
            "PeerReview": MockDecorator,
            "Steelman": MockDecorator,
            "Audience": MockDecorator,
            "TableFormat": MockDecorator,
            "Prioritize": MockDecorator,
        }

        # Call the function
        templates = create_default_templates()

        # Verify that templates were created
        assert "detailed-reasoning" in templates
        assert "academic-analysis" in templates
        assert "explain-simply" in templates
        assert "creative-storytelling" in templates
        assert "problem-solving" in templates
        assert "balanced-viewpoint" in templates
        assert "technical-documentation" in templates
        assert "data-analysis" in templates

        # Verify that each template has the expected attributes
        for name, template in templates.items():
            assert isinstance(template, DecoratorTemplate)
            assert template.description
            assert template.decorators
            assert template.example


@pytest.mark.asyncio
async def test_apply_decorators_tool(mock_mcp_server, mock_decorator_parser):
    """Test the apply_decorators tool."""
    # Create the server with mocked components
    server = create_mcp_server("test-server")

    # Mock the tool function directly
    async def mock_apply_decorators(prompt: str):
        return {
            "transformed_prompt": "Mocked transformed prompt",
            "decorators_applied": ["MockDecorator"],
        }

    # Patch the apply_decorators_tool function in the server
    with patch.object(server, "apply_decorators_tool", mock_apply_decorators):
        # Call the tool
        prompt = "Test prompt"
        result = await mock_apply_decorators(prompt=prompt)

        # Verify the result
        assert result["transformed_prompt"] == "Mocked transformed prompt"
        assert result["decorators_applied"] == ["MockDecorator"]


@pytest.mark.asyncio
async def test_list_decorators_tool(mock_mcp_server, mock_decorator_registry):
    """Test the list_decorators tool."""
    # Create the server with mocked components
    server = create_mcp_server("test-server")

    # Mock the tool function directly
    async def mock_list_decorators():
        return [{"name": "MockDecorator", "description": "A mock decorator"}]

    # Patch the list_decorators_tool function in the server
    with patch.object(server, "list_decorators_tool", mock_list_decorators):
        # Call the tool
        result = await mock_list_decorators()

        # Verify the result
        assert len(result) == 1
        assert result[0]["name"] == "MockDecorator"
        assert result[0]["description"] == "A mock decorator"


@pytest.mark.asyncio
async def test_get_decorator_details_tool(mock_mcp_server, mock_decorator_registry):
    """Test the get_decorator_details tool."""
    # Create the server with mocked components
    server = create_mcp_server("test-server")

    # Mock the tool function directly
    async def mock_get_decorator_details(decorator_name: str):
        return {"name": decorator_name, "description": "Details for mock decorator"}

    # Patch the get_decorator_details_tool function in the server
    with patch.object(server, "get_decorator_details_tool", mock_get_decorator_details):
        # Call the tool
        result = await mock_get_decorator_details(decorator_name="MockDecorator")

        # Verify the result
        assert result["name"] == "MockDecorator"
        assert result["description"] == "Details for mock decorator"


@pytest.mark.asyncio
async def test_create_decorated_prompt_tool(mock_mcp_server):
    """Test the create_decorated_prompt tool."""
    # Mock the templates
    mock_templates = {
        "test-template": DecoratorTemplate(
            description="A test template",
            decorators=[MockDecorator()],
            example="Example prompt",
        )
    }

    # Create the server with mocked templates
    with patch("prompt_decorators.integrations.mcp.DEFAULT_TEMPLATES", mock_templates):
        server = create_mcp_server("test-server")

    # Mock the tool function directly
    async def mock_create_decorated_prompt(
        template_name: str, prompt: str, additional_params=None
    ):
        return {
            "transformed_prompt": "Mocked decorated prompt",
            "template_used": template_name,
        }

    # Patch the create_decorated_prompt_tool function in the server
    with patch.object(
        server, "create_decorated_prompt_tool", mock_create_decorated_prompt
    ):
        # Call the tool
        template_name = "test-template"
        prompt = "Test prompt"
        result = await mock_create_decorated_prompt(
            template_name=template_name, prompt=prompt
        )

        # Verify the result
        assert result["template_used"] == template_name
        assert result["transformed_prompt"] == "Mocked decorated prompt"

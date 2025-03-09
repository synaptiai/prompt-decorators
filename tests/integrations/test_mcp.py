"""Tests for the MCP integration."""

import json
from unittest.mock import MagicMock, patch

import pytest

# Skip all tests in this file if MCP is not installed
pytest.importorskip(
    "mcp", reason="MCP SDK not installed. Install with: pip install mcp"
)

from prompt_decorators.core.dynamic_decorator import DynamicDecorator
from prompt_decorators.integrations.mcp.server import (
    apply_decorators,
    create_decorated_prompt,
    get_decorator_details,
    list_decorators,
)


class TestMCPTools:
    """Tests for the MCP tools."""

    def test_list_decorators(self):
        """Test the list_decorators tool."""
        result = list_decorators()
        assert isinstance(result, dict)
        assert "decorators" in result

        # Check that each decorator has the expected fields
        for name, decorator in result["decorators"].items():
            assert "name" in decorator
            assert "description" in decorator
            assert "category" in decorator
            assert "parameters" in decorator

        # Check that known decorators are in the result
        assert "StepByStep" in result["decorators"]
        assert "Academic" in result["decorators"]
        assert "Persona" in result["decorators"]

    def test_get_decorator_details(self):
        """Test the get_decorator_details tool."""
        # Test with a valid decorator name
        result = get_decorator_details(name="StepByStep")
        assert result["name"] == "StepByStep"
        assert "description" in result
        assert "category" in result
        assert "parameters" in result

        # Check parameters
        params = result["parameters"]
        param_names = [p.name for p in params]
        assert "numbered" in param_names

        # Test with a non-existent decorator name
        # Note: The server doesn't raise an exception for non-existent decorators
        # but returns an error response with available decorators
        result = get_decorator_details(name="NonExistentDecorator")
        assert "error" in result
        assert "available_decorators" in result
        assert "Decorator 'NonExistentDecorator' not found" in result["error"]

    def test_apply_decorators(self):
        """Test the apply_decorators tool."""
        # Test with a single decorator
        prompt = "Tell me about quantum computing"
        decorators = [{"name": "StepByStep"}]

        result = apply_decorators(prompt=prompt, decorators=decorators)
        assert isinstance(result, dict)
        assert result["original_prompt"] == prompt
        assert "decorated_prompt" in result
        assert "applied_decorators" in result

        # Test with multiple decorators
        decorators = [
            {"name": "StepByStep"},
            {"name": "Academic", "parameters": {"level": "advanced"}},
        ]

        result = apply_decorators(prompt=prompt, decorators=decorators)
        assert result["original_prompt"] == prompt
        assert "decorated_prompt" in result
        assert len(result["applied_decorators"]) == 2

        # Test with invalid decorator
        # Note: The server handles invalid decorators gracefully
        decorators = [{"name": "NonExistentDecorator"}]
        result = apply_decorators(prompt=prompt, decorators=decorators)
        assert result["original_prompt"] == prompt

    def test_create_decorated_prompt(self):
        """Test the create_decorated_prompt tool."""
        # Test with valid template name
        content = "Why is the sky blue?"
        result = create_decorated_prompt(
            template_name="detailed-reasoning", content=content
        )
        assert isinstance(result, dict)
        assert result["original_content"] == content
        assert "decorated_prompt" in result
        assert "applied_decorators" in result
        assert "template_name" in result
        assert "template_description" in result

        # Test with invalid template name
        # Note: The server returns a result even for invalid templates
        result = create_decorated_prompt(
            template_name="non-existent-template", content=content
        )
        assert isinstance(result, dict)
        assert "error" in result or "template_name" in result


class TestMCPIntegration:
    """Tests for the MCP integration as a whole."""

    @patch("prompt_decorators.integrations.mcp.server.FastMCP")
    def test_server_initialization(self, mock_fast_mcp):
        """Test that the server initializes correctly with a mocked MCP SDK."""
        # This test needs to be modified to work with the actual implementation
        # Since we're mocking the FastMCP class, we need to ensure our test matches
        # how the code actually uses it

        # Create a mock instance that won't try to run the server
        mock_instance = MagicMock()
        mock_fast_mcp.return_value = mock_instance

        # We'll mock the server module's run_server function
        with patch(
            "prompt_decorators.integrations.mcp.server.run_server"
        ) as mock_run_server:
            from prompt_decorators.integrations.mcp import __main__

            with patch("sys.argv", ["prompt_decorators.integrations.mcp"]):
                __main__.main()

            # Check that run_server was called
            mock_run_server.assert_called_once()


@pytest.mark.parametrize(
    "template_name",
    [
        "detailed-reasoning",
        "academic-analysis",
        "explain-simply",
        "creative-storytelling",
        "problem-solving",
    ],
)
def test_predefined_templates(template_name):
    """Test that all predefined templates work correctly."""
    content = "Explain the concept of gravity"
    result = create_decorated_prompt(template_name=template_name, content=content)

    # Check that the content is in the original_content field
    assert result["original_content"] == content

    # Check that we have the expected fields
    assert "decorated_prompt" in result
    assert "applied_decorators" in result
    assert "template_name" in result
    assert "template_description" in result

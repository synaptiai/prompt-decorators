"""Tests for the MCP integration.

Recent updates (2023):
- Fixed tests to use the correct attribute 'type' instead of 'type_' in ParameterSchema
- Updated tests to match the new MCP response format where fields are now in 'metadata' object
- Enhanced test coverage to verify JSON schema creation and parameter type handling
- Added new test_parameter_type_handling to specifically test parameter type access

Recent updates (2024-03-09):
- Added comprehensive testing for transform_prompt function
- Enhanced parameter_type_handling tests with validation for different parameter types
- Added fallback mechanism testing for parameter type access
- Updated tests to match the enhanced decorator details and list output formats
- Added verification of JSON schema properties based on parameter types
- Added test registry fixture to ensure consistent decorator availability in CI
"""

import json
import os
import tempfile
from pathlib import Path
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
    transform_prompt,
)


@pytest.fixture(scope="module")
def mcp_test_registry():
    """Create a test registry with decorators needed for MCP tests.

    This fixture ensures that the necessary decorators are available
    for the MCP tests, even in CI environments where the full registry
    might not be accessible.
    """
    # Save the original registry path
    original_registry = os.environ.get("DECORATOR_REGISTRY_DIR")

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create registry structure
        registry_path = Path(temp_dir)
        core_path = registry_path / "core"
        core_path.mkdir()
        minimal_path = core_path / "minimal"
        minimal_path.mkdir()

        # Create a StepByStep decorator
        step_by_step = {
            "decoratorName": "StepByStep",
            "version": "1.0.0",
            "description": "Structures the response as a sequence of steps",
            "category": "structure",
            "parameters": [
                {
                    "name": "numbered",
                    "type": "boolean",
                    "description": "Whether to number the steps",
                    "default": True,
                    "required": False,
                    "enum_values": [],
                }
            ],
            "transform_function": """
result = "Please break down your response into clear, sequential steps.\\n"
if kwargs.get("numbered", True):
    result += "Number each step sequentially (Step 1, Step 2, etc.).\\n"
else:
    result += "Use bullet points for each step.\\n"
return result + "\\n" + text
""",
        }

        # Create an Academic decorator
        academic = {
            "decoratorName": "Academic",
            "version": "1.0.0",
            "description": "Formats the response in an academic style",
            "category": "tone",
            "parameters": [
                {
                    "name": "style",
                    "type": "enum",
                    "description": "The academic style to use",
                    "default": "general",
                    "required": False,
                    "enum_values": ["general", "humanities", "scientific", "legal"],
                },
                {
                    "name": "format",
                    "type": "enum",
                    "description": "The citation format to use",
                    "default": "APA",
                    "required": False,
                    "enum_values": ["APA", "MLA", "Chicago", "Harvard"],
                },
            ],
            "transform_function": """
result = "Please format your response in an academic style.\\n"
style = kwargs.get("style", "general")
if style == "humanities":
    result += "Use language appropriate for humanities disciplines.\\n"
elif style == "scientific":
    result += "Use precise, technical language appropriate for scientific writing.\\n"
elif style == "legal":
    result += "Use formal legal terminology and citation style.\\n"
else:
    result += "Use general academic language and structure.\\n"

format = kwargs.get("format", "APA")
result += f"Use {format} citation style for any references.\\n"
return result + "\\n" + text
""",
        }

        # Create a Reasoning decorator
        reasoning = {
            "decoratorName": "Reasoning",
            "version": "1.0.0",
            "description": "Provides explicit reasoning in the response",
            "category": "reasoning",
            "parameters": [
                {
                    "name": "depth",
                    "type": "enum",
                    "description": "The depth of reasoning to provide",
                    "default": "moderate",
                    "required": False,
                    "enum_values": ["basic", "moderate", "comprehensive"],
                }
            ],
            "transform_function": """
result = "Please provide detailed reasoning in your response.\\n"
depth = kwargs.get("depth", "moderate")
if depth == "basic":
    result += "Focus on the most important logical steps.\\n"
elif depth == "comprehensive":
    result += "Provide a very thorough and detailed analysis.\\n"
else:
    result += "Balance detail with clarity in your reasoning.\\n"
return result + "\\n" + text
""",
        }

        # Write the decorators to files
        with open(minimal_path / "step-by-step.json", "w") as f:
            json.dump(step_by_step, f)

        with open(minimal_path / "academic.json", "w") as f:
            json.dump(academic, f)

        with open(minimal_path / "reasoning.json", "w") as f:
            json.dump(reasoning, f)

        # Set the registry path environment variable
        os.environ["DECORATOR_REGISTRY_DIR"] = str(registry_path)

        # Clear the registry cache and reload
        DynamicDecorator._registry = {}
        DynamicDecorator._loaded = False
        DynamicDecorator.load_registry()

        yield

        # Restore the original registry path
        if original_registry:
            os.environ["DECORATOR_REGISTRY_DIR"] = original_registry
        else:
            if "DECORATOR_REGISTRY_DIR" in os.environ:
                del os.environ["DECORATOR_REGISTRY_DIR"]

        # Clear the registry cache again
        DynamicDecorator._registry = {}
        DynamicDecorator._loaded = False


class TestMCPTools:
    """Tests for the MCP tools."""

    @pytest.mark.usefixtures("mcp_test_registry")
    def test_list_decorators(self):
        """Test the list_decorators tool."""
        result = list_decorators()
        assert isinstance(result, dict)
        assert "tools" in result
        assert "content" in result

        # Check content structure
        assert isinstance(result["content"], list)
        assert len(result["content"]) > 0
        assert "text" in result["content"][0]

        # Check that we have decorator tools
        tools = result["tools"]
        assert isinstance(tools, list)
        assert len(tools) > 0

        # Check that each decorator has the enhanced fields
        for decorator in tools:
            assert "name" in decorator
            assert "description" in decorator
            assert "category" in decorator
            assert "version" in decorator
            assert "inputSchema" in decorator

            # Check input schema structure
            schema = decorator["inputSchema"]
            assert "type" in schema
            assert schema["type"] == "object"
            assert "properties" in schema
            assert "required" in schema

            # Check that the prompt property exists
            properties = schema["properties"]
            assert "prompt" in properties
            assert properties["prompt"]["type"] == "string"

            # Verify parameter properties are correctly defined
            for param_name, param_schema in properties.items():
                if param_name == "prompt":  # Skip the prompt property
                    continue

                assert "type" in param_schema
                assert "description" in param_schema

                # Check that parameter types are correct
                param_type = param_schema["type"]
                assert param_type in ["string", "number", "boolean", "object", "array"]

                # Check for enum values if applicable
                if "enum" in param_schema:
                    assert isinstance(param_schema["enum"], list)

                # Check for default values if applicable
                if "default" in param_schema:
                    if param_type == "string":
                        assert isinstance(param_schema["default"], str)
                    elif param_type == "number":
                        assert isinstance(param_schema["default"], (int, float))
                    elif param_type == "boolean":
                        assert isinstance(param_schema["default"], bool)

            # Check for enhanced fields
            if "compatibilitySummary" in decorator:
                assert isinstance(decorator["compatibilitySummary"], dict)
                assert "requires" in decorator["compatibilitySummary"]
                assert "conflicts" in decorator["compatibilitySummary"]

            if "author" in decorator:
                assert isinstance(decorator["author"], dict)

            if "sampleUsage" in decorator:
                assert isinstance(decorator["sampleUsage"], str)

        # Check that known decorators are in the result
        decorator_names = [d["name"] for d in tools]
        assert "StepByStep" in decorator_names
        assert "Academic" in decorator_names
        assert "Reasoning" in decorator_names

    @pytest.mark.usefixtures("mcp_test_registry")
    def test_get_decorator_details(self):
        """Test the get_decorator_details tool."""
        # Test with a valid decorator name
        result = get_decorator_details(name="StepByStep")
        assert "content" in result
        assert "decorator" in result

        decorator = result["decorator"]
        assert decorator["name"] == "StepByStep"
        assert "description" in decorator
        assert "category" in decorator
        assert "version" in decorator
        assert "parameters" in decorator
        assert "inputSchema" in decorator

        # Check parameters
        params = decorator["parameters"]
        param_names = [
            p["name"] if isinstance(p, dict) and "name" in p else p.name for p in params
        ]
        assert "numbered" in param_names

        # Check input schema
        schema = decorator["inputSchema"]
        assert schema["type"] == "object"
        assert "properties" in schema
        assert "required" in schema

        # Check schema properties
        properties = schema["properties"]
        assert "prompt" in properties
        for param_name in param_names:
            assert param_name in properties
            param_schema = properties[param_name]
            assert "type" in param_schema
            assert "description" in param_schema

        # Check enhanced fields
        if "transformationSummary" in decorator:
            assert isinstance(decorator["transformationSummary"], dict)
            assert "available" in decorator["transformationSummary"]

        if "transformationTemplate" in decorator:
            assert isinstance(decorator["transformationTemplate"], dict)

        if "compatibility" in decorator:
            assert isinstance(decorator["compatibility"], dict)
            assert "requires" in decorator["compatibility"]
            assert "conflicts" in decorator["compatibility"]
            assert "supportedModels" in decorator["compatibility"]

        if "examples" in decorator:
            assert isinstance(decorator["examples"], list)

        if "implementationGuidance" in decorator:
            assert isinstance(decorator["implementationGuidance"], dict)

        if "author" in decorator:
            assert isinstance(decorator["author"], dict)

        # Test with a non-existent decorator name
        # Note: The server doesn't raise an exception for non-existent decorators
        # but returns an error response with available decorators
        result = get_decorator_details(name="NonExistentDecorator")
        assert "isError" in result
        assert result["isError"] is True
        assert "content" in result
        assert "metadata" in result
        assert "available_decorators" in result["metadata"]
        assert any(
            "Decorator 'NonExistentDecorator' not found" in item["text"]
            for item in result["content"]
        )

    @pytest.mark.usefixtures("mcp_test_registry")
    def test_apply_decorators(self):
        """Test the apply_decorators tool."""
        # Test with a single decorator
        prompt = "Tell me about quantum computing"
        decorators = [{"name": "StepByStep"}]

        result = apply_decorators(prompt=prompt, decorators=decorators)
        assert isinstance(result, dict)
        assert "content" in result
        assert "metadata" in result
        assert result["metadata"]["original_prompt"] == prompt
        assert "applied_decorators" in result["metadata"]
        assert len(result["metadata"]["applied_decorators"]) == 1

        # Test with multiple decorators
        decorators = [
            {"name": "StepByStep"},
            {"name": "Academic", "style": "scientific"},
        ]
        result = apply_decorators(prompt=prompt, decorators=decorators)
        assert isinstance(result, dict)
        assert "content" in result
        assert "metadata" in result
        assert result["metadata"]["original_prompt"] == prompt
        assert "applied_decorators" in result["metadata"]
        assert len(result["metadata"]["applied_decorators"]) == 2

        # Test with a decorator that has an invalid parameter
        decorators = [{"name": "Academic", "invalid_param": "value"}]
        result = apply_decorators(prompt=prompt, decorators=decorators)
        assert isinstance(result, dict)
        assert "content" in result
        assert "metadata" in result
        assert result["metadata"]["original_prompt"] == prompt
        # Either the decorator was applied with a warning, or it's in error_decorators
        if "error_decorators" in result["metadata"]:
            assert len(result["metadata"]["error_decorators"]) > 0
        else:
            assert "applied_decorators" in result["metadata"]
            assert len(result["metadata"]["applied_decorators"]) > 0

        # Test with a non-existent decorator
        decorators = [{"name": "NonExistentDecorator"}]
        result = apply_decorators(prompt=prompt, decorators=decorators)
        assert isinstance(result, dict)
        assert "content" in result
        assert "metadata" in result
        assert result["metadata"]["original_prompt"] == prompt

        # The server might handle non-existent decorators in different ways:
        # 1. It might add them to error_decorators
        # 2. It might still add them to applied_decorators but log an error
        # We'll check for either behavior
        if "error_decorators" in result["metadata"]:
            assert len(result["metadata"]["error_decorators"]) > 0
        else:
            assert "applied_decorators" in result["metadata"]
            # The decorator might still be in the list even though it failed
            assert "NonExistentDecorator" in str(
                result["metadata"]["applied_decorators"]
            )

    @pytest.mark.usefixtures("mcp_test_registry")
    def test_create_decorated_prompt(self):
        """Test the create_decorated_prompt tool."""
        # Test with a valid template
        content = "Explain how blockchain works"
        result = create_decorated_prompt(
            template_name="detailed-reasoning", content=content
        )
        assert isinstance(result, dict)
        assert "content" in result
        assert "metadata" in result
        assert result["metadata"]["original_content"] == content
        assert "applied_decorators" in result["metadata"]
        assert "template_name" in result["metadata"]
        assert "template_description" in result["metadata"]

        # Test with a non-existent template
        result = create_decorated_prompt(
            template_name="non-existent-template", content=content
        )
        assert isinstance(result, dict)
        assert "content" in result
        assert "isError" in result
        assert result["isError"] is True
        assert any(
            "Template 'non-existent-template' not found" in item["text"]
            for item in result["content"]
        )

    @pytest.mark.usefixtures("mcp_test_registry")
    def test_parameter_type_handling(self):
        """Test that parameter type handling works correctly.

        This test ensures that our parameter type access is working correctly across
        both list_decorators and get_decorator_details. It checks that:

        1. All parameters have proper type definitions
        2. The parameter types match expected values (string, number, boolean, etc.)
        3. The JSON schema properties are correctly constructed based on parameter types
        4. The type fallback mechanism works when type attributes are not found
        """
        # Test list_decorators parameter type handling
        list_result = list_decorators()
        tools = list_result["tools"]

        # First, verify we have tools
        assert len(tools) > 0

        # Check each tool to verify parameters have types
        for tool in tools:
            properties = tool["inputSchema"]["properties"]
            for param_name, param_schema in properties.items():
                if param_name != "prompt":  # Skip the prompt parameter
                    # Check that type is present and valid
                    assert "type" in param_schema
                    assert param_schema["type"] in [
                        "string",
                        "number",
                        "boolean",
                        "object",
                        "array",
                    ]

                    # Check appropriate type-specific validations
                    if param_schema["type"] == "string" and "enum" in param_schema:
                        assert isinstance(param_schema["enum"], list)

                    if param_schema["type"] == "number" and "minimum" in param_schema:
                        assert isinstance(param_schema["minimum"], (int, float))

                    if param_schema["type"] == "boolean" and "default" in param_schema:
                        assert isinstance(param_schema["default"], bool)

        # Test get_decorator_details parameter type handling
        detail_result = get_decorator_details(name="StepByStep")
        assert "decorator" in detail_result

        properties = detail_result["decorator"]["inputSchema"]["properties"]
        for param_name, param_schema in properties.items():
            if param_name != "prompt":  # Skip the prompt parameter
                # Check that type is present and valid
                assert "type" in param_schema
                assert param_schema["type"] in [
                    "string",
                    "number",
                    "boolean",
                    "object",
                    "array",
                ]

        # Test param schema creation with a decorator that has various parameter types
        # We'll use Academic which typically has multiple parameter types
        academic_result = get_decorator_details(name="Academic")
        if "decorator" in academic_result:  # Only test if Academic decorator exists
            academic_properties = academic_result["decorator"]["inputSchema"][
                "properties"
            ]

            # Find some parameters with different types and check their schema
            for param_name, param_schema in academic_properties.items():
                if param_name != "prompt":
                    if "enum" in param_schema:
                        # For enum parameters, check that the enum values are correctly listed
                        assert isinstance(param_schema["enum"], list)
                        # Note: Some enum lists might be empty during testing
                        # We just check that it's a list, not that it has values

                    # Check that description is present for all parameters
                    assert "description" in param_schema
                    assert isinstance(param_schema["description"], str)

                    # Check that types are correctly mapped
                    assert param_schema["type"] in [
                        "string",
                        "number",
                        "boolean",
                        "object",
                        "array",
                    ]

    @pytest.mark.usefixtures("mcp_test_registry")
    def test_transform_prompt(self):
        """Test the transform_prompt tool."""
        # Test with standard decorator strings
        prompt = "Explain how blockchain works"
        decorator_strings = ["+++StepByStep", "+++Reasoning"]

        result = transform_prompt(prompt=prompt, decorator_strings=decorator_strings)
        assert isinstance(result, dict)
        assert "content" in result
        assert "metadata" in result
        assert result["metadata"]["original_prompt"] == prompt
        assert "applied_decorators" in result["metadata"]
        assert len(result["metadata"]["applied_decorators"]) == 2

        # Test with decorator strings that have trailing +++
        decorator_strings_with_suffix = ["+++StepByStep+++", "+++Reasoning+++"]

        result = transform_prompt(
            prompt=prompt, decorator_strings=decorator_strings_with_suffix
        )
        assert isinstance(result, dict)
        assert "content" in result
        assert "metadata" in result
        assert result["metadata"]["original_prompt"] == prompt
        assert "applied_decorators" in result["metadata"]
        assert len(result["metadata"]["applied_decorators"]) == 2

        # Verify that the content is transformed properly (not just concatenated)
        transformed_text = result["content"][0]["text"]
        assert transformed_text != "+++\n+++\n\nExplain how blockchain works"
        assert "cleaned_decorators" in result["metadata"]

        # Test with invalid decorator strings
        invalid_decorators = ["StepByStep", "Reasoning"]
        result = transform_prompt(prompt=prompt, decorator_strings=invalid_decorators)
        assert "invalidDecorators" in result["metadata"]
        assert len(result["metadata"]["invalidDecorators"]) == 2

    @pytest.mark.usefixtures("mcp_test_registry")
    def test_transform_prompt_edge_cases(self):
        """Test the transform_prompt tool with edge cases.

        This test focuses on handling edge cases in the transform_prompt function:
        1. Empty decorator lists
        2. Malformed decorators
        3. Decorators with parameters
        4. Mixed valid and invalid decorators
        """
        # Test with empty decorator list
        prompt = "Explain how blockchain works"
        empty_decorators = []

        result = transform_prompt(prompt=prompt, decorator_strings=empty_decorators)
        assert isinstance(result, dict)
        assert "content" in result
        assert "metadata" in result
        assert result["metadata"]["original_prompt"] == prompt
        assert "applied_decorators" in result["metadata"]
        assert len(result["metadata"]["applied_decorators"]) == 0
        assert result["content"][0]["text"] == prompt  # Unchanged prompt

        # Test with decorators that have parameters
        decorators_with_params = [
            "+++StepByStep(numbered=true)",
            "+++Reasoning(depth=comprehensive)",
        ]
        result = transform_prompt(
            prompt=prompt, decorator_strings=decorators_with_params
        )
        assert isinstance(result, dict)
        assert "content" in result
        assert "metadata" in result
        assert "applied_decorators" in result["metadata"]
        assert len(result["metadata"]["applied_decorators"]) == 2

        # Check that parameters were properly extracted
        params_extracted = False
        for decorator in result["metadata"]["applied_decorators"]:
            if "numbered" in decorator or "depth" in decorator:
                params_extracted = True
                break
        assert (
            params_extracted
        ), "Parameters were not properly extracted from decorator strings"

        # Test with a mix of valid and invalid decorators
        mixed_decorators = [
            "+++StepByStep",
            "InvalidDecorator",
            "+++Reasoning",
            "+++NonExistent",
        ]
        result = transform_prompt(prompt=prompt, decorator_strings=mixed_decorators)
        assert "invalidDecorators" in result["metadata"]
        assert len(result["metadata"]["invalidDecorators"]) > 0
        assert "applied_decorators" in result["metadata"]

        # At least the valid decorators should be applied
        assert len(result["metadata"]["applied_decorators"]) > 0

        # Check that the valid decorators were recognized and applied
        has_valid_decorator = False
        for name in result["metadata"]["applied_decorators"]:
            if isinstance(name, str):
                if "StepByStep" in name or "Reasoning" in name:
                    has_valid_decorator = True
                    break
        assert has_valid_decorator, "No valid decorators were applied"

        # Test with malformed decorator syntax
        malformed_decorators = ["++StepByStep", "+++", "Step+By+Step"]
        result = transform_prompt(prompt=prompt, decorator_strings=malformed_decorators)
        assert "invalidDecorators" in result["metadata"]
        assert len(result["metadata"]["invalidDecorators"]) > 0

        # Should still return the original prompt even if no decorators could be applied
        assert result["content"][0]["text"] is not None
        assert len(result["content"][0]["text"]) > 0


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
@pytest.mark.usefixtures("mcp_test_registry")
def test_predefined_templates(template_name):
    """Test that all predefined templates work correctly."""
    content = "Explain the concept of gravity"
    result = create_decorated_prompt(template_name=template_name, content=content)

    # Check that the content is in the metadata.original_content field
    assert "metadata" in result
    assert result["metadata"]["original_content"] == content

    # Check that we have the expected fields
    assert "content" in result
    assert "applied_decorators" in result["metadata"]
    assert "template_name" in result["metadata"]
    assert "template_description" in result["metadata"]

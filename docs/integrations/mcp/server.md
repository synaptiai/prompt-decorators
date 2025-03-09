# MCP Server

The Prompt Decorators MCP server exposes prompt decorators as MCP tools, allowing any MCP-compatible client to access and use them. This document provides detailed information about the server implementation and usage.

## Implementation Overview

The MCP server is implemented using the official [MCP SDK](https://github.com/modelcontextprotocol/python-sdk), specifically the `FastMCP` class, which provides a high-level API for creating MCP servers.

The server exposes four tools:

1. `list_decorators`: Lists all available prompt decorators.
2. `get_decorator_details`: Retrieves detailed information about a specific decorator.
3. `apply_decorators`: Applies decorators to a prompt using the +++ syntax.
4. `create_decorated_prompt`: Creates a decorated prompt using a predefined template.

## Source Code

The main server implementation is in the `prompt_decorators/integrations/mcp/server.py` file. It uses the dynamic decorator module to load and apply decorators.

```python
from mcp.server.fastmcp import FastMCP
from prompt_decorators.dynamic_decorators_module import (
    get_available_decorators,
    apply_dynamic_decorators,
    load_decorator_definitions,
)

# Create the MCP server
mcp = FastMCP("Prompt Decorators")

@mcp.tool()
def list_decorators() -> Dict[str, Any]:
    """Lists all available prompt decorators."""
    # Implementation...

@mcp.tool()
def get_decorator_details(name: str) -> Dict[str, Any]:
    """Get detailed information about a specific decorator."""
    # Implementation...

@mcp.tool()
def apply_decorators(prompt: str, decorators: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Apply decorators to a prompt using the +++ syntax."""
    # Implementation...

@mcp.tool()
def create_decorated_prompt(template_name: str, content: str, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a decorated prompt using a predefined template."""
    # Implementation...

def run_server(host: str = "0.0.0.0", port: int = 5000) -> None:
    """Run the MCP server."""
    # Implementation...
```

## Running the Server

You can run the MCP server using the following command:

```bash
python -m prompt_decorators.integrations.mcp [--host HOST] [--port PORT] [--verbose]
```

Options:
- `--verbose`: Enable verbose logging for debugging
- `--host`: Specify the host to bind to (default: "0.0.0.0")
- `--port`: Specify the port to listen on (default: 5000)

## Tool Details

### list_decorators

Lists all available prompt decorators.

**Parameters**: None

**Returns**: A dictionary containing information about all available decorators, including their names, descriptions, categories, and parameters.

**Example Response**:
```json
{
  "decorators": {
    "Academic": {
      "name": "Academic",
      "description": "Apply academic writing style and tone",
      "category": "Style",
      "parameters": [{"name": "level", "description": "Academic level", "type": "string", "required": false}]
    },
    "Reasoning": {
      "name": "Reasoning",
      "description": "Enhance reasoning capabilities",
      "category": "Critical Thinking",
      "parameters": [{"name": "depth", "description": "Reasoning depth", "type": "string", "required": false}]
    }
    // ... more decorators
  }
}
```

### get_decorator_details

Retrieves detailed information about a specific decorator.

**Parameters**:
- `name` (string, required): The name of the decorator to get details for.

**Returns**: A dictionary containing detailed information about the decorator, including its name, description, category, parameters, and version.

**Example Request**:
```json
{
  "name": "StepByStep"
}
```

**Example Response**:
```json
{
  "name": "StepByStep",
  "description": "Break down the response into step-by-step instructions",
  "category": "Structure",
  "parameters": [
    {"name": "numbered", "description": "Use numbered steps", "type": "boolean", "required": false}
  ],
  "version": "1.0.0"
}
```

### apply_decorators

Applies decorators to a prompt using the +++ syntax.

**Parameters**:
- `prompt` (string, required): The prompt text to decorate.
- `decorators` (array, required): List of decorators to apply, each with name and parameters.

**Returns**: A dictionary containing the original prompt, the decorated prompt, and the list of applied decorators.

**Example Request**:
```json
{
  "prompt": "Explain quantum computing",
  "decorators": [
    {"name": "StepByStep"},
    {"name": "Academic", "parameters": {"level": "advanced"}}
  ]
}
```

**Example Response**:
```json
{
  "original_prompt": "Explain quantum computing",
  "decorated_prompt": "I'll provide a step-by-step academic explanation of quantum computing at an advanced level...",
  "applied_decorators": ["StepByStep", "Academic"]
}
```

### create_decorated_prompt

Creates a decorated prompt using a predefined template.

**Parameters**:
- `template_name` (string, required): The name of the template to use.
- `content` (string, required): The content to include in the prompt.
- `parameters` (object, optional): Optional parameters for customizing the template.

**Returns**: A dictionary containing the template name, description, original content, decorated prompt, and applied decorators.

**Example Request**:
```json
{
  "template_name": "detailed-reasoning",
  "content": "Why is the sky blue?",
  "parameters": {
    "depth": "comprehensive"
  }
}
```

**Example Response**:
```json
{
  "template_name": "detailed-reasoning",
  "template_description": "Enhanced critical thinking template with structured reasoning",
  "original_content": "Why is the sky blue?",
  "decorated_prompt": "I'll analyze why the sky appears blue, using detailed reasoning and a comprehensive approach...",
  "applied_decorators": [
    {"name": "SystemMessage", "parameters": {"message": "Analyze this problem step-by-step with detailed reasoning."}},
    {"name": "Reasoning", "parameters": {"depth": "comprehensive"}},
    {"name": "Structured", "parameters": {"format": "markdown"}}
  ]
}
```

## Predefined Templates

The server includes the following predefined templates:

### detailed-reasoning

Enhanced critical thinking template with structured reasoning.

**Decorators**:
- `SystemMessage`: Sets the system message to guide detailed reasoning.
- `Reasoning`: Applies deep reasoning capabilities.
- `Structured`: Formats the response in Markdown.

### academic-analysis

Academic style analysis with citations and formal tone.

**Decorators**:
- `Academic`: Sets advanced academic level.
- `Citation`: Uses APA citation style.
- `Formal`: Applies formal tone.

### explain-simply

Simplify complex topics for broader understanding.

**Decorators**:
- `SystemMessage`: Sets the system message for simple explanations.
- `Simplify`: Sets beginner-level explanations.
- `Examples`: Includes examples to illustrate concepts.

### creative-storytelling

Creative writing with storytelling elements.

**Decorators**:
- `Creative`: Uses narrative style for creative content.
- `Engaging`: Makes the content engaging.
- `Vivid`: Adds high-level of vividness to descriptions.

### problem-solving

Structured approach to solving problems.

**Decorators**:
- `SystemMessage`: Sets the system message for problem-solving.
- `ProblemSolver`: Applies problem-solving methodology.
- `StepByStep`: Breaks down the solution into steps.

## Error Handling

The server includes robust error handling for various scenarios:

- Invalid decorator names: Returns an error with available decorators.
- Invalid template names: Returns an error with available templates.
- Server initialization issues: Logs detailed error information.
- Runtime errors: Logs exceptions and returns error messages.

## Implementation Details

### Server Lifecycle

The server lifecycle is managed by the `run_server` function, which:

1. Configures logging based on the verbose flag.
2. Loads all available decorators from the dynamic decorators module.
3. Starts the MCP server using the `mcp.run()` method.
4. Handles shutdown requests and exceptions.

### Tool Implementation

Each tool is implemented as a Python function decorated with `@mcp.tool()`. The function signature defines the parameters and return type of the tool.

### Dynamic Decorator Loading

The server uses the `get_available_decorators()` function from the dynamic decorators module to load all available decorators at runtime. This ensures that all decorators registered with the system are available to MCP clients.

### Template Management

Templates are defined as dictionaries with a description and a list of decorators to apply. Each decorator includes its name and parameters.

## Extending the Server

You can extend the server by adding new tools or templates:

### Adding a New Tool

```python
@mcp.tool()
def my_custom_tool(param1: str, param2: int) -> Dict[str, Any]:
    """
    Custom tool description.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        A dictionary with the result.
    """
    # Implementation...
    return {"result": "..."}
```

### Adding a New Template

```python
templates["my-template"] = {
    "description": "My custom template description",
    "decorators": [
        {"name": "Decorator1", "parameters": {"param1": "value1"}},
        {"name": "Decorator2", "parameters": {"param2": "value2"}}
    ]
}
```

## Next Steps

To learn more about integrating the MCP server with Claude Desktop, see [Claude Desktop Integration](./claude_desktop.md).

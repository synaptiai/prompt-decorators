# MCP Integration Examples for Prompt Decorators

This directory contains examples demonstrating how to use the Prompt Decorators framework with the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol).

## Overview

The Model Context Protocol (MCP) provides a standardized way for LLM clients and servers to communicate. The Prompt Decorators MCP integration allows you to:

- Run a dedicated MCP server with prompt decorator capabilities
- Apply decorators to prompts using a client-server architecture
- Define and use predefined decorator templates
- Integrate decorator functionality into existing MCP applications

## Installation Requirements

To run these examples, you'll need to install the MCP package:

```bash
pip install "mcp[cli]"
```

Alternatively, you can install prompt-decorators with the MCP extras:

```bash
pip install "prompt-decorators[mcp]"
```

## Examples

### 1. MCP Server Integration Example

[mcp_integration_example.py](./mcp_integration_example.py) demonstrates:
- Creating an MCP server with Prompt Decorators integration
- Starting the server and connecting a client
- Using the various tools provided by the integration
- Using predefined templates

```bash
# Run the example
python prompt_decorators/integrations/mcp/examples/mcp_integration_example.py
```

### 2. MCP Client Example

[mcp_client_example.py](./mcp_client_example.py) shows:
- Connecting to a Prompt Decorators MCP server
- Listing available decorators
- Getting details about specific decorators
- Applying decorators to prompts
- Using predefined templates

```bash
# Run the example
python prompt_decorators/integrations/mcp/examples/mcp_client_example.py
```

### 3. Claude Desktop Integration Example

[claude_desktop_example.py](./claude_desktop_example.py) simulates:
- How Claude Desktop might integrate with the Prompt Decorators MCP server
- Applying decorators to prompts before sending to the Claude API

```bash
# Run the example
python prompt_decorators/integrations/mcp/examples/claude_desktop_example.py
```

## Running the MCP Server Directly

You can run the MCP server directly without a client:

```bash
python -m prompt_decorators.integrations.mcp
```

## Using the MCP Integration in Your Projects

### 1. Running as a Standalone Server

```python
# Run the MCP server as a standalone application
from prompt_decorators.integrations.mcp import main

main()
```

### 2. Integrating with Your Own MCP Server

```python
from prompt_decorators.integrations.mcp import create_mcp_server

# Create an MCP server with prompt decorator integration
mcp_server = create_mcp_server("my-decorator-server")

# Run the server
mcp_server.run()
```

### 3. Connecting to the Server from a Client

```python
from mcp.client import MCPClient

# Connect to the MCP server
client = MCPClient("http://localhost:8000")

# Apply decorators using the +++ syntax
result = await client.tools.apply_decorators(
    prompt="+++Reasoning(depth='comprehensive') +++StepByStep() Explain quantum computing."
)

# Use a predefined template
template_result = await client.tools.create_decorated_prompt(
    template_name="detailed-reasoning",
    prompt="Explain how quantum computing works."
)
```

## Available Tools

The MCP integration provides the following tools:

### `apply_decorators`

Applies decorators to a prompt using the `+++` syntax.

```python
result = await client.tools.apply_decorators(
    prompt="+++Reasoning(depth='comprehensive')\n+++StepByStep()\nExplain quantum computing."
)
```

### `list_decorators`

Lists all available decorators in the registry.

```python
decorators = await client.tools.list_decorators()
```

### `get_decorator_details`

Gets detailed information about a specific decorator.

```python
details = await client.tools.get_decorator_details(
    decorator_name="Reasoning"
)
```

### `create_decorated_prompt`

Creates a decorated prompt using a predefined template.

```python
result = await client.tools.create_decorated_prompt(
    template_name="detailed-reasoning",
    prompt="Explain how quantum computing works."
)
```

## Predefined Templates

The MCP integration includes several predefined templates:

| Template Name | Description | Decorators |
|---------------|-------------|------------|
| `detailed-reasoning` | For comprehensive reasoning and analysis | `Reasoning(depth="comprehensive")`, `StepByStep(numbered=True)` |
| `academic-analysis` | For scholarly analysis with citations | `Reasoning(depth="comprehensive")`, `CiteSources(style="APA")`, `OutputFormat(format="markdown")` |
| `explain-simply` | For simple explanations of complex topics | `ELI5()`, `StepByStep(numbered=True)` |
| `creative-storytelling` | For creative narrative content | `Creative(level="high")`, `OutputFormat(format="markdown")` |
| `problem-solving` | For structured problem-solving | `StepByStep(numbered=True)`, `TreeOfThought(branches=3)`, `Limitations(position="end")` |

## Decorator Syntax

The MCP integration supports the `+++` syntax for applying decorators to prompts:

```
+++StepByStep(numbered='true')
+++Audience(level='beginner')
Explain how neural networks work
```

## Troubleshooting

If you encounter issues:

1. **Connection errors**: Ensure the server is running before connecting with the client
2. **Import errors**: Make sure you've installed the MCP package (`pip install "mcp[cli]"`)
3. **Tool not found errors**: Check that the tool name matches exactly what's provided by the server
4. **Decorator errors**: Verify decorator names and parameter values

## Additional Resources

- [MCP Integration Documentation](../../../docs/integrations/mcp.md)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)
- [Prompt Decorators Specification](../../../docs/prompt-decorators-specification-v1.0.md)

# Model Context Protocol (MCP) Integration

Prompt Decorators integrates with the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/python-sdk), allowing you to easily expose prompt decorators as MCP tools that can be used by any MCP-compatible client, including Claude Desktop.

## Overview

The Model Context Protocol (MCP) is a standardized protocol for communication between LLM clients and servers. Our integration allows you to expose your prompt decorators as MCP tools, which can then be accessed by any MCP client.

The integration is built using the official MCP SDK and follows all the best practices for MCP server implementation.

## Installation

First, install the MCP SDK:

```bash
pip install mcp
```

## Usage

### Running the Server

You can run the MCP server using:

```bash
# General use
python -m prompt_decorators.integrations.mcp [--verbose]

# For Claude Desktop specifically
python -m prompt_decorators.integrations.mcp.claude_desktop [--verbose]
```

### Available Tools

The MCP integration provides the following tools:

1. **list_decorators**: Lists all available prompt decorators.
2. **get_decorator_details**: Retrieves detailed information about a specific decorator.
3. **apply_decorators**: Applies decorators to a prompt using the +++ syntax.
4. **create_decorated_prompt**: Creates a decorated prompt using a predefined template.

### Using the Tools

Here's how you can use these tools from an MCP client:

#### List Decorators

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "callTool",
  "params": {
    "name": "list_decorators",
    "arguments": {}
  }
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
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
}
```

#### Get Decorator Details

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "callTool",
  "params": {
    "name": "get_decorator_details",
    "arguments": {
      "name": "StepByStep"
    }
  }
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "name": "StepByStep",
    "description": "Break down the response into step-by-step instructions",
    "category": "Structure",
    "parameters": [
      {"name": "numbered", "description": "Use numbered steps", "type": "boolean", "required": false}
    ],
    "version": "1.0.0"
  }
}
```

#### Apply Decorators

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "callTool",
  "params": {
    "name": "apply_decorators",
    "arguments": {
      "prompt": "Explain quantum computing",
      "decorators": [
        {"name": "StepByStep"},
        {"name": "Academic", "parameters": {"level": "advanced"}}
      ]
    }
  }
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "original_prompt": "Explain quantum computing",
    "decorated_prompt": "I'll provide a step-by-step academic explanation of quantum computing at an advanced level...",
    "applied_decorators": ["StepByStep", "Academic"]
  }
}
```

#### Create Decorated Prompt

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "callTool",
  "params": {
    "name": "create_decorated_prompt",
    "arguments": {
      "template_name": "detailed-reasoning",
      "content": "Why is the sky blue?"
    }
  }
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "template_name": "detailed-reasoning",
    "template_description": "Enhanced critical thinking template with structured reasoning",
    "original_content": "Why is the sky blue?",
    "decorated_prompt": "I'll analyze why the sky appears blue, using detailed reasoning and a step-by-step approach...",
    "applied_decorators": [
      {"name": "SystemMessage", "parameters": {"message": "Analyze this problem step-by-step with detailed reasoning."}},
      {"name": "Reasoning", "parameters": {"depth": "deep"}},
      {"name": "Structured", "parameters": {"format": "markdown"}}
    ]
  }
}
```

### Predefined Templates

The integration includes the following predefined templates:

- **detailed-reasoning**: Enhanced critical thinking template with structured reasoning.
- **academic-analysis**: Academic style analysis with citations and formal tone.
- **explain-simply**: Simplify complex topics for broader understanding.
- **creative-storytelling**: Creative writing with storytelling elements.
- **problem-solving**: Structured approach to solving problems.

## Implementation Details

The MCP integration is built using the official MCP SDK. The server implementation follows the FastMCP pattern from the SDK, which provides all the necessary functionality for running an MCP server.

The integration registers four tools with the MCP server:

1. `list_decorators`: Lists all available prompt decorators loaded from the dynamic decorators module.
2. `get_decorator_details`: Provides detailed information about a specific decorator, including its parameters and usage.
3. `apply_decorators`: Applies a list of decorators to a given prompt, returning the transformed prompt.
4. `create_decorated_prompt`: Uses a predefined template to create a decorated prompt, with customizable parameters.

## Next Steps

To learn more about the MCP server implementation and how to integrate it with Claude Desktop, see:

- [MCP Server](./mcp/server.md)
- [Claude Desktop Integration](./mcp/claude_desktop.md)

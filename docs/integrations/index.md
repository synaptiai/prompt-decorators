# Integrations

Prompt Decorators can be integrated with various systems and platforms to enhance their capabilities. This section documents the available integrations and how to use them.

## Available Integrations

### Model Context Protocol (MCP)

The [Model Context Protocol (MCP)](./mcp.md) integration allows you to expose prompt decorators as MCP tools, which can be used by MCP-compatible clients like Claude Desktop.

- [MCP Overview](./mcp.md) - General overview of the MCP integration
- [MCP Server](./mcp/server.md) - Documentation for the MCP server implementation
- [Claude Desktop Integration](./mcp/claude_desktop.md) - How to use prompt decorators with Claude Desktop

## Coming Soon

We're working on the following integrations:

- **Langchain**: Integration with the Langchain framework
- **Ollama**: Integration with the Ollama local LLM platform
- **FastAPI**: Expose prompt decorators as a REST API
- **LlamaIndex**: Integration with the LlamaIndex framework

## Why Use Integrations?

Integrations extend the capabilities of Prompt Decorators by making them available in different contexts:

1. **Enhanced Accessibility**: Integrate prompt decorators into your existing workflows and tools.
2. **Standardized Communication**: Use common protocols and interfaces to interact with prompt decorators.
3. **Expanded Functionality**: Combine the power of prompt decorators with other systems.
4. **User-Friendly Interfaces**: Make prompt decorators available through intuitive interfaces.

## Creating Custom Integrations

If you want to create a custom integration for Prompt Decorators, see the [Extension Development](../tutorials/extension_development.md) tutorial for guidance.

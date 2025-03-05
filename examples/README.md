# Prompt Decorators Examples

This directory contains examples and sample code for using the Prompt Decorators framework.

## Contents

- [Domain-Specific Extensions](./domain_extensions/): Examples of domain-specific decorator extensions
  - [Finance Decorators](./domain_extensions/finance_decorators/): Financial domain-specific decorators
- [MCP Integration Examples](#mcp-integration-examples): Examples of using Prompt Decorators with the Model Context Protocol

## MCP Integration Examples

The following examples demonstrate how to use Prompt Decorators with the Model Context Protocol (MCP):

- [MCP Integration Example](./mcp_integration_example.py): Demonstrates how to create an MCP server with Prompt Decorators integration and use the various tools provided.
- [MCP Client Example](./mcp_client_example.py): Shows how to connect to a Prompt Decorators MCP server using the MCP client SDK and use the available tools.
- [Claude Desktop Integration](./claude_desktop_integration.py): Simulates how Claude Desktop might integrate with the Prompt Decorators MCP server.

To run these examples, you'll need to install the MCP package:

```bash
pip install "mcp[cli]"
```

Then you can run the examples:

```bash
# Run the MCP integration example
python examples/mcp_integration_example.py

# Run the MCP client example
python examples/mcp_client_example.py

# Run the Claude Desktop integration example
python examples/claude_desktop_integration.py
```

## Using the Examples

Each example directory contains its own README with specific instructions for installation and usage.

## Contributing Examples

If you have a useful example that demonstrates how to use Prompt Decorators in a particular domain or for a specific use case, please consider contributing it to this directory.

To contribute an example:

1. Create a new directory with a descriptive name
2. Include a clear README.md with installation and usage instructions
3. Add any necessary code, tests, and documentation
4. Submit a pull request

## License

All examples in this directory are licensed under the MIT License.

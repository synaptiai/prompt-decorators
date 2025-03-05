# Integrations

Prompt Decorators can be integrated with various frameworks, protocols, and platforms to enhance their capabilities and extend their reach. This section provides documentation for the available integrations.

## Available Integrations

### [Model Context Protocol (MCP)](mcp.md)

The Model Context Protocol (MCP) integration allows you to use prompt decorators through MCP tools and predefined templates. This integration enables you to:

- Apply decorators to prompts using the MCP API
- Use predefined decorator templates
- Create custom templates for specific use cases
- Integrate with existing MCP servers

## Roadmap
Here are some additional improvements we are considering:
- **Dynamic Template Generation:**
You could extend the dynamic loading approach to automatically generate templates based on decorator categories or common use cases.
This would allow users to discover and use templates that showcase the capabilities of different decorators.
- **Template Customization:**
Add a way for users to customize templates or create their own templates through the MCP API.
This would allow users to save and reuse their favorite decorator combinations.
- **Decorator Composition:**
Add a tool that helps users compose decorators by suggesting compatible combinations.
This would make it easier for users to create effective decorator chains.
- **Documentation Integration:**
Add a tool that generates documentation for decorators and templates.
This would help users understand how to use the decorators effectively.

## Contributing New Integrations

If you'd like to contribute a new integration, please follow these steps:

1. Check the [roadmap](../roadmap.md) to see if the integration is already planned
2. Open an issue on GitHub to discuss the integration
3. Follow the [development guide](../development_guide.md) to implement the integration
4. Submit a pull request with your implementation
5. Add documentation for the integration in the `docs/integrations/` directory

For more information on contributing to Prompt Decorators, see the [contributing guidelines](../contributing.md).

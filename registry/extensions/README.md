# Extension Decorators

This directory contains decorators that are not defined in the original Prompt Decorators specification. These include:

1. **Community Extensions**: Decorators contributed by the community beyond the standard set
2. **Domain-Specific**: Specialized decorators for particular domains or industries
3. **Experimental**: New decorators being tested before potential inclusion in the core specification
4. **Implementation-Specific**: Decorators optimized for specific LLM implementations

## Contributing

To contribute a new decorator to the extensions registry:

1. Create a JSON file following the registry-entry.schema.json format
2. Include comprehensive documentation, parameters, examples, and compatibility information
3. Submit a pull request with your extension
4. Ensure your decorator does not conflict with existing core or extension decorators

Please follow the naming conventions and structure of existing decorators to maintain consistency across the registry.

# Prompt Decorators JSON Schemas

This directory contains the JSON Schema definitions for the Prompt Decorators standard. These schemas define the structure and validation rules for various aspects of the standard.

## Schema Files

### 1. `decorator.schema.json`
- Defines the base structure of a single prompt decorator
- Used as a reference by other schemas
- Includes parameter validation and metadata
- Core schema that all decorator implementations must follow

### 2. `api-request.schema.json`
- Defines the structure of API requests when using decorators
- Includes prompt text, decorator list, and metadata
- References the decorator schema for decorator validation
- Used by LLM providers implementing the standard

### 3. `registry-entry.schema.json`
- Defines how decorators are registered in the central registry
- Includes detailed metadata, documentation, and compatibility info
- Used for publishing decorators to the registry
- Ensures consistent documentation and versioning

### 4. `extension-package.schema.json`
- Defines how decorator extensions are packaged
- Includes dependency management and configuration
- References the registry entry schema for decorator definitions
- Used for distributing collections of related decorators

## Usage

### Validation
Use these schemas to validate your decorator implementations:

```bash
# Using ajv-cli
npx ajv-cli validate -s decorator.schema.json -d your-decorator.json

# Using python-jsonschema
jsonschema -i your-decorator.json decorator.schema.json
```

### Integration
Reference these schemas in your JSON files:

```json
{
  "$schema": "https://raw.githubusercontent.com/prompt-decorators/spec/main/schemas/decorator.schema.json",
  "name": "YourDecorator",
  ...
}
```

## Schema Relationships

``` mermaid
graph TD
    A[decorator.schema.json] --> B[api-request.schema.json]
    A --> C[registry-entry.schema.json]
    C --> D[extension-package.schema.json]
```

## Versioning

The schemas follow semantic versioning:
- Major version changes indicate breaking changes
- Minor version changes add features in a backward-compatible manner
- Patch version changes fix issues in a backward-compatible manner

## Contributing

When contributing changes to the schemas:
1. Ensure backward compatibility unless making a major version change
2. Update all affected example files
3. Add/update tests for new/modified validation rules
4. Document any breaking changes in CHANGELOG.md

## Testing

Test your changes against the provided examples:

```bash
# Test all examples
./test-schemas.sh

# Test a specific schema
./test-schemas.sh decorator.schema.json
```

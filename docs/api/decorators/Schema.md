# Schema Decorator

Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `schema` | string | JSON Schema definition or reference to a predefined schema that defines the structure of the response | Required |
| `strict` | boolean | Whether to enforce strict schema compliance or allow flexibility | False |

## Examples

### Basic schema for a person's information

```
+++Schema(schema={"type":"object","properties":{"name":{"type":"string"},"age":{"type":"number"},"interests":{"type":"array","items":{"type":"string"}}}})
Describe a fictional character.
```

Returns information about a fictional character structured according to the specified schema with name, age, and interests

### Strict schema for product information

```
+++Schema(schema={"type":"object","required":["productName","price","features"],"properties":{"productName":{"type":"string"},"price":{"type":"number"},"features":{"type":"array"},"availability":{"type":"boolean"}}}, strict=true)
Describe a smartphone.
```

Returns smartphone information strictly following the specified schema with all required fields and proper data types

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Format your entire response according to this schema: {schema}

Make sure to follow the exact data types and structure. {strict} Present the final output as valid JSON that follows this schema precisely. Do not include markdown code blocks or any explanatory text outside the JSON structure.

**Notes:** This model may need explicit reminders to avoid adding explanatory text outside the schema structure, especially for complex schemas


## Compatibility

- **Requires**: None
- **Conflicts**: OutputFormat
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **OutputFormat**: Conflicts with Schema Schema provides custom structural definitions while OutputFormat specifies predefined formats like JSON or YAML
- **TableFormat**: Conflicts with Schema Schema defines arbitrary structures that may not be compatible with tabular representation
- **MECE**: Enhances Schema MECE can provide logical organization principles within Schema's structural framework

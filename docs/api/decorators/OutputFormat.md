# OutputFormat Decorator

Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way.

**Category**: Minimal

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `format` | enum | The format to use for the response | markdown |

## Format Options

- `json`: Format your response as a valid JSON object. Ensure proper use of quotes, brackets, and commas.
- `markdown`: Format your response using Markdown syntax with appropriate headings, lists, code blocks, and formatting.
- `yaml`: Format your response as YAML with proper indentation and structure.
- `xml`: Format your response as valid XML with proper tags and structure.
- `plaintext`: Format your response as plain text without any special formatting.

## Examples

### JSON output for structured data

```
+++OutputFormat(format=json)
List the top 5 programming languages and their key features.
```

Returns a JSON object with programming languages and their features

### Markdown output for formatted text

```
+++OutputFormat(format=markdown)
Write a tutorial on setting up a React project.
```

Returns a nicely formatted markdown document with headings, code blocks, and lists

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Your response must be formatted exactly as specified. For JSON, ensure valid JSON syntax. For Markdown, use proper Markdown syntax with headings, lists, and code blocks.

**Notes:** This model may need more explicit formatting instructions to produce properly formatted output


## Implementation Guidance

### JSON format implementation

**Original Prompt:**
```
List the top 5 programming languages and their key features.
```

**Transformed Prompt:**
```
Please format your response according to the specified format. Format your response as a valid JSON object. Ensure proper use of quotes, brackets, and commas.

List the top 5 programming languages and their key features.
```

### Markdown format implementation

**Original Prompt:**
```
Write a tutorial on setting up a React project.
```

**Transformed Prompt:**
```
Please format your response according to the specified format. Format your response using Markdown syntax with appropriate headings, lists, code blocks, and formatting.

Write a tutorial on setting up a React project.
```

## Transformation Details

**Base Instruction:** Please format your response according to the specified format.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `format`:
  - When set to `json`: Format your response as a valid JSON object. Ensure proper use of quotes, brackets, and commas.
  - When set to `markdown`: Format your response using Markdown syntax with appropriate headings, lists, code blocks, and formatting.
  - When set to `yaml`: Format your response as YAML with proper indentation and structure.
  - When set to `xml`: Format your response as valid XML with proper tags and structure.
  - When set to `plaintext`: Format your response as plain text without any special formatting.

## Compatibility

- **Requires**: None
- **Conflicts**: Schema, TableFormat, Bullet
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Schema**: Conflicts with OutputFormat Schema provides a more specific structure than OutputFormat and may conflict
- **StepByStep**: Enhances OutputFormat Can be combined with StepByStep to create formatted step-by-step guides

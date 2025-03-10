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

### gpt-3.5-turbo

**Instruction:** Your response must be formatted exactly as specified. For JSON, ensure valid JSON syntax. For Markdown, use proper Markdown syntax with headings, lists, and code blocks.

**Notes:** This model may need more explicit formatting instructions to produce properly formatted output


## Compatibility

- **Requires**: None
- **Conflicts**: Schema, TableFormat, Bullet
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Schema**: Conflicts with OutputFormat Schema provides a more specific structure than OutputFormat and may conflict
- **StepByStep**: Enhances OutputFormat Can be combined with StepByStep to create formatted step-by-step guides

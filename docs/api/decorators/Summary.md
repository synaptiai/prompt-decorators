# Summary Decorator

Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `length` | `enum` | Relative length of the summary | `medium` |
| `wordCount` | `number` | Approximate target word count for the summary | `` |
| `position` | `enum` | Where to position the summary in relation to any full content | `standalone` |

## Length Options

- `short`: Make the summary very concise (approximately 2-3 sentences) capturing only the most essential points.
- `medium`: Create a moderate-length summary that includes main ideas and key supporting details (approximately 1 paragraph).
- `long`: Provide a comprehensive summary that covers all significant points while still being more condensed than a full explanation (approximately 2-3 paragraphs).

## Position Options

- `beginning`: Place the summary at the beginning of your response, before any detailed content.
- `end`: Place the summary at the end of your response, after providing the detailed content.
- `standalone`: Provide only the summary without additional detailed content.

## Examples

### Short standalone summary of a complex topic

```
+++Summary(length=short)
Explain quantum computing and its potential applications.
```

Delivers a concise overview of quantum computing and its applications in approximately 2-3 sentences

### Specific word count summary at the beginning of a response

```
+++Summary(wordCount=100, position=beginning)
Describe the causes and effects of climate change.
```

Starts with a 100-word summary of climate change causes and effects, followed by more detailed information

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a brief summary that captures the key points of your response. Focus on the most important information.

**Notes:** This model sometimes requires more explicit instructions about brevity


## Implementation Guidance

### Short standalone summary

**Original Prompt:**
```
Explain quantum computing and its potential applications.
```

**Transformed Prompt:**
```
Please provide a condensed summary of the information in your response. Make the summary very concise (approximately 2-3 sentences) capturing only the most essential points. Provide only the summary without additional detailed content.

Explain quantum computing and its potential applications.
```

### Word-count limited summary at beginning

**Original Prompt:**
```
Describe the causes and effects of climate change.
```

**Transformed Prompt:**
```
Please provide a condensed summary of the information in your response. The summary should be approximately 100 words in length. Place the summary at the beginning of your response, before any detailed content.

Describe the causes and effects of climate change.
```

## Transformation Details

**Base Instruction:** Please provide a condensed summary of the information in your response.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `length`:
  - When set to `short`: Make the summary very concise (approximately 2-3 sentences) capturing only the most essential points.
  - When set to `medium`: Create a moderate-length summary that includes main ideas and key supporting details (approximately 1 paragraph).
  - When set to `long`: Provide a comprehensive summary that covers all significant points while still being more condensed than a full explanation (approximately 2-3 paragraphs).

- `wordCount`:
  - Format: The summary should be approximately {value} words in length.

- `position`:
  - When set to `beginning`: Place the summary at the beginning of your response, before any detailed content.
  - When set to `end`: Place the summary at the end of your response, after providing the detailed content.
  - When set to `standalone`: Provide only the summary without additional detailed content.

## Compatibility

- **Requires**: None
- **Conflicts**: Detailed
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Detailed**: Conflicts with Summary Summary aims for concise information, which directly conflicts with Detailed's expansive approach
- **Concise**: Enhances Summary Summary and Concise work well together for extremely brief outputs

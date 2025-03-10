# Concise Decorator

Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `maxWords` | number | Maximum word count for the entire response |  |
| `bulletPoints` | boolean | Whether to use bullet points for maximum brevity | False |
| `level` | enum | The degree of conciseness to apply | moderate |

## Level Options

- `moderate`: Focus on the most important information while maintaining readability and essential context.
- `high`: Include only key points and critical information, eliminating all non-essential details.
- `extreme`: Provide only the absolute minimum information required to answer the question - be as brief as possible.

## Examples

### Basic concise explanation of a complex topic

```
+++Concise
Explain how blockchain technology works.
```

Provides a brief, to-the-point explanation of blockchain technology focusing only on essential concepts

### Extremely concise bulleted answer with word limit

```
+++Concise(maxWords=50, bulletPoints=true, level=extreme)
What are the key factors in successful project management?
```

Delivers a set of extremely concise bullet points covering only the most critical project management factors, totaling under 50 words

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Be extremely brief and direct. Focus only on essential information and eliminate all unnecessary words. Get straight to the point.

**Notes:** This model may need more explicit instructions about brevity requirements


## Implementation Guidance

### Basic concise explanation

**Original Prompt:**
```
Explain how blockchain technology works.
```

**Transformed Prompt:**
```
Please provide a concise, to-the-point response without unnecessary details or verbose language. Focus on the most important information while maintaining readability and essential context. Use concise paragraphs rather than bullet points.

Explain how blockchain technology works.
```

### Extremely concise bullet points with word limit

**Original Prompt:**
```
What are the key factors in successful project management?
```

**Transformed Prompt:**
```
Please provide a concise, to-the-point response without unnecessary details or verbose language. Limit your entire response to no more than 50 words. Use bullet points to present information in the most concise format possible. Provide only the absolute minimum information required to answer the question - be as brief as possible.

What are the key factors in successful project management?
```

## Transformation Details

**Base Instruction:** Please provide a concise, to-the-point response without unnecessary details or verbose language.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `maxWords`:
  - Format: Limit your entire response to no more than {value} words.

- `bulletPoints`:
  - When set to `true`: Use bullet points to present information in the most concise format possible.
  - When set to `false`: Use concise paragraphs rather than bullet points.

- `level`:
  - When set to `moderate`: Focus on the most important information while maintaining readability and essential context.
  - When set to `high`: Include only key points and critical information, eliminating all non-essential details.
  - When set to `extreme`: Provide only the absolute minimum information required to answer the question - be as brief as possible.

## Compatibility

- **Requires**: None
- **Conflicts**: Detailed
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Detailed**: Conflicts with Concise Concise aims for brevity while Detailed aims for comprehensive coverage, creating a direct conflict
- **Summary**: Enhances Concise Summary and Concise can work together to create extremely condensed outputs

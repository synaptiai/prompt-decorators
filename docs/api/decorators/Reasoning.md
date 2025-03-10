# Reasoning Decorator

Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy.

**Category**: Minimal

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `depth` | `enum` | The level of detail in the reasoning process | `moderate` |

## Depth Options

- `basic`: Focus on the most important logical steps.
- `moderate`: Balance detail with clarity in your reasoning.
- `comprehensive`: Provide a very thorough and detailed analysis with multiple perspectives.

## Examples

### Basic reasoning for a simple question

```
+++Reasoning(depth=basic)
What is the best programming language for beginners?
```

Provides a brief explanation of key factors before recommending a language

### Comprehensive analysis of a complex topic

```
+++Reasoning(depth=comprehensive)
What are the implications of quantum computing for cybersecurity?
```

Delivers an in-depth analysis covering multiple aspects and their interconnections

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Explain your reasoning step by step before giving your final answer. Show your thought process clearly.

**Notes:** This model may require more explicit instructions to produce detailed reasoning


## Implementation Guidance

### Standard implementation

**Original Prompt:**
```
What are the implications of artificial intelligence for education?
```

**Transformed Prompt:**
```
Please provide detailed reasoning in your response. Show your thought process before reaching a conclusion. Provide a very thorough and detailed analysis with multiple perspectives.

What are the implications of artificial intelligence for education?
```

### Basic depth implementation

**Original Prompt:**
```
How does compound interest work?
```

**Transformed Prompt:**
```
Please provide detailed reasoning in your response. Show your thought process before reaching a conclusion. Focus on the most important logical steps.

How does compound interest work?
```

## Transformation Details

**Base Instruction:** Please provide detailed reasoning in your response. Show your thought process before reaching a conclusion.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `depth`:
  - When set to `basic`: Focus on the most important logical steps.
  - When set to `moderate`: Balance detail with clarity in your reasoning.
  - When set to `comprehensive`: Provide a very thorough and detailed analysis with multiple perspectives.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Concise**: Conflicts with Reasoning The objectives of comprehensive reasoning and concise responses may contradict each other
- **StepByStep**: Enhances Reasoning Combining these decorators produces structured reasoning with clear steps

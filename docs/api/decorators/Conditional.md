# Conditional Decorator

A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.

**Category**: Meta

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `if_param` | string | The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}') | Required |
| `then` | string | The decorator to apply if the condition is true (can be a specific decorator with parameters) | Required |
| `else_param` | string | The decorator to apply if the condition is false (can be a specific decorator with parameters) |  |

## Examples

### Basic conditional application based on content complexity

```
+++Conditional(if_param=complex, then=StepByStep, else_param=Concise)
Explain how quantum computing works.
```

Evaluates if the topic is complex, which quantum computing is, so it applies the StepByStep decorator

### Conditional application with parameterized decorators

```
+++Conditional(if_param=controversial, then=Debate(perspectives=3), else_param=Reasoning(depth=moderate))
Discuss the ethical implications of gene editing in humans.
```

Determines that gene editing ethics is controversial, so it applies the Debate decorator with 3 perspectives rather than the Reasoning decorator

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** This response requires conditional formatting. First, analyze the topic to determine if it qualifies as '{if_param}'. Based on your determination, format your response using either the '{then}' approach (if true) or the '{else_param}' approach (if false).

**Notes:** This model may need more explicit instructions about the conditional evaluation process


## Implementation Guidance

### Conditional based on complexity

**Original Prompt:**
```
Explain how quantum computing works.
```

**Transformed Prompt:**
```
Please evaluate the topic and adapt your response formatting based on the conditional logic specified. First, determine if the topic or question can be classified as 'complex'. If the condition is true (the topic IS complex), then apply the following approach: StepByStep. If the condition is false (the topic is NOT complex), then apply the following approach instead: Concise.

Explain how quantum computing works.
```

### Conditional based on controversy

**Original Prompt:**
```
Discuss the ethical implications of gene editing in humans.
```

**Transformed Prompt:**
```
Please evaluate the topic and adapt your response formatting based on the conditional logic specified. First, determine if the topic or question can be classified as 'controversial'. If the condition is true (the topic IS controversial), then apply the following approach: Debate(perspectives=3). If the condition is false (the topic is NOT controversial), then apply the following approach instead: Reasoning(depth=moderate).

Discuss the ethical implications of gene editing in humans.
```

## Transformation Details

**Base Instruction:** Please evaluate the topic and adapt your response formatting based on the conditional logic specified.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `if_param`:
  - Format: First, determine if the topic or question can be classified as '{value}'.

- `then`:
  - Format: If the condition is true (the topic IS {if_param}), then apply the following approach: {value}.

- `else_param`:
  - Format: If the condition is false (the topic is NOT {if_param}), then apply the following approach instead: {value}.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **All**: Enhances Conditional Conditional is a meta-decorator that may use any other decorator as part of its then/else parameters
- **Priority**: Enhances Conditional Priority can be used with Conditional to establish fallback patterns if conditions aren't met

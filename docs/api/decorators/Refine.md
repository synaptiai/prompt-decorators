# Refine Decorator

A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.

**Category**: Meta

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `iterations` | number | Number of refinement cycles to perform | 2 |
| `focus` | array | Specific aspects to focus on during refinement (e.g., clarity, conciseness, evidence) |  |
| `showProcess` | boolean | Whether to show the intermediate steps in the refinement process | False |

## Examples

### Basic refinement of a complex explanation

```
+++Refine
Explain the implications of quantum computing for cybersecurity.
```

Provides a refined explanation of quantum computing implications for cybersecurity, with two hidden iterations improving clarity and accuracy

### Detailed refinement with visible iterations

```
+++Refine(iterations=3, focus=[clarity,evidence,conciseness], showProcess=true)
Analyze the economic impacts of artificial intelligence.
```

Shows three visible iterations of analyzing AI economic impacts, with each step focusing on improving clarity, strengthening evidence, and enhancing conciseness

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** For this response, you will create multiple drafts, with each draft improving on the previous one. Think carefully about how to enhance each version.

**Notes:** This model may require more explicit instructions about the refinement process


## Implementation Guidance

### Standard implementation with two iterations

**Original Prompt:**
```
Explain the implications of quantum computing for cybersecurity.
```

**Transformed Prompt:**
```
Please apply an iterative refinement process to your response, with each iteration improving upon the previous version. Perform 2 refinement iterations to improve your response. Only provide the final refined response without showing the intermediate steps.

Explain the implications of quantum computing for cybersecurity.
```

### Comprehensive refinement with visible process

**Original Prompt:**
```
Analyze the economic impacts of artificial intelligence.
```

**Transformed Prompt:**
```
Please apply an iterative refinement process to your response, with each iteration improving upon the previous version. Perform 3 refinement iterations to improve your response. Focus your refinements on improving these specific aspects: clarity,evidence,conciseness. Show each iteration separately in your response, labeling them as 'Draft 1', 'Draft 2', etc., to demonstrate the refinement process.

Analyze the economic impacts of artificial intelligence.
```

## Transformation Details

**Base Instruction:** Please apply an iterative refinement process to your response, with each iteration improving upon the previous version.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `iterations`:
  - Format: Perform {value} refinement iterations to improve your response.

- `focus`:
  - Format: Focus your refinements on improving these specific aspects: {value}.

- `showProcess`:
  - When set to `true`: Show each iteration separately in your response, labeling them as 'Draft 1', 'Draft 2', etc., to demonstrate the refinement process.
  - When set to `false`: Only provide the final refined response without showing the intermediate steps.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **StepByStep**: Enhances Refine Refine can improve a StepByStep response by making each step clearer and more precise
- **Chain**: Conflicts with Refine Chain and Refine both control multi-step processing and may conflict

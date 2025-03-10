# StepByStep Decorator

Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.

**Category**: Minimal

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `numbered` | boolean | Whether to number the steps or use bullet points | True |

## Examples

### Numbered steps for a technical process

```
+++StepByStep(numbered=true)
How do I set up a Python virtual environment?
```

Provides numbered steps for creating and activating a virtual environment

### Bullet-point steps for a creative process

```
+++StepByStep(numbered=false)
How do I brainstorm effectively?
```

Delivers bullet-pointed steps for conducting a brainstorming session

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Please provide a step-by-step guide with each step clearly labeled and explained. Break down the process into clear, manageable steps.

**Notes:** This model may need more explicit instructions to create well-structured steps


## Implementation Guidance

### Standard implementation with numbered steps

**Original Prompt:**
```
How do I create a sourdough starter?
```

**Transformed Prompt:**
```
Please break down your response into clear, sequential steps. Number each step sequentially (Step 1, Step 2, etc.).

How do I create a sourdough starter?
```

### Implementation with bullet points

**Original Prompt:**
```
What's the process for conducting user research?
```

**Transformed Prompt:**
```
Please break down your response into clear, sequential steps. Use bullet points for each step instead of numbers.

What's the process for conducting user research?
```

## Transformation Details

**Base Instruction:** Please break down your response into clear, sequential steps.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `numbered`:
  - When set to `true`: Number each step sequentially (Step 1, Step 2, etc.).
  - When set to `false`: Use bullet points for each step instead of numbers.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Reasoning**: Enhances StepByStep Combining these decorators produces step-by-step reasoning that is both structured and logical
- **OutputFormat**: Enhances StepByStep Can be combined with OutputFormat for structured formatting of the steps

# StepByStepImpl Decorator

Requests a step-by-step implementation approach, with explicitly labeled stages.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `detail` | `enum` | Level of explanation and comments | `moderate` |
| `steps` | `string` | Number of implementation steps | `auto` |
| `output` | `enum` | What to include in each step | `code-with-explanation` |

## Detail Options

- `minimal`: Keep explanations and comments minimal, focusing on essential information only.
- `moderate`: Provide balanced explanations and comments that clarify the implementation without being excessive.
- `comprehensive`: Include detailed explanations and comprehensive comments for each part of the implementation.

## Output Options

- `code-only`: Present only the code for each step, with minimal explanation.
- `code-with-explanation`: For each step, present the code along with explanations of what it does.
- `explanation-then-code`: For each step, first explain the concept or approach, then provide the implementation code.

## Examples

### Comprehensive implementation with explanation-first approach

```
+++StepByStepImpl(detail=comprehensive, steps=5, output=explanation-then-code)
Implement a JWT authentication middleware for Express.js that verifies tokens and extracts user roles.
```

The model will provide a 5-step implementation process for JWT authentication middleware, with detailed explanations followed by code for each step.

### Minimal code-focused implementation

```
+++StepByStepImpl(detail=minimal, output=code-only)
Create a React component that fetches and displays user data from an API.
```

The model will provide a step-by-step implementation with minimal comments, focusing primarily on the code for each step.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Break down the implementation into clearly labeled steps. For each step, {output_style}. Provide {detail_level} explanations.

**Notes:** For gpt-4 Turbo, more explicit instructions about the step structure may be needed.


## Implementation Guidance

### Web Development Implementation

**Original Prompt:**
```
Implement a JWT authentication middleware for Express.js that verifies tokens and extracts user roles.
```

**Transformed Prompt:**
```
Please provide a step-by-step implementation approach with explicitly labeled stages. Include detailed explanations and comprehensive comments for each part of the implementation. For each step, first explain the concept or approach, then provide the implementation code.

Implement a JWT authentication middleware for Express.js that verifies tokens and extracts user roles.
```

**Notes:** This example shows the decorator applied with comprehensive detail and explanation-then-code format.

## Transformation Details

**Base Instruction:** Please provide a step-by-step implementation approach with explicitly labeled stages.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `detail`:
  - When set to `minimal`: Keep explanations and comments minimal, focusing on essential information only.
  - When set to `moderate`: Provide balanced explanations and comments that clarify the implementation without being excessive.
  - When set to `comprehensive`: Include detailed explanations and comprehensive comments for each part of the implementation.

- `steps`:
  - Format: Organize the implementation into {value} distinct steps.

- `output`:
  - When set to `code-only`: Present only the code for each step, with minimal explanation.
  - When set to `code-with-explanation`: For each step, present the code along with explanations of what it does.
  - When set to `explanation-then-code`: For each step, first explain the concept or approach, then provide the implementation code.

## Compatibility

- **Requires**: None
- **Conflicts**: Concise, OneShot
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeQuality**: Enhances StepByStepImpl StepByStepImpl works well with CodeQuality to produce well-structured, high-quality implementation code.
- **Concise**: Conflicts with StepByStepImpl StepByStepImpl with detailed explanations conflicts with the Concise decorator's goal of brevity.

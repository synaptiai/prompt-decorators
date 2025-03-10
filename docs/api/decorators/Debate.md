# Debate Decorator

Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `perspectives` | number | Number of different perspectives to include in the debate | 2 |
| `balanced` | boolean | Whether to ensure equal representation and strength of arguments for each perspective | True |

## Examples

### Two-perspective debate on an ethical issue

```
+++Debate
Is it ethical to use AI-generated content without disclosure?
```

Presents balanced arguments for and against disclosure of AI-generated content

### Three-perspective debate on a policy issue with balanced representation

```
+++Debate(perspectives=3, balanced=true)
Should universal basic income be implemented nationally?
```

Presents three balanced perspectives on UBI in a debate format, ensuring equal representation of each viewpoint

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Present {perspectives} different viewpoints on this topic in a debate format. Structure the debate with clear labels for each perspective. Make sure each perspective presents strong arguments, and {balanced}. Ensure that no single perspective dominates the response.

**Notes:** This model sometimes needs explicit reminders to maintain quality arguments for perspectives it might not favor


## Implementation Guidance

### Two-sided debate on an ethical issue

**Original Prompt:**
```
Is it ethical to use AI-generated content without disclosure?
```

**Transformed Prompt:**
```
Please structure your response as a debate between multiple perspectives on the topic, presenting different viewpoints and their supporting arguments. Include 2 distinct perspectives or viewpoints in the debate, each with their own arguments and reasoning. Ensure that each perspective receives equal representation and that arguments for each side are of comparable strength and thoroughness.

Is it ethical to use AI-generated content without disclosure?
```

### Three-perspective balanced debate on a policy issue

**Original Prompt:**
```
Should universal basic income be implemented nationally?
```

**Transformed Prompt:**
```
Please structure your response as a debate between multiple perspectives on the topic, presenting different viewpoints and their supporting arguments. Include 3 distinct perspectives or viewpoints in the debate, each with their own arguments and reasoning. Ensure that each perspective receives equal representation and that arguments for each side are of comparable strength and thoroughness.

Should universal basic income be implemented nationally?
```

## Transformation Details

**Base Instruction:** Please structure your response as a debate between multiple perspectives on the topic, presenting different viewpoints and their supporting arguments.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `perspectives`:
  - Format: Include {value} distinct perspectives or viewpoints in the debate, each with their own arguments and reasoning.

- `balanced`:
  - When set to `true`: Ensure that each perspective receives equal representation and that arguments for each side are of comparable strength and thoroughness.
  - When set to `false`: Present different perspectives based on their merit or prevalence in the discourse, without forcing equal representation.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Balanced**: Enhances Debate Balanced complements Debate by ensuring fair treatment of each perspective
- **StepByStep**: Enhances Debate StepByStep can help organize the debates into clearer sequences of arguments and responses
- **FirstPrinciples**: Enhances Debate FirstPrinciples helps ground each debate perspective in fundamental assumptions and axioms

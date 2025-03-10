# Socratic Decorator

Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `iterations` | number | Number of question-answer cycles to include | 3 |

## Examples

### Basic socratic exploration of a philosophical concept

```
+++Socratic
What is justice?
```

Explores the concept of justice through a series of guiding questions

### Deep socratic analysis with 5 iterations

```
+++Socratic(iterations=5)
How do we know what we know?
```

Provides an extended series of 5 question-answer cycles to explore epistemology

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Format your response as a series of thought-provoking questions. For each question, provide a thoughtful answer that leads to the next question. This creates a step-by-step exploration of the topic.

**Notes:** This model benefits from more explicit instructions on the question-answer structure


## Implementation Guidance

### Standard implementation with 3 iterations

**Original Prompt:**
```
What is justice?
```

**Transformed Prompt:**
```
Please structure your response as a Socratic dialogue that guides through the topic using thought-provoking questions followed by answers. Include approximately 3 question-answer cycles in your exploration.

What is justice?
```

### Extended exploration with 5 iterations

**Original Prompt:**
```
How do we know what we know?
```

**Transformed Prompt:**
```
Please structure your response as a Socratic dialogue that guides through the topic using thought-provoking questions followed by answers. Include approximately 5 question-answer cycles in your exploration.

How do we know what we know?
```

## Transformation Details

**Base Instruction:** Please structure your response as a Socratic dialogue that guides through the topic using thought-provoking questions followed by answers.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `iterations`:
  - Format: Include approximately {value} question-answer cycles in your exploration.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **StepByStep**: Enhances Socratic Can be combined with StepByStep to create a structured Socratic analysis
- **OutputFormat**: Enhances Socratic Can be combined with OutputFormat for consistent presentation

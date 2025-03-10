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

### gpt-3.5-turbo

**Instruction:** Format your response as a series of thought-provoking questions. For each question, provide a thoughtful answer that leads to the next question. This creates a step-by-step exploration of the topic.

**Notes:** This model benefits from more explicit instructions on the question-answer structure


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **StepByStep**: Enhances Socratic Can be combined with StepByStep to create a structured Socratic analysis
- **OutputFormat**: Enhances Socratic Can be combined with OutputFormat for consistent presentation

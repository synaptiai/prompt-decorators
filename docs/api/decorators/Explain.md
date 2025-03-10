# Explain Decorator

Explains code or technical concepts with appropriate depth.

**Category**: Developer Education

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `level` | enum | Expertise assumption | intermediate |
| `approach` | enum | Explanation style | examples |
| `focus` | enum | Explanation emphasis | both |

## Level Options

- `beginner`: Explain this as if to someone new to the field, avoiding jargon and using simple concepts.
- `intermediate`: Explain this to someone with moderate familiarity with the subject area.
- `advanced`: Provide an in-depth technical explanation suitable for experts in the field.

## Approach Options

- `analogy`: Use relevant analogies to make the concept more relatable.
- `examples`: Include concrete examples to illustrate the concept.
- `theory`: Focus on the theoretical foundations and principles.
- `step-by-step`: Break down the explanation into clear sequential steps.
- `visual`: Describe visual representations or diagrams that would help understand the concept.

## Focus Options

- `how`: Focus on how it works and practical implementation details.
- `why`: Focus on why it exists and the underlying rationale.
- `both`: Cover both how it works and why it exists or is designed this way.

## Examples

### Explaining a programming concept at intermediate level with examples

```
+++Explain(level=intermediate, approach=examples, focus=both)
Explain React's useEffect hook and its dependency array.
```

A comprehensive explanation of React's useEffect hook that assumes intermediate knowledge, uses concrete examples, and covers both how it works and why it's designed that way.

### Explaining a complex concept to beginners using analogies

```
+++Explain(level=beginner, approach=analogy, focus=how)
Explain how public key cryptography works.
```

A beginner-friendly explanation of public key cryptography using analogies, focusing on how it works rather than theoretical underpinnings.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Please explain the following concept or code with clarity and detail.

**Notes:** Slightly simplified instruction for models with less context capacity.


## Implementation Guidance

### Explaining a programming concept

**Original Prompt:**
```
Explain React's useEffect hook and its dependency array.
```

**Transformed Prompt:**
```
Explain the following concept or code clearly and thoroughly. Explain this to someone with moderate familiarity with the subject area. Include concrete examples to illustrate the concept. Cover both how it works and why it exists or is designed this way.

Explain React's useEffect hook and its dependency array.
```

**Notes:** The transformation adds context about the target audience level, preferred explanation approach, and what aspects to focus on.

## Transformation Details

**Base Instruction:** Explain the following concept or code clearly and thoroughly.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `level`:
  - When set to `beginner`: Explain this as if to someone new to the field, avoiding jargon and using simple concepts.
  - When set to `intermediate`: Explain this to someone with moderate familiarity with the subject area.
  - When set to `advanced`: Provide an in-depth technical explanation suitable for experts in the field.

- `approach`:
  - When set to `analogy`: Use relevant analogies to make the concept more relatable.
  - When set to `examples`: Include concrete examples to illustrate the concept.
  - When set to `theory`: Focus on the theoretical foundations and principles.
  - When set to `step-by-step`: Break down the explanation into clear sequential steps.
  - When set to `visual`: Describe visual representations or diagrams that would help understand the concept.

- `focus`:
  - When set to `how`: Focus on how it works and practical implementation details.
  - When set to `why`: Focus on why it exists and the underlying rationale.
  - When set to `both`: Cover both how it works and why it exists or is designed this way.

## Compatibility

- **Requires**: None
- **Conflicts**: ELI5, TechnicalDetail
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **ELI5**: Conflicts with Explain ELI5 sets a specific explanation level that would override the level parameter in Explain.
- **CodeReview**: Enhances Explain Can be used together to explain code while reviewing it.

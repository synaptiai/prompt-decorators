# Inductive Decorator

Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `examples` | `number` | Number of specific examples or observations to include before generalizing | `3` |
| `confidence` | `boolean` | Whether to explicitly state the confidence level of the inductive conclusions | `False` |
| `structure` | `enum` | The pattern of inductive reasoning to follow | `generalization` |

## Structure Options

- `generalization`: Use generalization induction, where common properties among the examples are used to form a general rule or principle.
- `causal`: Apply causal induction, focusing on identifying cause-and-effect relationships across the examples to establish causal patterns.
- `statistical`: Employ statistical induction, using quantitative patterns and probabilistic reasoning to derive statistical generalizations from the examples.
- `analogical`: Utilize analogical induction, where similarities between examples are used to infer that they likely share other properties as well.

## Examples

### Basic inductive reasoning from examples to general principles

```
+++Inductive
What factors contribute to successful startups?
```

Provides specific examples of successful startups, identifies patterns across them, and derives general principles of startup success

### Causal inductive reasoning with confidence levels

```
+++Inductive(examples=5, confidence=true, structure=causal)
How does screen time affect child development?
```

Presents 5 specific observations about screen time and child development, infers causal relationships, and generalizes with explicit confidence levels for each conclusion

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Use inductive reasoning to address this question. Start with {examples} specific real-world examples. Analyze these examples to identify patterns. Then use {structure} reasoning to derive general principles or conclusions. {confidence} Make each step in your reasoning explicit and clearly show how you move from specific cases to general insights.

**Notes:** This model sometimes needs explicit instruction to avoid jumping directly to conclusions without thoroughly examining specific examples first


## Implementation Guidance

### Basic inductive reasoning about successful startups

**Original Prompt:**
```
What factors contribute to successful startups?
```

**Transformed Prompt:**
```
Please structure your response using inductive reasoning, moving from specific observations or examples to broader generalizations and theories. Focus on pattern recognition and deriving general principles from particular instances. Begin with 3 specific, concrete examples or observations before deriving generalizations from them. Present the inductive conclusions without explicitly stating confidence levels. Use generalization induction, where common properties among the examples are used to form a general rule or principle.

What factors contribute to successful startups?
```

### Causal inductive reasoning about screen time

**Original Prompt:**
```
How does screen time affect child development?
```

**Transformed Prompt:**
```
Please structure your response using inductive reasoning, moving from specific observations or examples to broader generalizations and theories. Focus on pattern recognition and deriving general principles from particular instances. Begin with 5 specific, concrete examples or observations before deriving generalizations from them. Explicitly state the confidence level for each inductive conclusion, acknowledging the inherent uncertainty in generalizing from specific cases. Apply causal induction, focusing on identifying cause-and-effect relationships across the examples to establish causal patterns.

How does screen time affect child development?
```

## Transformation Details

**Base Instruction:** Please structure your response using inductive reasoning, moving from specific observations or examples to broader generalizations and theories. Focus on pattern recognition and deriving general principles from particular instances.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `examples`:
  - Format: Begin with {value} specific, concrete examples or observations before deriving generalizations from them.

- `confidence`:
  - When set to `true`: Explicitly state the confidence level for each inductive conclusion, acknowledging the inherent uncertainty in generalizing from specific cases.
  - When set to `false`: Present the inductive conclusions without explicitly stating confidence levels.

- `structure`:
  - When set to `generalization`: Use generalization induction, where common properties among the examples are used to form a general rule or principle.
  - When set to `causal`: Apply causal induction, focusing on identifying cause-and-effect relationships across the examples to establish causal patterns.
  - When set to `statistical`: Employ statistical induction, using quantitative patterns and probabilistic reasoning to derive statistical generalizations from the examples.
  - When set to `analogical`: Utilize analogical induction, where similarities between examples are used to infer that they likely share other properties as well.

## Compatibility

- **Requires**: None
- **Conflicts**: Deductive
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Deductive**: Conflicts with Inductive Inductive and Deductive represent opposite reasoning approaches (specific-to-general vs. general-to-specific)
- **Uncertainty**: Enhances Inductive Uncertainty works well with Inductive (especially with confidence=true) to acknowledge the probabilistic nature of inductive conclusions
- **StepByStep**: Enhances Inductive StepByStep can help organize the progression from specific examples to general principles

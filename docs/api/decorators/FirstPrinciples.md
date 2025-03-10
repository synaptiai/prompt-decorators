# FirstPrinciples Decorator

Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `depth` | number | Level of detail in breaking down to fundamental principles | 3 |

## Examples

### Basic first principles analysis of a concept

```
+++FirstPrinciples
How do electric vehicles work?
```

Breaks down electric vehicles into fundamental principles of electricity, motors, and energy storage before explaining the complete system

### Deep first principles analysis with maximum depth

```
+++FirstPrinciples(depth=5)
What makes machine learning effective?
```

Provides an extensive breakdown of machine learning starting from mathematical foundations and progressively building up to complex algorithms

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Start by identifying the most basic, fundamental truths about this topic - the axioms that cannot be broken down further. Then build your explanation step by step from these foundations, showing how complex aspects emerge from these simple principles.

**Notes:** This model benefits from more explicit instructions about the process of first principles analysis


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Reasoning**: Enhances FirstPrinciples FirstPrinciples provides a specific reasoning approach that complements the general Reasoning decorator
- **StepByStep**: Enhances FirstPrinciples StepByStep can organize the first principles analysis into clearer sequential steps

# FirstPrinciples Decorator

Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `depth` | `number` | Level of detail in breaking down to fundamental principles | `3` |

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

### gpt-4-turbo

**Instruction:** Start by identifying the most basic, fundamental truths about this topic - the axioms that cannot be broken down further. Then build your explanation step by step from these foundations, showing how complex aspects emerge from these simple principles.

**Notes:** This model benefits from more explicit instructions about the process of first principles analysis


## Implementation Guidance

### Standard implementation with moderate depth

**Original Prompt:**
```
How do electric vehicles work?
```

**Transformed Prompt:**
```
Please structure your response using first principles thinking. Break down the topic into fundamental truths or axioms that cannot be reduced further, then build up your explanation from these foundations. Provide a thorough analysis of the fundamental principles underlying the topic.

How do electric vehicles work?
```

### Deep fundamental analysis

**Original Prompt:**
```
What makes machine learning effective?
```

**Transformed Prompt:**
```
Please structure your response using first principles thinking. Break down the topic into fundamental truths or axioms that cannot be reduced further, then build up your explanation from these foundations. Provide an extremely comprehensive analysis of all fundamental axioms, exploring their origins and interconnections in depth.

What makes machine learning effective?
```

## Transformation Details

**Base Instruction:** Please structure your response using first principles thinking. Break down the topic into fundamental truths or axioms that cannot be reduced further, then build up your explanation from these foundations.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `depth`:
  - When set to `1`: Provide a basic breakdown with only the most essential fundamental principles.
  - When set to `2`: Break down the topic into key fundamental principles with moderate detail.
  - When set to `3`: Provide a thorough analysis of the fundamental principles underlying the topic.
  - When set to `4`: Break down the topic extensively into detailed fundamental principles and their relationships.
  - When set to `5`: Provide an extremely comprehensive analysis of all fundamental axioms, exploring their origins and interconnections in depth.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Reasoning**: Enhances FirstPrinciples FirstPrinciples provides a specific reasoning approach that complements the general Reasoning decorator
- **StepByStep**: Enhances FirstPrinciples StepByStep can organize the first principles analysis into clearer sequential steps

# Detailed Decorator

Enhances the response with comprehensive information, thorough explanations, and rich context. This decorator is ideal for in-depth learning, complex topics requiring nuance, or when completeness is valued over brevity.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `depth` | enum | The level of detail and comprehensiveness | comprehensive |
| `aspects` | array | Specific aspects or dimensions to explore in detail |  |
| `examples` | boolean | Whether to include detailed examples to illustrate points | True |

## Depth Options

- `moderate`: Include a good level of detail that covers the main points thoroughly while avoiding excessive information.
- `comprehensive`: Provide extensive detail, covering both main concepts and secondary aspects with thorough explanation of each.
- `exhaustive`: Deliver an extremely detailed analysis that leaves no aspect unexplored, including nuances, edge cases, theoretical foundations, and practical applications.

## Examples

### Comprehensive detailed explanation of a concept

```
+++Detailed
Explain how the human immune system works.
```

Provides a thorough, in-depth explanation of the immune system covering all major components, processes, and functions with illustrative examples

### Exhaustive detailed analysis of specific aspects

```
+++Detailed(depth=exhaustive, aspects=[economic,environmental,social,technological], examples=true)
Analyze the implications of transitioning to renewable energy.
```

Delivers an extremely detailed analysis of renewable energy transition, exhaustively covering all four specified aspects with comprehensive examples

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Provide an extremely thorough and comprehensive response that covers all aspects of this topic in detail. Don't simplify or abbreviate. Include explanations of core concepts, nuances, relationships between ideas, and practical implications.

**Notes:** This model sometimes needs more explicit instructions to maintain depth throughout a long response


## Compatibility

- **Requires**: None
- **Conflicts**: Concise, Summary
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Concise**: Conflicts with Detailed Detailed's comprehensive approach directly conflicts with Concise's brevity focus
- **Summary**: Conflicts with Detailed Detailed aims for comprehensiveness while Summary aims for conciseness
- **StepByStep**: Enhances Detailed StepByStep can organize detailed information into a more digestible format

# ComplexityLevel Decorator

Specifies the permitted complexity level for the implementation.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `code` | enum | Code complexity limit | moderate |
| `concepts` | enum | Conceptual complexity limit | intermediate |
| `dependencies` | enum | External dependency usage | standard |

## Code Options

- `simple`: Use simple, straightforward code structures. Avoid complex algorithms or patterns.
- `moderate`: Balance simplicity with efficiency. Use standard patterns where appropriate.
- `complex`: Optimize for performance and scalability. Use advanced patterns when beneficial.
- `necessary-only`: Use only the complexity that is absolutely necessary for the task.

## Concepts Options

- `beginner-friendly`: Use only basic concepts that beginners would understand. Explain any non-trivial concepts.
- `intermediate`: You can use intermediate-level concepts that most practitioners would be familiar with.
- `advanced`: You can use advanced concepts and techniques appropriate for experienced developers.

## Dependencies Options

- `none`: Do not use any external dependencies or libraries.
- `minimal`: Use only essential dependencies. Prefer standard libraries when possible.
- `standard`: Use common, well-established dependencies as needed.
- `whatever-needed`: Use any dependencies that would make the implementation better, regardless of number.

## Examples

### Simple date formatter with beginner-friendly concepts

```
+++ComplexityLevel(code=simple, concepts=beginner-friendly, dependencies=minimal)
Implement a simple date formatter utility that converts between different date formats without external libraries.
```

The model will provide a simple date formatter implementation using only basic programming concepts and minimal dependencies, suitable for beginners.

### Complex algorithm with standard dependencies

```
+++ComplexityLevel(code=complex, concepts=advanced, dependencies=standard)
Implement a machine learning algorithm for sentiment analysis.
```

The model will provide an optimized, advanced implementation using standard libraries and frameworks appropriate for experienced developers.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Implement this with the following complexity constraints: {code_complexity}, {concept_complexity}, {dependency_usage}.

**Notes:** More explicit phrasing works better with this model.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **LanguagePreference**: Enhances ComplexityLevel ComplexityLevel works well with LanguagePreference to specify both the programming language and its complexity level.
- **OptimizationFocus**: Conflicts with ComplexityLevel May conflict with OptimizationFocus if that decorator requests optimizations that would increase complexity beyond the specified level.

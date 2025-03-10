# Optimize Decorator

Optimizes code for specific metrics while respecting constraints.

**Category**: Code Generation

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `for` | enum | The primary optimization target | speed |
| `constraints` | enum | Limitations that must be respected | none |
| `priority` | enum | Trade-off preference when optimizations conflict | balanced |

## For Options

- `speed`: execution speed and performance
- `memory`: memory usage and efficiency
- `readability`: code clarity and maintainability
- `size`: code size and compactness
- `network`: network efficiency and reduced data transfer

## Constraints Options

- `backwards-compatible`: maintaining backward compatibility
- `minimal-changes`: making minimal changes to the original code
- `no-external-dependencies`: using no additional external dependencies
- `same-api`: preserving the same API interface
- `none`: Option: none

## Priority Options

- `max-gains`: maximum optimization gains even if it involves more risk
- `min-risk`: minimal risk approaches even if the optimization gains are smaller
- `balanced`: a balanced approach between optimization gains and risk

## Examples

### Optimizing code for memory usage with backward compatibility

```
+++Optimize(for=memory, constraints=backwards-compatible, priority=min-risk)
Optimize this image processing function that's consuming too much memory.
```

The model will optimize the code focusing on memory efficiency, while ensuring backward compatibility and taking a conservative approach to changes.

### Optimizing for speed with default constraints

```
+++Optimize(for=speed)
Make this sorting algorithm faster.
```

The model will focus on improving execution speed with balanced risk approach and no specific constraints.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Please optimize this code for {for}, making sure to follow these constraints: {constraints}. When there are trade-offs to make, prioritize {priority}.

**Notes:** More explicit instruction format works better with this model.


## Compatibility

- **Requires**: None
- **Conflicts**: Refactor
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Explain**: Enhances Optimize Can be combined with Explain to request optimization with explanations of the changes made.
- **Refactor**: Conflicts with Optimize Both decorators attempt to modify code structure which may lead to conflicting instructions.

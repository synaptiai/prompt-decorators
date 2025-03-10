# Analogical Decorator

Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `domain` | string | Specific domain or context to draw analogies from (if not specified, will choose appropriate domains) | general |
| `count` | number | Number of distinct analogies to provide | 1 |
| `depth` | enum | Level of detail in developing the analogy | moderate |

## Depth Options

- `brief`: Keep each analogy concise, covering only the most essential mappings between the concept and the analogy.
- `moderate`: Develop each analogy with balanced detail, explaining key mappings and their relevance.
- `extended`: Elaborate each analogy thoroughly, exploring multiple aspects of the mapping and their implications in detail.

## Examples

### Single analogy from a specific domain

```
+++Analogical(domain=sports)
Explain how the immune system works.
```

Explains the immune system using extended sports analogies, comparing immune cells to players, pathogens to opponents, etc.

### Multiple brief analogies from different domains

```
+++Analogical(count=3, depth=brief)
Describe how blockchain technology functions.
```

Provides three different brief analogies for blockchain from different domains (perhaps physical ledgers, chain of custody, and distributed networks)

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Explain this concept through {count} analogy(ies) that compare it to something from {domain}. For each analogy, establish clear mappings between elements of the original concept and the analogy. Make the analogy {depth} in detail to help readers understand the concept through familiar comparisons.

**Notes:** This model sometimes generates analogies that are too superficial and may need explicit guidance to develop deeper mappings


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ELI5**: Enhances Analogical Analogical reasoning pairs exceptionally well with ELI5 to create child-friendly explanations through familiar comparisons
- **ForcedAnalogy**: Enhances Analogical ForcedAnalogy can direct the analogical reasoning to specific predefined domains for creative comparisons
- **Precision**: Conflicts with Analogical Precision's focus on exactness may conflict with the inherent approximations in analogical reasoning

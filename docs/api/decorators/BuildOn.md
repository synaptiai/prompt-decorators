# BuildOn Decorator

A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.

**Category**: Meta

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `reference` | enum | What to build upon from the previous context | last |
| `approach` | enum | How to build upon the referenced content | extend |
| `preserveStructure` | boolean | Whether to maintain the structure of the referenced content | True |

## Reference Options

- `last`: Build specifically upon the most recent response or context provided.
- `specific`: Build upon the specific part of the previous context mentioned in the current prompt.
- `all`: Consider all previous exchanges in the conversation when building your response.

## Approach Options

- `extend`: Add new information, examples, or dimensions that extend and complement the existing content.
- `refine`: Improve, correct, or enhance the existing content while preserving its core message.
- `contrast`: Provide alternative perspectives or approaches that contrast with those in the existing content.
- `synthesize`: Combine and integrate ideas from the existing content into a new cohesive whole.

## Examples

### Basic extension of the previous response

```
+++BuildOn
Add more detail about implementation challenges.
```

Extends the previous response by adding more detailed information about implementation challenges while maintaining continuity

### Specific refinement with structural changes

```
+++BuildOn(reference=specific, approach=refine, preserveStructure=false)
Improve the section on risk analysis with more quantitative measures.
```

Refines specifically the risk analysis section from the previous content with more quantitative measures, potentially restructuring it

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Continue from {reference} response, building on what was already said. {approach} the existing content while {preserveStructure}. Make sure your response feels like a natural continuation rather than starting over.

**Notes:** This model sometimes needs explicit reminders to fully incorporate previous context

### gpt-4

**Instruction:** Treating the {reference} as your foundation, please {approach} that content. {preserveStructure} Ensure your response maintains continuity with what came before.

**Notes:** This model handles contextual building well but benefits from clear instructions about which aspects to preserve


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Refine**: Enhances BuildOn BuildOn and Refine can work together to iteratively improve content over multiple interactions
- **Contrast**: Enhances BuildOn When using the contrast approach, BuildOn works well with decorators that provide multiple perspectives

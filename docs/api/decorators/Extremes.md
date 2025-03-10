# Extremes Decorator

Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `versions` | enum | Which extreme versions to include | both |
| `dimension` | string | The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity') | ambition |
| `compare` | boolean | Whether to include a comparative analysis of the extreme versions | True |

## Versions Options

- `radical`: Focus exclusively on presenting a radical, ambitious, or maximalist version that pushes boundaries and represents the most expansive vision possible.
- `minimal`: Focus exclusively on presenting a minimal, conservative, or basic version that emphasizes simplicity, feasibility, and immediate implementability.
- `both`: Present both a radical, ambitious version and a minimal, conservative version, clearly contrasting these opposite approaches.

## Examples

### Basic exploration of minimal and radical approaches

```
+++Extremes
Describe a strategy for reducing carbon emissions.
```

Presents both a minimal, immediately achievable carbon reduction strategy and a radical, transformative approach, with a comparison of their respective impacts, feasibility, and trade-offs

### Only radical version along a specific dimension

```
+++Extremes(versions=radical, dimension=technological innovation, compare=false)
Outline the future of transportation.
```

Provides only a technologically radical vision of transportation's future, focusing on the most innovative and disruptive possibilities without comparison to other approaches

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Present {versions} versions of this topic along the spectrum of {dimension}. If showing a minimal version, focus on what's practical, immediately achievable, and conservative. If showing a radical version, explore ambitious, transformative possibilities that push boundaries. {compare} Make the contrast between approaches very clear, and ensure each version is fully developed.

**Notes:** This model sometimes needs reminders to ensure the radical version is truly ambitious and not just a moderate enhancement of conventional approaches


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Alternatives**: Enhances Extremes Extremes complements Alternatives by specifically focusing on opposite ends of a spectrum while Alternatives generates distinct options
- **Constraints**: Enhances Extremes Constraints can help define the parameters for the minimal version in the Extremes decorator
- **Balanced**: Conflicts with Extremes Extremes intentionally presents polarized views rather than the balanced perspective promoted by the Balanced decorator

# TemporalResonance Decorator

Analyzes topics across multiple time horizons to identify patterns, principles, and possibilities that transcend present-focused thinking

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `horizons` | number | Number of distinct time horizons to explore | 3 |
| `resonancePoints` | number | Number of resonance points to identify across time horizons | 3 |
| `futureScenarios` | number | Number of potential future scenarios to consider | 3 |
| `domain` | enum | Specific domain context for the temporal analysis | general |
| `depth` | enum | Depth of historical analysis and future projection | moderate |

## Domain Options

- `business`: Focus on organizational patterns, market cycles, and business model evolution across time periods.
- `technology`: Examine technological adoption cycles, innovation patterns, and digital transformation dynamics across different eras.
- `society`: Analyze social movements, cultural shifts, and institutional changes across historical periods.
- `personal`: Focus on individual development patterns, career trajectories, and personal growth cycles.
- `science`: Examine scientific paradigm shifts, research methodologies, and knowledge development across different periods.
- `general`: Apply a general temporal analysis approach appropriate to the topic.

## Depth Options

- `shallow`: Conduct a brief analysis of obvious patterns across time horizons.
- `moderate`: Perform a balanced temporal analysis that identifies substantive patterns without excessive historical detail.
- `deep`: Conduct a comprehensive temporal analysis with detailed historical context, nuanced present assessment, and well-developed future projections.

## Examples

### Business transformation analysis

```
+++TemporalResonance(domain=business, resonancePoints=3, depth=moderate)
```

Analyzes business transformation through three time horizons, identifying three key resonance points with moderate historical depth

### Personal career planning

```
+++TemporalResonance(domain=personal, futureScenarios=4, depth=deep)
```

Provides deep analysis of personal career development across time horizons with four detailed future scenarios

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: claude-3-opus-20240229, claude-3-sonnet-20240229, gpt-4, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **StepByStep**: Enhances TemporalResonance StepByStep can be used to structure the temporal analysis process
- **Debate**: Enhances TemporalResonance Debate can be used to explore contrasting views across different time horizons

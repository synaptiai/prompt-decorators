# TemporalResonance Decorator

Analyzes topics across multiple time horizons to identify patterns, principles, and possibilities that transcend present-focused thinking

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `horizons` | `number` | Number of distinct time horizons to explore | `3` |
| `resonancePoints` | `number` | Number of resonance points to identify across time horizons | `3` |
| `futureScenarios` | `number` | Number of potential future scenarios to consider | `3` |
| `domain` | `enum` | Specific domain context for the temporal analysis | `general` |
| `depth` | `enum` | Depth of historical analysis and future projection | `moderate` |

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

## Implementation Guidance

### Organizational change management

**Original Prompt:**
```
How can I approach implementing a new CRM system effectively?
```

**Transformed Prompt:**
```
Analyze the topic using the Temporal Resonance approach, which examines patterns across different time horizons (past, present, and future) to generate insights that transcend present limitations. Identify recurring patterns, underlying principles, and resonance points where insights from different time periods amplify each other. Explore three distinct time horizons: historical patterns, current dynamics, and emergent possibilities. Identify three powerful resonance points that demonstrate persistent patterns across different time contexts. Develop three distinct future scenarios representing different potential trajectories. Focus on organizational patterns, market cycles, and business model evolution across time periods. Perform a balanced temporal analysis that identifies substantive patterns without excessive historical detail.

How can I approach implementing a new CRM system effectively?
```

## Transformation Details

**Base Instruction:** Analyze the topic using the Temporal Resonance approach, which examines patterns across different time horizons (past, present, and future) to generate insights that transcend present limitations. Identify recurring patterns, underlying principles, and resonance points where insights from different time periods amplify each other.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `horizons`:
  - When set to `2`: Explore two primary time horizons.
  - When set to `3`: Explore three distinct time horizons: historical patterns, current dynamics, and emergent possibilities.
  - When set to `4`: Explore four time horizons, including distant past, recent past, present, and future possibilities.
  - When set to `5`: Conduct a comprehensive exploration across five time horizons, ranging from distant historical patterns to long-term future possibilities.

- `resonancePoints`:
  - When set to `1`: Identify one key resonance point where patterns across time horizons converge.
  - When set to `2`: Identify two significant resonance points that reveal patterns transcending specific time periods.
  - When set to `3`: Identify three powerful resonance points that demonstrate persistent patterns across different time contexts.
  - When set to `4`: Conduct an extensive analysis to identify four or more resonance points that reveal deep underlying principles.

- `futureScenarios`:
  - When set to `1`: Consider one primary future trajectory.
  - When set to `2`: Explore two contrasting future scenarios.
  - When set to `3`: Develop three distinct future scenarios representing different potential trajectories.
  - When set to `4`: Create a comprehensive set of four or more future scenarios to capture a wide range of possibilities.

- `domain`:
  - When set to `business`: Focus on organizational patterns, market cycles, and business model evolution across time periods.
  - When set to `technology`: Examine technological adoption cycles, innovation patterns, and digital transformation dynamics across different eras.
  - When set to `society`: Analyze social movements, cultural shifts, and institutional changes across historical periods.
  - When set to `personal`: Focus on individual development patterns, career trajectories, and personal growth cycles.
  - When set to `science`: Examine scientific paradigm shifts, research methodologies, and knowledge development across different periods.
  - When set to `general`: Apply a general temporal analysis approach appropriate to the topic.

- `depth`:
  - When set to `shallow`: Conduct a brief analysis of obvious patterns across time horizons.
  - When set to `moderate`: Perform a balanced temporal analysis that identifies substantive patterns without excessive historical detail.
  - When set to `deep`: Conduct a comprehensive temporal analysis with detailed historical context, nuanced present assessment, and well-developed future projections.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: claude-3-opus-20240229, claude-3-sonnet-20240229, gpt-4o, gpt-4o-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **StepByStep**: Enhances TemporalResonance StepByStep can be used to structure the temporal analysis process
- **Debate**: Enhances TemporalResonance Debate can be used to explore contrasting views across different time horizons

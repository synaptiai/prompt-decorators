# BreakAndBuild Decorator

Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `breakdown` | enum | Primary approach for the critical breakdown phase | comprehensive |
| `intensity` | enum | How thorough and challenging the breakdown phase should be | thorough |
| `buildRatio` | number | Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique) | 1 |

## Breakdown Options

- `weaknesses`: In the breakdown phase, focus primarily on identifying functional weaknesses, operational gaps, and practical limitations.
- `assumptions`: In the breakdown phase, focus primarily on identifying and questioning underlying assumptions, unstated premises, and taken-for-granted elements.
- `risks`: In the breakdown phase, focus primarily on identifying potential risks, failure modes, and negative scenarios.
- `comprehensive`: In the breakdown phase, conduct a comprehensive critique that addresses weaknesses, assumptions, risks, and any other relevant vulnerabilities.

## Intensity Options

- `mild`: Keep the breakdown phase constructive and moderate in tone, highlighting issues without overly aggressive critique.
- `thorough`: Make the breakdown phase thorough and substantial, with detailed examination of significant issues.
- `intense`: Make the breakdown phase rigorous and challenging, with incisive critique that explores fundamental flaws and serious concerns.

## Examples

### Basic break and build analysis of a business concept

```
+++BreakAndBuild
Evaluate this startup idea: a subscription service for plant care.
```

First thoroughly critiques the plant care subscription concept by identifying weaknesses and risks, then reconstructs it with improvements and solutions of equal depth

### Intense breakdown of assumptions with substantial rebuilding

```
+++BreakAndBuild(breakdown=assumptions, intensity=intense, buildRatio=2)
Analyze this public policy proposal for reducing urban congestion.
```

Delivers an intense critique focused specifically on the assumptions underlying the urban congestion proposal, followed by twice as much content reconstructing it with stronger foundations and improvements

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Analyze this idea in two clear sections:
1. BREAK: {intensity} critique focusing on {breakdown}. Be specific about what doesn't work and why.
2. BUILD: Create an improved version that addresses all the problems you identified. Make this section approximately {buildRatio}x longer than the BREAK section.

Clearly separate these sections with headings.

**Notes:** This model may need explicit reminders to ensure that the build phase directly addresses the specific issues identified in the breakdown phase


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **RedTeam**: Enhances BreakAndBuild RedTeam can strengthen the breakdown phase while BreakAndBuild ensures a constructive rebuilding follows the critique
- **Steelman**: Enhances BreakAndBuild Steelman can be applied to the build phase to create the strongest possible version after breaking down the original
- **Prioritize**: Enhances BreakAndBuild Prioritize can help focus both the breakdown and build phases on the most important aspects of the topic

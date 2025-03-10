# Alternatives Decorator

Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `count` | `number` | Number of alternative options or approaches to generate | `3` |
| `diversity` | `enum` | How different or varied the alternatives should be from each other | `medium` |
| `comparison` | `boolean` | Whether to include a comparative analysis of the alternatives | `False` |

## Diversity Options

- `low`: Generate alternatives that are variations on the same fundamental approach with different implementations or emphases.
- `medium`: Generate alternatives that offer substantively different approaches while still being practical and conventional.
- `high`: Generate alternatives that are radically different from each other, exploring unconventional approaches and diverse paradigms.

## Examples

### Basic alternative approaches to a problem

```
+++Alternatives
How can I improve my public speaking skills?
```

Provides three distinct approaches to improving public speaking skills, each with its own methodology and focus

### Highly diverse alternatives with comparative analysis

```
+++Alternatives(count=5, diversity=high, comparison=true)
What are some ways to reduce carbon emissions in urban areas?
```

Presents five highly diverse approaches to reducing urban carbon emissions, followed by a comparative analysis of their effectiveness, cost, and implementation challenges

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Generate {count} significantly different approaches to address this question. Each approach should be distinct and labeled clearly. Make sure these alternatives are {diversity} in terms of their fundamental strategy. {comparison}

**Notes:** This model sometimes needs more explicit instructions about maintaining meaningful differences between alternatives


## Implementation Guidance

### Basic alternative approaches to improving public speaking

**Original Prompt:**
```
How can I improve my public speaking skills?
```

**Transformed Prompt:**
```
Please provide multiple distinct options, approaches, or solutions to this question or problem rather than a single definitive answer. Present exactly 3 different alternatives. Generate alternatives that offer substantively different approaches while still being practical and conventional. Present each alternative independently without explicitly comparing them to each other.

How can I improve my public speaking skills?
```

### Diverse alternatives for reducing carbon emissions with comparative analysis

**Original Prompt:**
```
What are some ways to reduce carbon emissions in urban areas?
```

**Transformed Prompt:**
```
Please provide multiple distinct options, approaches, or solutions to this question or problem rather than a single definitive answer. Present exactly 5 different alternatives. Generate alternatives that are radically different from each other, exploring unconventional approaches and diverse paradigms. After presenting all alternatives, include a comparative analysis that evaluates their relative strengths, weaknesses, and suitability for different contexts or priorities.

What are some ways to reduce carbon emissions in urban areas?
```

## Transformation Details

**Base Instruction:** Please provide multiple distinct options, approaches, or solutions to this question or problem rather than a single definitive answer.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `count`:
  - Format: Present exactly {value} different alternatives.

- `diversity`:
  - When set to `low`: Generate alternatives that are variations on the same fundamental approach with different implementations or emphases.
  - When set to `medium`: Generate alternatives that offer substantively different approaches while still being practical and conventional.
  - When set to `high`: Generate alternatives that are radically different from each other, exploring unconventional approaches and diverse paradigms.

- `comparison`:
  - When set to `true`: After presenting all alternatives, include a comparative analysis that evaluates their relative strengths, weaknesses, and suitability for different contexts or priorities.
  - When set to `false`: Present each alternative independently without explicitly comparing them to each other.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Comparison**: Enhances Alternatives When used with comparison=true, the Comparison decorator can provide additional structure to the comparative analysis
- **DecisionMatrix**: Enhances Alternatives DecisionMatrix works well with Alternatives to evaluate the different options against criteria
- **Debate**: Enhances Alternatives Debate can add dialectical consideration of the pros and cons of different alternatives

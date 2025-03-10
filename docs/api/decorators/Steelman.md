# Steelman Decorator

Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `sides` | number | Number of different viewpoints to steel-man | 2 |
| `critique` | boolean | Whether to include critique after presenting the steel-manned arguments | False |
| `separation` | boolean | Whether to clearly separate the steel-manned presentations from any analysis | True |

## Examples

### Steel-manning both sides of a controversial issue

```
+++Steelman
Is universal basic income a good policy?
```

Presents the strongest possible cases both for and against universal basic income, with each position articulated in its most compelling form

### Steel-manning one position with subsequent critique

```
+++Steelman(sides=1, critique=true, separation=true)
What is the strongest case for cryptocurrency as the future of finance?
```

Provides the most compelling possible argument for cryptocurrency as the future of finance, clearly separated from a subsequent balanced critique

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Present the most compelling and charitable version of {sides} positions on this topic. For each position, include the strongest evidence, most persuasive reasoning, and most thoughtful responses to potential objections. Make each position as convincing as possible, even those you might disagree with. {critique} {separation} Avoid straw-manning any position.

**Notes:** This model sometimes needs explicit reminders to avoid unconsciously weakening positions it might not favor


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Debate**: Enhances Steelman Steelman works effectively with Debate to ensure all positions are presented in their strongest form before being debated
- **Critique**: Enhances Steelman When critique=true, Steelman pairs well with Critique to first present the strongest form of a position, then analyze it critically
- **Balanced**: Enhances Steelman Steelman helps ensure the Balance decorator presents the strongest form of each position when discussing multiple viewpoints

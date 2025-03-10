# Abductive Decorator

Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `hypotheses` | number | Number of alternative hypotheses or explanations to generate | 3 |
| `criteria` | array | Specific criteria to evaluate hypotheses against (e.g., simplicity, explanatory power) |  |
| `rank` | boolean | Whether to explicitly rank hypotheses by likelihood | True |

## Examples

### Basic abductive reasoning with multiple hypotheses

```
+++Abductive
Why have bee populations been declining globally?
```

Presents observed facts about bee population decline, generates three possible explanations, and identifies the most likely causes based on available evidence

### Detailed abductive reasoning with specific evaluation criteria

```
+++Abductive(hypotheses=4, criteria=[comprehensiveness,simplicity,novelty,testability], rank=true)
What might explain the Fermi Paradox?
```

Develops four hypotheses explaining the Fermi Paradox, evaluates each against the specified criteria, and ranks them from most to least likely explanation

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Develop {hypotheses} possible explanations for this phenomenon. For each explanation: 1) Describe the hypothesis, 2) Connect it to the observed evidence, 3) Evaluate it against {criteria}, 4) Discuss its strengths and limitations. {rank} Present your reasoning clearly, acknowledging that we're working with incomplete information.

**Notes:** This model may sometimes need reminders to avoid conflating abductive reasoning with deductive or inductive approaches


## Implementation Guidance

### Basic abductive reasoning about bee population decline

**Original Prompt:**
```
Why have bee populations been declining globally?
```

**Transformed Prompt:**
```
Please use abductive reasoning to develop the most likely explanations for the observations or phenomena described. Focus on inferring the best explanation from limited information, clearly presenting hypotheses that could account for the available evidence. Generate exactly 3 distinct alternative hypotheses or explanations that could account for the observations. Explicitly rank the hypotheses from most to least likely based on how well they explain the observations and meet the evaluation criteria.

Why have bee populations been declining globally?
```

### Detailed abductive reasoning about the Fermi Paradox

**Original Prompt:**
```
What might explain the Fermi Paradox?
```

**Transformed Prompt:**
```
Please use abductive reasoning to develop the most likely explanations for the observations or phenomena described. Focus on inferring the best explanation from limited information, clearly presenting hypotheses that could account for the available evidence. Generate exactly 4 distinct alternative hypotheses or explanations that could account for the observations. Evaluate each hypothesis against these specific criteria: [comprehensiveness,simplicity,novelty,testability]. For each criterion, explain how well the hypothesis satisfies it. Explicitly rank the hypotheses from most to least likely based on how well they explain the observations and meet the evaluation criteria.

What might explain the Fermi Paradox?
```

## Transformation Details

**Base Instruction:** Please use abductive reasoning to develop the most likely explanations for the observations or phenomena described. Focus on inferring the best explanation from limited information, clearly presenting hypotheses that could account for the available evidence.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `hypotheses`:
  - Format: Generate exactly {value} distinct alternative hypotheses or explanations that could account for the observations.

- `criteria`:
  - Format: Evaluate each hypothesis against these specific criteria: {value}. For each criterion, explain how well the hypothesis satisfies it.

- `rank`:
  - When set to `true`: Explicitly rank the hypotheses from most to least likely based on how well they explain the observations and meet the evaluation criteria.
  - When set to `false`: Present the hypotheses without explicit ranking, focusing on the strengths and limitations of each potential explanation.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **FindGaps**: Enhances Abductive FindGaps helps identify missing information that could strengthen or challenge the abductive hypotheses
- **Uncertainty**: Enhances Abductive Uncertainty pairs well with Abductive to acknowledge the probabilistic nature of inferential explanations
- **Limitations**: Enhances Abductive Limitations helps clarify the constraints of each abductive hypothesis and the overall analysis

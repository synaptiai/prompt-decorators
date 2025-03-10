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


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **FindGaps**: Enhances Abductive FindGaps helps identify missing information that could strengthen or challenge the abductive hypotheses
- **Uncertainty**: Enhances Abductive Uncertainty pairs well with Abductive to acknowledge the probabilistic nature of inferential explanations
- **Limitations**: Enhances Abductive Limitations helps clarify the constraints of each abductive hypothesis and the overall analysis

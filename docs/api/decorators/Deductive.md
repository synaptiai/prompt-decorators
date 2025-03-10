# Deductive Decorator

Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `premises` | number | Number of main premises to include before deducing conclusions | 2 |
| `formal` | boolean | Whether to use formal logical structures with explicit syllogisms | False |
| `steps` | number | Number of logical steps to include in the deductive process | 3 |

## Examples

### Basic deductive reasoning from principles to specific conclusions

```
+++Deductive
Should social media companies be regulated like utilities?
```

Starts with general principles about utilities and regulation, establishes premises about social media characteristics, and deduces conclusions about appropriate regulatory approaches

### Formal deductive logic with multiple steps

```
+++Deductive(formal=true, steps=5)
Is artificial intelligence conscious?
```

Presents formal logical syllogisms about consciousness and intelligence, proceeding through 5 distinct logical steps to reach conclusions about AI consciousness

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Use deductive reasoning to answer this question. Start with {premises} general principles or premises. Follow a logical process through {steps} clear steps from these premises to a conclusion. {formal} Make each step in your reasoning explicit and label it clearly.

**Notes:** This model sometimes needs more explicit structure to maintain rigorous deductive reasoning throughout a response


## Compatibility

- **Requires**: None
- **Conflicts**: Inductive
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Inductive**: Conflicts with Deductive Deductive and Inductive represent opposite reasoning approaches (general-to-specific vs. specific-to-general)
- **StepByStep**: Enhances Deductive StepByStep can help organize the deductive reasoning process into clearly labeled steps
- **Academic**: Enhances Deductive Academic pairs well with Deductive for scholarly logical analysis in formal contexts

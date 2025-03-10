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


## Implementation Guidance

### Basic deductive reasoning about social media regulation

**Original Prompt:**
```
Should social media companies be regulated like utilities?
```

**Transformed Prompt:**
```
Please structure your response using deductive reasoning, moving from general principles to specific conclusions. Start with clear premises and work methodically through logical steps to reach necessary conclusions. Begin with 2 main premises or general principles that establish the foundation for your reasoning. Use natural language deductive reasoning without requiring formal syllogisms. Develop your logical argument through 3 distinct, sequential steps, where each builds upon the previous ones.

Should social media companies be regulated like utilities?
```

### Formal deductive reasoning about AI consciousness

**Original Prompt:**
```
Is artificial intelligence conscious?
```

**Transformed Prompt:**
```
Please structure your response using deductive reasoning, moving from general principles to specific conclusions. Start with clear premises and work methodically through logical steps to reach necessary conclusions. Begin with 2 main premises or general principles that establish the foundation for your reasoning. Use formal logical structures with explicitly stated syllogisms, clearly identifying major premises, minor premises, and conclusions. Develop your logical argument through 5 distinct, sequential steps, where each builds upon the previous ones.

Is artificial intelligence conscious?
```

## Transformation Details

**Base Instruction:** Please structure your response using deductive reasoning, moving from general principles to specific conclusions. Start with clear premises and work methodically through logical steps to reach necessary conclusions.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `premises`:
  - Format: Begin with {value} main premises or general principles that establish the foundation for your reasoning.

- `formal`:
  - When set to `true`: Use formal logical structures with explicitly stated syllogisms, clearly identifying major premises, minor premises, and conclusions.
  - When set to `false`: Use natural language deductive reasoning without requiring formal syllogisms.

- `steps`:
  - Format: Develop your logical argument through {value} distinct, sequential steps, where each builds upon the previous ones.

## Compatibility

- **Requires**: None
- **Conflicts**: Inductive
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Inductive**: Conflicts with Deductive Deductive and Inductive represent opposite reasoning approaches (general-to-specific vs. specific-to-general)
- **StepByStep**: Enhances Deductive StepByStep can help organize the deductive reasoning process into clearly labeled steps
- **Academic**: Enhances Deductive Academic pairs well with Deductive for scholarly logical analysis in formal contexts

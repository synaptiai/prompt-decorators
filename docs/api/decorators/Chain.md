# Chain Decorator

A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.

**Category**: Meta

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `decorators` | array | Ordered list of decorators to apply in sequence | Required |
| `showSteps` | boolean | Whether to show intermediate outputs after each decorator in the chain | False |
| `stopOnFailure` | boolean | Whether to stop the chain if a decorator fails to apply correctly | True |

## Examples

### Basic sequential application of decorators

```
+++Chain(decorators=[StepByStep,Concise])
Explain how neural networks learn.
```

First generates a step-by-step explanation of neural network learning, then applies conciseness to that output

### Complex decorator chain with visible intermediate steps

```
+++Chain(decorators=[Socratic,Academic,TreeOfThought], showSteps=true, stopOnFailure=false)
Discuss the ethics of autonomous weapons.
```

Shows the progression of applying Socratic questioning, then academic tone, then tree-of-thought reasoning to discuss autonomous weapons ethics

## Model-Specific Implementations

### gpt-4

**Instruction:** Apply these decorators in sequence: {decorators}. Each decorator processes the output of the previous one. {showSteps} {stopOnFailure}

**Notes:** This model handles decorator chains well, but benefits from clear instructions about showing steps or handling failures

### gpt-3.5-turbo

**Instruction:** Process this request through a series of steps. For each step, apply one of these decorators in this exact order: {decorators}. Make sure to follow the exact order and treat each output as input to the next decorator. {showSteps} {stopOnFailure}

**Notes:** This model may need more explicit instructions to maintain the correct sequence of decorators


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **All**: Enhances Chain Chain can work with any decorators, as it's designed to combine them in sequence
- **Priority**: Conflicts with Chain Priority and Chain represent different approaches to handling multiple decorators (parallel vs. sequential)

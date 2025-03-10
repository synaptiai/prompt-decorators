# Compatibility Decorator

A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.

**Category**: Meta

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `models` | `array` | List of specific models to adapt for (e.g., gpt-4-turbo, gpt-4o, etc.) | `Required` |
| `fallback` | `string` | Decorator to apply if the current model doesn't match any in the models list | `` |
| `behaviors` | `string` | JSON string mapping model names to specific adaptations (e.g., '{"gpt-4-turbo": "simplify complex reasoning", "gpt-4o": "maximize detailed analysis"}') | `` |

## Examples

### Basic model-specific adaptation

```
+++Compatibility(models=[gpt-4o], fallback=StepByStep)
+++TreeOfThought(branches=3, depth=3)
Solve this complex optimization problem.
```

If using gpt-4o, applies the TreeOfThought decorator with full functionality; if using any other model, falls back to the simpler StepByStep decorator

### Detailed model-specific behavior adaptations

```
+++Compatibility(models=[gpt-4o,gpt-4-turbo], behaviors={"gpt-4o":"use full mathematical notation and derivations", "gpt-4-turbo":"use simplified equations and more intuitive explanations"})
+++Academic(style=scientific)
Explain quantum field theory.
```

Applies the Academic decorator but adapts how quantum field theory is explained based on the specific model capabilities, with full mathematical rigor for gpt-4o or simplified explanations for gpt-4-turbo

## Model-Specific Implementations

### gpt-4o

**Instruction:** Apply special handling for different model capabilities. If using {models}, implement the full decorator capabilities. If not using one of these models, {fallback}. For model-specific behavior adjustments: {behaviors}. Adapt your response based on the capabilities of the model you're currently running on.

**Notes:** This model can effectively implement complex model-specific adaptation logic across different decorator combinations


## Implementation Guidance

### gpt-4o specific complex reasoning with StepByStep fallback

**Original Prompt:**
```
+++Compatibility(models=[gpt-4o], fallback=StepByStep)
+++TreeOfThought(branches=3, depth=3)
Solve this complex optimization problem.
```

**Transformed Prompt:**
```
Please apply model-specific adaptations to ensure optimal performance on the current language model. Apply the specialized behavior for these specific models: [gpt-4o]. If the current model is not in this list, use the default or fallback behavior. If the current model is not one of the specified models, fall back to using the StepByStep decorator instead.

+++TreeOfThought(branches=3, depth=3)
Solve this complex optimization problem.
```

### Model-specific explanations for quantum field theory

**Original Prompt:**
```
+++Compatibility(models=[gpt-4o,gpt-4-turbo], behaviors={"gpt-4o":"use full mathematical notation and derivations", "gpt-4-turbo":"use simplified equations and more intuitive explanations"})
+++Academic(style=scientific)
Explain quantum field theory.
```

**Transformed Prompt:**
```
Please apply model-specific adaptations to ensure optimal performance on the current language model. Apply the specialized behavior for these specific models: [gpt-4o,gpt-4-turbo]. If the current model is not in this list, use the default or fallback behavior. Apply these model-specific behavior adaptations: {"gpt-4o":"use full mathematical notation and derivations", "gpt-4-turbo":"use simplified equations and more intuitive explanations"}. Each adaptation should be used only when running on the corresponding model.

+++Academic(style=scientific)
Explain quantum field theory.
```

## Transformation Details

**Base Instruction:** Please apply model-specific adaptations to ensure optimal performance on the current language model.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `models`:
  - Format: Apply the specialized behavior for these specific models: {value}. If the current model is not in this list, use the default or fallback behavior.

- `fallback`:
  - Format: If the current model is not one of the specified models, fall back to using the {value} decorator instead.

- `behaviors`:
  - Format: Apply these model-specific behavior adaptations: {value}. Each adaptation should be used only when running on the corresponding model.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **All**: Enhances Compatibility Compatibility is designed to work with all other decorators to optimize their performance across different models
- **Priority**: Enhances Compatibility Priority can be used to control the sequence when both Compatibility and other meta-decorators are applied
- **Override**: Enhances Compatibility Compatibility and Override can work together to provide both model-specific adaptations and parameter customizations

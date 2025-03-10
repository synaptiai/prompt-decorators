# Compatibility Decorator

A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.

**Category**: Meta

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `models` | array | List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.) | Required |
| `fallback` | string | Decorator to apply if the current model doesn't match any in the models list |  |
| `behaviors` | string | JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}') |  |

## Examples

### Basic model-specific adaptation

```
+++Compatibility(models=[gpt-4], fallback=StepByStep)
+++TreeOfThought(branches=3, depth=3)
Solve this complex optimization problem.
```

If using GPT-4, applies the TreeOfThought decorator with full functionality; if using any other model, falls back to the simpler StepByStep decorator

### Detailed model-specific behavior adaptations

```
+++Compatibility(models=[gpt-4,gpt-3.5-turbo], behaviors={"gpt-4":"use full mathematical notation and derivations", "gpt-3.5-turbo":"use simplified equations and more intuitive explanations"})
+++Academic(style=scientific)
Explain quantum field theory.
```

Applies the Academic decorator but adapts how quantum field theory is explained based on the specific model capabilities, with full mathematical rigor for GPT-4 or simplified explanations for GPT-3.5-turbo

## Model-Specific Implementations

### gpt-4

**Instruction:** Apply special handling for different model capabilities. If using {models}, implement the full decorator capabilities. If not using one of these models, {fallback}. For model-specific behavior adjustments: {behaviors}. Adapt your response based on the capabilities of the model you're currently running on.

**Notes:** This model can effectively implement complex model-specific adaptation logic across different decorator combinations


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **All**: Enhances Compatibility Compatibility is designed to work with all other decorators to optimize their performance across different models
- **Priority**: Enhances Compatibility Priority can be used to control the sequence when both Compatibility and other meta-decorators are applied
- **Override**: Enhances Compatibility Compatibility and Override can work together to provide both model-specific adaptations and parameter customizations

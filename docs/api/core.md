# Core API

This page provides an overview of the core API components in the Prompt Decorators framework.

## Base Components

- [Base](modules/prompt_decorators.core.base.md): Base classes for decorators
- [Registry](modules/prompt_decorators.core.registry.md): Registry system for decorators
- [Validation](modules/prompt_decorators.core.validation.md): Validation utilities for decorators
- [Request](modules/prompt_decorators.core.request.md): Request handling for decorated prompts
- [Exceptions](modules/prompt_decorators.core.exceptions.md): Exception classes for error handling

## Model-Specific Adaptations

The Prompt Decorators framework provides support for model-specific adaptations through the `ModelSpecificDecorator` class. This allows decorators to adapt their behavior based on the capabilities of the target model.

### Using Model-Specific Decorators

```python
from prompt_decorators.core import ModelSpecificDecorator

class CustomModelSpecificDecorator(ModelSpecificDecorator):
    """A model-specific decorator that adapts to different models."""

    name = "CustomModelSpecific"
    version = "1.0.0"

    def apply_for_model(self, prompt: str) -> str:
        """Apply model-specific behavior."""
        if self.model_capabilities.supports_feature("reasoning"):
            return f"Use your reasoning capabilities to answer: {prompt}"
        else:
            return self.apply_fallback(prompt)

    def apply_fallback(self, prompt: str) -> str:
        """Fallback for models without specific capabilities."""
        return f"Answer this question step by step: {prompt}"

# Use with a specific model
decorator = CustomModelSpecificDecorator(model_id="gpt-4")
decorated_prompt = decorator.apply("Explain quantum computing.")
```

For more details, see the [Model Specific](modules/prompt_decorators.core.model_specific.md) module documentation. 
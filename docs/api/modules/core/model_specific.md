# Model Specific Module

The `model_specific` module provides functionality for adapting decorators to specific language models. It handles model-specific implementations and adaptations.

## ModelAdapter

```python
class ModelAdapter:
    """Adapts decorators to specific language models.

    This class provides methods for adapting decorators to specific language
    models, handling model-specific implementations and requirements.
    """
```

The `ModelAdapter` class adapts decorators to specific language models, handling model-specific implementations and requirements.

### Key Methods

- `adapt_decorator(decorator: BaseDecorator, model: str) -> BaseDecorator`: Adapt a decorator to a specific model
- `adapt_request(request: DecoratedRequest, model: str) -> DecoratedRequest`: Adapt a request to a specific model
- `get_model_capabilities(model: str) -> dict`: Get the capabilities of a specific model

## ModelCapabilities

```python
class ModelCapabilities:
    """Defines the capabilities of a language model.

    This class represents the capabilities of a language model,
    including supported decorators and features.
    """
```

The `ModelCapabilities` class defines the capabilities of a language model, including supported decorators and features.

### Key Attributes

- `model_id`: The identifier of the model
- `supported_decorators`: The decorators supported by the model
- `supported_features`: The features supported by the model
- `max_tokens`: The maximum number of tokens supported by the model

## ModelRegistry

```python
class ModelRegistry:
    """Registry of language models and their capabilities.

    This class manages the registration and retrieval of language models
    and their capabilities.
    """
```

The `ModelRegistry` class manages the registration and retrieval of language models and their capabilities.

### Key Methods

- `register_model(model_id: str, capabilities: ModelCapabilities) -> None`: Register a model and its capabilities
- `get_model_capabilities(model_id: str) -> ModelCapabilities`: Get the capabilities of a model
- `is_decorator_supported(model_id: str, decorator_name: str) -> bool`: Check if a decorator is supported by a model

## Usage Example

```python
from prompt_decorators.core.model_specific import ModelAdapter, ModelRegistry
from prompt_decorators.decorators import Reasoning, StepByStep
from prompt_decorators.core.request import DecoratedRequest

# Create model adapter
adapter = ModelAdapter()

# Adapt decorator to model
reasoning = Reasoning(depth="comprehensive")
adapted_reasoning = adapter.adapt_decorator(reasoning, "gpt-4")

# Adapt request to model
request = DecoratedRequest(
    prompt="Explain how nuclear fusion works.",
    decorators=[
        Reasoning(depth="comprehensive"),
        StepByStep(numbered=True)
    ],
    metadata={"model": "gpt-4"}
)
adapted_request = adapter.adapt_request(request, "gpt-4")

# Check model capabilities
registry = ModelRegistry()
capabilities = registry.get_model_capabilities("gpt-4")
is_supported = registry.is_decorator_supported("gpt-4", "Reasoning")
```

## API Reference {: #core-model-specific-api-reference }

::: prompt_decorators.core.model_specific

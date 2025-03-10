# model_specific

Model-Specific Decorator Module.

This module provides base classes and utilities for model-specific decorator adaptations.

## Module Variables

### `T`

Type: `TypeVar`

Value: `~T`

### `logger`

Type: `Logger`

Value: `<Logger prompt_decorators.core.model_specific (INFO)>`

## Classes

### `ModelSpecificDecorator`

Base class for model-specific decorator adaptations.

This class extends BaseDecorator to support model-specific adaptations,
allowing decorators to adjust their behavior based on the model being used.

**Bases:** `prompt_decorators.core.base.DecoratorBase`, `typing.Generic`

#### Attributes

- `from_dict`: `classmethod` = `<classmethod(<function ModelSpecificDecorator.from_dict at 0x105c18d60>)>`

#### Methods

##### `__init__`

Initialize a model-specific decorator.

Args:
    model_id: ID of the model to adapt for (optional)
    **kwargs: Additional parameters for the decorator. These are passed to the parent class constructor.

**Signature:** `__init__(self, model_id: Optional[str] = None, **kwargs)`

**Parameters:**

- `model_id`: `Optional` (default: `None`)
- `kwargs`:

##### `apply`

Apply the decorator to a prompt with model-specific adaptations.

This implementation first checks if the decorator is supported by the model,
then delegates to either apply_for_model or apply_fallback based on support.

Args:
    prompt: The original prompt to decorate

Returns:
    The decorated prompt

**Signature:** `apply(self, prompt: str) -> str`

**Parameters:**

- `prompt`: `str`

**Returns:** `str`

##### `apply_fallback`

Apply a fallback decoration when model doesn't support this decorator.

This method provides a fallback implementation that still attempts to
achieve a similar effect, but with simplified instructions.

Args:
    prompt: The original prompt to decorate

Returns:
    The decorated prompt

**Signature:** `apply_fallback(self, prompt: str) -> str`

**Parameters:**

- `prompt`: `str`

**Returns:** `str`

##### `apply_for_model`

Apply the decorator with model-specific adaptations.

This method should be implemented by subclasses to provide
model-specific adaptations.

Args:
    prompt: The original prompt to decorate

Returns:
    The decorated prompt

**Signature:** `apply_for_model(self, prompt: str) -> str`

**Parameters:**

- `prompt`: `str`

**Returns:** `str`

##### `apply_to_prompt`

Apply the decorator to a prompt.

This method uses the transformation_template to transform the prompt
according to the decorator's intended behavior.

Args:
    prompt: The prompt to decorate

Returns:
    The decorated prompt

**Signature:** `apply_to_prompt(self, prompt: str) -> str`

**Parameters:**

- `prompt`: `str`

**Returns:** `str`

##### `is_supported_by_model`

Check if this decorator is supported by the current model.

Args:
    self: The decorator instance

Returns:
    True if supported, False otherwise

**Signature:** `is_supported_by_model(self) -> bool`

**Parameters:**


**Returns:** `bool`

##### `set_model`

Set the model ID for this decorator.

Args:
    model_id: ID of the model to adapt for

Returns:
    None

**Signature:** `set_model(self, model_id: str) -> None`

**Parameters:**

- `model_id`: `str`

##### `to_dict`

Convert the decorator to a dictionary.

Args:
    self: The decorator instance

Returns:
    Dictionary representation of the decorator

**Signature:** `to_dict(self) -> Dict[str, Any]`

**Parameters:**


**Returns:** `Dict`

##### `transform_response`

Transform the LLM response according to the decorator's behavior.

The base implementation returns the response unchanged. Subclasses
should override this method if they need to modify the response.

Args:
    response: The LLM response to transform

Returns:
    The transformed response

**Signature:** `transform_response(self, response: str) -> str`

**Parameters:**

- `response`: `str`

**Returns:** `str`

### `ModelSpecificDecoratorFactory`

Factory for creating model-specific decorators.

This class provides methods for creating model-specific versions of decorators.
It allows for customizing decorator behavior based on specific model requirements.

The factory creates decorator instances that are tailored to work optimally with
particular language models, taking into account their unique capabilities and limitations.

#### Attributes

- `create_for_model`: `staticmethod` = `<staticmethod(<function ModelSpecificDecoratorFactory.create_for_model at 0x105c18c20>)>`

#### Methods

##### `create_for_model`

Create a model-specific version of a decorator.

This method creates a new class that extends both ModelSpecificDecorator and
the original decorator class, allowing for model-specific adaptations.

Args:
    decorator_class: Original decorator class
    model_id: ID of the model to adapt for
    **params: Parameters for the decorator. These are passed to the decorator constructor.

Returns:
    Instance of the model-specific decorator

**Signature:** `create_for_model(decorator_class: Type[prompt_decorators.core.base.DecoratorBase], model_id: str, **params) -> prompt_decorators.core.base.DecoratorBase`

**Parameters:**

- `decorator_class`: `Type`
- `model_id`: `str`
- `params`:

**Returns:** `DecoratorBase`

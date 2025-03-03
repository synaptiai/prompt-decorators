# Module `prompt_decorators.core.model_specific`

Model-Specific Decorator Module.

This module provides base classes and utilities for model-specific decorator adaptations.

## Classes

- [`ModelSpecificDecorator`](#class-modelspecificdecorator): Base class for model-specific decorator adaptations.
- [`ModelSpecificDecoratorFactory`](#class-modelspecificdecoratorfactory): Factory for creating model-specific decorators.

### Class `ModelSpecificDecorator`

Base class for model-specific decorator adaptations.

This class extends BaseDecorator to support model-specific adaptations,
allowing decorators to adjust their behavior based on the model being used.

**Inherits from:** `BaseDecorator, Generic`

#### Methods

- `__init__(model_id, kwargs)`
- `apply(prompt) -> <class 'str'>`
- `apply_fallback(prompt) -> <class 'str'>`
- `apply_for_model(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.model_specific.ModelSpecificDecorator'>`
- `is_supported_by_model() -> <class 'bool'>`
- `set_model(model_id) -> <class 'NoneType'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `transform_response(response) -> <class 'str'>`

### Class `ModelSpecificDecoratorFactory`

Factory for creating model-specific decorators.

This class provides methods for creating model-specific versions of decorators.
It allows for customizing decorator behavior based on specific model requirements.

The factory creates decorator instances that are tailored to work optimally with
particular language models, taking into account their unique capabilities and limitations.

#### Methods

- `create_for_model(decorator_class, model_id, params) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

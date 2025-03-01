# Module `prompt_decorators.core.model_specific`

Model-Specific Decorator Module

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
- `from_dict(data) -> <class 'prompt_decorators.core.model_specific.ModelSpecificDecorator'>`
- `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `get_version() -> <class 'prompt_decorators.core.base.Version'>`
- `is_compatible_with_version(version_str) -> <class 'bool'>`
- `is_supported_by_model() -> <class 'bool'>`
- `set_model(model_id) -> <class 'NoneType'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_json(indent) -> <class 'str'>`
- `validate() -> <class 'NoneType'>`

### Class `ModelSpecificDecoratorFactory`

Factory for creating model-specific decorators.

This class provides methods for creating model-specific versions of decorators.

#### Methods

- `create_for_model(decorator_class, model_id, params) -> <class 'prompt_decorators.core.base.BaseDecorator'>`


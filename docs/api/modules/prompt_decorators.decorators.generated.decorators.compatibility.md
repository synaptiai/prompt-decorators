# Module `prompt_decorators.decorators.generated.decorators.compatibility`

Implementation of the Compatibility decorator.

This module provides the Compatibility decorator class for use in prompt engineering.

A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.

## Classes

- [`Compatibility`](#class-compatibility): A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.

### Class `Compatibility`

A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.

Attributes:
    models: List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.). (List[Any])
    fallback: Decorator to apply if the current model doesn't match any in the models list. (str)
    behaviors: JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}'). (str)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(models, fallback, behaviors) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `behaviors`: Get the behaviors parameter value.
- `fallback`: Get the fallback parameter value.
- `models`: Get the models parameter value.
- `name`: Get the name of the decorator.

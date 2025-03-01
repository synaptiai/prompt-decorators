# Module `prompt_decorators.decorators.generated.decorators.compatibility`

Compatibility Decorator

A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.

## Classes

- [`Compatibility`](#class-compatibility): A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.

### Class `Compatibility`

A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(models, fallback, behaviors)`
- `apply(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `get_version() -> <class 'prompt_decorators.core.base.Version'>`
- `is_compatible_with_version(version_str) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_json(indent) -> <class 'str'>`
- `validate() -> <class 'NoneType'>`
#### Properties

- `behaviors`: JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}')
- `fallback`: Decorator to apply if the current model doesn't match any in the models list
- `models`: List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.)


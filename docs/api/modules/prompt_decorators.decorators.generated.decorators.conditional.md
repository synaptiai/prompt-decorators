# Module `prompt_decorators.decorators.generated.decorators.conditional`

Conditional Decorator

A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.

## Classes

- [`Conditional`](#class-conditional): A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.

### Class `Conditional`

A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(if_param, then, else_param)`
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

- `else_param`: The decorator to apply if the condition is false (can be a specific decorator with parameters)
- `if_param`: The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}')
- `then`: The decorator to apply if the condition is true (can be a specific decorator with parameters)

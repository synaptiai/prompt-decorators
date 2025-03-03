# Module `prompt_decorators.decorators.generated.decorators.conditional`

Implementation of the Conditional decorator.

This module provides the Conditional decorator class for use in prompt engineering.

A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.

## Classes

- [`Conditional`](#class-conditional): A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.

### Class `Conditional`

A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.

Attributes:
    if_param: The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}'). (str)
    then: The decorator to apply if the condition is true (can be a specific decorator with parameters). (str)
    else_param: The decorator to apply if the condition is false (can be a specific decorator with parameters). (str)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(if_param, then, else_param) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `else_param`: Get the else_param parameter value.
- `if_param`: Get the if_param parameter value.
- `name`: Get the name of the decorator.
- `then`: Get the then parameter value.

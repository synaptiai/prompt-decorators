# Module `prompt_decorators.decorators.generated.decorators.override`

Implementation of the Override decorator.

This module provides the Override decorator class for use in prompt engineering.

A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.

## Classes

- [`Override`](#class-override): A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.

### Class `Override`

A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.

Attributes:
    decorator: The specific decorator whose behavior to override. (str)
    parameters: JSON string specifying the parameters to override (e.g., '{"depth": "comprehensive", "focus": "methodology"}'). (str)
    behavior: Optional custom behavior modification instructions that override the standard decorator interpretation. (str)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(decorator, parameters, behavior) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `behavior`: Get the behavior parameter value.
- `decorator`: Get the decorator parameter value.
- `name`: Get the name of the decorator.
- `params`: Get the parameters parameter value.

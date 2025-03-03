# Module `prompt_decorators.decorators.generated.decorators.priority`

Implementation of the Priority decorator.

This module provides the Priority decorator class for use in prompt engineering.

A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.

## Classes

- [`Priority`](#class-priority): A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.

### Class `Priority`

A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.

Attributes:
    decorators: Ordered list of decorators by priority (highest priority first). (List[Any])
    explicit: Whether to explicitly mention overridden behaviors in the response. (bool)
    mode: How to handle conflicts between decorators. (Literal["override", "merge", "cascade"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(decorators, explicit=False, mode=override) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `decorators`: Get the decorators parameter value.
- `explicit`: Get the explicit parameter value.
- `mode`: Get the mode parameter value.
- `name`: Get the name of the decorator.

# Module `prompt_decorators.decorators.generated.decorators.priority`

Priority Decorator

A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.

## Classes

- [`Priority`](#class-priority): A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.

### Class `Priority`

A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(decorators, explicit=False, mode=PriorityModeEnum.OVERRIDE)`
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

- `decorators`: Ordered list of decorators by priority (highest priority first)
- `explicit`: Whether to explicitly mention overridden behaviors in the response
- `mode`: How to handle conflicts between decorators


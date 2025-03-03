# Module `prompt_decorators.decorators.generated.decorators.override`

Override Decorator

A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.

## Classes

- [`Override`](#class-override): A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.

### Class `Override`

A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(decorator, parameters, behavior)`
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

- `behavior`: Optional custom behavior modification instructions that override the standard decorator interpretation
- `decorator`: The specific decorator whose behavior to override
- `parameters`: JSON string specifying the parameters to override (e.g., '{"depth": "comprehensive", "focus": "methodology"}')

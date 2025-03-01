# Module `prompt_decorators.decorators.generated.decorators.limitations`

Limitations Decorator

Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.

## Classes

- [`Limitations`](#class-limitations): Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.

### Class `Limitations`

Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(detail=LimitationsDetailEnum.MODERATE, position=LimitationsPositionEnum.END, focus=LimitationsFocusEnum.ALL)`
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

- `detail`: The level of detail in the limitations statement
- `focus`: The primary aspect to focus on in the limitations
- `position`: Where to place the limitations statement in the response


# Module `prompt_decorators.decorators.generated.decorators.limitations`

Implementation of the Limitations decorator.

This module provides the Limitations decorator class for use in prompt engineering.

Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.

## Classes

- [`Limitations`](#class-limitations): Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.

### Class `Limitations`

Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.

Attributes:
    detail: The level of detail in the limitations statement. (Literal["brief", "moderate", "comprehensive"])
    position: Where to place the limitations statement in the response. (Literal["beginning", "end"])
    focus: The primary aspect to focus on in the limitations. (Literal["knowledge", "methodology", "context", "biases", "all"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(detail=moderate, position=end, focus=all) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `detail`: Get the detail parameter value.
- `focus`: Get the focus parameter value.
- `name`: Get the name of the decorator.
- `position`: Get the position parameter value.

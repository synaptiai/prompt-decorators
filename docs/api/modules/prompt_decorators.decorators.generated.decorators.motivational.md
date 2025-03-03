# Module `prompt_decorators.decorators.generated.decorators.motivational`

Implementation of the Motivational decorator.

This module provides the Motivational decorator class for use in prompt engineering.

Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.

## Classes

- [`Motivational`](#class-motivational): Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.

### Class `Motivational`

Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.

Attributes:
    intensity: The level of motivational energy and enthusiasm. (Literal["mild", "moderate", "high"])
    focus: The primary motivational approach to emphasize. (Literal["achievement", "growth", "resilience", "purpose", "balanced"])
    actionable: Whether to include specific actionable steps or only inspirational content. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(intensity=moderate, focus=balanced, actionable=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `actionable`: Get the actionable parameter value.
- `focus`: Get the focus parameter value.
- `intensity`: Get the intensity parameter value.
- `name`: Get the name of the decorator.

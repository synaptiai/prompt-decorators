# Module `prompt_decorators.decorators.generated.decorators.motivational`

Motivational Decorator

Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.

## Classes

- [`Motivational`](#class-motivational): Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.

### Class `Motivational`

Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(intensity=MotivationalIntensityEnum.MODERATE, focus=MotivationalFocusEnum.BALANCED, actionable=True)`
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

- `actionable`: Whether to include specific actionable steps or only inspirational content
- `focus`: The primary motivational approach to emphasize
- `intensity`: The level of motivational energy and enthusiasm

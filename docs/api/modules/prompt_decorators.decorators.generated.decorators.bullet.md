# Module `prompt_decorators.decorators.generated.decorators.bullet`

Bullet Decorator

Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.

## Classes

- [`Bullet`](#class-bullet): Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.

### Class `Bullet`

Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(style=BulletStyleEnum.DASH, indented=True, compact=False)`
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

- `compact`: Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false)
- `indented`: Whether to allow nested, indented bullet points
- `style`: The visual marker used for bullet points


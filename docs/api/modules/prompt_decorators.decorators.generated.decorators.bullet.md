# Module `prompt_decorators.decorators.generated.decorators.bullet`

Implementation of the Bullet decorator.

This module provides the Bullet decorator class for use in prompt engineering.

Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.

## Classes

- [`Bullet`](#class-bullet): Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.

### Class `Bullet`

Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.

Attributes:
    style: The visual marker used for bullet points. (Literal["dash", "dot", "arrow", "star", "plus"])
    indented: Whether to allow nested, indented bullet points. (bool)
    compact: Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false). (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(style=dash, indented=True, compact=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `compact`: Get the compact parameter value.
- `indented`: Get the indented parameter value.
- `name`: Get the name of the decorator.
- `style`: Get the style parameter value.

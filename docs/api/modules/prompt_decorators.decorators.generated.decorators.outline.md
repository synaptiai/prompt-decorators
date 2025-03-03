# Module `prompt_decorators.decorators.generated.decorators.outline`

Implementation of the Outline decorator.

This module provides the Outline decorator class for use in prompt engineering.

Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.

## Classes

- [`Outline`](#class-outline): Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.

### Class `Outline`

Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.

Attributes:
    depth: Maximum nesting level of the outline. (Any)
    style: Numbering or bullet style for the outline. (Literal["numeric", "bullet", "roman", "alpha", "mixed"])
    detailed: Whether to include brief explanations under each outline point. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(depth=3, style=numeric, detailed=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `depth`: Get the depth parameter value.
- `detailed`: Get the detailed parameter value.
- `name`: Get the name of the decorator.
- `style`: Get the style parameter value.

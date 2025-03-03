# Module `prompt_decorators.decorators.generated.decorators.nested`

Implementation of the Nested decorator.

This module provides the Nested decorator class for use in prompt engineering.

Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.

## Classes

- [`Nested`](#class-nested): Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.

### Class `Nested`

Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.

Attributes:
    depth: Maximum nesting level of the hierarchy. (Any)
    style: Visual style for hierarchical levels. (Literal["bullet", "numbered", "mixed"])
    collapsible: Whether to suggest the hierarchy could be rendered as collapsible sections (for UI implementations). (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(depth=3, style=mixed, collapsible=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `collapsible`: Get the collapsible parameter value.
- `depth`: Get the depth parameter value.
- `name`: Get the name of the decorator.
- `style`: Get the style parameter value.

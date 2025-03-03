# Module `prompt_decorators.decorators.generated.decorators.nested`

Nested Decorator

Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.

## Classes

- [`Nested`](#class-nested): Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.

### Class `Nested`

Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(depth=3, style=NestedStyleEnum.MIXED, collapsible=False)`
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

- `collapsible`: Whether to suggest the hierarchy could be rendered as collapsible sections (for UI implementations)
- `depth`: Maximum nesting level of the hierarchy
- `style`: Visual style for hierarchical levels

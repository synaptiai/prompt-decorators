# Module `prompt_decorators.decorators.generated.decorators.comparison`

Implementation of the Comparison decorator.

This module provides the Comparison decorator class for use in prompt engineering.

Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.

## Classes

- [`Comparison`](#class-comparison): Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.

### Class `Comparison`

Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.

Attributes:
    aspects: Specific aspects or dimensions to compare. (List[Any])
    format: The presentation format for the comparison. (Literal["table", "prose", "bullets"])
    highlight: Whether to explicitly emphasize key differences. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(aspects, format=table, highlight=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `aspects`: Get the aspects parameter value.
- `format`: Get the format parameter value.
- `highlight`: Get the highlight parameter value.
- `name`: Get the name of the decorator.

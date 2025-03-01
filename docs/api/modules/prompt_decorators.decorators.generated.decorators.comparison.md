# Module `prompt_decorators.decorators.generated.decorators.comparison`

Comparison Decorator

Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.

## Classes

- [`Comparison`](#class-comparison): Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.

### Class `Comparison`

Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(aspects, format=ComparisonFormatEnum.TABLE, highlight=True)`
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

- `aspects`: Specific aspects or dimensions to compare
- `format`: The presentation format for the comparison
- `highlight`: Whether to explicitly emphasize key differences


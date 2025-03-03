# Module `prompt_decorators.decorators.generated.decorators.timeline`

Implementation of the Timeline decorator.

This module provides the Timeline decorator class for use in prompt engineering.

Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.

## Classes

- [`Timeline`](#class-timeline): Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.

### Class `Timeline`

Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.

Attributes:
    granularity: The level of time detail to include in the timeline. (Literal["day", "month", "year", "decade", "century", "era"])
    format: The presentation format for the timeline. (Literal["list", "narrative", "table"])
    details: The level of detail to include for each timeline event. (Literal["minimal", "moderate", "comprehensive"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(granularity=year, format=list, details=moderate) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `details`: Get the details parameter value.
- `format`: Get the format parameter value.
- `granularity`: Get the granularity parameter value.
- `name`: Get the name of the decorator.

# Module `prompt_decorators.decorators.generated.decorators.timeline`

Timeline Decorator

Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.

## Classes

- [`Timeline`](#class-timeline): Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.

### Class `Timeline`

Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(granularity=TimelineGranularityEnum.YEAR, format=TimelineFormatEnum.LIST, details=TimelineDetailsEnum.MODERATE)`
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

- `details`: The level of detail to include for each timeline event
- `format`: The presentation format for the timeline
- `granularity`: The level of time detail to include in the timeline


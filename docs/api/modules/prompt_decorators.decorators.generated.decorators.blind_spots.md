# Module `prompt_decorators.decorators.generated.decorators.blind_spots`

Implementation of the BlindSpots decorator.

This module provides the BlindSpots decorator class for use in prompt engineering.

Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.

## Classes

- [`BlindSpots`](#class-blindspots): Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.

### Class `BlindSpots`

Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.

Attributes:
    categories: Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias). (List[Any])
    depth: How thoroughly to analyze for blind spots. (Literal["basic", "thorough", "comprehensive"])
    position: Where to place the blind spots analysis. (Literal["after", "before", "integrated"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(categories, depth=thorough, position=after) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `categories`: Get the categories parameter value.
- `depth`: Get the depth parameter value.
- `name`: Get the name of the decorator.
- `position`: Get the position parameter value.

# Module `prompt_decorators.decorators.generated.decorators.blind_spots`

BlindSpots Decorator

Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.

## Classes

- [`BlindSpots`](#class-blindspots): Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.

### Class `BlindSpots`

Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(categories, depth=BlindSpotsDepthEnum.THOROUGH, position=BlindSpotsPositionEnum.AFTER)`
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

- `categories`: Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias)
- `depth`: How thoroughly to analyze for blind spots
- `position`: Where to place the blind spots analysis

# Module `prompt_decorators.decorators.generated.decorators.narrative`

Narrative Decorator

Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.

## Classes

- [`Narrative`](#class-narrative): Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.

### Class `Narrative`

Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(structure=NarrativeStructureEnum.CLASSIC, characters=True, length=NarrativeLengthEnum.MODERATE)`
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

- `characters`: Whether to include character elements in the narrative
- `length`: The relative length of the narrative
- `structure`: The narrative structure to employ


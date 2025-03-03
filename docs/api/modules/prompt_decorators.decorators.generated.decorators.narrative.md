# Module `prompt_decorators.decorators.generated.decorators.narrative`

Implementation of the Narrative decorator.

This module provides the Narrative decorator class for use in prompt engineering.

Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.

## Classes

- [`Narrative`](#class-narrative): Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.

### Class `Narrative`

Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.

Attributes:
    structure: The narrative structure to employ. (Literal["classic", "nonlinear", "case-study"])
    characters: Whether to include character elements in the narrative. (bool)
    length: The relative length of the narrative. (Literal["brief", "moderate", "extended"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(structure=classic, characters=True, length=moderate) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `characters`: Get the characters parameter value.
- `length`: Get the length parameter value.
- `name`: Get the name of the decorator.
- `structure`: Get the structure parameter value.

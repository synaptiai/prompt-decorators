# Module `prompt_decorators.decorators.generated.decorators.constraints`

Implementation of the Constraints decorator.

This module provides the Constraints decorator class for use in prompt engineering.

Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.

## Classes

- [`Constraints`](#class-constraints): Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.

### Class `Constraints`

Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.

Attributes:
    wordCount: Maximum number of words allowed in the response. (Any)
    timeframe: Maximum time required to implement or consume the response (e.g., '5min', '1hr', '1week'). (str)
    vocabulary: Constraints on vocabulary usage. (Literal["simple", "technical", "domain-specific", "creative"])
    custom: Custom constraint to apply (e.g., 'no negatives', 'use only questions', 'each sentence starts with consecutive letters of the alphabet'). (str)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(wordCount, timeframe, vocabulary, custom) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `custom`: Get the custom parameter value.
- `name`: Get the name of the decorator.
- `timeframe`: Get the timeframe parameter value.
- `vocabulary`: Get the vocabulary parameter value.
- `wordCount`: Get the wordCount parameter value.

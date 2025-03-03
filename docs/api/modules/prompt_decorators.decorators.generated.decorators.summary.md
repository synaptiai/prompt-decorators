# Module `prompt_decorators.decorators.generated.decorators.summary`

Implementation of the Summary decorator.

This module provides the Summary decorator class for use in prompt engineering.

Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.

## Classes

- [`Summary`](#class-summary): Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.

### Class `Summary`

Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.

Attributes:
    length: Relative length of the summary. (Literal["short", "medium", "long"])
    wordCount: Approximate target word count for the summary. (Any)
    position: Where to position the summary in relation to any full content. (Literal["beginning", "end", "standalone"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(length=medium, wordCount, position=standalone) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `length`: Get the length parameter value.
- `name`: Get the name of the decorator.
- `position`: Get the position parameter value.
- `wordCount`: Get the wordCount parameter value.

# Module `prompt_decorators.decorators.generated.decorators.summary`

Summary Decorator

Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.

## Classes

- [`Summary`](#class-summary): Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.

### Class `Summary`

Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(length=SummaryLengthEnum.MEDIUM, wordCount, position=SummaryPositionEnum.STANDALONE)`
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

- `length`: Relative length of the summary
- `position`: Where to position the summary in relation to any full content
- `wordCount`: Approximate target word count for the summary


# Module `prompt_decorators.decorators.generated.decorators.concise`

Implementation of the Concise decorator.

This module provides the Concise decorator class for use in prompt engineering.

Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.

## Classes

- [`Concise`](#class-concise): Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.

### Class `Concise`

Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.

Attributes:
    maxWords: Maximum word count for the entire response. (Any)
    bulletPoints: Whether to use bullet points for maximum brevity. (bool)
    level: The degree of conciseness to apply. (Literal["moderate", "high", "extreme"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(maxWords, bulletPoints=False, level=moderate) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `bulletPoints`: Get the bulletPoints parameter value.
- `level`: Get the level parameter value.
- `maxWords`: Get the maxWords parameter value.
- `name`: Get the name of the decorator.

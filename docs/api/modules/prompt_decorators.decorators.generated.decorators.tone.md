# Module `prompt_decorators.decorators.generated.decorators.tone`

Implementation of the Tone decorator.

This module provides the Tone decorator class for use in prompt engineering.

Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.

## Classes

- [`Tone`](#class-tone): Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.

### Class `Tone`

Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.

Attributes:
    style: The desired tone and style for the response. (Literal["formal", "casual", "friendly", "technical", "humorous"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(style) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `name`: Get the name of the decorator.
- `style`: Get the style parameter value.

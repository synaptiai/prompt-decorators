# Module `prompt_decorators.decorators.generated.decorators.output_format`

Implementation of the OutputFormat decorator.

This module provides the OutputFormat decorator class for use in prompt engineering.

Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way.

## Classes

- [`OutputFormat`](#class-outputformat): Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way.

### Class `OutputFormat`

Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way.

Attributes:
    format: The format to use for the response. (Literal["json", "markdown", "yaml", "xml", "plaintext"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(format) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `format`: Get the format parameter value.
- `name`: Get the name of the decorator.

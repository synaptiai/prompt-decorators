# Module `prompt_decorators.decorators.generated.decorators.schema`

Implementation of the Schema decorator.

This module provides the Schema decorator class for use in prompt engineering.

Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.

## Classes

- [`Schema`](#class-schema): Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.

### Class `Schema`

Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.

Attributes:
    schema: JSON Schema definition or reference to a predefined schema that defines the structure of the response. (str)
    strict: Whether to enforce strict schema compliance or allow flexibility. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(schema, strict=False) -> <class 'NoneType'>`
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
- `schema`: Get the schema parameter value.
- `strict`: Get the strict parameter value.

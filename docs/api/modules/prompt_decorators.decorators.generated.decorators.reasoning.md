# Module `prompt_decorators.decorators.generated.decorators.reasoning`

Implementation of the Reasoning decorator.

This module provides the Reasoning decorator class for use in prompt engineering.

Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy.

## Classes

- [`Reasoning`](#class-reasoning): Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy.

### Class `Reasoning`

Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy.

Attributes:
    depth: The level of detail in the reasoning process. (Literal["basic", "moderate", "comprehensive"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(depth=moderate) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `depth`: Get the depth parameter value.
- `name`: Get the name of the decorator.

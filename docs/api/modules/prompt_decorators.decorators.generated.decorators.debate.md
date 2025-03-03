# Module `prompt_decorators.decorators.generated.decorators.debate`

Implementation of the Debate decorator.

This module provides the Debate decorator class for use in prompt engineering.

Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.

## Classes

- [`Debate`](#class-debate): Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.

### Class `Debate`

Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.

Attributes:
    perspectives: Number of different perspectives to include in the debate. (Any)
    balanced: Whether to ensure equal representation and strength of arguments for each perspective. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(perspectives=2, balanced=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `balanced`: Get the balanced parameter value.
- `name`: Get the name of the decorator.
- `perspectives`: Get the perspectives parameter value.

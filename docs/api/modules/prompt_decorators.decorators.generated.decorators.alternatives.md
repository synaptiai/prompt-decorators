# Module `prompt_decorators.decorators.generated.decorators.alternatives`

Implementation of the Alternatives decorator.

This module provides the Alternatives decorator class for use in prompt engineering.

Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.

## Classes

- [`Alternatives`](#class-alternatives): Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.

### Class `Alternatives`

Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.

Attributes:
    count: Number of alternative options or approaches to generate. (Any)
    diversity: How different or varied the alternatives should be from each other. (Literal["low", "medium", "high"])
    comparison: Whether to include a comparative analysis of the alternatives. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(count=3, diversity=medium, comparison=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `comparison`: Get the comparison parameter value.
- `count`: Get the count parameter value.
- `diversity`: Get the diversity parameter value.
- `name`: Get the name of the decorator.

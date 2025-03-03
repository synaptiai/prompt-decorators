# Module `prompt_decorators.decorators.generated.decorators.balanced`

Implementation of the Balanced decorator.

This module provides the Balanced decorator class for use in prompt engineering.

Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.

## Classes

- [`Balanced`](#class-balanced): Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.

### Class `Balanced`

Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.

Attributes:
    perspectives: Number of different perspectives to include. (Any)
    structure: How to structure the different perspectives. (Literal["alternating", "sequential", "comparative"])
    equal: Whether to strictly enforce equal word count for each perspective. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(perspectives=2, structure=sequential, equal=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `equal`: Get the equal parameter value.
- `name`: Get the name of the decorator.
- `perspectives`: Get the perspectives parameter value.
- `structure`: Get the structure parameter value.

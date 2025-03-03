# Module `prompt_decorators.decorators.generated.decorators.steelman`

Implementation of the Steelman decorator.

This module provides the Steelman decorator class for use in prompt engineering.

Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.

## Classes

- [`Steelman`](#class-steelman): Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.

### Class `Steelman`

Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.

Attributes:
    sides: Number of different viewpoints to steel-man. (Any)
    critique: Whether to include critique after presenting the steel-manned arguments. (bool)
    separation: Whether to clearly separate the steel-manned presentations from any analysis. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(sides=2, critique=False, separation=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `critique`: Get the critique parameter value.
- `name`: Get the name of the decorator.
- `separation`: Get the separation parameter value.
- `sides`: Get the sides parameter value.

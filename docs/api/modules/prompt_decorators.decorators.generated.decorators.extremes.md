# Module `prompt_decorators.decorators.generated.decorators.extremes`

Implementation of the Extremes decorator.

This module provides the Extremes decorator class for use in prompt engineering.

Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.

## Classes

- [`Extremes`](#class-extremes): Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.

### Class `Extremes`

Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.

Attributes:
    versions: Which extreme versions to include. (Literal["radical", "minimal", "both"])
    dimension: The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity'). (str)
    compare: Whether to include a comparative analysis of the extreme versions. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(versions=both, dimension=ambition, compare=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `compare`: Get the compare parameter value.
- `dimension`: Get the dimension parameter value.
- `name`: Get the name of the decorator.
- `versions`: Get the versions parameter value.

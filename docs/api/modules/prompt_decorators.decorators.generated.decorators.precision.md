# Module `prompt_decorators.decorators.generated.decorators.precision`

Implementation of the Precision decorator.

This module provides the Precision decorator class for use in prompt engineering.

Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.

## Classes

- [`Precision`](#class-precision): Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.

### Class `Precision`

Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.

Attributes:
    level: The degree of precision to apply. (Literal["moderate", "high", "scientific"])
    units: Whether to consistently provide units for all measurements. (bool)
    definitions: Whether to include precise definitions for key terms. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(level=high, units=True, definitions=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `definitions`: Get the definitions parameter value.
- `level`: Get the level parameter value.
- `name`: Get the name of the decorator.
- `units`: Get the units parameter value.

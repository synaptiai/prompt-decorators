# Module `prompt_decorators.decorators.generated.decorators.version`

Implementation of the Version decorator.

This module provides the Version decorator class for use in prompt engineering.

Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.

## Classes

- [`Version`](#class-version): Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.

### Class `Version`

Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.

Attributes:
    standard: The semantic version of the Prompt Decorators standard to use. (str)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(standard) -> <class 'NoneType'>`
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
- `standard`: Get the standard parameter value.

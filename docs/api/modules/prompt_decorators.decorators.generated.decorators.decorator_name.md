# Module `prompt_decorators.decorators.generated.decorators.decorator_name`

Implementation of the DecoratorName decorator.

This module provides the DecoratorName decorator class for use in prompt engineering.

A detailed description of what the decorator does, its purpose, and how it modifies AI behavior.

## Classes

- [`DecoratorName`](#class-decoratorname): A detailed description of what the decorator does, its purpose, and

### Class `DecoratorName`

A detailed description of what the decorator does, its purpose, and
how it modifies AI behavior.

Attributes:
    parameterName: Description of what this parameter does

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(parameterName=defaultValue) -> <class 'NoneType'>`
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
- `parameterName`: Get the parameterName parameter value.

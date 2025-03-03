# Module `prompt_decorators.decorators.generated.decorators.custom`

Implementation of the Custom decorator.

This module provides the Custom decorator class for use in prompt engineering.

A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.

## Classes

- [`Custom`](#class-custom): A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.

### Class `Custom`

A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.

Attributes:
    rules: Explicit instructions defining the custom behavior (e.g., 'present all examples in a numbered list with exactly three items'). (str)
    name: Optional name for the custom decorator to reference in documentation or explanations. (str)
    priority: How to prioritize custom rules relative to other decorators. (Literal["override", "supplement", "fallback"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(rules, name, priority=override) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `name`: Get the name parameter value.
- `priority`: Get the priority parameter value.
- `rules`: Get the rules parameter value.

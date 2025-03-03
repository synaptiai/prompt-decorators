# Module `prompt_decorators.decorators.generated.decorators.eli5`

Implementation of the ELI5 decorator.

This module provides the ELI5 decorator class for use in prompt engineering.

Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.

## Classes

- [`ELI5`](#class-eli5): Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.

### Class `ELI5`

Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.

Attributes:
    strictness: Whether to strictly maintain a child-appropriate level of simplicity or allow slightly more complexity when necessary. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(strictness=False) -> <class 'NoneType'>`
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
- `strictness`: Get the strictness parameter value.

# Module `prompt_decorators.decorators.generated.decorators.as_expert`

Implementation of the AsExpert decorator.

This module provides the AsExpert decorator class for use in prompt engineering.

Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.

## Classes

- [`AsExpert`](#class-asexpert): Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.

### Class `AsExpert`

Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.

Attributes:
    domain: The specific field or discipline the expert specializes in. (str)
    experience: The experience level of the expert. (Literal["junior", "senior", "leading", "pioneering"])
    technical: Whether to use highly technical language and domain-specific terminology. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(domain, experience=senior, technical=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `domain`: Get the domain parameter value.
- `experience`: Get the experience parameter value.
- `name`: Get the name of the decorator.
- `technical`: Get the technical parameter value.

# Module `prompt_decorators.decorators.generated.decorators.professional`

Implementation of the Professional decorator.

This module provides the Professional decorator class for use in prompt engineering.

Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.

## Classes

- [`Professional`](#class-professional): Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.

### Class `Professional`

Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.

Attributes:
    industry: The specific industry context to adapt the language for. (str)
    formality: The level of formality to maintain in the response. (Literal["standard", "high", "executive"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(industry=general, formality=standard) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `formality`: Get the formality parameter value.
- `industry`: Get the industry parameter value.
- `name`: Get the name of the decorator.

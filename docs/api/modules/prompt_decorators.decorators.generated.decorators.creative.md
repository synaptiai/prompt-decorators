# Module `prompt_decorators.decorators.generated.decorators.creative`

Implementation of the Creative decorator.

This module provides the Creative decorator class for use in prompt engineering.

Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.

## Classes

- [`Creative`](#class-creative): Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.

### Class `Creative`

Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.

Attributes:
    level: The degree of creative thinking to apply. (Literal["moderate", "high", "unconventional"])
    elements: Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative). (List[Any])
    constraints: Optional creative constraints to work within. (List[Any])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(level=high, elements, constraints) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `constraints`: Get the constraints parameter value.
- `elements`: Get the elements parameter value.
- `level`: Get the level parameter value.
- `name`: Get the name of the decorator.

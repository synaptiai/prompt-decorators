# Module `prompt_decorators.decorators.generated.decorators.audience`

Implementation of the Audience decorator.

This module provides the Audience decorator class for use in prompt engineering.

Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.

## Classes

- [`Audience`](#class-audience): Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.

### Class `Audience`

Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.

Attributes:
    level: The expertise level of the target audience. (Literal["beginner", "intermediate", "expert", "technical"])
    domain: Specific knowledge domain or field for domain-specific terminology adaptation. (str)
    examples: Whether to include additional examples for clarity. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(level=intermediate, domain=general, examples=True) -> <class 'NoneType'>`
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
- `examples`: Get the examples parameter value.
- `level`: Get the level parameter value.
- `name`: Get the name of the decorator.

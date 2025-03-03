# Module `prompt_decorators.decorators.generated.decorators.context`

Implementation of the Context decorator.

This module provides the Context decorator class for use in prompt engineering.

A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.

## Classes

- [`Context`](#class-context): A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.

### Class `Context`

A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.

Attributes:
    domain: The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education'). (str)
    scope: Which aspects of decorators to contextualize. (Literal["terminology", "examples", "structure", "all"])
    level: The expertise level to target within the domain. (Literal["beginner", "intermediate", "expert", "mixed"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(domain, scope=all, level=mixed) -> <class 'NoneType'>`
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
- `level`: Get the level parameter value.
- `name`: Get the name of the decorator.
- `scope`: Get the scope parameter value.

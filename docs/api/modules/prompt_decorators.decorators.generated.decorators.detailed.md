# Module `prompt_decorators.decorators.generated.decorators.detailed`

Implementation of the Detailed decorator.

This module provides the Detailed decorator class for use in prompt engineering.

Enhances the response with comprehensive information, thorough explanations, and rich context. This decorator is ideal for in-depth learning, complex topics requiring nuance, or when completeness is valued over brevity.

## Classes

- [`Detailed`](#class-detailed): Enhances the response with comprehensive information, thorough explanations, and rich context. This decorator is ideal for in-depth learning, complex topics requiring nuance, or when completeness is valued over brevity.

### Class `Detailed`

Enhances the response with comprehensive information, thorough explanations, and rich context. This decorator is ideal for in-depth learning, complex topics requiring nuance, or when completeness is valued over brevity.

Attributes:
    depth: The level of detail and comprehensiveness. (Literal["moderate", "comprehensive", "exhaustive"])
    aspects: Specific aspects or dimensions to explore in detail. (List[Any])
    examples: Whether to include detailed examples to illustrate points. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(depth=comprehensive, aspects, examples=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `aspects`: Get the aspects parameter value.
- `depth`: Get the depth parameter value.
- `examples`: Get the examples parameter value.
- `name`: Get the name of the decorator.

# Module `prompt_decorators.decorators.generated.decorators.detailed`

Detailed Decorator

This module defines the Detailed decorator which enhances responses with comprehensive information.

## Classes

- [`Detailed`](#class-detailed): Enhances the response with comprehensive information, thorough explanations, and rich context.
- [`DetailedDepthEnum`](#class-detaileddepthenum): Enumeration of detail levels for the Detailed decorator.

### Class `Detailed`

Enhances the response with comprehensive information, thorough explanations, and rich context.

This decorator is ideal for in-depth learning, complex topics requiring nuance,
or when completeness is valued over brevity.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(depth=comprehensive, aspects, examples=True)`
- `apply(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `get_version() -> <class 'prompt_decorators.core.base.Version'>`
- `is_compatible_with_version(version_str) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_json(indent) -> <class 'str'>`
- `validate() -> <class 'NoneType'>`

### Class `DetailedDepthEnum`

Enumeration of detail levels for the Detailed decorator.

**Inherits from:** `Enum`

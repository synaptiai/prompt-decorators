# Module `prompt_decorators.decorators.generated.decorators.build_on`

Implementation of the BuildOn decorator.

This module provides the BuildOn decorator class for use in prompt engineering.

A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.

## Classes

- [`BuildOn`](#class-buildon): A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.

### Class `BuildOn`

A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.

Attributes:
    reference: What to build upon from the previous context. (Literal["last", "specific", "all"])
    approach: How to build upon the referenced content. (Literal["extend", "refine", "contrast", "synthesize"])
    preserveStructure: Whether to maintain the structure of the referenced content. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(reference=last, approach=extend, preserveStructure=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `approach`: Get the approach parameter value.
- `name`: Get the name of the decorator.
- `preserveStructure`: Get the preserveStructure parameter value.
- `reference`: Get the reference parameter value.

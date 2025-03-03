# Module `prompt_decorators.decorators.generated.decorators.inductive`

Implementation of the Inductive decorator.

This module provides the Inductive decorator class for use in prompt engineering.

Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.

## Classes

- [`Inductive`](#class-inductive): Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.

### Class `Inductive`

Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.

Attributes:
    examples: Number of specific examples or observations to include before generalizing. (Any)
    confidence: Whether to explicitly state the confidence level of the inductive conclusions. (bool)
    structure: The pattern of inductive reasoning to follow. (Literal["generalization", "causal", "statistical", "analogical"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(examples=3, confidence=False, structure=generalization) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `confidence`: Get the confidence parameter value.
- `examples`: Get the examples parameter value.
- `name`: Get the name of the decorator.
- `structure`: Get the structure parameter value.

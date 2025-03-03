# Module `prompt_decorators.decorators.generated.decorators.inductive`

Inductive Decorator

Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.

## Classes

- [`Inductive`](#class-inductive): Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.

### Class `Inductive`

Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(examples=3, confidence=False, structure=InductiveStructureEnum.GENERALIZATION)`
- `apply(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `get_version() -> <class 'prompt_decorators.core.base.Version'>`
- `is_compatible_with_version(version_str) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_json(indent) -> <class 'str'>`
- `validate() -> <class 'NoneType'>`
#### Properties

- `confidence`: Whether to explicitly state the confidence level of the inductive conclusions
- `examples`: Number of specific examples or observations to include before generalizing
- `structure`: The pattern of inductive reasoning to follow

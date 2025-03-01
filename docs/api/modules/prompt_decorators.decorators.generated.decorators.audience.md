# Module `prompt_decorators.decorators.generated.decorators.audience`

Audience Decorator

Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.

## Classes

- [`Audience`](#class-audience): Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.

### Class `Audience`

Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(level=AudienceLevelEnum.INTERMEDIATE, domain=general, examples=True)`
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

- `domain`: Specific knowledge domain or field for domain-specific terminology adaptation
- `examples`: Whether to include additional examples for clarity
- `level`: The expertise level of the target audience


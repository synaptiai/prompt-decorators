# Module `prompt_decorators.decorators.generated.decorators.context`

Context Decorator

A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.

## Classes

- [`Context`](#class-context): A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.

### Class `Context`

A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(domain, scope=ContextScopeEnum.ALL, level=ContextLevelEnum.MIXED)`
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

- `domain`: The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education')
- `level`: The expertise level to target within the domain
- `scope`: Which aspects of decorators to contextualize


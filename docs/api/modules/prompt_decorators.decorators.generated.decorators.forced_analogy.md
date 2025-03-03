# Module `prompt_decorators.decorators.generated.decorators.forced_analogy`

ForcedAnalogy Decorator

Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.

## Classes

- [`ForcedAnalogy`](#class-forcedanalogy): Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.

### Class `ForcedAnalogy`

Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(source, comprehensiveness=ForcedAnalogyComprehensivenessEnum.COMPREHENSIVE, mappings=3)`
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

- `comprehensiveness`: How comprehensively to map concepts between domains
- `mappings`: Number of distinct concept mappings to create between domains
- `source`: The specific domain, field, or context to draw analogies from

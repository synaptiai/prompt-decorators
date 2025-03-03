# Module `prompt_decorators.decorators.generated.decorators.build_on`

BuildOn Decorator

A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.

## Classes

- [`BuildOn`](#class-buildon): A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.

### Class `BuildOn`

A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(reference=BuildOnReferenceEnum.LAST, approach=BuildOnApproachEnum.EXTEND, preserveStructure=True)`
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

- `approach`: How to build upon the referenced content
- `preserveStructure`: Whether to maintain the structure of the referenced content
- `reference`: What to build upon from the previous context

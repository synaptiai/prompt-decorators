# Module `prompt_decorators.decorators.generated.decorators.creative`

Creative Decorator

Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.

## Classes

- [`Creative`](#class-creative): Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.

### Class `Creative`

Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(level=CreativeLevelEnum.HIGH, elements, constraints)`
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

- `constraints`: Optional creative constraints to work within
- `elements`: Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative)
- `level`: The degree of creative thinking to apply


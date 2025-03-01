# Module `prompt_decorators.decorators.generated.decorators.version`

Version Decorator

Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.

## Classes

- [`Version`](#class-version): Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.

### Class `Version`

Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(standard)`
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

- `standard`: The semantic version of the Prompt Decorators standard to use


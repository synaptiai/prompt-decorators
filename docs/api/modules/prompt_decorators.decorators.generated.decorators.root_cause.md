# Module `prompt_decorators.decorators.generated.decorators.root_cause`

RootCause Decorator

Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.

## Classes

- [`RootCause`](#class-rootcause): Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.

### Class `RootCause`

Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(method=RootCauseMethodEnum.VALUE_5WHYS, depth=5)`
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

- `depth`: Level of detail in the analysis (for 5whys, represents number of 'why' iterations)
- `method`: The specific root cause analysis methodology to apply


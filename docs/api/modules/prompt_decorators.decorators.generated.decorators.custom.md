# Module `prompt_decorators.decorators.generated.decorators.custom`

Custom Decorator

A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.

## Classes

- [`Custom`](#class-custom): A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.

### Class `Custom`

A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(rules, name, priority=CustomPriorityEnum.OVERRIDE)`
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

- `name`: Optional name for the custom decorator to reference in documentation or explanations
- `priority`: How to prioritize custom rules relative to other decorators
- `rules`: Explicit instructions defining the custom behavior (e.g., 'present all examples in a numbered list with exactly three items')


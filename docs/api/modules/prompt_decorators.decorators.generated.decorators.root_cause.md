# Module `prompt_decorators.decorators.generated.decorators.root_cause`

Implementation of the RootCause decorator.

This module provides the RootCause decorator class for use in prompt engineering.

Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.

## Classes

- [`RootCause`](#class-rootcause): Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.

### Class `RootCause`

Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.

Attributes:
    method: The specific root cause analysis methodology to apply. (Literal["fivewhys", "fishbone", "pareto"])
    depth: Level of detail in the analysis (for fivewhys, represents number of 'why' iterations). (Any)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(method=fivewhys, depth=5) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `depth`: Get the depth parameter value.
- `method`: Get the method parameter value.
- `name`: Get the name of the decorator.

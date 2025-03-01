# Module `prompt_decorators.decorators.generated.decorators.debate`

Debate Decorator

Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.

## Classes

- [`Debate`](#class-debate): Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.

### Class `Debate`

Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(perspectives=2, balanced=True)`
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

- `balanced`: Whether to ensure equal representation and strength of arguments for each perspective
- `perspectives`: Number of different perspectives to include in the debate


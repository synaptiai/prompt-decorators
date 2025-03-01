# Module `prompt_decorators.decorators.generated.decorators.alternatives`

Alternatives Decorator

Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.

## Classes

- [`Alternatives`](#class-alternatives): Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.

### Class `Alternatives`

Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(count=3, diversity=AlternativesDiversityEnum.MEDIUM, comparison=False)`
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

- `comparison`: Whether to include a comparative analysis of the alternatives
- `count`: Number of alternative options or approaches to generate
- `diversity`: How different or varied the alternatives should be from each other


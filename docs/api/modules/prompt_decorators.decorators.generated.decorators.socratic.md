# Module `prompt_decorators.decorators.generated.decorators.socratic`

Socratic Decorator

Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.

## Classes

- [`Socratic`](#class-socratic): Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.

### Class `Socratic`

Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(iterations=3)`
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

- `iterations`: Number of question-answer cycles to include


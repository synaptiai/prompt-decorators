# Module `prompt_decorators.decorators.generated.decorators.step_by_step`

StepByStep Decorator

Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.

## Classes

- [`StepByStep`](#class-stepbystep): Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.

### Class `StepByStep`

Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(numbered=True)`
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

- `numbered`: Whether to number the steps or use bullet points


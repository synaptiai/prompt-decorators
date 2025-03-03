# Module `prompt_decorators.decorators.generated.decorators.step_by_step`

Implementation of the StepByStep decorator.

This module provides the StepByStep decorator class for use in prompt engineering.

Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.

## Classes

- [`StepByStep`](#class-stepbystep): Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.

### Class `StepByStep`

Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.

Attributes:
    numbered: Whether to number the steps or use bullet points. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(numbered=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `name`: Get the name of the decorator.
- `numbered`: Get the numbered parameter value.

# Module `prompt_decorators.decorators.generated.decorators.socratic`

Implementation of the Socratic decorator.

This module provides the Socratic decorator class for use in prompt engineering.

Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.

## Classes

- [`Socratic`](#class-socratic): Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.

### Class `Socratic`

Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.

Attributes:
    iterations: Number of question-answer cycles to include. (Any)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(iterations=3) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `iterations`: Get the iterations parameter value.
- `name`: Get the name of the decorator.

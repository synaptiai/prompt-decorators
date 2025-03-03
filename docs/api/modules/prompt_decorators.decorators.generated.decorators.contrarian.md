# Module `prompt_decorators.decorators.generated.decorators.contrarian`

Implementation of the Contrarian decorator.

This module provides the Contrarian decorator class for use in prompt engineering.

Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.

## Classes

- [`Contrarian`](#class-contrarian): Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.

### Class `Contrarian`

Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.

Attributes:
    approach: The specific contrarian approach to take. (Literal["outsider", "skeptic", "devils-advocate"])
    maintain: Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false). (bool)
    focus: Optional specific aspect of the topic to focus contrarian analysis on. (str)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(approach=devils-advocate, maintain=False, focus) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `approach`: Get the approach parameter value.
- `focus`: Get the focus parameter value.
- `maintain`: Get the maintain parameter value.
- `name`: Get the name of the decorator.

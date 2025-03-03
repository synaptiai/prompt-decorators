# Module `prompt_decorators.decorators.generated.decorators.remix`

Implementation of the Remix decorator.

This module provides the Remix decorator class for use in prompt engineering.

Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.

## Classes

- [`Remix`](#class-remix): Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.

### Class `Remix`

Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.

Attributes:
    target: The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch'). (str)
    preserve: What aspects of the original content to prioritize preserving. (Literal["facts", "structure", "tone", "comprehensiveness"])
    contrast: Whether to highlight differences between the original framing and the remixed version. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(target, preserve=facts, contrast=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `contrast`: Get the contrast parameter value.
- `name`: Get the name of the decorator.
- `preserve`: Get the preserve parameter value.
- `target`: Get the target parameter value.

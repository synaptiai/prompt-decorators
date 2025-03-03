# Module `prompt_decorators.decorators.generated.decorators.style_shift`

Implementation of the StyleShift decorator.

This module provides the StyleShift decorator class for use in prompt engineering.

Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.

## Classes

- [`StyleShift`](#class-styleshift): Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.

### Class `StyleShift`

Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.

Attributes:
    aspect: The specific style aspect to modify. (Literal["formality", "persuasion", "urgency", "confidence", "complexity"])
    level: The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal). (Any)
    maintain: Style aspects to explicitly maintain while modifying the target aspect. (List[Any])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(aspect, level=3, maintain) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `aspect`: Get the aspect parameter value.
- `level`: Get the level parameter value.
- `maintain`: Get the maintain parameter value.
- `name`: Get the name of the decorator.

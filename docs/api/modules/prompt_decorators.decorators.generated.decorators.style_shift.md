# Module `prompt_decorators.decorators.generated.decorators.style_shift`

StyleShift Decorator

Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.

## Classes

- [`StyleShift`](#class-styleshift): Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.

### Class `StyleShift`

Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(aspect, level=3, maintain)`
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

- `aspect`: The specific style aspect to modify
- `level`: The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal)
- `maintain`: Style aspects to explicitly maintain while modifying the target aspect


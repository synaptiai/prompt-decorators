# Module `prompt_decorators.decorators.generated.decorators.layered`

Implementation of the Layered decorator.

This module provides the Layered decorator class for use in prompt engineering.

Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.

## Classes

- [`Layered`](#class-layered): Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.

### Class `Layered`

Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.

Attributes:
    levels: The granularity of explanation levels to include. (Literal["sentence-paragraph-full", "basic-intermediate-advanced", "summary-detail-technical"])
    count: Number of distinct explanation layers to provide. (Any)
    progression: How to structure the progression between layers. (Literal["separate", "nested", "incremental"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(levels=summary-detail-technical, count=3, progression=separate) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `count`: Get the count parameter value.
- `levels`: Get the levels parameter value.
- `name`: Get the name of the decorator.
- `progression`: Get the progression parameter value.

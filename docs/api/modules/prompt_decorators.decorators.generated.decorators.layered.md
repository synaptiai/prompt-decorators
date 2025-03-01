# Module `prompt_decorators.decorators.generated.decorators.layered`

Layered Decorator

Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.

## Classes

- [`Layered`](#class-layered): Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.

### Class `Layered`

Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(levels=LayeredLevelsEnum.SUMMARY_DETAIL_TECHNICAL, count=3, progression=LayeredProgressionEnum.SEPARATE)`
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

- `count`: Number of distinct explanation layers to provide
- `levels`: The granularity of explanation levels to include
- `progression`: How to structure the progression between layers


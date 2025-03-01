# Module `prompt_decorators.decorators.generated.decorators.prioritize`

Prioritize Decorator

Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.

## Classes

- [`Prioritize`](#class-prioritize): Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.

### Class `Prioritize`

Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(criteria=importance, count=5, showRationale=False)`
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

- `count`: Number of prioritized items to include
- `criteria`: The specific criterion to use for prioritization (e.g., importance, urgency, ROI)
- `showRationale`: Whether to explain the reasoning behind each priority ranking


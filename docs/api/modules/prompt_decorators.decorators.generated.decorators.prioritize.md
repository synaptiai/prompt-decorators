# Module `prompt_decorators.decorators.generated.decorators.prioritize`

Implementation of the Prioritize decorator.

This module provides the Prioritize decorator class for use in prompt engineering.

Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.

## Classes

- [`Prioritize`](#class-prioritize): Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.

### Class `Prioritize`

Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.

Attributes:
    criteria: The specific criterion to use for prioritization (e.g., importance, urgency, ROI). (str)
    count: Number of prioritized items to include. (Any)
    showRationale: Whether to explain the reasoning behind each priority ranking. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(criteria=importance, count=5, showRationale=False) -> <class 'NoneType'>`
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
- `criteria`: Get the criteria parameter value.
- `name`: Get the name of the decorator.
- `showRationale`: Get the showRationale parameter value.

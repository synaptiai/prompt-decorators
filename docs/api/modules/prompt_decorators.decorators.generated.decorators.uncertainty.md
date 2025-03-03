# Module `prompt_decorators.decorators.generated.decorators.uncertainty`

Implementation of the Uncertainty decorator.

This module provides the Uncertainty decorator class for use in prompt engineering.

Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.

## Classes

- [`Uncertainty`](#class-uncertainty): Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.

### Class `Uncertainty`

Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.

Attributes:
    format: How to format uncertainty indications in the response. (Literal["inline", "section", "confidence"])
    threshold: The threshold for flagging uncertain content. (Literal["low", "medium", "high"])
    reason: Whether to explain the reason for uncertainty. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(format=inline, threshold=medium, reason=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `format`: Get the format parameter value.
- `name`: Get the name of the decorator.
- `reason`: Get the reason parameter value.
- `threshold`: Get the threshold parameter value.

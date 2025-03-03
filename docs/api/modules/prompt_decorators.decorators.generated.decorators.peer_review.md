# Module `prompt_decorators.decorators.generated.decorators.peer_review`

Implementation of the PeerReview decorator.

This module provides the PeerReview decorator class for use in prompt engineering.

Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.

## Classes

- [`PeerReview`](#class-peerreview): Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.

### Class `PeerReview`

Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.

Attributes:
    criteria: Primary criteria to focus on in the review. (Literal["accuracy", "methodology", "limitations", "completeness", "all"])
    style: The tone and approach of the peer review. (Literal["constructive", "critical", "balanced"])
    position: Where to place the peer review relative to the main content. (Literal["after", "before", "alongside"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(criteria=all, style=balanced, position=after) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `criteria`: Get the criteria parameter value.
- `name`: Get the name of the decorator.
- `position`: Get the position parameter value.
- `style`: Get the style parameter value.

# Module `prompt_decorators.decorators.generated.decorators.peer_review`

PeerReview Decorator

Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.

## Classes

- [`PeerReview`](#class-peerreview): Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.

### Class `PeerReview`

Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(criteria=PeerReviewCriteriaEnum.ALL, style=PeerReviewStyleEnum.BALANCED, position=PeerReviewPositionEnum.AFTER)`
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

- `criteria`: Primary criteria to focus on in the review
- `position`: Where to place the peer review relative to the main content
- `style`: The tone and approach of the peer review


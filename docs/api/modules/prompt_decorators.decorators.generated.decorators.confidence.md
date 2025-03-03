# Module `prompt_decorators.decorators.generated.decorators.confidence`

Implementation of the Confidence decorator.

This module provides the Confidence decorator class for use in prompt engineering.

Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.

## Classes

- [`Confidence`](#class-confidence): Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.

### Class `Confidence`

Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.

Attributes:
    scale: The method used to express confidence levels. (Literal["percent", "qualitative", "stars", "numeric"])
    threshold: Minimum confidence level for including information (as a percentage). (Any)
    detailed: Whether to provide explanations for confidence assessments. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(scale=qualitative, threshold=50, detailed=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `detailed`: Get the detailed parameter value.
- `name`: Get the name of the decorator.
- `scale`: Get the scale parameter value.
- `threshold`: Get the threshold parameter value.

# Module `prompt_decorators.decorators.generated.decorators.confidence`

Confidence Decorator

Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.

## Classes

- [`Confidence`](#class-confidence): Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.

### Class `Confidence`

Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(scale=ConfidenceScaleEnum.QUALITATIVE, threshold=50, detailed=False)`
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

- `detailed`: Whether to provide explanations for confidence assessments
- `scale`: The method used to express confidence levels
- `threshold`: Minimum confidence level for including information (as a percentage)


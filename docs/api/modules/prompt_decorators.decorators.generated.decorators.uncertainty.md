# Module `prompt_decorators.decorators.generated.decorators.uncertainty`

Uncertainty Decorator

Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.

## Classes

- [`Uncertainty`](#class-uncertainty): Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.

### Class `Uncertainty`

Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(format=UncertaintyFormatEnum.INLINE, threshold=UncertaintyThresholdEnum.MEDIUM, reason=False)`
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

- `format`: How to format uncertainty indications in the response
- `reason`: Whether to explain the reason for uncertainty
- `threshold`: The threshold for flagging uncertain content

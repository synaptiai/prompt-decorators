# Module `prompt_decorators.decorators.generated.decorators.fact_check`

FactCheck Decorator

Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.

## Classes

- [`FactCheck`](#class-factcheck): Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.

### Class `FactCheck`

Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(confidence=True, uncertain=FactCheckUncertainEnum.MARK, strictness=FactCheckStrictnessEnum.MODERATE)`
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

- `confidence`: Whether to include explicit confidence levels for claims
- `strictness`: The threshold for considering information verified
- `uncertain`: How to handle uncertain information


# Module `prompt_decorators.decorators.generated.decorators.fact_check`

Implementation of the FactCheck decorator.

This module provides the FactCheck decorator class for use in prompt engineering.

Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.

## Classes

- [`FactCheck`](#class-factcheck): Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.

### Class `FactCheck`

Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.

Attributes:
    confidence: Whether to include explicit confidence levels for claims. (bool)
    uncertain: How to handle uncertain information. (Literal["mark", "exclude", "qualify"])
    strictness: The threshold for considering information verified. (Literal["low", "moderate", "high"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(confidence=True, uncertain=mark, strictness=moderate) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `confidence`: Get the confidence parameter value.
- `name`: Get the name of the decorator.
- `strictness`: Get the strictness parameter value.
- `uncertain`: Get the uncertain parameter value.

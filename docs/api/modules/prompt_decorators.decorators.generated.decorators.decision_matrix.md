# Module `prompt_decorators.decorators.generated.decorators.decision_matrix`

Implementation of the DecisionMatrix decorator.

This module provides the DecisionMatrix decorator class for use in prompt engineering.

Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.

## Classes

- [`DecisionMatrix`](#class-decisionmatrix): Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.

### Class `DecisionMatrix`

Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.

Attributes:
    options: Specific options or alternatives to evaluate in the matrix. (List[Any])
    criteria: Evaluation criteria to assess each option against. (List[Any])
    weighted: Whether to include weights for criteria importance. (bool)
    scale: Rating scale to use for evaluations. (Literal["1-5", "1-10", "qualitative", "percentage"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(options, criteria, weighted=False, scale=1-5) -> <class 'NoneType'>`
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
- `options`: Get the options parameter value.
- `scale`: Get the scale parameter value.
- `weighted`: Get the weighted parameter value.

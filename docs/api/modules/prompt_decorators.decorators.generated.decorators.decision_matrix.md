# Module `prompt_decorators.decorators.generated.decorators.decision_matrix`

DecisionMatrix Decorator

Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.

## Classes

- [`DecisionMatrix`](#class-decisionmatrix): Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.

### Class `DecisionMatrix`

Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(options, criteria, weighted=False, scale=DecisionMatrixScaleEnum.VALUE_1_5)`
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

- `criteria`: Evaluation criteria to assess each option against
- `options`: Specific options or alternatives to evaluate in the matrix
- `scale`: Rating scale to use for evaluations
- `weighted`: Whether to include weights for criteria importance

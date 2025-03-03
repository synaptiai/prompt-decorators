# Module `prompt_decorators.decorators.generated.decorators.abductive`

Abductive Decorator

Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.

## Classes

- [`Abductive`](#class-abductive): Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.

### Class `Abductive`

Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(hypotheses=3, criteria, rank=True)`
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

- `criteria`: Specific criteria to evaluate hypotheses against (e.g., simplicity, explanatory power)
- `hypotheses`: Number of alternative hypotheses or explanations to generate
- `rank`: Whether to explicitly rank hypotheses by likelihood

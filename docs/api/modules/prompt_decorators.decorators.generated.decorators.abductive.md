# Module `prompt_decorators.decorators.generated.decorators.abductive`

Implementation of the Abductive decorator.

This module provides the Abductive decorator class for use in prompt engineering.

Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.

## Classes

- [`Abductive`](#class-abductive): Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.

### Class `Abductive`

Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.

Attributes:
    hypotheses: Number of alternative hypotheses or explanations to generate. (Any)
    criteria: Specific criteria to evaluate hypotheses against (e.g., simplicity, explanatory power). (List[Any])
    rank: Whether to explicitly rank hypotheses by likelihood. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(hypotheses=3, criteria, rank=True) -> <class 'NoneType'>`
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
- `hypotheses`: Get the hypotheses parameter value.
- `name`: Get the name of the decorator.
- `rank`: Get the rank parameter value.

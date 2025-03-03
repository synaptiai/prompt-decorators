# Module `prompt_decorators.decorators.generated.decorators.break_and_build`

Implementation of the BreakAndBuild decorator.

This module provides the BreakAndBuild decorator class for use in prompt engineering.

Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.

## Classes

- [`BreakAndBuild`](#class-breakandbuild): Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.

### Class `BreakAndBuild`

Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.

Attributes:
    breakdown: Primary approach for the critical breakdown phase. (Literal["weaknesses", "assumptions", "risks", "comprehensive"])
    intensity: How thorough and challenging the breakdown phase should be. (Literal["mild", "thorough", "intense"])
    buildRatio: Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique). (Any)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(breakdown=comprehensive, intensity=thorough, buildRatio=1) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `breakdown`: Get the breakdown parameter value.
- `buildRatio`: Get the buildRatio parameter value.
- `intensity`: Get the intensity parameter value.
- `name`: Get the name of the decorator.

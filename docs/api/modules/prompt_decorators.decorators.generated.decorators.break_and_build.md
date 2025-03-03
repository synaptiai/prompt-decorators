# Module `prompt_decorators.decorators.generated.decorators.break_and_build`

BreakAndBuild Decorator

Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.

## Classes

- [`BreakAndBuild`](#class-breakandbuild): Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.

### Class `BreakAndBuild`

Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(breakdown=BreakAndBuildBreakdownEnum.COMPREHENSIVE, intensity=BreakAndBuildIntensityEnum.THOROUGH, buildRatio=1)`
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

- `breakdown`: Primary approach for the critical breakdown phase
- `buildRatio`: Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique)
- `intensity`: How thorough and challenging the breakdown phase should be

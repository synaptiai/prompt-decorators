# Module `prompt_decorators.decorators.generated.decorators.find_gaps`

FindGaps Decorator

Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.

## Classes

- [`FindGaps`](#class-findgaps): Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.

### Class `FindGaps`

Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(aspects=FindGapsAspectsEnum.COMPREHENSIVE, depth=FindGapsDepthEnum.THOROUGH, solutions=True)`
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

- `aspects`: The specific types of gaps to focus on finding
- `depth`: How thoroughly to analyze for gaps
- `solutions`: Whether to suggest solutions or approaches for addressing the identified gaps


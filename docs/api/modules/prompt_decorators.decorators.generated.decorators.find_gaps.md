# Module `prompt_decorators.decorators.generated.decorators.find_gaps`

Implementation of the FindGaps decorator.

This module provides the FindGaps decorator class for use in prompt engineering.

Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.

## Classes

- [`FindGaps`](#class-findgaps): Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.

### Class `FindGaps`

Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.

Attributes:
    aspects: The specific types of gaps to focus on finding. (Literal["questions", "resources", "stakeholders", "risks", "dependencies", "comprehensive"])
    depth: How thoroughly to analyze for gaps. (Literal["basic", "thorough", "exhaustive"])
    solutions: Whether to suggest solutions or approaches for addressing the identified gaps. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(aspects=comprehensive, depth=thorough, solutions=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `aspects`: Get the aspects parameter value.
- `depth`: Get the depth parameter value.
- `name`: Get the name of the decorator.
- `solutions`: Get the solutions parameter value.

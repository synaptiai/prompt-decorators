# Module `prompt_decorators.decorators.generated.decorators.negative_space`

Implementation of the NegativeSpace decorator.

This module provides the NegativeSpace decorator class for use in prompt engineering.

Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.

## Classes

- [`NegativeSpace`](#class-negativespace): Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.

### Class `NegativeSpace`

Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.

Attributes:
    focus: The specific aspect of negative space to emphasize. (Literal["implications", "missing", "unstated", "comprehensive"])
    depth: How deeply to explore the negative space. (Literal["surface", "moderate", "deep"])
    structure: How to present the negative space analysis. (Literal["before", "after", "integrated", "separate"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(focus=comprehensive, depth=moderate, structure=integrated) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `depth`: Get the depth parameter value.
- `focus`: Get the focus parameter value.
- `name`: Get the name of the decorator.
- `structure`: Get the structure parameter value.

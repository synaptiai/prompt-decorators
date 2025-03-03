# Module `prompt_decorators.decorators.generated.decorators.negative_space`

NegativeSpace Decorator

Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.

## Classes

- [`NegativeSpace`](#class-negativespace): Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.

### Class `NegativeSpace`

Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(focus=NegativeSpaceFocusEnum.COMPREHENSIVE, depth=NegativeSpaceDepthEnum.MODERATE, structure=NegativeSpaceStructureEnum.INTEGRATED)`
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

- `depth`: How deeply to explore the negative space
- `focus`: The specific aspect of negative space to emphasize
- `structure`: How to present the negative space analysis

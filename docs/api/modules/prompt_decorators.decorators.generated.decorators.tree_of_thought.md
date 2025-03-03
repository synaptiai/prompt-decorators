# Module `prompt_decorators.decorators.generated.decorators.tree_of_thought`

Implementation of the TreeOfThought decorator.

This module provides the TreeOfThought decorator class for use in prompt engineering.

Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.

## Classes

- [`TreeOfThought`](#class-treeofthought): Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.

### Class `TreeOfThought`

Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.

Attributes:
    branches: Number of different reasoning branches to explore. (Any)
    depth: Maximum depth of reasoning in each branch. (Any)
    pruning: Whether to eliminate less promising branches early. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(branches=3, depth=3, pruning=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `branches`: Get the branches parameter value.
- `depth`: Get the depth parameter value.
- `name`: Get the name of the decorator.
- `pruning`: Get the pruning parameter value.

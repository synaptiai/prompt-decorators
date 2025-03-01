# Module `prompt_decorators.decorators.generated.decorators.tree_of_thought`

TreeOfThought Decorator

Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.

## Classes

- [`TreeOfThought`](#class-treeofthought): Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.

### Class `TreeOfThought`

Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(branches=3, depth=3, pruning=False)`
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

- `branches`: Number of different reasoning branches to explore
- `depth`: Maximum depth of reasoning in each branch
- `pruning`: Whether to eliminate less promising branches early


# Module `prompt_decorators.decorators.generated.decorators.analogical`

Implementation of the Analogical decorator.

This module provides the Analogical decorator class for use in prompt engineering.

Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.

## Classes

- [`Analogical`](#class-analogical): Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.

### Class `Analogical`

Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.

Attributes:
    domain: Specific domain or context to draw analogies from (if not specified, will choose appropriate domains). (str)
    count: Number of distinct analogies to provide. (Any)
    depth: Level of detail in developing the analogy. (Literal["brief", "moderate", "extended"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(domain=general, count=1, depth=moderate) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `count`: Get the count parameter value.
- `depth`: Get the depth parameter value.
- `domain`: Get the domain parameter value.
- `name`: Get the name of the decorator.

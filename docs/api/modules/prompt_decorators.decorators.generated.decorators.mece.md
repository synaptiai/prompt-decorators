# Module `prompt_decorators.decorators.generated.decorators.mece`

Implementation of the MECE decorator.

This module provides the MECE decorator class for use in prompt engineering.

Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.

## Classes

- [`MECE`](#class-mece): Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.

### Class `MECE`

Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.

Attributes:
    dimensions: Number of top-level MECE dimensions to use for categorization. (Any)
    depth: Maximum level of hierarchical breakdown within each dimension. (Any)
    framework: Optional predefined MECE framework to apply. (Literal["issue tree", "value chain", "business segments", "stakeholders", "custom"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(dimensions=3, depth=2, framework=custom) -> <class 'NoneType'>`
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
- `dimensions`: Get the dimensions parameter value.
- `framework`: Get the framework parameter value.
- `name`: Get the name of the decorator.

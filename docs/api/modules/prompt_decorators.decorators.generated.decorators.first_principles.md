# Module `prompt_decorators.decorators.generated.decorators.first_principles`

Implementation of the FirstPrinciples decorator.

This module provides the FirstPrinciples decorator class for use in prompt engineering.

Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.

## Classes

- [`FirstPrinciples`](#class-firstprinciples): Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.

### Class `FirstPrinciples`

Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.

Attributes:
    depth: Level of detail in breaking down to fundamental principles. (Any)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(depth=3) -> <class 'NoneType'>`
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
- `name`: Get the name of the decorator.

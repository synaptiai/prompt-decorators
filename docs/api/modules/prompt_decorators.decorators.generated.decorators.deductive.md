# Module `prompt_decorators.decorators.generated.decorators.deductive`

Implementation of the Deductive decorator.

This module provides the Deductive decorator class for use in prompt engineering.

Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.

## Classes

- [`Deductive`](#class-deductive): Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.

### Class `Deductive`

Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.

Attributes:
    premises: Number of main premises to include before deducing conclusions. (Any)
    formal: Whether to use formal logical structures with explicit syllogisms. (bool)
    steps: Number of logical steps to include in the deductive process. (Any)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(premises=2, formal=False, steps=3) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `formal`: Get the formal parameter value.
- `name`: Get the name of the decorator.
- `premises`: Get the premises parameter value.
- `steps`: Get the steps parameter value.

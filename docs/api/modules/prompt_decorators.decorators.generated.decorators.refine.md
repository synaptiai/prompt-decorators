# Module `prompt_decorators.decorators.generated.decorators.refine`

Implementation of the Refine decorator.

This module provides the Refine decorator class for use in prompt engineering.

A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.

## Classes

- [`Refine`](#class-refine): A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.

### Class `Refine`

A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.

Attributes:
    iterations: Number of refinement cycles to perform. (Any)
    focus: Specific aspects to focus on during refinement (e.g., clarity, conciseness, evidence). (List[Any])
    showProcess: Whether to show the intermediate steps in the refinement process. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(iterations=2, focus, showProcess=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `focus`: Get the focus parameter value.
- `iterations`: Get the iterations parameter value.
- `name`: Get the name of the decorator.
- `showProcess`: Get the showProcess parameter value.

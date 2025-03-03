# Module `prompt_decorators.decorators.generated.decorators.chain`

Implementation of the Chain decorator.

This module provides the Chain decorator class for use in prompt engineering.

A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.

## Classes

- [`Chain`](#class-chain): A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.

### Class `Chain`

A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.

Attributes:
    decorators: Ordered list of decorators to apply in sequence. (List[Any])
    showSteps: Whether to show intermediate outputs after each decorator in the chain. (bool)
    stopOnFailure: Whether to stop the chain if a decorator fails to apply correctly. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(decorators, showSteps=False, stopOnFailure=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `decorators`: Get the decorators parameter value.
- `name`: Get the name of the decorator.
- `showSteps`: Get the showSteps parameter value.
- `stopOnFailure`: Get the stopOnFailure parameter value.

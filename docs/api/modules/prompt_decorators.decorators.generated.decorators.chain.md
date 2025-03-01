# Module `prompt_decorators.decorators.generated.decorators.chain`

Chain Decorator

A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.

## Classes

- [`Chain`](#class-chain): A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.

### Class `Chain`

A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(decorators, showSteps=False, stopOnFailure=True)`
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

- `decorators`: Ordered list of decorators to apply in sequence
- `showSteps`: Whether to show intermediate outputs after each decorator in the chain
- `stopOnFailure`: Whether to stop the chain if a decorator fails to apply correctly


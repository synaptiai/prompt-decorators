# Module `prompt_decorators.decorators.generated.decorators.deductive`

Deductive Decorator

Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.

## Classes

- [`Deductive`](#class-deductive): Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.

### Class `Deductive`

Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(premises=2, formal=False, steps=3)`
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

- `formal`: Whether to use formal logical structures with explicit syllogisms
- `premises`: Number of main premises to include before deducing conclusions
- `steps`: Number of logical steps to include in the deductive process


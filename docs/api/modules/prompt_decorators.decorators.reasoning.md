# Module `prompt_decorators.decorators.reasoning`

Reasoning Decorator

This decorator instructs the model to explicitly reason through a problem step by step.

## Classes

- [`Reasoning`](#class-reasoning): Decorator that instructs the model to use explicit reasoning.
- [`ReasoningStyle`](#class-reasoningstyle): Enumeration of reasoning styles.

### Class `Reasoning`

Decorator that instructs the model to use explicit reasoning.

This decorator enhances responses by prompting the model to:
1. Break down complex problems into steps
2. Show its thought process explicitly
3. Consider multiple perspectives where relevant

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(style=standard, show_working=True, consider_alternatives=False, depth=3, name, version, parameters, metadata)`
- `apply(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `get_version() -> <class 'prompt_decorators.core.base.Version'>`
- `is_compatible_with_version(version_str) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_json(indent) -> <class 'str'>`
- `validate() -> <class 'NoneType'>`

### Class `ReasoningStyle`

Enumeration of reasoning styles.

**Inherits from:** `Enum`



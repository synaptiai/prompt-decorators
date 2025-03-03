# Module `prompt_decorators.decorators.generated.decorators.forced_analogy`

Implementation of the ForcedAnalogy decorator.

This module provides the ForcedAnalogy decorator class for use in prompt engineering.

Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.

## Classes

- [`ForcedAnalogy`](#class-forcedanalogy): Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.

### Class `ForcedAnalogy`

Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.

Attributes:
    source: The specific domain, field, or context to draw analogies from. (str)
    comprehensiveness: How comprehensively to map concepts between domains. (Literal["basic", "comprehensive", "detailed"])
    mappings: Number of distinct concept mappings to create between domains. (Any)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(source, comprehensiveness=comprehensive, mappings=3) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `comprehensiveness`: Get the comprehensiveness parameter value.
- `mappings`: Get the mappings parameter value.
- `name`: Get the name of the decorator.
- `source`: Get the source parameter value.

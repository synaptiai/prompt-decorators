# Module `prompt_decorators.decorators.format`

Output Format Decorator

This decorator controls the output format of the model response.

## Classes

- [`FormatType`](#class-formattype): Enumeration of output format types.
- [`OutputFormat`](#class-outputformat): Decorator that controls the output format of the model response.

### Class `FormatType`

Enumeration of output format types.

**Inherits from:** `Enum`


### Class `OutputFormat`

Decorator that controls the output format of the model response.

This decorator specifies the format of the model's output, such as:
- Plain text
- Markdown
- JSON
- HTML
- CSV
- YAML
- XML

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(format_type=text, schema, headers, pretty_print=True, name, version, parameters, metadata)`
- `apply(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `get_version() -> <class 'prompt_decorators.core.base.Version'>`
- `is_compatible_with_version(version_str) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_json(indent) -> <class 'str'>`
- `validate() -> <class 'NoneType'>`

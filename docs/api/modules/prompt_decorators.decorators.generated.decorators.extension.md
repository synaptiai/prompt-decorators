# Module `prompt_decorators.decorators.generated.decorators.extension`

Implementation of the Extension decorator.

This module provides the Extension decorator class for use in prompt engineering.

A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations.

## Classes

- [`Extension`](#class-extension): A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations.

### Class `Extension`

A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations.

Attributes:
    source: URI or identifier for the extension package (e.g., URL, namespace, or registry identifier). (str)
    version: Specific version of the extension package to use. (str)
    decorators: Specific decorators to load from the extension (if empty, loads all decorators from the package). (List[Any])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(source, version, decorators) -> <class 'NoneType'>`
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
- `source`: Get the source parameter value.
- `version`: Get the version parameter value.

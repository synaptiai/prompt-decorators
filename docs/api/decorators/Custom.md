# Decorator `Custom`

**Version:** 1.0.0

A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.

## Parameters

### `rules`

**Type:** string
**Required:** Yes

Explicit instructions defining the custom behavior (e.g., 'present all examples in a numbered list with exactly three items')

### `name`

**Type:** string
**Required:** No

Optional name for the custom decorator to reference in documentation or explanations

### `priority`

**Type:** enum
**Required:** No
**Default:** `override`

How to prioritize custom rules relative to other decorators

**Allowed values:**

- `override`
- `supplement`
- `fallback`

## Examples

### Basic custom formatting rule

```
+++Custom(rules=every paragraph must start with a word that begins with the letter A)
Explain how search engines work.
```

Result:

Provides an explanation of search engines where every paragraph begins with a word starting with the letter A

### Complex custom behavior with named reference

```
+++Custom(name=DualPerspective, rules=present two contrasting viewpoints on each main point, label them as 'Perspective A' and 'Perspective B', and then provide a synthesis, priority=supplement)
Analyze the impact of social media on politics.
```

Result:

Analyzes social media's impact on politics using dual contrasting perspectives for each point, labeled as specified, with synthesis after each point, while still respecting other decorators

## Compatibility

**Supported models:**

- `gpt-4`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(rules, name, priority=CustomPriorityEnum.OVERRIDE)`

Initialize Custom decorator.

Args:
    rules: Explicit instructions defining the custom behavior (e.g., 'present all examples in a numbered list with exactly three items')
    name: Optional name for the custom decorator to reference in documentation or explanations
    priority: How to prioritize custom rules relative to other decorators

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the decorator to a prompt.

Args:
    prompt: The original prompt

Returns:
    The modified prompt with the decorator applied

#### `from_dict`

**Signature:** `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator from a dictionary.

Args:
    data: Dictionary representation of a decorator

Returns:
    New decorator instance

Raises:
    ValueError: If the data is invalid or incompatible with this class
    IncompatibleVersionError: If the version is incompatible

#### `from_json`

**Signature:** `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator from a JSON string.

Args:
    json_str: JSON string representation of a decorator

Returns:
    New decorator instance

Raises:
    ValueError: If the JSON is invalid or incompatible with this class
    json.JSONDecodeError: If the JSON is malformed
    IncompatibleVersionError: If the version is incompatible

#### `get_metadata`

**Signature:** `get_metadata() -> typing.Dict[str, typing.Any]`

Get metadata about this decorator class.

Returns:
    Dictionary with decorator metadata

#### `get_version`

**Signature:** `get_version() -> <class 'prompt_decorators.core.base.Version'>`

Get the decorator version.

Returns:
    Version object for the decorator

#### `is_compatible_with_version`

**Signature:** `is_compatible_with_version(version_str) -> <class 'bool'>`

Check if this decorator is compatible with the specified version.

Args:
    version_str: Version string to check compatibility with

Returns:
    True if compatible, False otherwise

#### `to_dict`

**Signature:** `to_dict() -> typing.Dict[str, typing.Any]`

Convert decorator to a dictionary representation.

Returns:
    Dictionary representation of the decorator

#### `to_json`

**Signature:** `to_json(indent) -> <class 'str'>`

Convert decorator to a JSON string.

Args:
    indent: Optional indentation for pretty-printing

Returns:
    JSON string representation of the decorator

#### `validate`

**Signature:** `validate() -> <class 'NoneType'>`

Validate decorator parameters.

This base implementation does basic type checking.
Subclasses should override for specific validation.

Raises:
    ValidationError: If any parameter fails validation

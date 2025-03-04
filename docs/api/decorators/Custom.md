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

**Signature:** `__init__(rules, name, priority=override) -> <class 'NoneType'>`

Initialize the Custom decorator.

Args:
    rules: Explicit instructions defining the custom behavior (e.g., 'present all examples in a numbered list with exactly three items')
    name: Optional name for the custom decorator to reference in documentation or explanations
    priority: How to prioritize custom rules relative to other decorators

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the decorator to a prompt string.

Args:
    prompt: The prompt to apply the decorator to


Returns:
    The modified prompt

#### `apply_to_prompt`

**Signature:** `apply_to_prompt(prompt) -> <class 'str'>`

Apply the decorator to a prompt.

Args:
    prompt: The prompt to decorate

Returns:
    The decorated prompt

#### `from_dict`

**Signature:** `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator instance from a dictionary representation.

Args:
    data: Dictionary representation of the decorator

Returns:
    A new decorator instance

Raises:
    ValidationError: If the dictionary is invalid

#### `get_metadata`

**Signature:** `get_metadata() -> typing.Dict[str, typing.Any]`

Get metadata about the decorator.

Returns:
    Dictionary containing metadata about the decorator


Args:
    cls: The decorator class

#### `is_compatible_with_version`

**Signature:** `is_compatible_with_version(version) -> <class 'bool'>`

Check if the decorator is compatible with a specific version.

Args:
    version: The version to check compatibility with.


Returns:
    True if compatible, False otherwise.


Raises:
    IncompatibleVersionError: If the version is incompatible.

#### `to_dict`

**Signature:** `to_dict() -> typing.Dict[str, typing.Any]`

Convert the decorator to a dictionary.

Args:
    self: The decorator instance

Returns:
    Dictionary representation of the decorator

#### `to_string`

**Signature:** `to_string() -> <class 'str'>`

Convert the decorator to a string.

Args:
    self: The decorator instance

Returns:
    String representation of the decorator

#### `transform_response`

**Signature:** `transform_response(response) -> <class 'str'>`

Transform the response from the model.

Args:
    response: The response to transform

Returns:
    The transformed response

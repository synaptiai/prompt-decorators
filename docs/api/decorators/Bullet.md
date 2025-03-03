# Decorator `Bullet`

**Version:** 1.0.0

Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.

## Parameters

### `style`

**Type:** enum
**Required:** No
**Default:** `dash`

The visual marker used for bullet points

**Allowed values:**

- `dash`
- `dot`
- `arrow`
- `star`
- `plus`

### `indented`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to allow nested, indented bullet points

### `compact`

**Type:** boolean
**Required:** No

Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false)

## Examples

### Basic bulleted list of key points

```
+++Bullet
What are the main factors to consider when buying a laptop?
```

Result:

Presents key laptop purchasing factors as a bulleted list with dash markers

### Compact star bullets with nesting disabled

```
+++Bullet(style=star, indented=false, compact=true)
List the benefits of regular exercise.
```

Result:

Provides a flat list of concise, star-bulleted points about exercise benefits, with no nested sub-points

## Compatibility

**Conflicts with:**

- `OutputFormat`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(style=dash, indented=True, compact=False) -> <class 'NoneType'>`

Initialize the Bullet decorator.

Args:
    style: The visual marker used for bullet points
    indented: Whether to allow nested, indented bullet points
    compact: Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false)

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

Returns:
    Dictionary representation of the decorator

#### `to_string`

**Signature:** `to_string() -> <class 'str'>`

Convert the decorator to a string.

Returns:
    String representation of the decorator

#### `transform_response`

**Signature:** `transform_response(response) -> <class 'str'>`

Transform the response from the model.

Args:
    response: The response to transform

Returns:
    The transformed response

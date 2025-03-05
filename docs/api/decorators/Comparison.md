# Decorator `Comparison`

**Version:** 1.0.0

Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.

## Parameters

### `aspects`

**Type:** array
**Required:** No

Specific aspects or dimensions to compare

### `format`

**Type:** enum
**Required:** No
**Default:** `table`

The presentation format for the comparison

**Allowed values:**

- `table`
- `prose`
- `bullets`

### `highlight`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to explicitly emphasize key differences

## Examples

### Basic tabular comparison of specific aspects

```
+++Comparison(aspects=[performance,cost,ease of use,ecosystem])
Compare React, Angular, and Vue for front-end development.
```

Result:

Creates a table comparing React, Angular, and Vue across the specified aspects, with key differences highlighted

### Prose-based comparison without specific aspects

```
+++Comparison(format=prose, highlight=false)
Compare democracy and authoritarianism as political systems.
```

Result:

Delivers a flowing prose comparison between democracy and authoritarianism, covering key differences and similarities in paragraph form

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(aspects, format=table, highlight=True) -> <class 'NoneType'>`

Initialize the Comparison decorator.

Args:
    aspects: Specific aspects or dimensions to compare
    format: The presentation format for the comparison
    highlight: Whether to explicitly emphasize key differences


Returns:
    None

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

This method transforms the prompt using the transformation template.

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

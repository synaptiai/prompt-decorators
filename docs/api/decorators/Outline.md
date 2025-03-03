# Decorator `Outline`

**Version:** 1.0.0

Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.

## Parameters

### `depth`

**Type:** number
**Required:** No
**Default:** `3`

Maximum nesting level of the outline

### `style`

**Type:** enum
**Required:** No
**Default:** `numeric`

Numbering or bullet style for the outline

**Allowed values:**

- `numeric`
- `bullet`
- `roman`
- `alpha`
- `mixed`

### `detailed`

**Type:** boolean
**Required:** No

Whether to include brief explanations under each outline point

## Examples

### Simple numeric outline of a complex topic

```
+++Outline
Explain the structure of the United States government.
```

Result:

Presents the US government structure as a numbered outline with up to 3 levels of hierarchy

### Detailed outline with mixed notation and deep hierarchy

```
+++Outline(style=mixed, depth=5, detailed=true)
Provide a comprehensive overview of machine learning techniques.
```

Result:

Creates a 5-level deep outline using mixed notation (numbers, letters, roman numerals) with brief explanations under each point, covering machine learning techniques

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(depth=3, style=numeric, detailed=False) -> <class 'NoneType'>`

Initialize the Outline decorator.

Args:
    depth: Maximum nesting level of the outline
    style: Numbering or bullet style for the outline
    detailed: Whether to include brief explanations under each outline point

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

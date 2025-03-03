# Decorator `Nested`

**Version:** 1.0.0

Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.

## Parameters

### `depth`

**Type:** number
**Required:** No
**Default:** `3`

Maximum nesting level of the hierarchy

### `style`

**Type:** enum
**Required:** No
**Default:** `mixed`

Visual style for hierarchical levels

**Allowed values:**

- `bullet`
- `numbered`
- `mixed`

### `collapsible`

**Type:** boolean
**Required:** No

Whether to suggest the hierarchy could be rendered as collapsible sections (for UI implementations)

## Examples

### Deep hierarchical organization of a complex domain

```
+++Nested
Explain the classification of living organisms.
```

Result:

Presents taxonomy in a nested hierarchy with domains, kingdoms, phyla, etc., using mixed notation styles for different levels

### Maximum depth collapsible structure for reference material

```
+++Nested(depth=5, style=bullet, collapsible=true)
Provide a comprehensive overview of programming paradigms.
```

Result:

Creates a 5-level deep bullet-point hierarchy of programming paradigms, designed to be rendered as collapsible sections

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(depth=3, style=mixed, collapsible=False) -> <class 'NoneType'>`

Initialize the Nested decorator.

Args:
    depth: Maximum nesting level of the hierarchy
    style: Visual style for hierarchical levels
    collapsible: Whether to suggest the hierarchy could be rendered as collapsible sections (for UI implementations)

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

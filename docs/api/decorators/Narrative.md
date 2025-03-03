# Decorator `Narrative`

**Version:** 1.0.0

Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.

## Parameters

### `structure`

**Type:** enum
**Required:** No
**Default:** `classic`

The narrative structure to employ

**Allowed values:**

- `classic`
- `nonlinear`
- `case-study`

### `characters`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to include character elements in the narrative

### `length`

**Type:** enum
**Required:** No
**Default:** `moderate`

The relative length of the narrative

**Allowed values:**

- `brief`
- `moderate`
- `extended`

## Examples

### Classic narrative structure to explain a concept

```
+++Narrative
Explain how the stock market works.
```

Result:

Explains the stock market through a classic narrative structure, introducing character elements and following a traditional story arc

### Brief case study without character elements

```
+++Narrative(structure=case-study, characters=false, length=brief)
Describe the impact of social media on mental health.
```

Result:

Presents a concise case study narrative about social media's impact on mental health, focusing on situations and outcomes without personified characters

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(structure=classic, characters=True, length=moderate) -> <class 'NoneType'>`

Initialize the Narrative decorator.

Args:
    structure: The narrative structure to employ
    characters: Whether to include character elements in the narrative
    length: The relative length of the narrative

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

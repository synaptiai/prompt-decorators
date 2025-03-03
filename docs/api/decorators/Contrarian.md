# Decorator `Contrarian`

**Version:** 1.0.0

Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.

## Parameters

### `approach`

**Type:** enum
**Required:** No
**Default:** `devils-advocate`

The specific contrarian approach to take

**Allowed values:**

- `outsider`
- `skeptic`
- `devils-advocate`

### `maintain`

**Type:** boolean
**Required:** No

Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false)

### `focus`

**Type:** string
**Required:** No

Optional specific aspect of the topic to focus contrarian analysis on

## Examples

### Basic devil's advocate approach with balanced conclusion

```
+++Contrarian
Why is renewable energy considered the future of power generation?
```

Result:

Challenges conventional thinking about renewable energy's dominance, presenting counterarguments and limitations, followed by a balanced perspective

### Maintained skeptical contrarian stance focused on a specific aspect

```
+++Contrarian(approach=skeptic, maintain=true, focus=methodology)
Discuss the reliability of climate models in predicting future global temperatures.
```

Result:

Provides a consistently skeptical analysis of climate model methodologies, questioning assumptions, limitations, and historical accuracy throughout the response

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(approach=devils-advocate, maintain=False, focus) -> <class 'NoneType'>`

Initialize the Contrarian decorator.

Args:
    approach: The specific contrarian approach to take
    maintain: Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false)
    focus: Optional specific aspect of the topic to focus contrarian analysis on

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

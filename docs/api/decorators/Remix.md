# Decorator `Remix`

**Version:** 1.0.0

Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.

## Parameters

### `target`

**Type:** string
**Required:** Yes

The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch')

### `preserve`

**Type:** enum
**Required:** No
**Default:** `facts`

What aspects of the original content to prioritize preserving

**Allowed values:**

- `facts`
- `structure`
- `tone`
- `comprehensiveness`

### `contrast`

**Type:** boolean
**Required:** No

Whether to highlight differences between the original framing and the remixed version

## Examples

### Basic remix for a different audience

```
+++Remix(target=high school students)
Explain how neural networks function in artificial intelligence.
```

Result:

Reframes the technical explanation of neural networks to be accessible and engaging for high school students while preserving the core facts

### Business remix with contrasting approach

```
+++Remix(target=board presentation, preserve=comprehensiveness, contrast=true)
Describe the technical details of our new software architecture.
```

Result:

Transforms the technical software architecture description into a board-appropriate presentation format, maintaining comprehensive coverage while highlighting how this differs from a technical explanation

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(target, preserve=facts, contrast=False) -> <class 'NoneType'>`

Initialize the Remix decorator.

Args:
    target: The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch')
    preserve: What aspects of the original content to prioritize preserving
    contrast: Whether to highlight differences between the original framing and the remixed version


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

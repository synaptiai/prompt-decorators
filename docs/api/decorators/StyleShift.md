# Decorator `StyleShift`

**Version:** 1.0.0

Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.

## Parameters

### `aspect`

**Type:** enum
**Required:** Yes

The specific style aspect to modify

**Allowed values:**

- `formality`
- `persuasion`
- `urgency`
- `confidence`
- `complexity`

### `level`

**Type:** number
**Required:** No
**Default:** `3`

The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal)

### `maintain`

**Type:** array
**Required:** No

Style aspects to explicitly maintain while modifying the target aspect

## Examples

### Highly formal style while maintaining normal complexity

```
+++StyleShift(aspect=formality, level=5, maintain=[complexity])
Explain the process of photosynthesis.
```

Result:

Provides a highly formal explanation of photosynthesis with elevated language and structure, while keeping the complexity at a moderate level

### Increased urgency for a business communication

```
+++StyleShift(aspect=urgency, level=4)
Describe the steps needed to prepare for the upcoming product launch.
```

Result:

Delivers a description of product launch preparation steps with heightened sense of urgency and time-sensitivity in the language and framing

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(aspect, level=3, maintain) -> <class 'NoneType'>`

Initialize the StyleShift decorator.

Args:
    aspect: The specific style aspect to modify
    level: The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal)
    maintain: Style aspects to explicitly maintain while modifying the target aspect


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

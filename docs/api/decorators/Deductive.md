# Decorator `Deductive`

**Version:** 1.0.0

Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.

## Parameters

### `premises`

**Type:** number
**Required:** No
**Default:** `2`

Number of main premises to include before deducing conclusions

### `formal`

**Type:** boolean
**Required:** No

Whether to use formal logical structures with explicit syllogisms

### `steps`

**Type:** number
**Required:** No
**Default:** `3`

Number of logical steps to include in the deductive process

## Examples

### Basic deductive reasoning from principles to specific conclusions

```
+++Deductive
Should social media companies be regulated like utilities?
```

Result:

Starts with general principles about utilities and regulation, establishes premises about social media characteristics, and deduces conclusions about appropriate regulatory approaches

### Formal deductive logic with multiple steps

```
+++Deductive(formal=true, steps=5)
Is artificial intelligence conscious?
```

Result:

Presents formal logical syllogisms about consciousness and intelligence, proceeding through 5 distinct logical steps to reach conclusions about AI consciousness

## Compatibility

**Conflicts with:**

- `Inductive`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(premises=2, formal=False, steps=3) -> <class 'NoneType'>`

Initialize the Deductive decorator.

Args:
    premises: Number of main premises to include before deducing conclusions
    formal: Whether to use formal logical structures with explicit syllogisms
    steps: Number of logical steps to include in the deductive process


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

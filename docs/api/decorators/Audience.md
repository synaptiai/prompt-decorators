# Decorator `Audience`

**Version:** 1.0.0

Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.

## Parameters

### `level`

**Type:** enum
**Required:** No
**Default:** `intermediate`

The expertise level of the target audience

**Allowed values:**

- `beginner`
- `intermediate`
- `expert`
- `technical`

### `domain`

**Type:** string
**Required:** No
**Default:** `general`

Specific knowledge domain or field for domain-specific terminology adaptation

### `examples`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to include additional examples for clarity

## Examples

### Technical explanation for experts in a specific field

```
+++Audience(level=technical, domain=cybersecurity)
Explain zero-knowledge proofs.
```

Result:

Provides an in-depth technical explanation of zero-knowledge proofs using cybersecurity-specific terminology and concepts

### Beginner-friendly explanation with examples

```
+++Audience(level=beginner, examples=true)
How does machine learning work?
```

Result:

Explains machine learning concepts in simple terms with multiple illustrative examples suitable for complete beginners

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(level=intermediate, domain=general, examples=True) -> <class 'NoneType'>`

Initialize the Audience decorator.

Args:
    level: The expertise level of the target audience
    domain: Specific knowledge domain or field for domain-specific terminology adaptation
    examples: Whether to include additional examples for clarity

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

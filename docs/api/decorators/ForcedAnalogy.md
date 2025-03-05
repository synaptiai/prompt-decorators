# Decorator `ForcedAnalogy`

**Version:** 1.0.0

Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.

## Parameters

### `source`

**Type:** string
**Required:** Yes

The specific domain, field, or context to draw analogies from

### `comprehensiveness`

**Type:** enum
**Required:** No
**Default:** `comprehensive`

How comprehensively to map concepts between domains

**Allowed values:**

- `basic`
- `comprehensive`
- `detailed`

### `mappings`

**Type:** number
**Required:** No
**Default:** `3`

Number of distinct concept mappings to create between domains

## Examples

### Explaining a technical concept using sports analogies

```
+++ForcedAnalogy(source=sports)
Explain how blockchain technology works.
```

Result:

Explains blockchain technology by mapping concepts to sports analogies (e.g., ledger as scoreboard, miners as referees, consensus as rulebook)

### Detailed cooking analogy for complex scientific process

```
+++ForcedAnalogy(source=cooking, comprehensiveness=detailed, mappings=5)
Describe how CRISPR gene editing works.
```

Result:

Provides a detailed explanation of CRISPR through cooking analogies, with 5 distinct concept mappings (e.g., DNA as recipe, Cas9 as kitchen knife, guide RNA as cooking instructions)

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(source, comprehensiveness=comprehensive, mappings=3) -> <class 'NoneType'>`

Initialize the ForcedAnalogy decorator.

Args:
    source: The specific domain, field, or context to draw analogies from
    comprehensiveness: How comprehensively to map concepts between domains
    mappings: Number of distinct concept mappings to create between domains


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

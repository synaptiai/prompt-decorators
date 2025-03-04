# Decorator `Academic`

**Version:** 1.0.0

Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.

## Parameters

### `style`

**Type:** enum
**Required:** No
**Default:** `scientific`

The academic discipline style to follow

**Allowed values:**

- `humanities`
- `scientific`
- `legal`

### `format`

**Type:** enum
**Required:** No
**Default:** `APA`

The citation format to use for references

**Allowed values:**

- `APA`
- `MLA`
- `Chicago`
- `Harvard`
- `IEEE`

## Examples

### Scientific academic response with APA citations

```
+++Academic
Discuss the evidence for climate change.
```

Result:

Produces a scholarly analysis of climate change evidence using formal scientific language and proper APA citations

### Humanities-focused academic response with MLA citations

```
+++Academic(style=humanities, format=MLA)
Analyze the themes in Shakespeare's Hamlet.
```

Result:

Provides a literary analysis of Hamlet using humanities-appropriate terminology and MLA citation format

## Compatibility

**Conflicts with:**

- `ELI5`
- `Creative`
- `Motivational`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(style=scientific, format=APA) -> <class 'NoneType'>`

Initialize the Academic decorator.

Args:
    style: The academic discipline style to follow
    format: The citation format to use for references


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

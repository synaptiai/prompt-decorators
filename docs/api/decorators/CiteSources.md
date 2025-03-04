# Decorator `CiteSources`

**Version:** 1.0.0

Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.

## Parameters

### `style`

**Type:** enum
**Required:** No
**Default:** `inline`

The placement and format of citations within the response

**Allowed values:**

- `inline`
- `footnote`
- `endnote`

### `format`

**Type:** enum
**Required:** No
**Default:** `APA`

The citation format to use

**Allowed values:**

- `APA`
- `MLA`
- `Chicago`
- `Harvard`
- `IEEE`

### `comprehensive`

**Type:** boolean
**Required:** No

Whether to cite every claim (true) or only major claims (false)

## Examples

### Basic inline citations for a scientific topic

```
+++CiteSources
Explain the evidence for climate change.
```

Result:

Explains climate change with inline citations to scientific sources in APA format

### Comprehensive footnote citations in Chicago style

```
+++CiteSources(style=footnote, format=Chicago, comprehensive=true)
Describe the major events of World War II.
```

Result:

Delivers a detailed account of WWII with comprehensive footnote citations in Chicago style for all factual claims

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(style=inline, format=APA, comprehensive=False) -> <class 'NoneType'>`

Initialize the CiteSources decorator.

Args:
    style: The placement and format of citations within the response
    format: The citation format to use
    comprehensive: Whether to cite every claim (true) or only major claims (false)


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

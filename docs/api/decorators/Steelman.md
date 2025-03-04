# Decorator `Steelman`

**Version:** 1.0.0

Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.

## Parameters

### `sides`

**Type:** number
**Required:** No
**Default:** `2`

Number of different viewpoints to steel-man

### `critique`

**Type:** boolean
**Required:** No

Whether to include critique after presenting the steel-manned arguments

### `separation`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to clearly separate the steel-manned presentations from any analysis

## Examples

### Steel-manning both sides of a controversial issue

```
+++Steelman
Is universal basic income a good policy?
```

Result:

Presents the strongest possible cases both for and against universal basic income, with each position articulated in its most compelling form

### Steel-manning one position with subsequent critique

```
+++Steelman(sides=1, critique=true, separation=true)
What is the strongest case for cryptocurrency as the future of finance?
```

Result:

Provides the most compelling possible argument for cryptocurrency as the future of finance, clearly separated from a subsequent balanced critique

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(sides=2, critique=False, separation=True) -> <class 'NoneType'>`

Initialize the Steelman decorator.

Args:
    sides: Number of different viewpoints to steel-man
    critique: Whether to include critique after presenting the steel-manned arguments
    separation: Whether to clearly separate the steel-manned presentations from any analysis


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

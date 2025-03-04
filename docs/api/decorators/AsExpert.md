# Decorator `AsExpert`

**Version:** 1.0.0

Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.

## Parameters

### `domain`

**Type:** string
**Required:** Yes

The specific field or discipline the expert specializes in

### `experience`

**Type:** enum
**Required:** No
**Default:** `senior`

The experience level of the expert

**Allowed values:**

- `junior`
- `senior`
- `leading`
- `pioneering`

### `technical`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to use highly technical language and domain-specific terminology

## Examples

### Basic response as a domain expert

```
+++AsExpert(domain=neuroscience)
Explain how memories are formed in the brain.
```

Result:

Provides an explanation of memory formation from the perspective of a senior neuroscientist, using appropriate terminology and references to relevant research

### Highly technical response as pioneering expert

```
+++AsExpert(domain=cryptography, experience=pioneering, technical=true)
Assess the security implications of quantum computing for current encryption standards.
```

Result:

Delivers a technically sophisticated assessment of quantum computing's encryption impacts from the perspective of a pioneering cryptography expert, using advanced terminology and nuanced analysis

## Compatibility

**Conflicts with:**

- `ELI5`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(domain, experience=senior, technical=True) -> <class 'NoneType'>`

Initialize the AsExpert decorator.

Args:
    domain: The specific field or discipline the expert specializes in
    experience: The experience level of the expert
    technical: Whether to use highly technical language and domain-specific terminology

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

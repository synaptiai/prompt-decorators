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

**Signature:** `__init__(domain, experience=AsExpertExperienceEnum.SENIOR, technical=True)`

Initialize AsExpert decorator.

Args:
    domain: The specific field or discipline the expert specializes in
    experience: The experience level of the expert
    technical: Whether to use highly technical language and domain-specific terminology

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the decorator to a prompt.

Args:
    prompt: The original prompt

Returns:
    The modified prompt with the decorator applied

#### `from_dict`

**Signature:** `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator from a dictionary.

Args:
    data: Dictionary representation of a decorator

Returns:
    New decorator instance

Raises:
    ValueError: If the data is invalid or incompatible with this class
    IncompatibleVersionError: If the version is incompatible

#### `from_json`

**Signature:** `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator from a JSON string.

Args:
    json_str: JSON string representation of a decorator

Returns:
    New decorator instance

Raises:
    ValueError: If the JSON is invalid or incompatible with this class
    json.JSONDecodeError: If the JSON is malformed
    IncompatibleVersionError: If the version is incompatible

#### `get_metadata`

**Signature:** `get_metadata() -> typing.Dict[str, typing.Any]`

Get metadata about this decorator class.

Returns:
    Dictionary with decorator metadata

#### `get_version`

**Signature:** `get_version() -> <class 'prompt_decorators.core.base.Version'>`

Get the decorator version.

Returns:
    Version object for the decorator

#### `is_compatible_with_version`

**Signature:** `is_compatible_with_version(version_str) -> <class 'bool'>`

Check if this decorator is compatible with the specified version.

Args:
    version_str: Version string to check compatibility with

Returns:
    True if compatible, False otherwise

#### `to_dict`

**Signature:** `to_dict() -> typing.Dict[str, typing.Any]`

Convert decorator to a dictionary representation.

Returns:
    Dictionary representation of the decorator

#### `to_json`

**Signature:** `to_json(indent) -> <class 'str'>`

Convert decorator to a JSON string.

Args:
    indent: Optional indentation for pretty-printing

Returns:
    JSON string representation of the decorator

#### `validate`

**Signature:** `validate() -> <class 'NoneType'>`

Validate decorator parameters.

This base implementation does basic type checking.
Subclasses should override for specific validation.

Raises:
    ValidationError: If any parameter fails validation

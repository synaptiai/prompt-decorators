# Decorator `Professional`

**Version:** 1.0.0

Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.

## Parameters

### `industry`

**Type:** string
**Required:** No
**Default:** `general`

The specific industry context to adapt the language for

### `formality`

**Type:** enum
**Required:** No
**Default:** `standard`

The level of formality to maintain in the response

**Allowed values:**

- `standard`
- `high`
- `executive`

## Examples

### Standard professional business communication

```
+++Professional
Explain the benefits of implementing a CRM system.
```

Result:

Delivers a clear, professional explanation of CRM benefits using business-appropriate language and structure

### Industry-specific executive-level communication

```
+++Professional(industry=healthcare, formality=executive)
Summarize the impact of telehealth adoption on patient outcomes.
```

Result:

Produces an executive-level analysis of telehealth impacts using healthcare industry terminology and highly formal business language

## Compatibility

**Conflicts with:**

- `ELI5`
- `Creative`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(industry=general, formality=standard) -> <class 'NoneType'>`

Initialize the Professional decorator.

Args:
    industry: The specific industry context to adapt the language for
    formality: The level of formality to maintain in the response

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

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

**Signature:** `__init__(industry=general, formality=ProfessionalFormalityEnum.STANDARD)`

Initialize Professional decorator.

Args:
    industry: The specific industry context to adapt the language for
    formality: The level of formality to maintain in the response

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


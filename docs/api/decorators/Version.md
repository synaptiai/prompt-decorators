# Decorator `Version`

**Version:** 1.0.0

Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.

## Parameters

### `standard`

**Type:** string  
**Required:** Yes  
**Default:** `1.0.0`  

The semantic version of the Prompt Decorators standard to use

## Examples

### Specify standard version for compatibility

```
+++Version(standard=1.0.0)
+++Reasoning(depth=comprehensive)
Explain quantum entanglement
```

Result:

Ensures decorators are interpreted according to version 1.0.0 of the standard

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

### Methods

#### `__init__`

**Signature:** `__init__(version_str)`

Initialize a version from a string.

Args:
    version_str: Semantic version string (e.g., "1.2.3")
    
Raises:
    ValueError: If the version string is invalid

#### `is_compatible_with`

**Signature:** `is_compatible_with(other) -> <class 'bool'>`

Check if this version is compatible with another version.

For compatibility, major versions must match and this version's
minor and patch must be greater than or equal to the other version's.

Args:
    other: Version to compare with
    
Returns:
    True if compatible, False otherwise


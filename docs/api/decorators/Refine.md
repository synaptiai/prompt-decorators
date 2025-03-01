# Decorator `Refine`

**Version:** 1.0.0

A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.

## Parameters

### `iterations`

**Type:** number  
**Required:** No  
**Default:** `2`  

Number of refinement cycles to perform

### `focus`

**Type:** array  
**Required:** No  

Specific aspects to focus on during refinement (e.g., clarity, conciseness, evidence)

### `showProcess`

**Type:** boolean  
**Required:** No  

Whether to show the intermediate steps in the refinement process

## Examples

### Basic refinement of a complex explanation

```
+++Refine
Explain the implications of quantum computing for cybersecurity.
```

Result:

Provides a refined explanation of quantum computing implications for cybersecurity, with two hidden iterations improving clarity and accuracy

### Detailed refinement with visible iterations

```
+++Refine(iterations=3, focus=[clarity,evidence,conciseness], showProcess=true)
Analyze the economic impacts of artificial intelligence.
```

Result:

Shows three visible iterations of analyzing AI economic impacts, with each step focusing on improving clarity, strengthening evidence, and enhancing conciseness

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(iterations=2, focus, showProcess=False)`

Initialize Refine decorator.

Args:
    iterations: Number of refinement cycles to perform
    focus: Specific aspects to focus on during refinement (e.g., clarity, conciseness, evidence)
    showProcess: Whether to show the intermediate steps in the refinement process

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


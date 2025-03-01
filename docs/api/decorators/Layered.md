# Decorator `Layered`

**Version:** 1.0.0

Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.

## Parameters

### `levels`

**Type:** enum  
**Required:** No  
**Default:** `summary-detail-technical`  

The granularity of explanation levels to include

**Allowed values:**

- `sentence-paragraph-full`
- `basic-intermediate-advanced`
- `summary-detail-technical`

### `count`

**Type:** number  
**Required:** No  
**Default:** `3`  

Number of distinct explanation layers to provide

### `progression`

**Type:** enum  
**Required:** No  
**Default:** `separate`  

How to structure the progression between layers

**Allowed values:**

- `separate`
- `nested`
- `incremental`

## Examples

### Basic three-level explanation of a complex concept

```
+++Layered
Explain how blockchain technology works.
```

Result:

Provides a summary-level explanation of blockchain, followed by a detailed explanation, and finally a technical deep dive with implementation details

### Multi-layered nested progression with custom levels

```
+++Layered(levels=basic-intermediate-advanced, count=4, progression=nested)
Describe the principles of quantum computing.
```

Result:

Delivers a nested explanation of quantum computing with four progressive layers of understanding, each building on the previous and increasing in complexity from basic to advanced

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(levels=LayeredLevelsEnum.SUMMARY_DETAIL_TECHNICAL, count=3, progression=LayeredProgressionEnum.SEPARATE)`

Initialize Layered decorator.

Args:
    levels: The granularity of explanation levels to include
    count: Number of distinct explanation layers to provide
    progression: How to structure the progression between layers

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


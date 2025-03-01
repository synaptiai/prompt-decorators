# Decorator `Prioritize`

**Version:** 1.0.0

Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.

## Parameters

### `criteria`

**Type:** string  
**Required:** No  
**Default:** `importance`  

The specific criterion to use for prioritization (e.g., importance, urgency, ROI)

### `count`

**Type:** number  
**Required:** No  
**Default:** `5`  

Number of prioritized items to include

### `showRationale`

**Type:** boolean  
**Required:** No  

Whether to explain the reasoning behind each priority ranking

## Examples

### Basic prioritization of key factors

```
+++Prioritize
What factors should be considered when designing a mobile app?
```

Result:

Presents the top 5 factors for mobile app design, ranked by importance from most to least critical

### Detailed prioritization with custom criteria and rationale

```
+++Prioritize(criteria=ROI, count=7, showRationale=true)
What marketing strategies should our startup focus on?
```

Result:

Provides 7 marketing strategies ranked by return on investment, with explanations for each ranking position

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(criteria=importance, count=5, showRationale=False)`

Initialize Prioritize decorator.

Args:
    criteria: The specific criterion to use for prioritization (e.g., importance, urgency, ROI)
    count: Number of prioritized items to include
    showRationale: Whether to explain the reasoning behind each priority ranking

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


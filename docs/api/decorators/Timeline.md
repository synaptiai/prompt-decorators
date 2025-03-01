# Decorator `Timeline`

**Version:** 1.0.0

Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.

## Parameters

### `granularity`

**Type:** enum  
**Required:** No  
**Default:** `year`  

The level of time detail to include in the timeline

**Allowed values:**

- `day`
- `month`
- `year`
- `decade`
- `century`
- `era`

### `format`

**Type:** enum  
**Required:** No  
**Default:** `list`  

The presentation format for the timeline

**Allowed values:**

- `list`
- `narrative`
- `table`

### `details`

**Type:** enum  
**Required:** No  
**Default:** `moderate`  

The level of detail to include for each timeline event

**Allowed values:**

- `minimal`
- `moderate`
- `comprehensive`

## Examples

### Basic chronological timeline of major events

```
+++Timeline
Describe the key developments in artificial intelligence.
```

Result:

Presents a year-by-year list of important AI milestones and breakthroughs from earliest developments to present day

### Detailed narrative timeline with specific date granularity

```
+++Timeline(granularity=month, format=narrative, details=comprehensive)
What were the major events of the Apollo 11 mission?
```

Result:

Provides a flowing narrative account of the Apollo 11 mission with month/day dates and comprehensive details of each significant event

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(granularity=TimelineGranularityEnum.YEAR, format=TimelineFormatEnum.LIST, details=TimelineDetailsEnum.MODERATE)`

Initialize Timeline decorator.

Args:
    granularity: The level of time detail to include in the timeline
    format: The presentation format for the timeline
    details: The level of detail to include for each timeline event

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


# Decorator `Alternatives`

**Version:** 1.0.0

Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.

## Parameters

### `count`

**Type:** number  
**Required:** No  
**Default:** `3`  

Number of alternative options or approaches to generate

### `diversity`

**Type:** enum  
**Required:** No  
**Default:** `medium`  

How different or varied the alternatives should be from each other

**Allowed values:**

- `low`
- `medium`
- `high`

### `comparison`

**Type:** boolean  
**Required:** No  

Whether to include a comparative analysis of the alternatives

## Examples

### Basic alternative approaches to a problem

```
+++Alternatives
How can I improve my public speaking skills?
```

Result:

Provides three distinct approaches to improving public speaking skills, each with its own methodology and focus

### Highly diverse alternatives with comparative analysis

```
+++Alternatives(count=5, diversity=high, comparison=true)
What are some ways to reduce carbon emissions in urban areas?
```

Result:

Presents five highly diverse approaches to reducing urban carbon emissions, followed by a comparative analysis of their effectiveness, cost, and implementation challenges

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(count=3, diversity=AlternativesDiversityEnum.MEDIUM, comparison=False)`

Initialize Alternatives decorator.

Args:
    count: Number of alternative options or approaches to generate
    diversity: How different or varied the alternatives should be from each other
    comparison: Whether to include a comparative analysis of the alternatives

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


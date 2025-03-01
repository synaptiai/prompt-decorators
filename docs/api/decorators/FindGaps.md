# Decorator `FindGaps`

**Version:** 1.0.0

Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.

## Parameters

### `aspects`

**Type:** enum  
**Required:** No  
**Default:** `comprehensive`  

The specific types of gaps to focus on finding

**Allowed values:**

- `questions`
- `resources`
- `stakeholders`
- `risks`
- `dependencies`
- `comprehensive`

### `depth`

**Type:** enum  
**Required:** No  
**Default:** `thorough`  

How thoroughly to analyze for gaps

**Allowed values:**

- `basic`
- `thorough`
- `exhaustive`

### `solutions`

**Type:** boolean  
**Required:** No  
**Default:** `True`  

Whether to suggest solutions or approaches for addressing the identified gaps

## Examples

### Basic comprehensive gap analysis of a business plan

```
+++FindGaps
We plan to launch our SaaS product with these features and marketing channels...
```

Result:

First identifies gaps across various aspects of the SaaS product launch plan, then suggests solutions for addressing each gap

### Exhaustive stakeholder-focused gap analysis without solutions

```
+++FindGaps(aspects=stakeholders, depth=exhaustive, solutions=false)
Here's our urban redevelopment proposal...
```

Result:

Provides an exhaustive analysis of overlooked or inadequately considered stakeholders in the urban redevelopment proposal, without suggesting solutions

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(aspects=FindGapsAspectsEnum.COMPREHENSIVE, depth=FindGapsDepthEnum.THOROUGH, solutions=True)`

Initialize FindGaps decorator.

Args:
    aspects: The specific types of gaps to focus on finding
    depth: How thoroughly to analyze for gaps
    solutions: Whether to suggest solutions or approaches for addressing the identified gaps

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


# Decorator `Steelman`

**Version:** 1.0.0

Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.

## Parameters

### `sides`

**Type:** number  
**Required:** No  
**Default:** `2`  

Number of different viewpoints to steel-man

### `critique`

**Type:** boolean  
**Required:** No  

Whether to include critique after presenting the steel-manned arguments

### `separation`

**Type:** boolean  
**Required:** No  
**Default:** `True`  

Whether to clearly separate the steel-manned presentations from any analysis

## Examples

### Steel-manning both sides of a controversial issue

```
+++Steelman
Is universal basic income a good policy?
```

Result:

Presents the strongest possible cases both for and against universal basic income, with each position articulated in its most compelling form

### Steel-manning one position with subsequent critique

```
+++Steelman(sides=1, critique=true, separation=true)
What is the strongest case for cryptocurrency as the future of finance?
```

Result:

Provides the most compelling possible argument for cryptocurrency as the future of finance, clearly separated from a subsequent balanced critique

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(sides=2, critique=False, separation=True)`

Initialize Steelman decorator.

Args:
    sides: Number of different viewpoints to steel-man
    critique: Whether to include critique after presenting the steel-manned arguments
    separation: Whether to clearly separate the steel-manned presentations from any analysis

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


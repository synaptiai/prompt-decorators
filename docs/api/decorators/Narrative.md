# Decorator `Narrative`

**Version:** 1.0.0

Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.

## Parameters

### `structure`

**Type:** enum  
**Required:** No  
**Default:** `classic`  

The narrative structure to employ

**Allowed values:**

- `classic`
- `nonlinear`
- `case-study`

### `characters`

**Type:** boolean  
**Required:** No  
**Default:** `True`  

Whether to include character elements in the narrative

### `length`

**Type:** enum  
**Required:** No  
**Default:** `moderate`  

The relative length of the narrative

**Allowed values:**

- `brief`
- `moderate`
- `extended`

## Examples

### Classic narrative structure to explain a concept

```
+++Narrative
Explain how the stock market works.
```

Result:

Explains the stock market through a classic narrative structure, introducing character elements and following a traditional story arc

### Brief case study without character elements

```
+++Narrative(structure=case-study, characters=false, length=brief)
Describe the impact of social media on mental health.
```

Result:

Presents a concise case study narrative about social media's impact on mental health, focusing on situations and outcomes without personified characters

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(structure=NarrativeStructureEnum.CLASSIC, characters=True, length=NarrativeLengthEnum.MODERATE)`

Initialize Narrative decorator.

Args:
    structure: The narrative structure to employ
    characters: Whether to include character elements in the narrative
    length: The relative length of the narrative

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


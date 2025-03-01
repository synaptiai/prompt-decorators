# Decorator `Summary`

**Version:** 1.0.0

Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.

## Parameters

### `length`

**Type:** enum  
**Required:** No  
**Default:** `medium`  

Relative length of the summary

**Allowed values:**

- `short`
- `medium`
- `long`

### `wordCount`

**Type:** number  
**Required:** No  

Approximate target word count for the summary

### `position`

**Type:** enum  
**Required:** No  
**Default:** `standalone`  

Where to position the summary in relation to any full content

**Allowed values:**

- `beginning`
- `end`
- `standalone`

## Examples

### Short standalone summary of a complex topic

```
+++Summary(length=short)
Explain quantum computing and its potential applications.
```

Result:

Delivers a concise overview of quantum computing and its applications in approximately 2-3 sentences

### Specific word count summary at the beginning of a response

```
+++Summary(wordCount=100, position=beginning)
Describe the causes and effects of climate change.
```

Result:

Starts with a 100-word summary of climate change causes and effects, followed by more detailed information

## Compatibility

**Conflicts with:**

- `Detailed`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(length=SummaryLengthEnum.MEDIUM, wordCount, position=SummaryPositionEnum.STANDALONE)`

Initialize Summary decorator.

Args:
    length: Relative length of the summary
    wordCount: Approximate target word count for the summary
    position: Where to position the summary in relation to any full content

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


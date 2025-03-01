# Decorator `OutputFormat`

**Version:** 1.0.0

Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way.

## Parameters

### `format`

**Type:** enum  
**Required:** Yes  
**Default:** `markdown`  

The format to use for the response

**Allowed values:**

- `json`
- `markdown`
- `yaml`
- `xml`
- `plaintext`

## Examples

### JSON output for structured data

```
+++OutputFormat(format=json)
List the top 5 programming languages and their key features.
```

Result:

Returns a JSON object with programming languages and their features

### Markdown output for formatted text

```
+++OutputFormat(format=markdown)
Write a tutorial on setting up a React project.
```

Result:

Returns a nicely formatted markdown document with headings, code blocks, and lists

## Compatibility

**Conflicts with:**

- `Schema`
- `TableFormat`
- `Bullet`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(format_type=text, schema, headers, pretty_print=True, name, version, parameters, metadata)`

Initialize an OutputFormat decorator.

Args:
    format_type: Type of output format (text, markdown, json, etc.)
    schema: Optional schema for structured formats (JSON, XML)
    headers: Optional headers for tabular formats (CSV)
    pretty_print: Whether to pretty-print the output
    name: Optional decorator name override
    version: Optional version override
    parameters: Optional parameter dictionary (overrides individual parameters)
    metadata: Optional metadata dictionary

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the output format decorator to a prompt.

Args:
    prompt: The original prompt
    
Returns:
    The modified prompt with output format instructions

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

Raises:
    ValidationError: If any parameter fails validation


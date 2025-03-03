# Decorator `TableFormat`

**Version:** 1.0.0

Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.

## Parameters

### `columns`

**Type:** array
**Required:** Yes

List of column names for the table

### `format`

**Type:** enum
**Required:** No
**Default:** `markdown`

Format style for the table representation

**Allowed values:**

- `markdown`
- `ascii`
- `csv`

### `alignment`

**Type:** enum
**Required:** No
**Default:** `left`

Text alignment within table cells

**Allowed values:**

- `left`
- `center`
- `right`

## Examples

### Simple comparison table in markdown format

```
+++TableFormat(columns=[Feature, TypeScript, JavaScript])
Compare TypeScript and JavaScript features.
```

Result:

Presents a markdown table comparing features of TypeScript and JavaScript with three columns

### Detailed CSV table with specific columns

```
+++TableFormat(columns=[Planet, Diameter, Distance from Sun, Orbital Period, Number of Moons], format=csv)
List the planets in our solar system with their key characteristics.
```

Result:

Generates a CSV-formatted table containing detailed information about each planet with the specified columns

## Compatibility

**Conflicts with:**

- `OutputFormat`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(columns, format=TableFormatFormatEnum.MARKDOWN, alignment=TableFormatAlignmentEnum.LEFT)`

Initialize TableFormat decorator.

Args:
    columns: List of column names for the table
    format: Format style for the table representation
    alignment: Text alignment within table cells

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

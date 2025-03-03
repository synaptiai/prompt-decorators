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

**Signature:** `__init__(columns, format=markdown, alignment=left) -> <class 'NoneType'>`

Initialize the TableFormat decorator.

Args:
    columns: List of column names for the table
    format: Format style for the table representation
    alignment: Text alignment within table cells

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the decorator to a prompt string.

Args:
    prompt: The prompt to apply the decorator to


Returns:
    The modified prompt

#### `apply_to_prompt`

**Signature:** `apply_to_prompt(prompt) -> <class 'str'>`

Apply the decorator to a prompt.

Args:
    prompt: The prompt to decorate

Returns:
    The decorated prompt

#### `from_dict`

**Signature:** `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator instance from a dictionary representation.

Args:
    data: Dictionary representation of the decorator

Returns:
    A new decorator instance

Raises:
    ValidationError: If the dictionary is invalid

#### `get_metadata`

**Signature:** `get_metadata() -> typing.Dict[str, typing.Any]`

Get metadata about the decorator.

Returns:
    Dictionary containing metadata about the decorator

#### `is_compatible_with_version`

**Signature:** `is_compatible_with_version(version) -> <class 'bool'>`

Check if the decorator is compatible with a specific version.

Args:
    version: The version to check compatibility with.


Returns:
    True if compatible, False otherwise.


Raises:
    IncompatibleVersionError: If the version is incompatible.

#### `to_dict`

**Signature:** `to_dict() -> typing.Dict[str, typing.Any]`

Convert the decorator to a dictionary.

Returns:
    Dictionary representation of the decorator

#### `to_string`

**Signature:** `to_string() -> <class 'str'>`

Convert the decorator to a string.

Returns:
    String representation of the decorator

#### `transform_response`

**Signature:** `transform_response(response) -> <class 'str'>`

Transform the response from the model.

Args:
    response: The response to transform

Returns:
    The transformed response

# json_loader

JSON loading utilities for decorator definitions.

This module provides utilities for loading and validating decorator definitions from JSON.

## Module Variables

### `logger`

Type: `Logger`

Value: `<Logger prompt_decorators.utils.json_loader (INFO)>`

## Classes

### `JSONLoader`

Loader for decorator definitions from JSON.

This class provides utilities for loading decorator definitions from JSON strings,
files, or directories, and validating them against a schema.

#### Attributes

- `DEFAULT_SCHEMA_PATH`: `PosixPath` = `PosixPath('/Users/danielbentes/prompt-decorators/prompt_decorators/schemas/decorator_schema.json')`

#### Methods

##### `__init__`

Initialize the JSON loader.

Args:
    schema_path: Path to the schema file for validation (optional)

**Signature:** `__init__(self, schema_path: Optional[str] = None)`

**Parameters:**

- `schema_path`: `Optional` (default: `None`)

##### `load_from_directory`

Load all decorator definitions from JSON files in a directory.

Args:
    directory_path: Path to the directory containing JSON files
    validate: Whether to validate against the schema (default: True)

Returns:
    List of decorator definitions as dictionaries

**Signature:** `load_from_directory(self, directory_path: str, validate: bool = True) -> List[Dict[str, Any]]`

**Parameters:**

- `directory_path`: `str`
- `validate`: `bool` (default: `True`)

**Returns:** `List`

##### `load_from_file`

Load a decorator definition from a JSON file.

Args:
    file_path: Path to the JSON file
    validate: Whether to validate against the schema (default: True)

Returns:
    The decorator definition as a dictionary

Raises:
    FileNotFoundError: If the file is not found
    json.JSONDecodeError: If the JSON is invalid
    jsonschema.exceptions.ValidationError: If validation fails

**Signature:** `load_from_file(self, file_path: str, validate: bool = True) -> Dict[str, Any]`

**Parameters:**

- `file_path`: `str`
- `validate`: `bool` (default: `True`)

**Returns:** `Dict`

##### `load_from_string`

Load a decorator definition from a JSON string.

Args:
    json_string: The JSON string to load
    validate: Whether to validate against the schema (default: True)

Returns:
    The decorator definition as a dictionary

Raises:
    json.JSONDecodeError: If the JSON is invalid
    jsonschema.exceptions.ValidationError: If validation fails

**Signature:** `load_from_string(self, json_string: str, validate: bool = True) -> Dict[str, Any]`

**Parameters:**

- `json_string`: `str`
- `validate`: `bool` (default: `True`)

**Returns:** `Dict`

## Functions

### `load_json_file`

Load a JSON file.

Args:
    file_path: Path to the JSON file

Returns:
    The loaded JSON data as a dictionary

Raises:
    FileNotFoundError: If the file is not found
    json.JSONDecodeError: If the JSON is invalid

**Signature:** `load_json_file(file_path: str) -> Dict[str, Any]`

**Parameters:**

- `file_path`: `str`

**Returns:** `Dict`

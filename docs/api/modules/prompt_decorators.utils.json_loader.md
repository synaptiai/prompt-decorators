# Module `prompt_decorators.utils.json_loader`

JSON loading utilities for decorator definitions.

This module provides utilities for loading and validating decorator definitions from JSON.

## Classes

- [`JSONLoader`](#class-jsonloader): Loader for decorator definitions from JSON.

### Class `JSONLoader`

Loader for decorator definitions from JSON.

This class provides utilities for loading decorator definitions from JSON strings,
files, or directories, and validating them against a schema.

#### Methods

- `__init__(schema_path)`
- `load_from_directory(directory_path, validate=True) -> typing.List[typing.Dict[str, typing.Any]]`
- `load_from_file(file_path, validate=True) -> typing.Dict[str, typing.Any]`
- `load_from_string(json_string, validate=True) -> typing.Dict[str, typing.Any]`

## Functions

- [`load_json_file`](#function-load_json_file): Load a JSON file.

### Function `load_json_file`

**Signature:** `load_json_file(file_path) -> typing.Dict[str, typing.Any]`

Load a JSON file.

Args:
    file_path: Path to the JSON file

Returns:
    The loaded JSON data as a dictionary

Raises:
    FileNotFoundError: If the file is not found
    json.JSONDecodeError: If the JSON is invalid

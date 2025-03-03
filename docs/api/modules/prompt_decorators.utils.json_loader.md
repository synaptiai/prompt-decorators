# Module `prompt_decorators.utils.json_loader`

JSON Loader Module

This module provides utilities for loading decorator definitions from JSON.

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

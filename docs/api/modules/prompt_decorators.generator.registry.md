# Module `prompt_decorators.generator.registry`

Registry Scanner Module

This module scans the registry directory and parses decorator JSON files.

## Classes

- [`RegistryScanner`](#class-registryscanner): Scanner for decorator registry files.

### Class `RegistryScanner`

Scanner for decorator registry files.

#### Methods

- `__init__(registry_path)`
- `get_decorators_by_category(category) -> typing.List[typing.Dict[str, typing.Any]]`
- `scan() -> typing.List[typing.Dict[str, typing.Any]]`

## Functions

- [`scan_registry`](#function-scan_registry): Scan the registry at the given path and return all decorator definitions.

### Function `scan_registry`

**Signature:** `scan_registry(registry_path) -> typing.List[typing.Dict[str, typing.Any]]`

Scan the registry at the given path and return all decorator definitions.

Args:
    registry_path: Path to the decorator registry

Returns:
    List of decorator definitions

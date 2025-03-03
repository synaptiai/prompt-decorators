# Module `prompt_decorators.generator.code_gen`

Code Generator Module.

This module generates Python code from decorator definitions in the registry.

## Classes

- [`CodeGenerator`](#class-codegenerator): Generator for Python code from decorator definitions.

### Class `CodeGenerator`

Generator for Python code from decorator definitions.

#### Methods

- `__init__(decorators)`
- `generate_all() -> dict[str, str]`

## Functions

- [`camel_to_snake`](#function-camel_to_snake): Convert CamelCase to snake_case.
- [`generate_code`](#function-generate_code): Generate Python code from decorator definitions.
- [`snake_to_camel`](#function-snake_to_camel): Convert snake_case to CamelCase.

### Function `camel_to_snake`

**Signature:** `camel_to_snake(name) -> <class 'str'>`

Convert CamelCase to snake_case.

### Function `generate_code`

**Signature:** `generate_code(decorators, output_dir) -> typing.Dict[str, str]`

Generate Python code from decorator definitions.

Args:
    decorators: List of decorator definitions
    output_dir: Optional output directory to write files to

Returns:
    Dictionary mapping file paths to generated code

### Function `snake_to_camel`

**Signature:** `snake_to_camel(name) -> <class 'str'>`

Convert snake_case to CamelCase.

If the input is already in camelCase, it will be properly converted to CamelCase
with the first letter capitalized.

Args:
    name: The name to convert

Returns:
    The converted name

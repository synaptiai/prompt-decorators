# Module `prompt_decorators.generator.code_gen`

Code Generator Module

This module generates Python code from decorator definitions in the registry.

## Classes

- [`CodeGenerator`](#class-codegenerator): Generator for Python code from decorator definitions.

### Class `CodeGenerator`

Generator for Python code from decorator definitions.

#### Methods

- `__init__(decorators)`
- `generate_all() -> typing.Dict[str, str]`

## Functions

- [`generate_code`](#function-generate_code): Generate Python code from decorator definitions.

### Function `generate_code`

**Signature:** `generate_code(decorators, output_dir) -> typing.Dict[str, str]`

Generate Python code from decorator definitions.

Args:
    decorators: List of decorator definitions
    output_dir: Optional output directory to write files to
    
Returns:
    Dictionary mapping file paths to generated code


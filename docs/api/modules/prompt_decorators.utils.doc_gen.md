# Module `prompt_decorators.utils.doc_gen`

Documentation Generator Module

This module provides utilities for generating API documentation from code and registry metadata.

## Classes

- [`DocGenerator`](#class-docgenerator): Generator for API documentation from code and registry metadata.

### Class `DocGenerator`

Generator for API documentation from code and registry metadata.

This class provides utilities for extracting docstrings, type annotations,
and other metadata from Python code, and generating documentation in various formats.

#### Methods

- `__init__(package_path, registry_path, output_dir)`
- `extract_package_docs(package_name) -> typing.Dict[str, typing.Any]`
- `generate_cli() -> <class 'NoneType'>`
- `generate_html_docs(output_dir) -> <class 'NoneType'>`
- `generate_markdown_docs(output_dir) -> <class 'NoneType'>`
- `load_registry_data() -> typing.Dict[str, typing.Dict[str, typing.Any]]`
- `merge_code_and_registry_docs() -> typing.Dict[str, typing.Dict[str, typing.Any]]`

## Functions

- [`get_doc_generator`](#function-get_doc_generator): Get a documentation generator.

### Function `get_doc_generator`

**Signature:** `get_doc_generator(package_path, registry_path, output_dir) -> <class 'prompt_decorators.utils.doc_gen.DocGenerator'>`

Get a documentation generator.

Args:
    package_path: Path to the Python package to document
    registry_path: Path to the registry directory containing decorator definitions
    output_dir: Directory where documentation should be written

Returns:
    A documentation generator instance

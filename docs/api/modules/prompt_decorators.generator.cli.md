# Module `prompt_decorators.generator.cli`

CLI for the prompt decorators generator.

This module provides a command-line interface for:
1. Scanning the registry for decorator definitions
2. Generating Python code for the decorators
3. Generating tests for the decorators

## Functions

- [`generate_code`](#function-generate_code): Generate Python code for decorators in the registry.
- [`generate_tests`](#function-generate_tests): Generate tests for decorators in the registry.
- [`main`](#function-main): Main entry point for the CLI.
- [`scan_registry`](#function-scan_registry): Scan the registry and report on found decorators.

### Function `generate_code`

**Signature:** `generate_code(args) -> <class 'NoneType'>`

Generate Python code for decorators in the registry.

Args:
    args: Command-line arguments

### Function `generate_tests`

**Signature:** `generate_tests(args) -> <class 'NoneType'>`

Generate tests for decorators in the registry.

Args:
    args: Command-line arguments

### Function `main`

**Signature:** `main() -> <class 'NoneType'>`

Main entry point for the CLI.

### Function `scan_registry`

**Signature:** `scan_registry(args) -> <class 'NoneType'>`

Scan the registry and report on found decorators.

Args:
    args: Command-line arguments

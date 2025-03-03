# Prompt Decorators Script Tools

This directory contains utility scripts for working with the prompt decorators registry and codebase. The scripts help with validation, code generation, and test generation.

## Recommended Scripts

### 📌 `registry_tools.py` (Unified Tool)

This is the **recommended** tool for all registry-related operations. It provides a unified interface for validation, code generation, and test generation.

```bash
# Show available commands
python scripts/registry_tools.py --help

# Validate the registry
python scripts/registry_tools.py validate

# Generate Python code
python scripts/registry_tools.py generate-code

# Generate tests
python scripts/registry_tools.py generate-tests

# Run all operations in sequence (validate, generate code, generate tests)
python scripts/registry_tools.py all
```

## Development Scripts

These scripts may be useful for development purposes:

- `run_tests.py` - Helper script for running tests

## Contributing

When adding new functionality:

1. Consider adding it to the unified `registry_tools.py` script rather than creating new scripts
2. Ensure the new functionality is well-documented with docstrings and command-line help
3. Add appropriate error handling and logging
4. Follow the existing code style and patterns

## Workflow

The typical workflow for working with the prompt decorators registry is:

1. Make changes to JSON files in the `registry/` directory
2. Run `python scripts/registry_tools.py validate` to validate the registry
3. Run `python scripts/registry_tools.py generate-code` to generate Python code
4. Run `python scripts/registry_tools.py generate-tests` to generate tests
5. Run tests to ensure everything works correctly: `python -m pytest tests/auto -v`

For convenience, you can run all the steps at once with `python scripts/registry_tools.py all`.

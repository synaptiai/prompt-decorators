# Prompt Decorators Development Guide

This comprehensive guide provides detailed instructions for developers contributing to the Prompt Decorators project. It covers development environment setup, workflow, code standards, and best practices.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Development Environment](#development-environment)
3. [Project Structure](#project-structure)
4. [Development Workflow](#development-workflow)
5. [Code Standards](#code-standards)
6. [Testing](#testing)
7. [Documentation](#documentation)
8. [CI/CD and Automation](#cicd-and-automation)
9. [Release Process](#release-process)
10. [Troubleshooting](#troubleshooting)

## Prerequisites

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/) 1.4.0 or higher
- Git

## Development Environment

### Setting Up the Environment

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/prompt-decorators.git
   cd prompt-decorators
   ```

2. **Install Poetry** (if not already installed)

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install Dependencies**

   ```bash
   # Install all dependencies (including development and documentation)
   poetry install

   # Activate the virtual environment
   poetry shell
   ```

4. **Set Up Pre-commit Hooks**

   ```bash
   # Install and set up pre-commit hooks
   python scripts/setup_pre_commit.py
   ```

## Project Structure

The codebase is organized into the following main directories:

- **prompt_decorators/**
  - **core/**: Base classes and core functionality
  - **decorators/**: Decorator implementations
    - **generated/**: Auto-generated decorator classes
  - **generator/**: Code generation utilities
  - **utils/**: Utility functions and helpers
- **docs/**: Documentation files
- **tests/**: Test suite
- **scripts/**: Utility scripts for development
- **registry/**: JSON definitions for decorators
- **examples/**: Example scripts and notebooks

Key architectural features:
- Clean dependency flow from decorators → core and utils → core
- Separation of user-defined and generated code
- Registry-driven approach for decorator definitions

## Development Workflow

### Workflow with Poetry

Poetry provides a modern workflow for dependency management:

```bash
# Add a new dependency
poetry add package-name

# Add a development dependency
poetry add --group dev package-name

# Update dependencies
poetry update

# Run commands within the virtual environment
poetry run python script.py

# Build the package
poetry build
```

### Code Quality Tools

Our pre-commit hooks automate code quality checks, but you can also run them manually:

```bash
# Format code with Black
poetry run black prompt_decorators tests

# Sort imports with isort
poetry run isort prompt_decorators tests

# Lint code with Ruff
poetry run ruff prompt_decorators tests

# Type check with mypy
poetry run mypy prompt_decorators

# Check docstrings
python scripts/standardize_docstrings.py prompt_decorators --check

# Run all checks at once
pre-commit run --all-files
```

## Code Standards

### Import Formatting

We use `isort` with the following configuration:

```toml
[tool.isort]
profile = "black"
line_length = 88
multi_line_output = 3
```

Key rules:
- Standard library imports first, followed by third-party, then local imports
- Alphabetical ordering within each group
- Consistent use of `from x import y` style

### Python Code Style

We follow the Black code style with a line length of 88 characters:

```toml
[tool.black]
line-length = 88
target-version = ["py38", "py39", "py310", "py311"]
```

### Type Annotations

All functions and methods must have type annotations:

```python
def calculate_average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)
```

### Docstrings

We use Google-style docstrings throughout the codebase:

```python
def function_name(param1: str, param2: int) -> bool:
    """Short description of the function.

    More detailed description that can span multiple lines.

    Args:
        param1: Description of the first parameter.
        param2: Description of the second parameter.

    Returns:
        Description of the return value.

    Raises:
        ExceptionType: When and why this exception is raised.
    """
```

Required sections:
1. Short description (one line)
2. Detailed description (optional, can be multi-line)
3. Args (required if the function takes parameters)
4. Returns (required if the function returns a value)
5. Raises (optional, document exceptions that might be raised)

## Testing

We use pytest for testing:

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=prompt_decorators

# Run a specific test
poetry run pytest tests/test_specific_file.py::TestClass::test_specific_function
```

### Test Generation

For new decorators, tests can be auto-generated:

```bash
python scripts/generate_tests.py --registry-dir registry --output-dir tests/auto
```

## Documentation

We use MkDocs with the Material theme for documentation:

```bash
# Serve documentation locally
poetry run mkdocs serve

# Build documentation
poetry run mkdocs build
```

### Documentation Standards

1. **Code Reference Documentation**: Generated from docstrings
2. **User Guides**: Markdown files in the `docs/` directory
3. **Examples**: Executable examples in the `examples/` directory
4. **Tutorials**: Step-by-step guides in the `docs/tutorials/` directory

## CI/CD and Automation

### GitHub Actions Workflows

We have several GitHub Actions workflows:

1. **Code Quality**: Runs on all pull requests and pushes to main
   - Pre-commit checks
   - Tests on multiple Python versions
   - Type checking
   - Docstring validation

2. **Documentation**: Builds and deploys documentation when relevant files change

3. **Publish**: Publishes the package to PyPI when a new release is created

### Pre-commit Hooks

Our pre-commit hooks enforce:
- Code formatting with Black
- Import sorting with isort
- Linting with Ruff
- Type checking with mypy
- Documentation standards

## Release Process

To create a new release:

1. Update the version number in pyproject.toml
2. Update the CHANGELOG.md file
3. Create a pull request with these changes
4. After merging, create a new GitHub release with a tag matching the version
5. The GitHub Actions workflow will automatically publish to PyPI

## Troubleshooting

### Common Issues

#### Import Errors

If you encounter import errors, make sure your virtual environment is activated:

```bash
poetry shell
```

#### Pre-commit Hook Issues

If pre-commit hooks are failing:

```bash
# Update pre-commit hooks
pre-commit autoupdate

# Run with verbose output to debug
pre-commit run --all-files --verbose
```

#### Poetry Issues

If poetry is having dependency resolution issues:

```bash
# Clear poetry cache
poetry cache clear --all pypi

# Update poetry itself
pip install --upgrade poetry
```

## Additional Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [Black Documentation](https://black.readthedocs.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)

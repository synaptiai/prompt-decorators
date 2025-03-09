# Development Setup

This guide will help you set up a development environment for contributing to the Prompt Decorators project.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.11 or higher
- [Git](https://git-scm.com/)
- [Poetry](https://python-poetry.org/) (recommended) or pip

## Setting Up Your Development Environment

### 1. Clone the Repository

```bash
git clone https://github.com/synaptiai/prompt-decorators.git
cd prompt-decorators
```

### 2. Set Up a Virtual Environment

#### Using Poetry (Recommended)

Poetry automatically creates and manages a virtual environment for you:

```bash
# Install dependencies
poetry install

# Install development dependencies
poetry install --with dev,test,docs
```

#### Using venv and pip

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -e ".[dev,test,docs]"
```

### 3. Install Pre-commit Hooks

We use pre-commit hooks to ensure code quality:

```bash
# Install pre-commit
pip install pre-commit

# Install the pre-commit hooks
pre-commit install
```

### 4. Run Tests to Verify Setup

```bash
# Using Poetry
poetry run pytest

# Using pip
pytest
```

If all tests pass, your environment is set up correctly!

## Project Structure

The project follows this structure:

```
prompt-decorators/
├── prompt_decorators/          # Main package
│   ├── __init__.py             # Package exports
│   ├── core/                   # Core decorator functionality
│   ├── schemas/                # JSON schemas
│   ├── utils/                  # Utility functions
│   └── integrations/           # Integration with other systems
├── registry/                   # Decorator definitions
├── schemas/                    # JSON schema definitions
├── tests/                      # Test suite
├── docs/                       # Documentation
├── examples/                   # Example usage
├── scripts/                    # Development scripts
├── pyproject.toml              # Project metadata and dependencies
└── README.md                   # Project overview
```

## Development Workflow

### Setting Up Your Branch

```bash
# Create a new branch for your feature/bugfix
git checkout -b feature/your-feature-name
```

### Making Changes

1. Make your changes to the codebase
2. Write tests for your changes
3. Update documentation if necessary

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=prompt_decorators

# Run specific tests
pytest tests/test_specific_file.py

# Run tests with verbose output
pytest -v
```

### Running Linters

```bash
# Run ruff (linting and formatting)
ruff check .
ruff format .

# Run mypy (type checking)
mypy prompt_decorators
```

### Building Documentation

```bash
# Build documentation
cd docs
mkdocs build

# Serve documentation locally
mkdocs serve
```

Then visit http://localhost:8000 to view the documentation.

## Working with Decorators

### Creating a New Decorator

1. Define your decorator in the registry directory:

```json
// registry/my_custom_decorator.json
{
  "name": "MyCustomDecorator",
  "description": "A custom decorator that does X",
  "category": "Custom",
  "parameters": [
    {
      "name": "param1",
      "type": "string",
      "description": "Description of parameter",
      "default": "default value"
    }
  ],
  "transform_function": "return 'Modified: ' + text;"
}
```

2. Test your decorator:

```python
from prompt_decorators import apply_dynamic_decorators, register_decorator, DecoratorDefinition

# Define your decorator in Python
my_decorator_def = DecoratorDefinition(
    name="MyCustomDecorator",
    description="A custom decorator that does X",
    category="Custom",
    parameters=[
        {
            "name": "param1",
            "type": "string",
            "description": "Description of parameter",
            "default": "default value"
        }
    ],
    transform_function="return 'Modified: ' + text;"
)

# Register it
register_decorator(my_decorator_def)

# Test it
prompt = """
+++MyCustomDecorator(param1="test value")
This is a test prompt
"""

transformed = apply_dynamic_decorators(prompt)
print(transformed)
```

### Running the Validator

Use the validator to check your decorator:

```bash
python -m prompt_decorators.tools.validator validate path/to/my_decorator.json
```

## Code Style Guidelines

### Python Code

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use ruff for formatting and linting
- Include type hints for all functions and methods
- Write docstrings in Google style format

### Decorator Definitions

- Use clear, descriptive names for decorators and parameters
- Provide comprehensive descriptions
- Include reasonable default values for parameters
- Write efficient transform functions

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(optional scope): <description>

[optional body]

[optional footer(s)]
```

Types include:
- `feat:` (new feature)
- `fix:` (bug fix)
- `docs:` (documentation changes)
- `style:` (formatting changes)
- `refactor:` (code restructuring)
- `test:` (adding or refining tests)
- `chore:` (maintenance tasks)

## Contributing Changes

### Pull Request Process

1. Ensure all tests pass
2. Update documentation if needed
3. Create a pull request with a clear description of changes
4. Reference any related issues
5. Wait for review and address any feedback

### Code Review Checklist

Before submitting a PR, check that:

- [ ] Code follows the project's style guidelines
- [ ] Tests are added/updated and all tests pass
- [ ] Documentation is updated to reflect changes
- [ ] Code is properly typed with type annotations
- [ ] Pre-commit hooks pass with no issues
- [ ] Commit messages follow the project's format

## Dependency Management

### Adding a New Dependency

#### Using Poetry

```bash
# Add a main dependency
poetry add package-name

# Add a development dependency
poetry add --group dev package-name

# Add a test dependency
poetry add --group test package-name

# Add a documentation dependency
poetry add --group docs package-name
```

#### Using pip

Update `setup.py` or `pyproject.toml` with the new dependency, then:

```bash
pip install -e ".[dev,test,docs]"
```

## Testing Guidelines

### Writing Tests

- Every feature should have corresponding tests
- Use pytest fixtures for common test setups
- Aim for high test coverage (>90%)
- Include both unit tests and integration tests

### Test Structure

```python
import pytest
from prompt_decorators import apply_dynamic_decorators

def test_decorator_functionality():
    """Test that the decorator transforms the text as expected."""
    # Arrange
    prompt = """
    +++TestDecorator(param1="value")
    Test prompt
    """

    # Act
    result = apply_dynamic_decorators(prompt)

    # Assert
    assert "Expected transformation" in result
    assert "Test prompt" in result
```

## Release Process

### Preparing a Release

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Ensure all tests pass
4. Build the distribution:

```bash
# Using Poetry
poetry build

# Using setuptools
python -m build
```

### Publishing a Release

```bash
# Using Poetry
poetry publish

# Using Twine
twine upload dist/*
```

## Continuous Integration

We use GitHub Actions for CI. Workflows are defined in `.github/workflows/`:

- `tests.yml`: Runs tests on multiple Python versions
- `lint.yml`: Runs linters and style checks
- `docs.yml`: Builds and validates documentation
- `release.yml`: Handles package publishing

## Getting Help

If you need help during development:

- Check the [documentation](https://synaptiai.github.io/prompt-decorators/)
- Open an issue on GitHub
- Contact the maintainers

## Next Steps

- Read the [development guide](development_guide.md) for more detailed workflow information
- Check the [core concepts](concepts.md) to understand the framework's architecture
- Explore the [tutorials](tutorials/creating_custom_decorator.md) for practical examples

# Docstring Standards

This document outlines the docstring standards for the `prompt-decorators` project. All Python code in this project should follow these guidelines to ensure consistency and maintainability.

## Google-Style Docstrings

We use Google-style docstrings throughout the codebase. This style is chosen for its readability and compatibility with documentation generation tools.

### Basic Format

```python
def function_name(param1, param2):
    """Short description of the function.

    More detailed description that can span multiple lines and provide
    additional context about what the function does.

    Args:
        param1: Description of the first parameter.
        param2: Description of the second parameter.

    Returns:
        Description of the return value.

    Raises:
        ExceptionType: When and why this exception is raised.
    """
    # Function implementation
```

### Required Sections

1. **Short Description**: A concise one-line summary of what the function/class/method does.
2. **Detailed Description** (optional): A more detailed explanation if needed.
3. **Args**: Required if the function takes parameters (other than self/cls for methods).
4. **Returns**: Required if the function returns a value (other than None).
5. **Raises** (optional): Document exceptions that might be raised.

### Class Docstrings

```python
class ClassName:
    """Short description of the class.

    More detailed description of the class and its behavior.

    Attributes:
        attr1: Description of attr1.
        attr2: Description of attr2.
    """
```

### Method Docstrings

```python
def method_name(self, param1):
    """Short description of the method.

    Args:
        param1: Description of param1.

    Returns:
        Description of the return value.
    """
```

## Type Annotations

In addition to docstrings, all functions and methods should include type annotations:

```python
def function_name(param1: str, param2: int) -> bool:
    """Function description.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of the return value.
    """
```

## Examples

### Function Example

```python
def calculate_average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers: A list of numbers to average.

    Returns:
        The average value.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
```

### Class Example

```python
class DecoratorBase:
    """Base class for all decorators.

    This class provides the foundation for creating decorators with
    consistent interfaces and behaviors.

    Attributes:
        name: The name of the decorator.
        version: The version of the decorator.
        parameters: Dictionary of parameters for the decorator.
    """

    def __init__(self, name: str, version: str, parameters: Dict[str, Any]):
        """Initialize the decorator.

        Args:
            name: The name of the decorator.
            version: The version of the decorator.
            parameters: Dictionary of parameters for the decorator.
        """
        self.name = name
        self.version = version
        self.parameters = parameters

    def apply(self, text: str) -> str:
        """Apply the decorator to the input text.

        Args:
            text: The input text to decorate.

        Returns:
            The decorated text.
        """
        raise NotImplementedError("Subclasses must implement apply()")
```

## Checking and Fixing Docstrings

We have tools to check and fix docstring issues:

1. **Check docstrings**:
   ```bash
   python scripts/standardize_docstrings.py prompt_decorators --report
   ```

2. **Check without fixing (returns error code if issues found)**:
   ```bash
   python scripts/standardize_docstrings.py prompt_decorators --check
   ```

3. **Fix docstrings automatically**:
   ```bash
   python scripts/fix_docstrings.py prompt_decorators
   ```

Our docstring tools can detect several issues:
- Missing docstrings
- Missing required sections (Args, Returns)
- Malformed sections
- Inconsistent formatting

### Using the Standardization Script

The `standardize_docstrings.py` script offers several options:

```bash
python scripts/standardize_docstrings.py [path] [options]
```

Options:
- `--exclude [dirs]`: Directories to exclude
- `--report`: Generate a detailed report of issues
- `--check`: Only check for issues, don't fix (exits with code 1 if issues found)

The docstring standardization script uses Python's AST (Abstract Syntax Tree) to analyze Python files and identify docstring issues. It checks:

1. Functions with arguments that lack an Args section
2. Functions with return values that lack a Returns section
3. Malformed Args and Returns sections
4. Missing docstrings in functions, classes, and modules

## Integration with Development Workflow

Docstring checking is integrated into our development workflow through various mechanisms:

### Pre-commit Hooks

Our pre-commit configuration includes a docstring check that runs before each commit:

```yaml
- id: check-docstrings
  name: check-docstrings
  entry: python standardize_docstrings.py
  language: python
  types: [python]
  args: ["--check"]
  description: Check that docstrings follow Google-style format
```

This prevents commits that would introduce docstring issues.

### CI/CD Integration

GitHub Actions runs docstring checks on all pull requests and pushes to main branches:

```yaml
jobs:
  docstring-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install poetry
          poetry install
      - name: Check docstrings
        run: python standardize_docstrings.py prompt_decorators --check
```

This ensures that all merged code maintains high docstring quality standards.

## Current Status and Known Issues

As of the latest update, we've identified and are addressing several docstring issues across the codebase:

- 75 issues across 16 files for missing Args/Returns sections in function docstrings
- 8 issues for malformed Args sections
- 1 issue for a missing docstring

Our roadmap includes resolving all these issues as part of our code quality improvements before the next major release.

### Manual Fixes in Progress

While our automated tools can identify issues, some complex cases require manual intervention. We're currently working on:

1. Adding detailed parameter descriptions for complex functions
2. Improving return value descriptions
3. Adding examples to key API functions

Progress on fixing these issues is tracked in our project roadmap.

## Additional Resources

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [pydocstyle](https://www.pydocstyle.org/en/stable/) - A tool for checking compliance with Python docstring conventions

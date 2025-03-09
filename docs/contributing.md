# Contributing to Prompt Decorators

Thank you for your interest in contributing to the Prompt Decorators project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please read and follow our [Code of Conduct](https://github.com/yourusername/prompt-decorators/blob/main/CODE_OF_CONDUCT.md).

## How to Contribute

There are many ways to contribute to the Prompt Decorators project:

1. **Report bugs**: If you find a bug, please create an issue on our [GitHub repository](https://github.com/yourusername/prompt-decorators/issues).
2. **Suggest features**: If you have an idea for a new feature, please create an issue on our [GitHub repository](https://github.com/yourusername/prompt-decorators/issues).
3. **Improve documentation**: Help us improve our documentation by fixing typos, adding examples, or clarifying explanations.
4. **Write code**: Contribute bug fixes, new features, or improvements to existing features.

## Development Setup

### Prerequisites

- Python 3.11 or higher
- Poetry (dependency management)
- git

### Setting Up the Development Environment

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/prompt-decorators.git
   cd prompt-decorators
   ```
3. Install Poetry if you don't have it already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
4. Install the package with all dependencies:
   ```bash
   poetry install
   ```

### Running Tests

We use pytest for testing. To run the tests:

```bash
poetry run pytest
```

To run tests with coverage:

```bash
poetry run pytest --cov=prompt_decorators
```

### Code Style

We follow the PEP 8 style guide for Python code. We use the following tools to enforce code style:

- **black**: For code formatting
- **isort**: For import sorting
- **ruff**: For linting

To format your code:

```bash
poetry run black prompt_decorators tests
poetry run isort prompt_decorators tests
```

To check your code for style issues:

```bash
poetry run ruff check prompt_decorators tests
```

### Type Checking

We use mypy for type checking. To run type checking:

```bash
poetry run mypy prompt_decorators
```

### Docstring Standards

We follow **Google-style docstrings** for all Python code. Please refer to our [Docstring Standards](DOCSTRING_STANDARDS.md) for detailed guidelines.

To check if your docstrings follow our standards:

```bash
./standardize_docstrings.py path/to/your/file.py --report
```

To automatically fix common docstring issues:

```bash
./fix_docstrings.py path/to/your/file.py
```

We've also set up pre-commit hooks to check docstrings before commits:

```bash
# Install pre-commit hooks
poetry run pre-commit install
```

### Pre-commit Hooks

We use pre-commit hooks to check code style, types, and docstrings before commits. To install the pre-commit hooks:

```bash
poetry run pre-commit install
```

## Pull Request Process

1. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them with a descriptive commit message.
3. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
4. Create a pull request from your branch to the main repository.
5. Ensure that all tests pass and there are no style issues.
6. Update the documentation if necessary.
7. Wait for a maintainer to review your pull request.

## Adding a New Decorator

To add a new decorator to the registry:

1. Create a new JSON file in the appropriate category directory under `registry/`.
2. Define the decorator's parameters, constraints, and metadata.
3. Run the code generation script:
   ```bash
   poetry run python generate_decorators.py
   ```
4. Add tests for your new decorator.
5. Update the documentation if necessary.

## Documentation

We use MkDocs with the Material theme for documentation. To build the documentation locally:

```bash
poetry run mkdocs serve
```

This will start a local server at http://localhost:8000 where you can preview the documentation.

## License

By contributing to the Prompt Decorators project, you agree that your contributions will be licensed under the project's [MIT License](https://github.com/yourusername/prompt-decorators/blob/main/LICENSE).

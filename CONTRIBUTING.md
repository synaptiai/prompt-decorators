# Contributing to Prompt Decorators

Thank you for your interest in contributing to the Prompt Decorators project! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Environment](#development-environment)
4. [Project Structure](#project-structure)
5. [Coding Standards](#coding-standards)
6. [Testing](#testing)
7. [Documentation](#documentation)
8. [Pull Request Process](#pull-request-process)
9. [Registry Contributions](#registry-contributions)
10. [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## Getting Started

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/synaptiai/prompt-decorators.git
   cd prompt-decorators
   ```
3. **Set up the upstream remote**:
   ```bash
   git remote add upstream https://github.com/synaptiai/prompt-decorators.git
   ```
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Environment

We recommend using Poetry for dependency management and a virtual environment for development:

### Using Poetry
```bash
# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Activate the virtual environment
poetry shell
```

### Using venv
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate.bat

# Activate on Unix/MacOS
source venv/bin/activate

# Install dependencies with pip
pip install -e ".[dev,docs,all]"
```

### Setting up pre-commit hooks

We use pre-commit hooks to ensure code quality standards are met before committing changes. To set up the hooks:

```bash
# Using our setup script (recommended)
python scripts/setup_pre_commit.py

# Or manually
pip install pre-commit
pre-commit install
```

The pre-commit hooks will automatically check your code for:
- Formatting issues (black, isort)
- Linting issues (ruff)
- Type checking (mypy)
- Missing docstrings
- And more...

You can also run the hooks manually on all files:
```bash
pre-commit run --all-files
```

## Project Structure

The project follows this structure:

```
prompt-decorators/
├── docs/                       # Documentation files
├── examples/                   # Example scripts and notebooks
├── prompt_decorators/          # Main package
│   ├── core/                   # Core functionality
│   ├── decorators/             # Decorator implementations
│   │   └── generated/          # Generated decorators from registry
│   ├── generator/              # Code generation utilities
│   ├── registry/               # Decorator registry
│   └── utils/                  # Utility functions
├── tests/                      # Test suite
├── .github/                    # GitHub workflows and config
├── pyproject.toml              # Project configuration
├── setup.py                    # Setup script
└── README.md                   # Project overview
```

## Coding Standards

We follow these coding standards:

1. **Type Hints**: All functions and methods must have type annotations.
2. **Docstrings**: All functions, methods, and classes should have Google-style docstrings.
3. **Code Formatting**: We use `black` for code formatting and `isort` for import sorting.
4. **Linting**: We use `ruff` for linting to ensure code quality.
5. **Type Checking**: We use `mypy` for static type checking.
6. **Imports**: Use absolute imports for all imports.

Run our code quality tools:
```bash
# Format code
poetry run black prompt_decorators tests

# Sort imports
poetry run isort prompt_decorators tests

# Lint code
poetry run ruff prompt_decorators tests

# Type check
poetry run mypy prompt_decorators

# Check docstrings
python standardize_docstrings.py prompt_decorators --check

# Run all checks (using pre-commit)
pre-commit run --all-files
```

## Testing

We use `pytest` for testing. All tests should be placed in the `tests/` directory:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=prompt_decorators

# Run a specific test file
pytest tests/test_specific_module.py
```

### Testing Guidelines

1. All new features should include tests.
2. Tests should be independent of each other.
3. Use fixtures and parameterization where appropriate.
4. Mock external APIs in tests.

## Documentation

We use MkDocs with the Material theme for documentation:

```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

### Documentation Guidelines

1. Update or add documentation for any changes or additions.
2. Include docstrings for all public classes, methods, and functions.
3. Document parameters, return values, and exceptions.
4. Include examples where helpful.

## Pull Request Process

1. **Update your fork** with the latest changes from upstream:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Commit your changes** with clear, descriptive messages following [conventional commits](https://www.conventionalcommits.org/):
   ```bash
   git add .
   git commit -m "feat: add new feature X"
   ```
   Common types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

3. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request** against the main repository's `main` branch.

5. **Complete the PR template** with details about your changes.

### PR Requirements

- **Tests**: All tests must pass.
- **Code Quality**: PR should pass all code quality checks.
- **Documentation**: Include documentation updates if applicable.
- **Single Purpose**: PR should address a single concern.
- **Reviews**: PR requires at least one maintainer review.

## Registry Contributions

When adding new decorators to the registry:

1. Create a JSON file in the `registry/` directory following the schema.
2. Include comprehensive parameters, documentation, and examples.
3. Ensure compatibility information is accurate.
4. Run the code generator to create the Python class.
5. Add tests for the new decorator.

## Community

- **Issues**: Use GitHub issues for bug reports and feature requests.
- **Discussions**: Use GitHub discussions for questions and general discussion.
- **Code Review**: Be respectful and constructive in code reviews.

## Specific Contribution Areas

### 1. Adding New Decorators

To add a new decorator:

1. Create a JSON file in `registry/` following the naming convention: `decorator-name.json`.
2. Run the code generator to create the Python class.
3. Add tests for the new decorator in `tests/decorators/`.
4. Add example usage in the `examples/` directory.
5. Update documentation to include the new decorator.

### 2. Improving Documentation

Documentation improvements are always welcome:

1. Update API documentation.
2. Add or improve tutorials and guides.
3. Fix typos or clarify existing documentation.
4. Add examples of real-world usage.

### 3. Bug Fixes

When fixing bugs:

1. Add a test that reproduces the bug.
2. Fix the bug.
3. Ensure all tests pass.
4. Update documentation if necessary.

### 4. Feature Requests

For feature requests:

1. Open an issue describing the feature.
2. Discuss the feature with maintainers.
3. Implement the feature after approval.

## License

By contributing to this project, you agree that your contributions will be licensed under the same [MIT License](LICENSE) that covers the project.

Thank you for contributing to Prompt Decorators!

## Continuous Integration

We use GitHub Actions for continuous integration. Every pull request will automatically run:

1. **Pre-commit checks**: Code formatting, linting, and other quality checks
2. **Tests**: On multiple Python versions
3. **Type checking**: Using mypy
4. **Docstring validation**: Ensuring all docstrings follow our standards

If any of these checks fail, please fix the issues before requesting a review.

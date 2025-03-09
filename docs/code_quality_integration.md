# Code Quality Integration

This document outlines the code quality tools, processes, and integrations used in the Prompt Decorators project to maintain high standards of code quality.

## Overview

The Prompt Decorators project employs a comprehensive set of code quality tools and processes to ensure:

- Consistent code style and formatting
- Static type checking
- Comprehensive test coverage
- Documentation quality
- Security scanning
- Continuous integration

## Code Quality Tools

### Linting and Formatting

#### Ruff

[Ruff](https://github.com/charliermarsh/ruff) is the primary tool for linting and formatting Python code in the project. It replaces multiple tools (black, isort, flake8) with a single, fast tool.

Configuration is in `pyproject.toml`:

```toml
[tool.ruff]
line-length = 100
target-version = "py38"
select = ["E", "F", "I", "N", "B", "C4", "SIM", "ERA", "PL"]
ignore = ["E203", "E501"]

[tool.ruff.isort]
known-first-party = ["prompt_decorators"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

Usage:

```bash
# Check code
ruff check .

# Format code
ruff format .
```

### Type Checking

#### Mypy

[Mypy](https://mypy.readthedocs.io/) is used for static type checking to catch type-related errors before runtime.

Configuration is in `mypy.ini`:

```ini
[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True

[mypy.plugins.numpy.*]
follow_imports = skip

[mypy-pytest.*]
ignore_missing_imports = True
```

Usage:

```bash
mypy prompt_decorators
```

### Testing

#### Pytest

[Pytest](https://docs.pytest.org/) is used for unit and integration testing.

Configuration is in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"
python_classes = "Test*"
addopts = "--cov=prompt_decorators --cov-report=term --cov-report=xml"
```

Usage:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=prompt_decorators
```

#### Coverage

[Coverage.py](https://coverage.readthedocs.io/) is used to measure test coverage.

Configuration is in `.coveragerc`:

```ini
[run]
source = prompt_decorators
omit = tests/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
```

### Documentation Quality

#### Doc8

[Doc8](https://github.com/pycqa/doc8) is used to check documentation quality.

Configuration is in `pyproject.toml`:

```toml
[tool.doc8]
max-line-length = 100
ignore = ["D001"]
```

Usage:

```bash
doc8 docs/
```

### Security Scanning

#### Bandit

[Bandit](https://github.com/PyCQA/bandit) is used for security vulnerability scanning.

Configuration is in `.bandit`:

```ini
[bandit]
exclude = tests
```

Usage:

```bash
bandit -r prompt_decorators
```

## Pre-commit Integration

The project uses [pre-commit](https://pre-commit.com/) to run quality checks before each commit.

Configuration is in `.pre-commit-config.yaml`:

```yaml
repos:
-   repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.262
    hooks:
    -   id: ruff
        args: [--fix]
    -   id: ruff-format

-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
    -   id: mypy
        additional_dependencies: [types-requests, types-PyYAML]

-   repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
    -   id: bandit
        args: [-c, .bandit]
        exclude: tests/

-   repo: https://github.com/pycqa/doc8
    rev: v1.1.1
    hooks:
    -   id: doc8
        args: [--max-line-length=100]
```

Installation:

```bash
pip install pre-commit
pre-commit install
```

Usage:

```bash
# Run on all files
pre-commit run --all-files

# Run automatically on commit
git commit -m "Your commit message"
```

## Continuous Integration

### GitHub Actions

The project uses GitHub Actions for continuous integration.

#### Test Workflow

The test workflow runs tests on multiple Python versions:

```yaml
name: Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', '3.11']

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[test]"
    - name: Run tests
      run: |
        pytest --cov=prompt_decorators
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

#### Lint Workflow

The lint workflow checks code style and typing:

```yaml
name: Lint

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install ruff mypy
        pip install -e ".[dev]"
    - name: Lint with ruff
      run: |
        ruff check .
    - name: Check formatting with ruff
      run: |
        ruff format --check .
    - name: Type check with mypy
      run: |
        mypy prompt_decorators
```

#### Docs Workflow

The docs workflow builds and validates documentation:

```yaml
name: Docs

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[docs]"
    - name: Build docs
      run: |
        cd docs
        mkdocs build --strict
    - name: Check documentation quality
      run: |
        doc8 docs/
```

## Code Quality Metrics

### Coverage Reporting

The project uses [Codecov](https://codecov.io/) for coverage reporting.

Integration is through GitHub Actions:

```yaml
- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```

### Code Quality Badges

The project includes badges in the README.md to show code quality metrics:

```markdown
[![Tests](https://github.com/synaptiai/prompt-decorators/actions/workflows/tests.yml/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions/workflows/tests.yml)
[![Codecov](https://codecov.io/gh/synaptiai/prompt-decorators/branch/main/graph/badge.svg)](https://codecov.io/gh/synaptiai/prompt-decorators)
[![Documentation Status](https://github.com/synaptiai/prompt-decorators/actions/workflows/docs.yml/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions/workflows/docs.yml)
```

## Pull Request Quality Checks

Pull requests must pass all quality checks before merging:

1. All tests must pass
2. Code must be properly formatted
3. Type checking must pass
4. Documentation must build successfully
5. Test coverage must not decrease

GitHub branch protection rules enforce these requirements.

## Developer Workflow

### Local Quality Checks

Developers should run quality checks locally before pushing:

```bash
# Format code
ruff format .

# Check code
ruff check .

# Run type checking
mypy prompt_decorators

# Run tests
pytest

# Build docs
cd docs && mkdocs build
```

### CI/CD Pipeline

The CI/CD pipeline follows these steps:

1. **Lint**: Check code style and formatting
2. **Type Check**: Verify type annotations
3. **Test**: Run unit and integration tests
4. **Coverage**: Generate coverage reports
5. **Docs**: Build and validate documentation
6. **Security**: Scan for security vulnerabilities
7. **Release**: (On main branch) Build and publish package

## Setting Up Quality Tools

### For New Contributors

New contributors should set up the quality tools:

```bash
# Clone the repository
git clone https://github.com/synaptiai/prompt-decorators.git
cd prompt-decorators

# Install dependencies
pip install -e ".[dev,test,docs]"

# Install pre-commit hooks
pre-commit install
```

### For CI/CD Systems

CI/CD systems should install the necessary dependencies:

```bash
# Install dependencies
python -m pip install --upgrade pip
pip install -e ".[dev,test,docs]"
```

## Best Practices

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use consistent naming conventions
- Keep functions and methods focused and small
- Use descriptive variable names

### Type Annotations

- Use type annotations for all functions and methods
- Use `Optional[T]` for parameters that could be `None`
- Use `Union[T1, T2]` for parameters that could be multiple types
- Use `Any` only when absolutely necessary

### Testing

- Write tests for all new features and bug fixes
- Include both positive and negative test cases
- Test edge cases and error conditions
- Aim for high test coverage (>90%)

### Documentation

- Document all public APIs
- Keep documentation up to date with code changes
- Include examples in documentation
- Use clear, concise language

## Conclusion

The Prompt Decorators project maintains high code quality through a combination of automated tools, continuous integration, and developer best practices. By following these guidelines, contributors can help ensure the project remains maintainable, reliable, and secure.

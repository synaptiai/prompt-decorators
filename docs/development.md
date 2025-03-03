# Development Setup

This page provides a quick overview of the development setup for the Prompt Decorators framework. For a comprehensive guide, please see the [Development Guide](development_guide.md).

## Prerequisites

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- Git

## Quick Start

### Clone the Repository

```bash
git clone https://github.com/yourusername/prompt-decorators.git
cd prompt-decorators
```

### Install Dependencies with Poetry

```bash
# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

### Set Up Pre-commit Hooks

```bash
python scripts/setup_pre_commit.py
```

## Running Tests

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=prompt_decorators
```

## Building Documentation

```bash
# Serve documentation locally
poetry run mkdocs serve

# Build documentation
poetry run mkdocs build
```

## Code Quality Tools

```bash
# Run all checks
pre-commit run --all-files
```

## Additional Resources

For more detailed information, please refer to:

- [Development Guide](development_guide.md) - Comprehensive development documentation
- [Contributing Guide](contributing.md) - How to contribute to the project
- [Code Standards](DOCSTRING_STANDARDS.md) - Coding standards and docstring guidelines
- [Project Structure](project_summaries/code_structure_analysis.md) - Analysis of the codebase structure

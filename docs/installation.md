# Installation

This guide will help you install the Prompt Decorators framework and its dependencies.

## Requirements

- Python 3.8 or higher
- pip (Python package installer)

## Basic Installation

You can install the Prompt Decorators framework directly from PyPI (once it's published):

```bash
pip install prompt-decorators
```

## Development Installation

For development or to get the latest unreleased version, you can install directly from the GitHub repository:

```bash
git clone https://github.com/yourusername/prompt-decorators.git
cd prompt-decorators
pip install -e .
```

The `-e` flag installs the package in "editable" mode, which means changes to the source code will be immediately reflected without needing to reinstall.

## Installing with Optional Dependencies

The Prompt Decorators framework offers several optional dependency sets for different use cases:

### Development Dependencies

```bash
pip install prompt-decorators[dev]
```

This includes:
- pytest (for running tests)
- pytest-cov (for test coverage)
- black (for code formatting)
- isort (for import sorting)
- mypy (for type checking)
- ruff (for linting)

### Documentation Dependencies

```bash
pip install prompt-decorators[docs]
```

This includes:
- mkdocs (for building documentation)
- mkdocs-material (for documentation theme)
- mkdocstrings (for API documentation generation)

### LLM Provider Dependencies

```bash
# For OpenAI integration
pip install prompt-decorators[openai]

# For Anthropic integration
pip install prompt-decorators[anthropic]

# For LangChain integration
pip install prompt-decorators[langchain]
```

### All Dependencies

To install all optional dependencies:

```bash
pip install prompt-decorators[all]
```

## Verifying Installation

To verify that the installation was successful, you can run:

```python
import prompt_decorators
print(prompt_decorators.__version__)
```

## Troubleshooting

If you encounter any issues during installation:

1. Ensure you have the latest version of pip:
   ```bash
   pip install --upgrade pip
   ```

2. Check that you meet the minimum Python version requirement (3.8+):
   ```bash
   python --version
   ```

3. If you're installing from source and encounter build errors, make sure you have the necessary build tools installed for your platform.

4. For any other issues, please check the [GitHub issues](https://github.com/yourusername/prompt-decorators/issues) or open a new one.

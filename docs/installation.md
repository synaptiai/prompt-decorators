# Installation

This guide provides step-by-step instructions for installing the Prompt Decorators package.

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Installation Methods

### Using pip (Recommended)

The simplest way to install Prompt Decorators is using pip:

```bash
pip install prompt-decorators
```

### Using Poetry

If you're using Poetry for dependency management:

```bash
poetry add prompt-decorators
```

### Development Installation

For development purposes, you can install the package from source:

```bash
# Clone the repository
git clone https://github.com/synaptiai/prompt-decorators.git
cd prompt-decorators

# Install in development mode
pip install -e .
```

For development with all optional dependencies:

```bash
pip install -e ".[dev,test,docs]"
```

## Verifying Installation

You can verify your installation by running:

```python
import prompt_decorators
print(prompt_decorators.__version__)
```

You should see the version number printed to the console.

## Environment Setup

### Configuration

The Prompt Decorators package has minimal configuration requirements. However, when using specific integrations, additional configuration may be needed.

For example, if you're using the OpenAI integration, you'll need to set up your API key:

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

Alternatively, you can create a `.env` file in your project directory:

```
OPENAI_API_KEY=your-api-key
```

And then use a library like `python-dotenv` to load it:

```python
from dotenv import load_dotenv
load_dotenv()
```

## MCP Integration Installation

If you plan to use the Model Context Protocol (MCP) integration:

```bash
pip install "prompt-decorators[mcp]"
```

This will install the MCP dependencies required for using Prompt Decorators with any MCP-compatible client.

## Optional Dependencies

The package supports several optional dependency groups:

- `dev`: Development dependencies
- `test`: Testing dependencies
- `docs`: Documentation dependencies
- `mcp`: Model Context Protocol integration

You can install any combination:

```bash
# Install with MCP and testing dependencies
pip install "prompt-decorators[mcp,test]"
```

## Troubleshooting

### Common Installation Issues

#### Package Not Found

If you see "Package not found" errors, ensure that:
- You're using the correct package name (`prompt-decorators`)
- Your PyPI or pip configuration is correct
- Your internet connection is stable

#### Version Conflicts

If you encounter version conflicts with dependencies:

```bash
# Install with a specific version
pip install prompt-decorators==0.3.0

# Or resolve dependencies explicitly
pip install --upgrade pip setuptools wheel
pip install prompt-decorators
```

#### Permission Errors

If you encounter permission errors:

```bash
# Use the --user flag
pip install --user prompt-decorators

# Or use a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install prompt-decorators
```

## Next Steps

After installation, proceed to the [Quick Start](quickstart.md) guide to begin using the package.

# Prompt Decorators

<div align="center">

![Prompt Decorators Logo](https://raw.githubusercontent.com/synaptiai/prompt-decorators/main/docs/assets/logo.png)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org/)
[![Documentation](https://img.shields.io/badge/docs-MkDocs-blue)](https://synaptiai.github.io/prompt-decorators/)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-black)](https://github.com/astral-sh/ruff)

**A Python framework implementing the Prompt Decorators Specification for enhancing interactions with Large Language Models (LLMs) through standardized, composable prompt modifications.**

[Documentation](https://synaptiai.github.io/prompt-decorators/) •
[Installation](#installation) •
[Examples](#example-usage) •
[Contributing](#contributing)

</div>

## 📋 Table of Contents

- [Overview](#overview)
- [Implemented Functionality](#implemented-functionality)
- [Architecture](#architecture)
- [Example Usage](#example-usage)
- [Getting Started](#getting-started)
- [Prompt Decorators Specification](#prompt-decorators-specification)
- [Development](#development)
- [License](#license)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [Acknowledgments](#acknowledgments)
- [Code Quality](#code-quality)

## 🔍 Overview

Prompt Decorators is a powerful and flexible framework that enables systematic modification of prompts to achieve specific behaviors in LLM responses. Based on the [Prompt Decorators Specification](docs/prompt-decorators-specification-v1.0.md), it provides a structured way to define, combine, and apply decorators to prompts.

### Background & Motivation

As Large Language Models become increasingly integrated into workflows across industries, the need for standardized, consistent ways to interact with these systems has become apparent. Current prompt engineering approaches are largely ad-hoc, requiring extensive documentation, reinvention, and significant cognitive overhead when switching between systems or use cases.

Prompt Decorators address this challenge by providing a systematic approach to modifying AI behavior through simple, composable annotations. Inspired by the Decorator pattern in programming and Python's function decorators, they serve as a layer of abstraction that decouples the core prompt from instructions about how to process and present the response.

### Challenges in Prompt Engineering

Current prompt engineering suffers from several limitations:

- **Inconsistency**: Instructions vary widely between users, platforms, and models
- **Verbosity**: Detailed instructions consume token context that could be used for content
- **Cognitive Overhead**: Users must remember or document specific prompting techniques
- **Lack of Composability**: Combining different instruction paradigms is cumbersome
- **Undocumented Behavior**: Expected model behavior is often implicit rather than explicit

### Benefits of Prompt Decorators

The Prompt Decorators framework addresses these challenges through:

- **Standardization**: Common vocabulary and syntax across platforms and models
- **Efficiency**: Concise annotations that reduce token consumption
- **Reusability**: Consistent behaviors that can be reused across different contexts
- **Composability**: Ability to combine decorators for complex interaction patterns
- **Explicit Behavior**: Clear documentation of expected model responses
- **Reduced Cognitive Load**: Simple annotations instead of lengthy instructions

### Key Features

- **📚 Registry-based decorator management**: Centralized registry of decorators with metadata
- **✅ Parameter validation and type checking**: Robust validation of decorator parameters
- **🔢 Decorator versioning**: Support for semantic versioning of decorators
- **🔄 Compatibility checking**: Verification of decorator compatibility
- **📝 Documentation generation**: Automatic generation of documentation for decorators
- **⚙️ Code generation**: Tools for generating decorator code from registry definitions
- **🔍 Runtime decorator discovery**: Dynamic discovery and registration of decorators

## 🚀 Implemented Functionality

The framework currently implements:

1. **Core Decorators**:
   - `Reasoning`: Enhances reasoning capabilities in responses
   - `StepByStep`: Breaks down reasoning into sequential steps
   - `TreeOfThought`: Explores multiple reasoning paths
   - `FirstPrinciples`: Applies first principles reasoning
   - `OutputFormat`: Controls the format of the output (markdown, JSON, etc.)
   - `Tone`: Adjusts the tone of the response
   - And many more...

2. **Registry System**:
   - JSON-based decorator definitions
   - Metadata for documentation and compatibility
   - Versioning and dependency management

3. **Documentation System**:
   - Automatic generation of markdown documentation
   - Integration with MkDocs for comprehensive documentation site
   - API reference documentation

4. **Code Generation**:
   - Generation of decorator classes from registry definitions
   - Test generation for decorators

## 🏗️ Architecture

The framework is organized into several key components:

1. **Core** (`prompt_decorators/core/`):
   - `BaseDecorator`: The foundation for all decorators with parameter validation and versioning support
   - `ModelSpecificDecorator`: Adapts decorators for specific LLM models
   - `Request`: Handles API requests decorated with multiple prompt decorators

2. **Generator** (`prompt_decorators/generator/`):
   - `Registry`: Scans and parses decorator registry files
   - `CodeGen`: Generates Python code for decorator classes
   - `TestGen`: Generates test code for decorators

3. **Utils** (`prompt_decorators/utils/`):
   - `Discovery`: Runtime decorator discovery and registration
   - `Compatibility`: Checks compatibility between decorators
   - `Cache`: Caching utilities for decorator responses
   - `DocGen`: Documentation generation utilities

4. **Decorators** (`prompt_decorators/decorators/`):
   - Implementation of specific decorator types organized by category

## 💻 Example Usage

### Creating and Using Decorators

```python
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to a prompt
prompt = "Explain quantum entanglement."
decorated_prompt = output_format.apply(reasoning.apply(prompt))

# Use the decorated prompt with an LLM API
# ...
```

### Using the Decorator Registry

```python
from prompt_decorators.utils import get_registry

# Get the registry instance
registry = get_registry()

# Create decorators through the registry
concise = registry.create_decorator("Concise", max_words=150, bullet_points=True)
eli5 = registry.create_decorator("ELI5", age=10)

# Apply decorators to a prompt
prompt = "Explain how neural networks work."
decorated_prompt = concise.apply(eli5.apply(prompt))

# Find decorators by category
reasoning_decorators = registry.find_decorators_by_category("reasoning")
for name in reasoning_decorators:
    print(f"- {name}")
```

### Using Decorated Requests

```python
from prompt_decorators.core.request import DecoratedRequest

# Create a decorated request
request = DecoratedRequest(
    prompt="Explain quantum mechanics.",
    decorators=[reasoning, output_format],
    model="gpt-4",
    api_params={"temperature": 0.7}
)

# Apply all decorators
decorated_prompt = request.apply_decorators()

# Serialize for storage or transmission
request_json = request.to_json()
```

### Model-Specific Adaptations

```python
from prompt_decorators.core import ModelSpecificDecorator

class CustomModelSpecificDecorator(ModelSpecificDecorator):
    """A model-specific decorator that adapts to different models."""

    name = "CustomModelSpecific"
    version = "1.0.0"

    def apply_for_model(self, prompt: str) -> str:
        """Apply model-specific behavior."""
        if self.model_capabilities.supports_feature("reasoning"):
            return f"Use your reasoning capabilities to answer: {prompt}"
        else:
            return self.apply_fallback(prompt)

    def apply_fallback(self, prompt: str) -> str:
        """Fallback for models without specific capabilities."""
        return f"Answer this question step by step: {prompt}"

# Use with a specific model
decorator = CustomModelSpecificDecorator(model_id="gpt-4")
decorated_prompt = decorator.apply("Explain quantum computing.")
```

## 🚦 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

```bash
# Not yet available on PyPI
git clone https://github.com/synaptiai/prompt-decorators.git
cd prompt-decorators
pip install -e .
```

### Documentation

Comprehensive documentation is available in the `docs/` directory. You can build the documentation site using MkDocs:

```bash
pip install mkdocs mkdocs-material
mkdocs serve
```

Then visit `http://localhost:8000` to view the documentation.

### Generating Decorator Code

```bash
python scripts/generate_decorators.py
```

## 📄 Prompt Decorators Specification

This implementation is based on the [Prompt Decorators Specification](docs/prompt-decorators-specification-v1.0.md), which defines:

- Core decorator syntax and grammar
- Standard decorator definitions and behavior
- Implementation guidelines
- Extension mechanisms
- Versioning and evolution processes

The specification provides a standardized approach to prompt engineering that can be implemented across different platforms and tools.

## 🛠️ Development

### Decorator Registry

The registry defines all available decorators and their parameters. It uses JSON files in the `registry/` directory to specify:

- Decorator name and category
- Parameters with types and constraints
- Compatibility with other decorators
- Description and usage examples

The `DecoratorRegistry` class provides runtime discovery and management of decorators. See [DECORATOR_REGISTRY.md](docs/DECORATOR_REGISTRY.md) for detailed documentation on how to use the decorator registry.

### Adding a New Decorator

1. Define the decorator in the registry
2. Generate the code with `scripts/generate_decorators.py`
3. Customize the generated code if needed
4. Add tests using the test generator

## 📜 License

This project is licensed under the [Apache License 2.0](LICENSE) - see the LICENSE file for details.

## 👥 Contributing

We welcome contributions from the community! Here's how you can help:

- **Report bugs**: Open an issue if you find a bug
- **Suggest features**: Have an idea for a new feature? Open an issue to discuss it
- **Submit pull requests**: Implement new features or fix bugs

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.

### Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## 🗺️ Roadmap

See [ROADMAP.md](docs/roadmap.md) for the development roadmap and upcoming features.

## 🙏 Acknowledgments

This project was inspired by the need for more structured prompt engineering techniques when working with LLMs. It aims to standardize and simplify the process of creating effective prompts for different use cases and models.

## 🔍 Code Quality

This project uses several tools to maintain high code quality:

- **Pre-commit hooks**: Automated checks run before each commit
- **Docstring standardization**: Tools to check and fix docstring issues
- **Type annotations**: Comprehensive type hints throughout the codebase
- **CI/CD integration**: GitHub Actions workflow for continuous quality checks

### Setting Up Development Environment

1. Install pre-commit:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

2. Run code quality checks:
   ```bash
   # Run all pre-commit hooks
   pre-commit run --all-files

   # Check docstrings
   python scripts/check_docstrings.py

   # Fix docstring issues automatically
   python scripts/fix_docstrings.py
   ```

For more details, see the [Code Quality Integration](docs/code_quality_integration.md) and [Docstring Standards](docs/DOCSTRING_STANDARDS.md) documentation.

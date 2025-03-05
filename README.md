# Prompt Decorators

<div align="center">

<img src="docs/assets/logo.png" alt="Prompt Decorators Logo" width="400"/>

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org/)
[![Documentation](https://img.shields.io/badge/docs-MkDocs-blue)](https://synaptiai.github.io/prompt-decorators/)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-black)](https://github.com/astral-sh/ruff)

[![Code Quality and Testing](https://github.com/synaptiai/prompt-decorators/workflows/Code%20Quality%20and%20Testing/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Code+Quality+and+Testing%22)
[![Documentation](https://github.com/synaptiai/prompt-decorators/workflows/Documentation/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Documentation%22)
[![Publish to PyPI](https://github.com/synaptiai/prompt-decorators/workflows/Publish%20to%20PyPI/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Publish+to+PyPI%22)

**A Python framework implementing the Prompt Decorators Specification for enhancing interactions with Large Language Models (LLMs) through standardized, composable prompt modifications.**

[Documentation](https://synaptiai.github.io/prompt-decorators/) •
[Prompt Decorators Specification](/docs/prompt-decorators-specification-v1.0.md)

</div>

## 📋 Table of Contents

- [Overview](#overview)
- [Implemented Functionality](#implemented-functionality)
- [Architecture](#architecture)
- [Example Usage](#example-usage)
- [Getting Started](#getting-started)
- [Prompt Decorators Specification](#prompt-decorators-specification)
- [Domain-Specific Extensions](#domain-specific-extensions)
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

5. **Integrations**:
   - **Model Context Protocol (MCP)**: Integration with the [Model Context Protocol](https://github.com/microsoft/model-context-protocol) for standardized LLM interactions
   - Predefined decorator templates for common use cases
   - MCP tools for applying decorators and retrieving decorator information

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

### Using Domain-Specific Extensions

```python
from prompt_decorators.utils.discovery import DecoratorRegistry
from finance_decorators import register_extensions

# Initialize registry and register finance extensions
registry = DecoratorRegistry()
register_extensions(registry)

# Create a prompt with finance decorators
prompt = """
+++RiskDisclosure.us_investment()
+++FinancialAnalysis.long_term_fundamental()
Analyze Microsoft (MSFT) as a potential addition to a retirement portfolio.
"""

# Process the prompt
processed_prompt = registry.process_prompt(prompt)

# Send to LLM API
response = llm_api.generate(processed_prompt)
```

### Using the Decorator Registry

```python
from prompt_decorators.utils.discovery import get_registry

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

### Using the MCP Integration

```python
from prompt_decorators.integrations.mcp import create_mcp_server

# Create an MCP server with prompt decorator integration
mcp_server = create_mcp_server("my-decorator-server")

# Run the server
mcp_server.run()
```

Connect to the server using an MCP client:

```python
from mcp.client import MCPClient

# Connect to the MCP server
client = MCPClient("http://localhost:8000")

# Apply decorators using the +++ syntax
result = await client.tools.apply_decorators(
    prompt="+++Reasoning(depth='comprehensive') +++StepByStep() Explain quantum computing."
)

# Use a predefined template
template_result = await client.tools.create_decorated_prompt(
    template_name="detailed-reasoning",
    prompt="Explain how quantum computing works."
)

# Use a template through the prompts API
prompt_response = await client.prompts.get(
    name="explain-simply",
    arguments={"prompt": "Explain how nuclear fusion works."}
)
```

See the [MCP Integration Documentation](docs/integrations/mcp.md) for more details.

## 📄 Prompt Decorators Specification

This implementation is based on the [Prompt Decorators Specification](docs/prompt-decorators-specification-v1.0.md), which defines:

- Core decorator syntax and grammar
- Standard decorator definitions and behavior
- Implementation guidelines
- Extension mechanisms
- Versioning and evolution processes

The specification provides a standardized approach to prompt engineering that can be implemented across different platforms and tools.

## 🌐 Domain-Specific Extensions

Prompt Decorators can be extended with domain-specific decorators tailored to particular fields or industries:

### Available Domain Extensions

- **Finance**: Decorators for financial analysis, risk disclosures, and investment recommendations
- **Medical**: Decorators for evidence-based medicine, patient education, and clinical documentation
- **Legal**: Decorators for legal analysis, case citations, and jurisdiction-specific responses

### Creating Your Own Extensions

The framework provides comprehensive tools and documentation for creating your own domain-specific extensions:

- [Domain-Specific Extensions Guide](docs/guides/domain_specific_extensions.md): Detailed guide on creating domain-specific extensions
- [Extension Development Tutorial](docs/tutorials/extension_development.md): Step-by-step tutorial for developing extensions
- [Examples](examples/domain_extensions/): Example domain-specific extensions with full source code

Domain-specific extensions allow you to encapsulate domain knowledge, terminology, and best practices into reusable decorators that can be shared with your team or the broader community.

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

## 📝 License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more information.

## 🤝 Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## 🚧 Roadmap

The roadmap for this project is outlined in the [ROADMAP](ROADMAP.md) file.

## 🤖 Acknowledgments

This project would not be possible without the contributions of the following individuals and organizations:

- **[Synaptiai](https://synaptiai.com)**: The original creators and maintainers of the framework
- **[Contributors](https://github.com/synaptiai/prompt-decorators/graphs/contributors)**: All the wonderful people who have contributed to this project

## 🔢 Code Quality

This project uses a variety of tools and practices to ensure high code quality:

- **[Code Style](https://github.com/astral-sh/ruff)**: Enforces consistent coding style
- **[Code Quality and Testing](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Code+Quality+and+Testing%22)**: Continuous integration and testing
- **[Documentation Verification](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Documentation+Verification%22)**: Ensures documentation accuracy
- **[Documentation](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Documentation%22)**: Comprehensive documentation site
- **[Publish to PyPI](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Publish+to+PyPI%22)**: Automated deployment to PyPI

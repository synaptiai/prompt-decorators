# Prompt Decorators

Welcome to the Prompt Decorators documentation! This framework provides a structured way to enhance prompts for Large Language Models (LLMs) through the application of modular, reusable "decorators."

## Table of Contents

- [What is Prompt Decorators?](#what-is-prompt-decorators)
- [Quick Start](#quick-start)
  - [Installation](#installation)
  - [Basic Usage](#basic-usage)
- [Documentation](#documentation)
  - [Guides](#guides)
  - [Project Information](#project-information)
- [Why Use Prompt Decorators?](#why-use-prompt-decorators)
  - [Modularity](#modularity)
  - [Reusability](#reusability)
  - [Standardization](#standardization)
  - [Experimentation](#experimentation)
  - [Compatibility](#compatibility)
- [Getting Help](#getting-help)
- [License](#license)

## What is Prompt Decorators?

Prompt Decorators is a Python framework that allows you to apply various "decorators" to your prompts, each adding specific functionality or behavior. This approach makes prompt engineering more modular, reusable, and maintainable.

Key features include:

- **Modular Prompt Engineering**: Apply specific prompt techniques independently
- **Decorator Registry**: Discover and use decorators dynamically
- **Compatibility Checking**: Ensure decorators work well together
- **Dynamic Implementation**: Runtime loading of decorators from definitions
- **API Integration**: Work with multiple LLM providers
- **MCP Integration**: Integration with the Model Context Protocol

## Quick Start

### Installation

```bash
pip install prompt-decorators
```

### Basic Usage

```python
from prompt_decorators import apply_dynamic_decorators, create_decorator_instance

# Using inline decorator syntax
prompt = """
+++Reasoning(depth="comprehensive")
+++OutputFormat(format="markdown")
Explain quantum entanglement.
"""
decorated_prompt = apply_dynamic_decorators(prompt)

# Or using programmatic approach
reasoning = create_decorator_instance("Reasoning", depth="comprehensive")
output_format = create_decorator_instance("OutputFormat", format="markdown")

prompt = "Explain quantum entanglement."
decorated_prompt = output_format(reasoning(prompt))

# Use the decorated prompt with your favorite LLM API
# ...
```

## Documentation

### Guides

- [Installation](installation.md) - How to install the framework
- [Quickstart](quickstart.md) - Get up and running quickly
- [Core Concepts](concepts.md) - Core concepts and design philosophy
- [Creating Decorators](creating_decorators.md) - Create your own decorators
- [Compatibility](compatibility.md) - Compatibility with different LLM providers

### Project Information

- [Contributing](contributing.md) - How to contribute to the project
- [Development](development.md) - Setting up the development environment
- [FAQ](faq.md) - Frequently asked questions
- [Glossary](glossary.md) - Definitions of key terms
- [Roadmap](roadmap.md) - Future development plans

## Why Use Prompt Decorators?

### Modularity

Each decorator focuses on a specific prompt engineering technique, allowing you to mix and match them as needed.

### Reusability

Create a library of prompt techniques that can be reused across different projects and applications.

### Standardization

Establish consistent prompt patterns across your organization or project.

### Experimentation

Easily test different prompt engineering approaches by swapping decorators.

### Compatibility

Work with multiple LLM providers using the same decorator patterns.

## Getting Help

If you need help with Prompt Decorators, you can:

- Check the [FAQ](faq.md) for answers to common questions
- Read the [Troubleshooting](faq.md#troubleshooting) section in the FAQ
- Open an issue on our [GitHub repository](https://github.com/synaptiai/prompt-decorators)
- Join our community discussions

## License

Prompt Decorators is released under the Apache 2.0 License. See the LICENSE file for details.

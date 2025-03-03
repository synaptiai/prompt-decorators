# Prompt Decorators

Welcome to the Prompt Decorators documentation! This framework provides a structured way to enhance prompts for Large Language Models (LLMs) through the application of modular, reusable "decorators."

## What is Prompt Decorators?

Prompt Decorators is a Python framework that allows you to apply various "decorators" to your prompts, each adding specific functionality or behavior. This approach makes prompt engineering more modular, reusable, and maintainable.

Key features include:

- **Modular Prompt Engineering**: Apply specific prompt techniques independently
- **Decorator Registry**: Discover and use decorators dynamically
- **Compatibility Checking**: Ensure decorators work well together
- **Serialization**: Store and retrieve decorated prompts
- **API Integration**: Work with multiple LLM providers
- **CLI Tools**: Apply decorators from the command line

## Quick Start

### Installation

```bash
pip install prompt-decorators
```

### Basic Usage

```python
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to a prompt
prompt = "Explain quantum entanglement."
decorated_prompt = output_format.apply(reasoning.apply(prompt))

# Use the decorated prompt with your favorite LLM API
# ...
```

## Documentation

### Guides

- [Installation](installation.md) - How to install the framework
- [Quickstart](quickstart.md) - Get up and running quickly
- [Basic Usage](guide/basic-usage.md) - Learn the basics of using decorators
- [Advanced Usage](guide/advanced-usage.md) - Explore advanced features
- [API Integration](guide/api-integration.md) - Integrate with LLM APIs
- [CLI Usage](guide/cli-usage.md) - Use the command-line interface
- [Troubleshooting](guide/troubleshooting.md) - Solve common issues

### API Reference

- [API Overview](api/index.md) - Overview of the API
- [Core](api/modules/prompt_decorators.core.md) - Core classes and functions
- [Decorators](api/modules/prompt_decorators.decorators.md) - Built-in decorators
- [Utilities](api/modules/prompt_decorators.utils.md) - Utility functions
- [Generator](api/modules/prompt_decorators.generator.md) - Code generation tools

### Examples

- [Basic Examples](examples/basic.md) - Simple usage examples
- [Advanced Examples](examples/advanced.md) - Complex usage patterns
- [Provider Examples](examples/providers.md) - Examples with different LLM providers

### Project Information

- [Contributing](contributing.md) - How to contribute to the project
- [Development](development.md) - Setting up the development environment
- [Project Summaries](project_summaries/index.md) - Documentation of modernization and standardization efforts
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
- Read the [Troubleshooting](guide/troubleshooting.md) guide
- Open an issue on our [GitHub repository](https://github.com/yourusername/prompt-decorators)
- Join our community discussions

## License

Prompt Decorators is released under the MIT License. See the LICENSE file for details.

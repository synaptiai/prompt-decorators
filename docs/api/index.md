# API Reference

This section provides detailed documentation for the Prompt Decorators API. It covers the core classes, built-in decorators, registry system, utilities, and code generation tools.

## Overview

The Prompt Decorators API is organized into several key modules:

- **Core**: The foundation of the framework, including base classes and core functionality
- **Decorators**: Built-in decorators for various prompt engineering techniques
- **Registry**: The system for discovering, registering, and retrieving decorators
- **Utilities**: Helper functions and utilities for working with decorators
- **Generator**: Tools for generating decorator code and managing the registry

## Core Module

The [Core Module](core.md) provides the foundation for the Prompt Decorators framework. It includes:

- `BaseDecorator`: The abstract base class that all decorators must inherit from
- `DecoratedRequest`: A class for managing decorated requests with multiple decorators
- `ParameterSchema`: Utilities for defining and validating decorator parameters
- `ModelAdaptation`: Tools for adapting decorators to specific LLM models

## Decorators Module

The [Decorators Module](decorators.md) contains all the built-in decorators provided by the framework. These include:

- **Reasoning Decorators**: Enhance the reasoning capabilities of LLMs
- **Output Format Decorators**: Control the format of LLM responses
- **Persona Decorators**: Add personality and role characteristics to prompts
- **Instruction Decorators**: Provide specific instructions to the LLM
- **Context Decorators**: Add context or background information to prompts

## Registry Module

The [Registry Module](registry.md) handles the discovery, registration, and retrieval of decorators. It includes:

- `DecoratorRegistry`: The central registry for managing decorators
- `Discovery`: Tools for discovering decorators at runtime
- `Compatibility`: Utilities for checking compatibility between decorators

## Utilities Module

The [Utilities Module](utilities.md) provides various helper functions and utilities, including:

- `Cache`: Caching utilities for decorator application
- `Factory`: Factory functions for creating decorators
- `JSON Loader`: Utilities for loading decorator definitions from JSON
- `Model Detection`: Tools for detecting and identifying LLM models
- `Plugins`: The plugin system for extending the framework
- `Telemetry`: Optional telemetry features

## Generator Module

The [Generator Module](generator.md) contains tools for generating decorator code and managing the registry, including:

- `Registry`: Tools for managing the decorator registry
- `Code Generation`: Utilities for generating decorator code
- `Test Generation`: Tools for generating test code for decorators
- `CLI`: Command-line interface for code generation

## Using the API

Here's a simple example of using the API to create and apply decorators:

```python
from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.decorators import Reasoning, OutputFormat
from prompt_decorators.registry import DecoratorRegistry

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to a prompt
prompt = "Explain quantum entanglement."
decorated_prompt = output_format.apply(reasoning.apply(prompt))

# Use the registry to find decorators
registry = DecoratorRegistry()
all_decorators = registry.get_all_decorators()
reasoning_decorators = registry.get_decorators_by_category("reasoning")

# Create a custom decorator
class MyCustomDecorator(BaseDecorator):
    def apply(self, prompt: str) -> str:
        return f"{prompt}\n\nPlease provide a detailed explanation with examples."

    def to_dict(self):
        return {"type": "MyCustomDecorator"}

    @classmethod
    def from_dict(cls, data):
        return cls()

# Register the custom decorator
registry.register(MyCustomDecorator)
```

## Next Steps

- Explore the [Core Module](core.md) to understand the foundation of the framework
- Check out the [Decorators Module](decorators.md) to see the built-in decorators
- Learn about the [Registry Module](registry.md) to understand how decorators are managed
- See the [Basic Usage Guide](../guide/basic-usage.md) for more examples

# Prompt Decorators Registry

This directory contains the registry of prompt decorators that are available in the prompt-decorators package.

## Structure

The registry is organized into the following directories:

- **core**: Contains the core decorators defined in the original Prompt Decorators specification
- **extensions**: Contains extensions to the core decorators, contributed by the community
- **simplified_decorators**: Contains simplified versions of decorators for specific use cases

## Usage

The registry is automatically loaded when the prompt-decorators package is imported. You can access the decorators through the `DynamicDecorator` class:

```python
from prompt_decorators.core.dynamic_decorator import DynamicDecorator

# Create a decorator instance
decorator = DynamicDecorator("StepByStep", numbered=True)

# Apply the decorator to a prompt
result = decorator("What is quantum computing?")
```

## Adding New Decorators

To add a new decorator to the registry, create a JSON file in the appropriate directory following the registry-entry.schema.json format. The file should contain the decorator definition, including its name, description, parameters, and transformation function.

For more information, see the [Decorator Registry documentation](https://synaptiai.github.io/prompt-decorators/DECORATOR_REGISTRY/).

## Notes for Package Maintainers

This directory is part of the prompt-decorators package and is included in the package distribution. The registry files are copied from the source registry directory during the build process.

For backward compatibility, a symlink is created from the source registry directory to this directory during installation. This allows code that expects the registry in the source location to continue working.

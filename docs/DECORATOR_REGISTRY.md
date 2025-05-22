# Decorator Registry

## Overview

The Decorator Registry is a central component of the Prompt Decorators package that enables runtime discovery and management of decorators. It provides a mechanism to register, discover, and use decorators dynamically, making it easier to extend the system with new decorators and to find decorators by name, category, or other criteria.

## Features

- **Dynamic Registration**: Register decorators at runtime from code or JSON definitions
- **Decorator Discovery**: Find decorators by name, category, or other criteria
- **Version Management**: Support for multiple versions of the same decorator
- **Compatibility Checking**: Verify compatibility between decorators
- **Category Organization**: Group decorators by category for easier discovery

## Implementation

The Decorator Registry is implemented in two main modules:

1. **Dynamic Registry**: The primary implementation in `prompt_decorators.core.dynamic_decorator`, which loads decorator definitions from JSON files at runtime
2. **Class Registry**: A secondary implementation in `prompt_decorators.utils.discovery` for backward compatibility

### Registry Structure

The registry is organized as a directory structure:

```
prompt_decorators/registry/
├── core/                 # Core decorators from the specification
├── extensions/           # Community extensions and domain-specific decorators
└── simplified_decorators/ # Simplified versions for specific use cases
```

Each decorator is defined in a JSON file following the registry-entry.schema.json format.

### Key Components

1. **DynamicDecorator**: The main class that loads and applies decorators from the registry
2. **load_registry**: Method to load decorator definitions from the registry directory
3. **register_decorator**: Method to register a decorator definition
4. **get_available_decorators**: Method to get all available decorators
5. **create_decorator_instance**: Method to create a decorator instance by name

## Usage

### Using Dynamic Decorators

The recommended way to use decorators is through the dynamic decorator system:

```python
from prompt_decorators.core.dynamic_decorator import DynamicDecorator
from prompt_decorators.dynamic_decorators_module import load_decorator_definitions

# Load the registry (this is done automatically when creating a decorator)
load_decorator_definitions()

# Create a decorator instance by name
concise = DynamicDecorator("Concise", maxWords=100, bulletPoints=True)

# Apply the decorator to a prompt
original_prompt = "Explain the concept of quantum computing in detail."
decorated_prompt = concise(original_prompt)
```

### Adding Custom Decorators

You can add custom decorators to the registry in several ways:

1. **Adding a JSON File to the Registry Directory**:

Create a JSON file in the appropriate registry directory (e.g., `prompt_decorators/registry/extensions/`) with the following structure:

```json
{
  "decoratorName": "MyCustomDecorator",
  "description": "A custom decorator that does something useful",
  "category": "custom",
  "parameters": [
    {
      "name": "param1",
      "description": "First parameter",
      "type": "string",
      "required": false,
      "default": "default value"
    }
  ],
  "transform_function": "return text + '\\n\\nThis was processed by MyCustomDecorator with param1=' + kwargs.get('param1', 'default value')"
}
```

2. **Registering a Decorator Programmatically**:

```python
from prompt_decorators.dynamic_decorators_module import DecoratorDefinition, register_decorator

# Create a decorator definition
my_decorator = DecoratorDefinition(
    name="MyCustomDecorator",
    description="A custom decorator that does something useful",
    category="custom",
    parameters=[
        {
            "name": "param1",
            "description": "First parameter",
            "type": "string",
            "required": False,
            "default": "default value"
        }
    ],
    transform_function="return text + '\\n\\nThis was processed by MyCustomDecorator with param1=' + kwargs.get('param1', 'default value')"
)

# Register the decorator
register_decorator(my_decorator)
```

### Finding Decorators

You can discover available decorators in several ways:

1. **Getting All Available Decorators**:

```python
from prompt_decorators.dynamic_decorators_module import get_available_decorators

# Get all available decorators
decorators = get_available_decorators()

# Print decorator names
for decorator in decorators:
    print(f"{decorator.name}: {decorator.description}")
```

2. **Listing Available Decorator Names**:

```python
from prompt_decorators.dynamic_decorators_module import list_available_decorators

# Get all available decorator names
decorator_names = list_available_decorators()
print(decorator_names)
```

3. **Checking if a Decorator Exists**:

```python
from prompt_decorators.core.dynamic_decorator import DynamicDecorator
from prompt_decorators.dynamic_decorators_module import load_decorator_definitions

# Load the registry
load_decorator_definitions()

# Try to create a decorator instance
try:
    decorator = DynamicDecorator("Concise")
    print(f"Decorator 'Concise' exists")
except ValueError:
    print(f"Decorator 'Concise' does not exist")
```

### Using Decorators in Text

You can also use decorators directly in text using the +++ syntax:

```python
from prompt_decorators.dynamic_decorators_module import apply_dynamic_decorators

# Text with decorator syntax
text = """+++Concise(maxWords=100, bulletPoints=true)
Explain the concept of quantum computing in detail.
"""

# Apply decorators to the text
result = apply_dynamic_decorators(text)
```

## Registry Location

The registry is located in the `prompt_decorators/registry` directory within the package. When the package is installed, this directory is included in the package distribution.

For backward compatibility, a symlink is created from the source registry directory to the package registry directory during installation. This allows code that expects the registry in the source location to continue working.

## Examples

For complete examples of how to use the Decorator Registry, see the following example scripts:

- `examples/use_dynamic_decorators.py`: Shows how to use dynamic decorators to modify prompts
- `examples/create_custom_decorator.py`: Demonstrates how to create and register a custom decorator

## Best Practices

1. **Use Dynamic Decorators**: The dynamic decorator system is the recommended way to use decorators.
2. **Handle Exceptions When Creating Decorators**: When creating decorators by name, handle exceptions properly to avoid breaking your application.
3. **Check Decorator Existence Before Use**: Always check if a decorator exists in the registry before trying to use it.
4. **Use Categories for Organization**: Organize decorators by category to make them easier to discover and use.
5. **Consider Version Compatibility**: When using multiple decorators together, consider their version compatibility to avoid unexpected behavior.
6. **Add Custom Decorators to the Extensions Directory**: When adding custom decorators, place them in the `extensions` directory to avoid conflicts with core decorators.

## Future Enhancements

The Decorator Registry is designed to be extensible and can be enhanced in several ways:

1. **Plugin System**: Add support for loading decorators from external plugins
2. **Web API**: Create a web API for discovering and using decorators
3. **Caching**: Implement caching for better performance
4. **Analytics**: Add analytics to track decorator usage
5. **UI Integration**: Create a user interface for browsing and selecting decorators
6. **Package Distribution**: Improve the packaging and distribution of decorators

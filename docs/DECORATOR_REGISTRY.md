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

The Decorator Registry is implemented in the `prompt_decorators.utils.discovery` module. The main class is `DecoratorRegistry`, which provides methods for registering and discovering decorators.

### Key Components

1. **DecoratorRegistry**: The main class that manages the registry of decorators
2. **register_decorator**: Method to register a decorator class or instance
3. **get_decorator**: Method to retrieve a decorator by name
4. **get_all_decorators**: Method to retrieve all registered decorators
5. **find_decorators_by_category**: Method to find decorators by category

## Usage

### Registering Decorators

Decorators can be registered in several ways:

1. **Registering a Decorator Class**:

```python
from prompt_decorators.utils.discovery import DecoratorRegistry
from prompt_decorators.decorators.generated.decorators.concise import Concise

# Get the registry instance
registry = DecoratorRegistry()

# Register a decorator class
registry.register_decorator(Concise)
```

2. **Registering a Decorator Instance**:

```python
from prompt_decorators.utils.discovery import DecoratorRegistry
from prompt_decorators.decorators.generated.decorators.concise import Concise

# Get the registry instance
registry = DecoratorRegistry()

# Create a decorator instance
concise = Concise(maxWords=100, bulletPoints=True, level=2)

# Register the decorator instance
registry.register_decorator(concise)
```

3. **Registering All Decorators from a Directory**:

```python
import os
import importlib
import inspect
from pathlib import Path
from prompt_decorators.utils.discovery import DecoratorRegistry
from prompt_decorators.core.base import BaseDecorator

def register_decorators():
    registry = DecoratorRegistry()
    registry.clear()
    
    # Path to the generated decorators directory
    decorators_dir = Path("prompt_decorators/decorators/generated/decorators")
    
    # Iterate through all Python files in the directory
    for file_path in decorators_dir.glob("*.py"):
        if file_path.name == "__init__.py":
            continue
            
        # Import the module
        module_name = f"prompt_decorators.decorators.generated.decorators.{file_path.stem}"
        try:
            module = importlib.import_module(module_name)
            
            # Find all classes in the module that are subclasses of BaseDecorator
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, BaseDecorator) and obj != BaseDecorator:
                    # Register the decorator
                    decorator_name = getattr(obj, "name", name)
                    registry.register_decorator(obj)
                    print(f"  - Registered: {decorator_name}")
        except Exception as e:
            print(f"Error registering decorators from {module_name}: {e}")
    
    # Print summary
    decorators = registry.get_all_decorators()
    print(f"\nRegistered {len(decorators)} decorators:")
    
    # Print categories
    categories = set(decorator.category for decorator in decorators)
    print(f"\nDecorator categories ({len(categories)}):")
    for category in categories:
        category_decorators = registry.find_decorators_by_category(category)
        print(f"  - {category}: {len(category_decorators)} decorators")
```

### Finding Decorators

Once decorators are registered, they can be discovered in several ways:

1. **Getting a Decorator by Name**:

```python
from prompt_decorators.utils.discovery import DecoratorRegistry

registry = DecoratorRegistry()
concise = registry.get_decorator("Concise")
```

2. **Getting All Decorators**:

```python
from prompt_decorators.utils.discovery import DecoratorRegistry

registry = DecoratorRegistry()
all_decorators = registry.get_all_decorators()
```

3. **Finding Decorators by Category**:

```python
from prompt_decorators.utils.discovery import DecoratorRegistry

registry = DecoratorRegistry()
tone_decorators = registry.find_decorators_by_category("tone")
```

### Using Registered Decorators

Once a decorator is retrieved from the registry, it can be used like any other decorator:

```python
from prompt_decorators.utils.discovery import DecoratorRegistry

registry = DecoratorRegistry()
concise = registry.get_decorator("Concise")

# Create an instance of the decorator
concise_instance = concise(maxWords=100, bulletPoints=True, level=2)

# Apply the decorator to a prompt
original_prompt = "Explain the concept of quantum computing in detail."
decorated_prompt = concise_instance.apply(original_prompt)
```

## Examples

For complete examples of how to use the Decorator Registry, see the following example scripts:

- `examples/register_all_decorators.py`: Demonstrates how to register all decorators from the generated directory
- `examples/use_registered_decorators.py`: Shows how to use registered decorators to modify prompts

## Best Practices

1. **Clear the Registry Before Bulk Registration**: If you're registering multiple decorators at once, it's a good practice to clear the registry first to avoid duplicates.
2. **Handle Exceptions During Registration**: When registering decorators from external sources, make sure to handle exceptions properly to avoid breaking your application.
3. **Check Decorator Existence Before Use**: Always check if a decorator exists in the registry before trying to use it.
4. **Use Categories for Organization**: Organize decorators by category to make them easier to discover and use.
5. **Consider Version Compatibility**: When using multiple decorators together, consider their version compatibility to avoid unexpected behavior.

## Future Enhancements

The Decorator Registry is designed to be extensible and can be enhanced in several ways:

1. **Plugin System**: Add support for loading decorators from external plugins
2. **Web API**: Create a web API for discovering and using decorators
3. **Caching**: Implement caching for better performance
4. **Analytics**: Add analytics to track decorator usage
5. **UI Integration**: Create a user interface for browsing and selecting decorators 
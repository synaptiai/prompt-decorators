# Registry Module

The `registry` module provides functionality for registering, discovering, and retrieving decorators. It serves as a central repository for all available decorators.

## DecoratorRegistry

```python
class DecoratorRegistry:
    """Central registry for decorator classes.

    This class manages the registration and retrieval of decorator classes,
    providing a central repository for all available decorators.
    """
```

The `DecoratorRegistry` class is the central registry for all decorator classes. It manages the registration and retrieval of decorators.

### Key Methods

- `register(decorator_class: Type[BaseDecorator]) -> None`: Register a decorator class
- `get_decorator(name: str) -> Type[BaseDecorator]`: Get a decorator class by name
- `get_all_decorators() -> List[Type[BaseDecorator]]`: Get all registered decorator classes
- `get_decorators_by_category(category: str) -> List[Type[BaseDecorator]]`: Get decorators by category

## RegistryEntry

```python
class RegistryEntry:
    """Entry in the decorator registry.

    This class represents an entry in the decorator registry, containing
    metadata about a decorator class.
    """
```

The `RegistryEntry` class represents an entry in the decorator registry, containing metadata about a decorator class.

### Key Attributes

- `name`: The name of the decorator
- `class_ref`: Reference to the decorator class
- `category`: The category of the decorator
- `description`: A description of the decorator
- `parameters`: The parameters accepted by the decorator
- `examples`: Example usages of the decorator

## Usage Example

```python
from prompt_decorators.core.registry import DecoratorRegistry
from prompt_decorators.core.base import BaseDecorator

# Create registry
registry = DecoratorRegistry()

# Define custom decorator
class MyCustomDecorator(BaseDecorator):
    def apply(self, prompt: str) -> str:
        return f"{prompt}\n\nPlease provide a detailed explanation with examples."

    def to_dict(self):
        return {"type": "MyCustomDecorator"}

    @classmethod
    def from_dict(cls, data):
        return cls()

# Register custom decorator
registry.register(MyCustomDecorator)

# Get decorator by name
decorator_class = registry.get_decorator("MyCustomDecorator")

# Get all decorators
all_decorators = registry.get_all_decorators()

# Get decorators by category
reasoning_decorators = registry.get_decorators_by_category("reasoning")
```

## API Reference

::: prompt_decorators.core.registry

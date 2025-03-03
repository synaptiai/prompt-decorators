# Base Module

The `base` module provides the fundamental classes and interfaces for the Prompt Decorators framework. It defines the base decorator class and related functionality.

## BaseDecorator

```python
class BaseDecorator:
    """Base class for all prompt decorators.

    All decorator implementations must inherit from this class and implement
    the required methods.
    """
```

The `BaseDecorator` class is the foundation of the decorator system. All decorators must inherit from this class and implement its abstract methods.

### Key Methods

- `apply(prompt: str) -> str`: Apply the decorator to a prompt
- `to_dict() -> dict`: Convert the decorator to a dictionary representation
- `from_dict(data: dict) -> BaseDecorator`: Create a decorator from a dictionary representation
- `validate() -> bool`: Validate the decorator's parameters

## DecoratorProcessor

```python
class DecoratorProcessor:
    """Processes and applies multiple decorators to prompts.

    This class handles the application of multiple decorators to a prompt,
    managing their order and interactions.
    """
```

The `DecoratorProcessor` class manages the application of multiple decorators to a prompt, handling their order and interactions.

### Key Methods

- `apply(decorators: List[BaseDecorator], prompt: str) -> str`: Apply multiple decorators to a prompt
- `validate_decorators(decorators: List[BaseDecorator]) -> bool`: Validate a list of decorators
- `check_compatibility(decorators: List[BaseDecorator]) -> List[str]`: Check for compatibility issues between decorators

## ParameterDefinition

```python
class ParameterDefinition:
    """Defines a parameter for a decorator.

    This class provides metadata about a decorator parameter, including
    its type, default value, and validation rules.
    """
```

The `ParameterDefinition` class defines the metadata for a decorator parameter, including its type, default value, and validation rules.

### Key Attributes

- `name`: The name of the parameter
- `type`: The expected type of the parameter
- `default`: The default value of the parameter
- `required`: Whether the parameter is required
- `description`: A description of the parameter
- `enum_values`: Allowed values for enum parameters

## Usage Example

```python
from prompt_decorators.core.base import BaseDecorator, DecoratorProcessor
from prompt_decorators.decorators import Reasoning, StepByStep

# Create decorators
reasoning = Reasoning(depth="comprehensive")
step_by_step = StepByStep(numbered=True)

# Create processor
processor = DecoratorProcessor()

# Apply decorators to prompt
prompt = "Explain how nuclear fusion works."
decorated_prompt = processor.apply([reasoning, step_by_step], prompt)
```

## API Reference {: #core-base-api-reference }

::: prompt_decorators.core.base

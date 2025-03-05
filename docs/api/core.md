# Core Module API

The `prompt_decorators.core` module provides the fundamental building blocks of the Prompt Decorators framework. This module contains the base classes, validation logic, and utility functions that power the decorator system.

## Base Components

### BaseDecorator

The `BaseDecorator` class is the foundation of all decorators in the system. It provides common functionality for applying transformations to prompts.

```python
from prompt_decorators.core import BaseDecorator

class MyCustomDecorator(BaseDecorator):
    def __init__(self, param1=None, param2=True):
        self.param1 = param1
        self.param2 = param2

    def apply_to_prompt(self, prompt):
        # Implement your custom transformation logic here
        return f"Custom transformation: {prompt}"
```

#### Methods

- `apply(prompt)`: Apply the decorator to a prompt string
- `apply_to_prompt(prompt)`: Apply the specific transformation to the prompt
- `to_dict()`: Convert the decorator to a dictionary representation
- `from_dict(data)`: Create a decorator instance from a dictionary
- `to_string()`: Convert the decorator to a string representation
- `transform_response(response)`: Transform the model's response (if needed)
- `get_metadata()`: Get metadata about the decorator
- `is_compatible_with_version(version)`: Check version compatibility

### Parameter

The `Parameter` class defines parameters that can be used with decorators, including validation rules and type information.

```python
from prompt_decorators.core import Parameter, ParameterType

# Define a parameter
my_param = Parameter(
    name="example_param",
    parameter_type=ParameterType.STRING,
    required=False,
    default="default value",
    description="An example parameter"
)
```

### ParameterType

An enumeration of supported parameter types:

- `STRING`: String values
- `NUMBER`: Numeric values
- `BOOLEAN`: Boolean values
- `ARRAY`: List/array values
- `OBJECT`: Dictionary/object values

## Validation

The validation module provides utilities for validating decorators and their parameters.

```python
from prompt_decorators.core.validation import validate_decorator

# Validate a decorator instance or dictionary
validation_result = validate_decorator(my_decorator)
if validation_result.is_valid:
    # Decorator is valid
    pass
else:
    # Handle validation errors
    print(validation_result.errors)
```

### ValidationError

Exception raised when validation fails.

```python
from prompt_decorators.core import ValidationError

try:
    # Some operation that might fail validation
    pass
except ValidationError as e:
    print(f"Validation failed: {e}")
```

## Model-Specific Functionality {#model-specific}

The `model_specific` module provides utilities for adapting decorators to different language models.

```python
from prompt_decorators.core.model_specific import is_compatible_with_model

# Check if a decorator is compatible with a specific model
if is_compatible_with_model(my_decorator, "gpt-4"):
    # Decorator is compatible with GPT-4
    pass
else:
    # Decorator is not compatible
    pass
```

### Model Adaptation

The framework provides model-specific adaptations to ensure decorators work consistently across different LLM providers:

```python
from prompt_decorators.core.model_specific import adapt_for_model

# Adapt a decorator for a specific model
adapted_decorator = adapt_for_model(my_decorator, "claude-2")
```

## Request Handling

The `request` module provides utilities for managing decorated requests.

### DecoratedRequest

The `DecoratedRequest` class represents a request that includes one or more decorators.

```python
from prompt_decorators.core.request import DecoratedRequest
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create a decorated request
request = DecoratedRequest(
    prompt="Explain quantum entanglement",
    decorators=[
        Reasoning(style="detailed"),
        OutputFormat(format_type="markdown")
    ],
    model="gpt-4",
    api_params={
        "temperature": 0.7,
        "max_tokens": 1000
    }
)

# Apply all decorators
decorated_prompt = request.apply_decorators()

# Use with your preferred API
```

## Registry

The `registry` module provides functionality for registering and retrieving decorators.

```python
from prompt_decorators.core.registry import DecoratorRegistry

# Get the global registry
registry = DecoratorRegistry()

# Register a decorator
registry.register("MyCustomDecorator", MyCustomDecorator)

# Get a decorator by name
decorator_class = registry.get("MyCustomDecorator")
```

## Exceptions

The `exceptions` module defines custom exceptions used throughout the framework.

```python
from prompt_decorators.core.exceptions import (
    DecoratorError,
    IncompatibleVersionError,
    RegistryError
)

try:
    # Some operation that might raise an exception
    pass
except DecoratorError as e:
    print(f"Decorator error: {e}")
except IncompatibleVersionError as e:
    print(f"Version incompatibility: {e}")
except RegistryError as e:
    print(f"Registry error: {e}")
```

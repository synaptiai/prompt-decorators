# Exceptions Module

The `exceptions` module defines custom exceptions used throughout the Prompt Decorators framework. These exceptions provide specific error information for different types of failures.

## DecoratorError

```python
class DecoratorError(Exception):
    """Base class for all decorator-related exceptions."""
```

The `DecoratorError` class is the base class for all decorator-related exceptions. All other exceptions in the framework inherit from this class.

## ValidationError

```python
class ValidationError(DecoratorError):
    """Raised when decorator validation fails."""
```

The `ValidationError` class is raised when decorator validation fails, such as when a decorator has invalid parameters or syntax.

## CompatibilityError

```python
class CompatibilityError(DecoratorError):
    """Raised when decorators are incompatible with each other."""
```

The `CompatibilityError` class is raised when decorators are incompatible with each other, such as when two decorators have conflicting requirements.

## RegistryError

```python
class RegistryError(DecoratorError):
    """Raised when there is an issue with the decorator registry."""
```

The `RegistryError` class is raised when there is an issue with the decorator registry, such as when a decorator is not found or cannot be registered.

## ModelAdaptationError

```python
class ModelAdaptationError(DecoratorError):
    """Raised when a decorator cannot be adapted to a specific model."""
```

The `ModelAdaptationError` class is raised when a decorator cannot be adapted to a specific model, such as when a model does not support a required feature.

## Usage Example

```python
from prompt_decorators.core.exceptions import ValidationError, CompatibilityError
from prompt_decorators.core.validation import DecoratorValidator
from prompt_decorators.decorators import Reasoning, ELI5

# Validate decorator parameters
validator = DecoratorValidator()
try:
    reasoning = Reasoning(depth="invalid_depth")
    validator.validate_parameters(reasoning)
except ValidationError as e:
    print(f"Validation error: {e}")

# Check compatibility
try:
    decorators = [Reasoning(depth="comprehensive"), ELI5(strictness=True)]
    compatibility_issues = validator.validate_compatibility(decorators)
    if compatibility_issues:
        raise CompatibilityError(f"Compatibility issues: {compatibility_issues}")
except CompatibilityError as e:
    print(f"Compatibility error: {e}")
```

## API Reference

::: prompt_decorators.core.exceptions

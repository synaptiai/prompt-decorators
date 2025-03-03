# Validation Module

The `validation` module provides utilities for validating decorator syntax, parameters, and compatibility. It ensures that decorators are properly defined and used.

## DecoratorValidator

```python
class DecoratorValidator:
    """Validates decorator syntax and parameters.

    This class provides methods for validating decorator syntax, parameters,
    and compatibility with other decorators.
    """
```

The `DecoratorValidator` class is responsible for validating decorator syntax, parameters, and compatibility.

### Key Methods

- `validate_syntax(decorator_str: str) -> bool`: Validate the syntax of a decorator string
- `validate_parameters(decorator: BaseDecorator) -> bool`: Validate the parameters of a decorator
- `validate_compatibility(decorators: List[BaseDecorator]) -> List[str]`: Check for compatibility issues between decorators

## ParameterValidator

```python
class ParameterValidator:
    """Validates decorator parameters against their definitions.

    This class provides methods for validating that decorator parameters
    match their expected types and constraints.
    """
```

The `ParameterValidator` class validates decorator parameters against their definitions.

### Key Methods

- `validate_parameter(param_name: str, param_value: Any, param_def: ParameterDefinition) -> bool`: Validate a single parameter
- `validate_type(value: Any, expected_type: str) -> bool`: Validate that a value matches an expected type
- `validate_enum(value: Any, enum_values: List[Any]) -> bool`: Validate that a value is in a list of allowed values

## SchemaValidator

```python
class SchemaValidator:
    """Validates decorator schemas against JSON Schema definitions.

    This class provides methods for validating decorator schemas against
    the JSON Schema definitions in the schemas directory.
    """
```

The `SchemaValidator` class validates decorator schemas against JSON Schema definitions.

### Key Methods

- `validate_schema(schema: dict, schema_type: str) -> bool`: Validate a schema against a JSON Schema definition
- `validate_decorator_schema(schema: dict) -> bool`: Validate a decorator schema
- `validate_registry_entry(entry: dict) -> bool`: Validate a registry entry

## Usage Example

```python
from prompt_decorators.core.validation import DecoratorValidator
from prompt_decorators.decorators import Reasoning, StepByStep

# Create validator
validator = DecoratorValidator()

# Validate decorator syntax
is_valid = validator.validate_syntax("+++Reasoning(depth=comprehensive)")

# Validate decorator parameters
reasoning = Reasoning(depth="comprehensive")
params_valid = validator.validate_parameters(reasoning)

# Check compatibility
decorators = [Reasoning(depth="comprehensive"), StepByStep(numbered=True)]
compatibility_issues = validator.validate_compatibility(decorators)
```

## API Reference {: #core-validation-api-reference }

::: prompt_decorators.core.validation

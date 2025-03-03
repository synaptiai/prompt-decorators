# Code Generation Module

The `code_gen` module provides functionality for generating decorator code. It automates the creation of decorator classes, tests, and documentation.

## CodeGenerator

```python
class CodeGenerator:
    """Generates decorator code from specifications.

    This class provides methods for generating decorator code from
    specifications, including class definitions, tests, and documentation.
    """
```

The `CodeGenerator` class generates decorator code from specifications, including class definitions, tests, and documentation.

### Key Methods

- `generate_decorator(spec: dict) -> str`: Generate a decorator class from a specification
- `generate_test(spec: dict) -> str`: Generate tests for a decorator
- `generate_documentation(spec: dict) -> str`: Generate documentation for a decorator

## DecoratorSpecification

```python
class DecoratorSpecification:
    """Specification for a decorator.

    This class represents a specification for a decorator, including
    its name, parameters, description, and behavior.
    """
```

The `DecoratorSpecification` class represents a specification for a decorator, including its name, parameters, description, and behavior.

### Key Attributes

- `name`: The name of the decorator
- `parameters`: The parameters accepted by the decorator
- `description`: A description of the decorator
- `category`: The category of the decorator
- `behavior`: The behavior of the decorator

## TemplateManager

```python
class TemplateManager:
    """Manages code templates for generation.

    This class manages code templates for generating decorator code,
    tests, and documentation.
    """
```

The `TemplateManager` class manages code templates for generating decorator code, tests, and documentation.

### Key Methods

- `get_template(template_name: str) -> str`: Get a template by name
- `render_template(template_name: str, context: dict) -> str`: Render a template with a context
- `register_template(template_name: str, template: str) -> None`: Register a new template

## Usage Example

```python
from prompt_decorators.generator.code_gen import CodeGenerator, DecoratorSpecification

# Create specification
spec = DecoratorSpecification(
    name="MyCustomDecorator",
    parameters=[
        {"name": "style", "type": "str", "default": "detailed", "description": "Style of the decorator"}
    ],
    description="A custom decorator for demonstration purposes",
    category="custom",
    behavior="Adds custom behavior to the prompt"
)

# Generate code
generator = CodeGenerator()
decorator_code = generator.generate_decorator(spec.to_dict())
test_code = generator.generate_test(spec.to_dict())
documentation = generator.generate_documentation(spec.to_dict())

# Write to files
with open("my_custom_decorator.py", "w") as f:
    f.write(decorator_code)

with open("test_my_custom_decorator.py", "w") as f:
    f.write(test_code)

with open("MyCustomDecorator.md", "w") as f:
    f.write(documentation)
```

## API Reference

::: prompt_decorators.generator.code_gen

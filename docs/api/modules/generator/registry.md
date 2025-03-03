# Generator Registry Module

The `registry` module in the generator package provides functionality for managing code generation templates and specifications. It serves as a central repository for all available templates and specifications.

## TemplateRegistry

```python
class TemplateRegistry:
    """Registry for code generation templates.

    This class manages the registration and retrieval of code generation
    templates, providing a central repository for all available templates.
    """
```

The `TemplateRegistry` class manages the registration and retrieval of code generation templates, providing a central repository for all available templates.

### Key Methods

- `register_template(template_name: str, template: str) -> None`: Register a template
- `get_template(template_name: str) -> str`: Get a template by name
- `list_templates() -> List[str]`: List all available templates

## SpecificationRegistry

```python
class SpecificationRegistry:
    """Registry for decorator specifications.

    This class manages the registration and retrieval of decorator
    specifications, providing a central repository for all available
    specifications.
    """
```

The `SpecificationRegistry` class manages the registration and retrieval of decorator specifications, providing a central repository for all available specifications.

### Key Methods

- `register_specification(spec: dict) -> None`: Register a specification
- `get_specification(name: str) -> dict`: Get a specification by name
- `list_specifications() -> List[str]`: List all available specifications

## RegistryManager

```python
class RegistryManager:
    """Manages the template and specification registries.

    This class provides a unified interface for managing the template
    and specification registries.
    """
```

The `RegistryManager` class provides a unified interface for managing the template and specification registries.

### Key Methods

- `register_template(template_name: str, template: str) -> None`: Register a template
- `get_template(template_name: str) -> str`: Get a template by name
- `register_specification(spec: dict) -> None`: Register a specification
- `get_specification(name: str) -> dict`: Get a specification by name
- `generate_code(spec_name: str) -> dict`: Generate code for a specification

## Usage Example

```python
from prompt_decorators.generator.registry import RegistryManager

# Create registry manager
manager = RegistryManager()

# Register a template
template = """
class {{ name }}(BaseDecorator):
    """{{ description }}"""

    def __init__(self, {% for param in parameters %}{{ param.name }}{% if param.default %} = {{ param.default }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}):
        self.{% for param in parameters %}{{ param.name }} = {{ param.name }}{% if not loop.last %}
        self.{% endif %}{% endfor %}

    def apply(self, prompt: str) -> str:
        # Implementation goes here
        return prompt
"""
manager.register_template("decorator_class", template)

# Register a specification
spec = {
    "name": "MyCustomDecorator",
    "parameters": [
        {"name": "style", "type": "str", "default": "detailed", "description": "Style of the decorator"}
    ],
    "description": "A custom decorator for demonstration purposes",
    "category": "custom",
    "behavior": "Adds custom behavior to the prompt"
}
manager.register_specification(spec)

# Generate code
code = manager.generate_code("MyCustomDecorator")

# Write to file
with open("my_custom_decorator.py", "w") as f:
    f.write(code["decorator"])

with open("test_my_custom_decorator.py", "w") as f:
    f.write(code["test"])

with open("MyCustomDecorator.md", "w") as f:
    f.write(code["documentation"])
```

## API Reference

::: prompt_decorators.generator.registry

# Prompt Decorators

A Python framework for defining, managing, and applying prompt decorators to enhance interactions with Large Language Models (LLMs).

## Overview

Prompt Decorators is a powerful and flexible framework that enables systematic modification of prompts to achieve specific behaviors in LLM responses. It provides a structured way to define decorators that can be combined, validated, and applied to prompts.

Key features include:
- Registry-based decorator management
- Parameter validation and type checking
- Decorator versioning with semantic version support
- Compatibility checking between decorators
- Serialization and deserialization support
- Runtime decorator discovery

## Architecture

The framework is organized into several key components:

1. **Core** (`prompt_decorators/core/`):
   - `BaseDecorator`: The foundation for all decorators with parameter validation and versioning support
   - `Request`: Handles API requests decorated with multiple prompt decorators

2. **Generator** (`prompt_decorators/generator/`):
   - `Registry`: Scans and parses decorator registry files
   - `CodeGen`: Generates Python code for decorator classes
   - `CLI`: Command-line interface for code generation

3. **Utils** (`prompt_decorators/utils/`):
   - `Discovery`: Runtime decorator discovery and registration
   - `Compatibility`: Checks compatibility between decorators

4. **Decorators** (`prompt_decorators/decorators/`):
   - Implementation of specific decorator types

## Decorator Types

The framework includes various decorator types, such as:

1. **Reasoning**: Instructs the model to use explicit reasoning in its response
2. **OutputFormat**: Controls the format of the model's output (markdown, JSON, etc.)
3. **Many more** (to be implemented based on the registry)

## Example Usage

### Creating and Using Decorators

```python
from prompt_decorators.decorators import Reasoning, OutputFormat
from prompt_decorators.decorators.reasoning import ReasoningStyle
from prompt_decorators.decorators.format import FormatType

# Create a Reasoning decorator
reasoning = Reasoning(
    style=ReasoningStyle.DETAILED.value,
    show_working=True,
    consider_alternatives=True
)

# Create an OutputFormat decorator
output_format = OutputFormat(
    format_type=FormatType.MARKDOWN.value,
    pretty_print=True
)

# Apply decorators to a prompt
prompt = "Explain quantum entanglement."
decorated_prompt = output_format.apply(reasoning.apply(prompt))

# Use the decorated prompt with an LLM API
# ...
```

### Using the Decorator Registry

```python
from prompt_decorators.utils.discovery import DecoratorRegistry

# Get the registry instance
registry = DecoratorRegistry()

# Register decorators (this is typically done automatically)
from prompt_decorators.decorators.generated.decorators.concise import Concise
from prompt_decorators.decorators.generated.decorators.eli5 import ELI5
registry.register_decorator(Concise)
registry.register_decorator(ELI5)

# Get a decorator by name
concise = registry.get_decorator("Concise")

# Create an instance with parameters
concise_instance = concise(maxWords=100, bulletPoints=True, level=2)

# Apply to a prompt
prompt = "Explain quantum computing in detail."
decorated_prompt = concise_instance.apply(prompt)

# Find decorators by category
tone_decorators = registry.find_decorators_by_category("tone")
```

For more examples of using the decorator registry, see the example scripts in the `examples/` directory:
- `register_all_decorators.py`: Demonstrates how to register all decorators from the generated directory
- `use_registered_decorators.py`: Shows how to use registered decorators to modify prompts

### Using Decorated Requests

```python
from prompt_decorators.core.request import DecoratedRequest

# Create a decorated request
request = DecoratedRequest(
    prompt="Explain quantum mechanics.",
    decorators=[reasoning, output_format],
    model="gpt-4",
    api_params={"temperature": 0.7}
)

# Apply all decorators
decorated_prompt = request.apply_decorators()

# Serialize for storage or transmission
request_json = request.to_json()
```

### Compatibility Checking

```python
from prompt_decorators.utils import get_compatibility_checker

checker = get_compatibility_checker()
issues = checker.check_compatibility(reasoning, output_format)

if issues:
    for issue in issues:
        print(f"Warning: {issue}")
```

## Getting Started

### Installation

```bash
# Not yet available on PyPI
git clone https://github.com/yourusername/prompt-decorators.git
cd prompt-decorators
pip install -e .
```

### Running the Demo

```bash
python examples/decorator_demo.py
```

### Generating Decorator Code

```bash
./generate_decorators.py
```

## Development

### Decorator Registry

The registry defines all available decorators and their parameters. It uses JSON files in the `registry/` directory to specify:

- Decorator name and category
- Parameters with types and constraints
- Compatibility with other decorators
- Description and usage examples

The `DecoratorRegistry` class provides runtime discovery and management of decorators. See [DECORATOR_REGISTRY.md](docs/DECORATOR_REGISTRY.md) for detailed documentation on how to use the decorator registry.

### Adding a New Decorator

1. Define the decorator in the registry
2. Generate the code with `generate_decorators.py`
3. Customize the generated code if needed
4. Add tests

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Roadmap

See [REGISTRY_IMPLEMENTATION_PLAN.md](REGISTRY_IMPLEMENTATION_PLAN.md) for the development roadmap.

## Acknowledgments

This project was inspired by the need for more structured prompt engineering techniques when working with LLMs.

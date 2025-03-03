# Basic Usage

This guide covers the basic usage of the Prompt Decorators framework.

## Installing the Package

First, install the Prompt Decorators package:

```bash
pip install prompt-decorators
```

For more installation options, see the [Installation Guide](../installation.md).

## Importing the Package

```python
import prompt_decorators
from prompt_decorators.decorators import Reasoning, OutputFormat
```

## Using Individual Decorators

### Creating a Decorator

To create a decorator, import the decorator class and instantiate it with the desired parameters:

```python
from prompt_decorators.decorators import Reasoning
from prompt_decorators.decorators.reasoning import ReasoningStyle

# Create a Reasoning decorator
reasoning = Reasoning(
    style=ReasoningStyle.DETAILED.value,
    show_working=True,
    consider_alternatives=True
)
```

### Applying a Decorator

To apply a decorator to a prompt, use the `apply()` method:

```python
prompt = "Explain quantum entanglement."
decorated_prompt = reasoning.apply(prompt)

print(decorated_prompt)
```

## Combining Multiple Decorators

You can combine multiple decorators by applying them in sequence:

```python
from prompt_decorators.decorators import Reasoning, OutputFormat
from prompt_decorators.decorators.reasoning import ReasoningStyle
from prompt_decorators.decorators.format import FormatType

# Create decorators
reasoning = Reasoning(
    style=ReasoningStyle.DETAILED.value,
    show_working=True,
    consider_alternatives=True
)

output_format = OutputFormat(
    format_type=FormatType.MARKDOWN.value,
    pretty_print=True
)

# Apply decorators to a prompt (order matters)
prompt = "Explain quantum entanglement."
decorated_prompt = output_format.apply(reasoning.apply(prompt))

print(decorated_prompt)
```

## Using the Decorator Registry

The registry provides a way to discover and use decorators dynamically:

```python
from prompt_decorators.utils.discovery import DecoratorRegistry

# Get the registry instance
registry = DecoratorRegistry()

# Get a decorator by name
concise = registry.get_decorator("Concise")

# Create an instance with parameters
concise_instance = concise(maxWords=100, bulletPoints=True)

# Apply to a prompt
prompt = "Explain quantum computing in detail."
decorated_prompt = concise_instance.apply(prompt)

print(decorated_prompt)
```

## Finding Decorators by Category

You can find decorators by category using the registry:

```python
# Find all reasoning decorators
reasoning_decorators = registry.find_decorators_by_category("reasoning")

# Find all format decorators
format_decorators = registry.find_decorators_by_category("format")

# Print available decorators in a category
for decorator_class in reasoning_decorators:
    print(f"- {decorator_class.__name__}")
```

## Using Decorated Requests

For more complex scenarios, you can use the `DecoratedRequest` class:

```python
from prompt_decorators.core.request import DecoratedRequest
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Create a decorated request
request = DecoratedRequest(
    prompt="Explain quantum mechanics.",
    decorators=[reasoning, output_format],
    model="gpt-4",
    api_params={"temperature": 0.7}
)

# Apply all decorators
decorated_prompt = request.apply_decorators()

print(decorated_prompt)

# Serialize for storage or transmission
request_json = request.to_json()
print(request_json)
```

## Checking Decorator Compatibility

You can check if decorators are compatible with each other:

```python
from prompt_decorators.utils.compatibility import get_compatibility_checker
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Get the compatibility checker
checker = get_compatibility_checker()

# Check compatibility
issues = checker.check_compatibility(reasoning, output_format)

if issues:
    for issue in issues:
        print(f"Warning: {issue}")
else:
    print("Decorators are compatible!")
```

## Next Steps

- Learn about [Advanced Usage](advanced-usage.md)
- Explore the [API Reference](../api/index.md)
- Check out more [Examples](../examples/basic.md)

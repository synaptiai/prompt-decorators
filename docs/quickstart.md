# Quick Start Guide

This guide will help you get started with the Prompt Decorators framework quickly.

## Installation

First, install the Prompt Decorators package:

```bash
pip install prompt-decorators
```

For development installation or other options, see the [Installation Guide](installation.md).

## Basic Usage

### Using Individual Decorators

Here's a simple example of using a decorator to modify a prompt:

```python
from prompt_decorators.decorators import Reasoning
from prompt_decorators.decorators.reasoning import ReasoningStyle

# Create a Reasoning decorator
reasoning = Reasoning(
    style=ReasoningStyle.DETAILED.value,
    show_working=True,
    consider_alternatives=True
)

# Apply the decorator to a prompt
prompt = "Explain quantum entanglement."
decorated_prompt = reasoning.apply(prompt)

print(decorated_prompt)
```

### Combining Multiple Decorators

You can combine multiple decorators to create more complex prompt modifications:

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

### Using the Decorator Registry

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

### Using Decorated Requests

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

## Next Steps

- Learn about [Core Concepts](concepts.md)
- Explore the [API Reference](api/index.md)
- Check out more [Examples](examples/basic.md)
- Learn about [Creating Custom Decorators](guide/advanced-usage.md)

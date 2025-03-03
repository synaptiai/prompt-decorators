# Basic Examples

This page provides basic examples of using the Prompt Decorators framework.

## Using Individual Decorators

### Reasoning Decorator

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

### Output Format Decorator

```python
from prompt_decorators.decorators import OutputFormat
from prompt_decorators.decorators.format import FormatType

# Create an OutputFormat decorator
output_format = OutputFormat(
    format_type=FormatType.MARKDOWN.value,
    pretty_print=True
)

# Apply the decorator to a prompt
prompt = "List the top 5 programming languages."
decorated_prompt = output_format.apply(prompt)

print(decorated_prompt)
```

## Combining Multiple Decorators

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

## Using Decorated Requests

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

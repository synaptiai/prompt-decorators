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

<a id="examples"></a>
## Common Usage Examples

Here are some common examples of using prompt decorators in different scenarios:

### Educational Content Generation

```python
from prompt_decorators.decorators import ELI5, StepByStep, OutputFormat

# Create decorators for educational content
eli5 = ELI5(age=10)
step_by_step = StepByStep(numbered=True, detail_level="high")
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to create educational content
prompt = "Explain how photosynthesis works."
decorated_prompt = output_format.apply(step_by_step.apply(eli5.apply(prompt)))

print(decorated_prompt)
```

### Technical Documentation

```python
from prompt_decorators.decorators import Detailed, OutputFormat, CiteSources

# Create decorators for technical documentation
detailed = Detailed(depth=3, examples=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)
cite_sources = CiteSources(required=True, format="apa")

# Apply decorators for technical documentation
prompt = "Explain RESTful API design principles."
decorated_prompt = output_format.apply(cite_sources.apply(detailed.apply(prompt)))

print(decorated_prompt)
```

### Creative Writing

```python
from prompt_decorators.decorators import Creative, Tone, Persona

# Create decorators for creative writing
creative = Creative(originality=0.8, metaphors=True)
tone = Tone(style="whimsical")
persona = Persona(character="storyteller")

# Apply decorators for creative writing
prompt = "Write a short story about a journey through space."
decorated_prompt = persona.apply(tone.apply(creative.apply(prompt)))

print(decorated_prompt)
```

### Data Analysis

```python
from prompt_decorators.decorators import Reasoning, OutputFormat, StepByStep

# Create decorators for data analysis
reasoning = Reasoning(style="analytical", show_working=True)
step_by_step = StepByStep(numbered=True, detail_level="high")
output_format = OutputFormat(format_type="markdown", code_blocks=True)

# Apply decorators for data analysis
prompt = "Analyze this dataset and explain trends: [data description]"
decorated_prompt = output_format.apply(step_by_step.apply(reasoning.apply(prompt)))

print(decorated_prompt)
```

## Next Steps

- Learn about [Advanced Usage](advanced-usage.md)
- Explore the [API Reference](../api/index.md)
- Check out more [Examples](../examples/basic.md)

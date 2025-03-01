# Prompt Decorators Framework: Quickstart Guide

This guide will help you get started with the Prompt Decorators framework for enhancing your LLM interactions.

## Installation

First, install the Prompt Decorators framework using pip:

```bash
pip install prompt-decorators
```

Or directly from the source:

```bash
git clone https://github.com/prompt-decorators/prompt-decorators.git
cd prompt-decorators
pip install -e .
```

## Basic Usage

### Using Built-in Decorators

The simplest way to use the framework is with built-in decorators:

```python
from prompt_decorators.decorators.generated.decorators.concise import Concise
from prompt_decorators.decorators.generated.decorators.professional import Professional

# Create the decorators with desired parameters
concise = Concise(max_words=150, bullet_points=True)
professional = Professional(industry="technology")

# Original prompt
prompt = "Explain the benefits of machine learning in healthcare."

# Apply decorators - order matters!
decorated_prompt = concise.apply(professional.apply(prompt))

# Use the decorated prompt with your LLM API
print(decorated_prompt)
```

This will output something like:

```
Please maintain a professional tone appropriate for the technology industry. Use industry-standard 
terminology, clear explanations, and well-structured arguments.

Please provide a concise response. Limit your response to 150 words or fewer. Format your response 
as bullet points.

Explain the benefits of machine learning in healthcare.
```

### Using the Decorator Registry

For more flexibility, you can use the decorator registry:

```python
from prompt_decorators.utils import get_registry

# Get the registry
registry = get_registry()

# Create decorators through the registry
concise = registry.create_decorator("Concise", max_words=150, bullet_points=True)
eli5 = registry.create_decorator("ELI5", age=10)

# Apply decorators to a prompt
prompt = "Explain how neural networks work."
decorated_prompt = concise.apply(eli5.apply(prompt))

# Use the decorated prompt with your LLM API
print(decorated_prompt)
```

### Finding Available Decorators

To explore the available decorators:

```python
from prompt_decorators.utils import get_registry

registry = get_registry()

# Get all categories
categories = registry.get_categories()
print(f"Available categories: {', '.join(categories)}")

# Find decorators by category
reasoning_decorators = registry.find_decorators_by_category("reasoning")
for name in reasoning_decorators:
    print(f"- {name}")
```

## Creating Your Own Decorator

You can easily create your own custom decorators:

```python
from prompt_decorators.core import BaseDecorator

class CustomDecorator(BaseDecorator):
    """A custom decorator for specialized instructions."""
    
    name = "Custom"
    version = "1.0.0"
    category = "custom"
    
    def __init__(self, instruction: str, emphasis: int = 1):
        super().__init__()
        self.instruction = instruction
        self.emphasis = max(1, min(3, emphasis))
    
    def apply(self, prompt: str) -> str:
        """Apply the custom instruction to the prompt."""
        emphasis_marks = "!" * self.emphasis
        return f"{self.instruction}{emphasis_marks}\n\n{prompt}"

# Create and use the custom decorator
custom = CustomDecorator("Remember to include real-world examples", emphasis=2)
prompt = "Explain how blockchain works."
decorated_prompt = custom.apply(prompt)
```

## Working with Model-Specific Adaptations

For adapting decorators to specific models:

```python
from prompt_decorators.utils import get_model_detector
from prompt_decorators.core import ModelSpecificDecorator

# Create a model-specific decorator
class CustomModelSpecificDecorator(ModelSpecificDecorator):
    name = "CustomModelSpecific"
    version = "1.0.0"
    
    def apply_for_model(self, prompt: str) -> str:
        """Adapt based on model capabilities."""
        if self.model_capabilities.supports_feature("reasoning"):
            return f"Use your reasoning capabilities to answer: {prompt}"
        else:
            return self.apply_fallback(prompt)
    
    def apply_fallback(self, prompt: str) -> str:
        """Fallback for models without specific capabilities."""
        return f"Answer this question step by step: {prompt}"

# Use with a specific model
decorator = CustomModelSpecificDecorator(model_id="gpt-4")
prompt = "Explain quantum computing."
decorated_prompt = decorator.apply(prompt)
```

## Next Steps

Check out these resources to learn more:

- [Complete API documentation](../api/index.md)
- [Decorator catalog](../api/decorators/)
- [Advanced usage tutorials](../tutorials/)
- [Example scripts](../../examples/)

For detailed information on specific decorators, see the generated documentation in the `docs/api/decorators/` directory. 
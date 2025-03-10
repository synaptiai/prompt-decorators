# Quick Start

This guide will help you get started with Prompt Decorators quickly, showing the most common usage patterns.

## Basic Usage

### 1. Import the Package

```python
from prompt_decorators import apply_dynamic_decorators, create_decorator_instance
```

### 2. Using Inline Decorator Syntax

The simplest way to use prompt decorators is with the inline syntax directly in your prompts:

```python
# Create a prompt with decorators using inline syntax
prompt = """
+++StepByStep(numbered=true)
Explain how photosynthesis works.
"""

# Apply the decorators to transform the prompt
transformed_prompt = apply_dynamic_decorators(prompt)

# Send the transformed prompt to any LLM
# response = your_llm_function(transformed_prompt)
print(transformed_prompt)
```

### 3. Using Decorator Instances

You can also create and use decorator instances programmatically:

```python
# Create a decorator instance
step_by_step = create_decorator_instance("StepByStep", numbered=True)

# Apply the decorator to a prompt
original_prompt = "Explain how photosynthesis works."
transformed_prompt = step_by_step(original_prompt)

# Send to your LLM
# response = your_llm_function(transformed_prompt)
print(transformed_prompt)
```

### 4. Combining Multiple Decorators

You can stack multiple decorators either inline or programmatically:

```python
# Inline stacking
prompt = """
+++Persona(role="scientist")
+++StepByStep(numbered=true)
+++Audience(level="beginner")
Explain how photosynthesis works.
"""
transformed_prompt = apply_dynamic_decorators(prompt)

# Or programmatically
persona = create_decorator_instance("Persona", role="scientist")
step_by_step = create_decorator_instance("StepByStep", numbered=True)
audience = create_decorator_instance("Audience", level="beginner")

original_prompt = "Explain how photosynthesis works."
transformed_prompt = persona(step_by_step(audience(original_prompt)))
```

## Working with Decorators

### Listing Available Decorators

You can list all available decorators:

```python
from prompt_decorators import get_available_decorators

decorators = get_available_decorators()
for decorator in decorators:
    print(f"{decorator.name}: {decorator.description}")
```

### Getting Decorator Details

To get detailed information about a specific decorator:

```python
# Find a specific decorator by name
decorators = get_available_decorators()
reasoning_decorator = next((d for d in decorators if d.name == "Reasoning"), None)

if reasoning_decorator:
    print(f"Name: {reasoning_decorator.name}")
    print(f"Description: {reasoning_decorator.description}")
    print(f"Category: {reasoning_decorator.category}")
    print("Parameters:")
    for param in reasoning_decorator.parameters:
        print(f"  - {param.name}: {param.description}")
        if hasattr(param, 'default'):
            print(f"    Default: {param.default}")
```

### Validating Decorator Syntax

You can validate decorator syntax using the validation tools:

```bash
# Validate decorator syntax in a prompt
python scripts/prompt_validator.py syntax -t "+++Reasoning(depth=comprehensive)\nExplain quantum computing."

# Validate a decorator schema file
python scripts/prompt_validator.py schema -f registry/core/reasoning/deductive.json

# Validate all files in a directory
python scripts/prompt_validator.py directory -d registry/core -s registry
```

You can also validate syntax programmatically:

```python
from prompt_decorators.core.dynamic_decorator import extract_decorators

# Extract and validate decorators from a prompt
prompt = """
+++Reasoning(depth=comprehensive)
+++StepByStep(numbered=true)
Explain quantum computing.
"""

decorators, cleaned_text = extract_decorators(prompt)
for decorator in decorators:
    print(f"Found decorator: {decorator.name} with parameters: {decorator.parameters}")
```

## Integration with LLM Providers

### Using with OpenAI

```python
import openai
from prompt_decorators import apply_dynamic_decorators

# Set up OpenAI API key
openai.api_key = "your-api-key-here"

# Create and transform a prompt
prompt = """
+++StepByStep(numbered=true)
+++Audience(level="beginner")
Explain quantum computing.
"""
transformed_prompt = apply_dynamic_decorators(prompt)

# Send to OpenAI
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": transformed_prompt}
    ],
    temperature=0.7,
    max_tokens=1000
)

# Print the response
print(response.choices[0].message.content)
```

### Using with Anthropic Claude

```python
import anthropic
from prompt_decorators import apply_dynamic_decorators

# Set up Anthropic client
client = anthropic.Anthropic(api_key="your-anthropic-api-key")

# Create and transform a prompt
prompt = """
+++StepByStep(numbered=true)
+++Persona(role="teacher")
Explain the water cycle.
"""
transformed_prompt = apply_dynamic_decorators(prompt)

# Send to Anthropic Claude
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.7,
    messages=[
        {"role": "user", "content": transformed_prompt}
    ]
)

# Print the response
print(message.content[0].text)
```

## MCP Integration

Prompt Decorators integrates with the [Model Context Protocol (MCP)](https://github.com/mpaepper/mcp) to provide decoration functionality to any MCP-compatible client:

```bash
# Run the MCP server (general use)
python -m prompt_decorators.integrations.mcp

# For Claude Desktop integration
python -m prompt_decorators.integrations.mcp.claude_desktop
```

For detailed MCP integration instructions, see the [MCP Integration Guide](integrations/mcp.md).

## Creating Custom Decorators

You can create your own decorators:

```python
from prompt_decorators import (
    DecoratorDefinition,
    register_decorator,
    create_decorator_instance
)

# Define a custom decorator
my_decorator_def = DecoratorDefinition(
    name="MyCustomDecorator",
    description="A custom decorator that adds a prefix and suffix",
    category="Custom",
    parameters=[
        {"name": "prefix", "type": "string", "description": "Text to add before", "default": "START: "},
        {"name": "suffix", "type": "string", "description": "Text to add after", "default": " :END"}
    ],
    transform_function="return prefix + text + suffix;"
)

# Register it for use
register_decorator(my_decorator_def)

# Use your custom decorator
my_decorator = create_decorator_instance("MyCustomDecorator", prefix="BEGINNING: ", suffix=" :COMPLETE")
result = my_decorator("This is my text")
print(result)  # Output: "BEGINNING: This is my text :COMPLETE"
```

For more examples of how to create custom decorators, see the [Creating Custom Decorators Tutorial](tutorials/creating_custom_decorator.md).

## Next Steps

- Explore [Core Concepts](concepts.md) to understand the design principles behind the framework
- Learn about [Creating Decorators](creating_decorators.md) to build your own custom decorators
- Check out the [Tutorials](tutorials/creating_custom_decorator.md) for step-by-step examples
- See the [MCP Integration](integrations/mcp.md) for using decorators with Claude and other LLMs

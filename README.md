# Prompt Decorators 🎨

[![PyPI version](https://badge.fury.io/py/prompt-decorators.svg)](https://badge.fury.io/py/prompt-decorators)
[![Python Versions](https://img.shields.io/pypi/pyversions/prompt-decorators.svg)](https://pypi.org/project/prompt-decorators/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A Python framework for enhancing prompts sent to Large Language Models (LLMs).

## 🚀 Dynamic Implementation

> **New in v0.3.0!** The framework has been completely refactored to use a dynamic implementation. This means decorators are now loaded directly from definitions at runtime, without code generation. This makes it easier to create, modify, and extend decorators without having to regenerate code.

## 📋 Features

- **Dynamic Decorators**: Create and use decorators without code generation
- **Inline Syntax**: Use the `+++DecoratorName(param=value)` syntax directly in your prompts
- **Registry**: Over 140 pre-defined decorators to enhance your prompts
- **Extensible**: Easily create your own custom decorators
- **MCP Integration**: Seamless integration with the [Model Context Protocol](https://github.com/mpaepper/mcp)
- **Framework Agnostic**: Use with any LLM provider (OpenAI, Anthropic, HuggingFace, etc.)

## ⚙️ Installation

```bash
pip install prompt-decorators
```

## 🔍 Quick Start

```python
from prompt_decorators import apply_dynamic_decorators, create_decorator_instance

# Using the inline syntax
prompt = """
+++StepByStep(numbered=true)
How do I build a website?
"""

# Apply decorators to transform the prompt
transformed_prompt = apply_dynamic_decorators(prompt)
print(transformed_prompt)

# Or create and use decorator instances programmatically
step_by_step = create_decorator_instance("StepByStep", numbered=True)
transformed_prompt = step_by_step("How do I build a website?")
print(transformed_prompt)
```

## 📚 Using Decorators

Prompt decorators use a simple syntax directly in your prompts:

```
+++DecoratorName(param1=value1, param2=value2)
Your prompt text goes here.
```

Multiple decorators can be stacked:

```
+++Persona(role="scientist")
+++StepByStep(numbered=true)
+++Reasoning(depth="comprehensive")
Explain quantum computing to me.
```

## 📓 Available Decorators

The framework includes over 140 pre-defined decorators in categories such as:

- **Reasoning**: Enhance logical thinking and problem-solving
- **Format**: Control output format and structure
- **Style**: Modify tone, voice, and writing style
- **Audience**: Target specific audiences
- **Persona**: Adopt specific roles or personalities
- **Domain**: Focus on specific knowledge domains
- **Length**: Control response length

List all available decorators:

```python
from prompt_decorators import get_available_decorators

decorators = get_available_decorators()
for decorator in decorators:
    print(f"{decorator.name}: {decorator.description}")
```

## 🔧 MCP Integration

The framework integrates with the [Model Context Protocol (MCP)](https://github.com/mpaepper/mcp) to provide decorator functionality to any MCP-compatible client:

```python
from prompt_decorators.integrations.mcp_dynamic import create_mcp_server

# Create and start the MCP server
server = create_mcp_server("prompt-decorators")
server.run_stdio()  # or server.run_async() for async operation
```

## 🧩 Creating Custom Decorators

Create your own decorator by defining a JSON schema:

```python
from prompt_decorators import (
    DynamicDecorator,
    DecoratorDefinition,
    register_decorator
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

# Use it
custom_decorator = DynamicDecorator.from_definition(my_decorator_def)
result = custom_decorator("This is my text")
print(result)  # "START: This is my text :END"
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

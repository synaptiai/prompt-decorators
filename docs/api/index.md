# API Reference

This section provides detailed documentation for the Prompt Decorators API. The API is organized into several modules:

## Core

The core module contains the fundamental components of the Prompt Decorators framework:

- [Base](modules/core/base.md): Base classes and interfaces for decorators
- [Registry](modules/core/registry.md): Decorator registration and management
- [Validation](modules/core/validation.md): Validation of decorator syntax and parameters
- [Request](modules/core/request.md): Request handling and processing
- [Exceptions](modules/core/exceptions.md): Exception classes for error handling
- [Model Specific](modules/core/model_specific.md): Model-specific implementations and adaptations

## Decorators

The [decorators module](decorators.md) contains all the decorator implementations, organized by category:

- **Reasoning Decorators**: Control how the AI approaches reasoning about a problem
- **Output Structure Decorators**: Specify the structure and format of the AI's response
- **Tone and Style Decorators**: Modify the linguistic style and tone of the AI's response
- **Verification and Quality Decorators**: Focus on ensuring accuracy, balance, and quality
- **Meta-Decorators**: Modify the behavior of other decorators or provide higher-level control

## Utilities

The utilities module provides supporting functionality:

- [Cache](modules/utils/cache.md): Caching mechanisms for improved performance

## Generator

The generator module contains code generation utilities:

- [Code Generation](modules/generator/code_gen.md): Generation of decorator code
- [Test Generation](modules/generator/test_gen.md): Generation of test code
- [Registry](modules/generator/registry.md): Registry for code generation templates

## Using the API

To use the Prompt Decorators API in your code, you typically start by importing the necessary components:

```python
from prompt_decorators import DecoratorProcessor
from prompt_decorators.decorators import Reasoning, StepByStep, OutputFormat
```

Then, you can create a processor and apply decorators to your prompts:

```python
processor = DecoratorProcessor()
decorated_prompt = processor.apply([
    Reasoning(depth="comprehensive"),
    StepByStep(numbered=True),
    OutputFormat(format="markdown")
], "Explain how nuclear fusion works.")
```

For more detailed examples, see the [Examples](../examples/basic.md) section.

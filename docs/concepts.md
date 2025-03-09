# Core Concepts

This document explains the core concepts behind the Prompt Decorators framework, including its design philosophy, implementation approach, and key components.

## What are Prompt Decorators?

Prompt Decorators are a structured framework for enhancing prompts sent to Large Language Models (LLMs). Based on the decorator pattern in software design, they provide a consistent way to modify how AI models process and respond to requests.

The framework uses a simple syntax where decorators are prefixed with `+++` followed by a decorator name and optional parameters, allowing users to consistently control AI behavior across different platforms.

### Key Features

- **Standardized Syntax**: Consistent way to apply modifications across different prompts
- **Composability**: Multiple decorators can be combined for complex behaviors
- **Extensibility**: The framework supports custom decorator definitions
- **Minimal Token Usage**: Concise annotations that reduce token consumption
- **Dynamic Implementation**: Runtime modification without code generation

## Design Philosophy

The Prompt Decorators framework is designed around these principles:

1. **Simplicity**: Decorators should be easy to learn, remember, and apply
2. **Consistency**: Behavior should be predictable across different models and contexts
3. **Composability**: Decorators should work well together without conflicts
4. **Extensibility**: The framework should allow for new decorators as needs evolve
5. **Human Readability**: Syntax should be comprehensible to humans, not just machines

## Core Components

### 1. Decorator Syntax

The canonical syntax for a Prompt Decorator follows this pattern:

```
+++<DecoratorName>[(parameter1=value1[, parameter2=value2, ...])]
```

Where:
- `+++` is the decorator prefix that identifies a decorator
- `<DecoratorName>` is the case-sensitive name of the decorator
- Parameters are optional and enclosed in parentheses
- Multiple parameters are separated by commas
- Parameter names and values are separated by equals signs

Example:
```
+++StepByStep(numbered=true)
Explain how nuclear fusion works.
```

### 2. Dynamic Decorator Implementation

The framework uses a dynamic implementation that loads decorator definitions at runtime, eliminating the need for code generation. This approach offers several advantages:

- **Flexibility**: Decorators can be created and modified without regenerating code
- **Runtime Loading**: Decorators are loaded from definitions when needed
- **Extensibility**: Custom decorators can be defined and used immediately

### 3. Decorator Registry

The framework maintains a registry of available decorators, including their:

- **Name**: Unique identifier for the decorator
- **Description**: Purpose and behavior of the decorator
- **Category**: Functional grouping (reasoning, format, style, etc.)
- **Parameters**: Configurable options with types and default values
- **Transform Function**: JavaScript function that defines the transformation logic

### 4. Decorator Categories

Decorators are organized into functional categories:

- **Reasoning**: Enhance logical thinking and problem-solving (e.g., `Reasoning`, `StepByStep`, `TreeOfThought`)
- **Format**: Control output format and structure (e.g., `OutputFormat`, `Bullet`, `TableFormat`)
- **Style**: Modify tone, voice, and writing style (e.g., `Tone`, `Academic`, `Creative`)
- **Audience**: Target specific audiences (e.g., `Audience`, `ELI5`, `Technical`)
- **Persona**: Adopt specific roles or personalities (e.g., `Persona`, `AsExpert`, `Professional`)
- **Domain**: Focus on specific knowledge domains (e.g., `Scientific`, `Legal`, `Medical`)
- **Length**: Control response length (e.g., `Concise`, `Detailed`, `Summary`)

## Core Classes and Functions

### DecoratorBase

The abstract base class for all decorators, providing common functionality:

```python
class DecoratorBase:
    """Base class for all decorators."""

    def __init__(self, **kwargs):
        """Initialize with parameters as keyword arguments."""

    def __call__(self, text: str) -> str:
        """Apply the decorator to the given text."""

    def to_string(self) -> str:
        """Convert the decorator to its string representation."""
```

### DynamicDecorator

The implementation class for dynamically defined decorators:

```python
class DynamicDecorator(DecoratorBase):
    """Dynamic decorator implementation."""

    @classmethod
    def from_definition(cls, definition: DecoratorDefinition) -> 'DynamicDecorator':
        """Create a decorator class from a definition."""

    def __call__(self, text: str) -> str:
        """Apply the decorator to the given text."""
```

### DecoratorDefinition

The class that defines a decorator's properties:

```python
class DecoratorDefinition:
    """Definition of a decorator."""

    def __init__(
        self,
        name: str,
        description: str,
        category: str,
        parameters: List[Dict[str, Any]],
        transform_function: str
    ):
        """Initialize a decorator definition."""
```

### Key Functions

- **apply_dynamic_decorators**: Parse and apply decorators from a text prompt
- **create_decorator_instance**: Create an instance of a decorator by name
- **get_available_decorators**: Get a list of all registered decorators
- **register_decorator**: Register a new decorator definition

## Transformation Process

When decorators are applied to a prompt, the framework follows these steps:

1. **Parsing**: Extract decorator names, parameters, and the base prompt text
2. **Loading**: Load decorator definitions from the registry
3. **Parameter Validation**: Validate parameter values against definitions
4. **Transformation**: Apply each decorator's transform function in sequence
5. **Composition**: Combine the transformed text from multiple decorators

The transformation converts decorator annotations into natural language instructions that the LLM can understand:

```
# Original prompt with decorator
+++Reasoning(depth=comprehensive)
What are the environmental impacts of electric vehicles?

# Transformed prompt
Please provide detailed reasoning in your response. Show your thought process step by step before reaching a conclusion. Provide a very thorough and detailed analysis with multiple perspectives.

What are the environmental impacts of electric vehicles?
```

## Decorator Compatibility

The framework includes mechanisms for handling decorator conflicts:

1. **Precedence**: When decorators have incompatible requirements, the later decorator takes precedence
2. **Parameter Conflicts**: For parameter conflicts, the parameter in the later decorator takes precedence
3. **Documentation**: The framework provides documentation on known decorator conflicts

## Extension Mechanisms

The framework supports several extension mechanisms:

1. **Custom Decorators**: Users can define and register their own decorators
2. **Decorator Packages**: Collections of related decorators can be packaged and distributed
3. **Integration Adapters**: The framework can be integrated with different LLM providers and platforms

## Next Steps

- Learn how to [create custom decorators](creating_decorators.md)
- Explore the [MCP integration](integrations/mcp.md) for using decorators with Claude and other LLMs
- See the [specification](prompt-decorators-specification-v1.0.md) for detailed technical information

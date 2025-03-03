# Core Concepts

This page explains the fundamental concepts behind the Prompt Decorators framework.

## What are Prompt Decorators?

Prompt decorators are modular, reusable components that modify prompts sent to Large Language Models (LLMs). They encapsulate specific modifications to prompts that can be combined, validated, and applied systematically.

The concept is inspired by the decorator pattern in object-oriented programming, where decorators add functionality to objects without modifying their structure.

## Key Components

### BaseDecorator

The `BaseDecorator` class is the foundation of all decorators in the framework. It provides:

- Parameter validation
- Versioning support
- Serialization/deserialization
- The `apply()` method for modifying prompts

All specific decorator types inherit from this base class.

### Decorator Registry

The registry system provides:

- Runtime discovery of available decorators
- Decorator metadata and documentation
- Categorization and organization of decorators
- Version management

### Decorator Types

The framework includes various types of decorators, such as:

1. **Reasoning Decorators**: Modify how the LLM approaches reasoning about a problem
2. **Format Decorators**: Control the output format (markdown, JSON, etc.)
3. **Style Decorators**: Adjust the tone, verbosity, or style of the response
4. **Verification Decorators**: Add verification steps or fact-checking
5. **Meta Decorators**: Modify or combine other decorators

## Decorator Lifecycle

1. **Definition**: Decorators are defined in the registry with their parameters, constraints, and metadata
2. **Generation**: Code is generated from the registry definitions
3. **Instantiation**: Decorators are instantiated with specific parameter values
4. **Application**: Decorators modify prompts through their `apply()` method
5. **Composition**: Multiple decorators can be combined in a specific order

## Decorator Parameters

Each decorator can have multiple parameters that control its behavior:

- Parameters have types (string, integer, boolean, etc.)
- Parameters can have constraints (min/max values, allowed values, etc.)
- Parameters can have default values
- Parameters are validated when a decorator is instantiated

## Versioning

The framework supports semantic versioning for decorators:

- Major version changes indicate breaking changes
- Minor version changes indicate new features
- Patch version changes indicate bug fixes
- Version compatibility is checked when combining decorators

## Compatibility

Not all decorators can be used together. The framework provides:

- A compatibility matrix to determine which decorators can be combined
- Runtime compatibility checking
- Warnings or errors when incompatible decorators are used together

## Request System

The `DecoratedRequest` class provides:

- A container for a prompt and its associated decorators
- Methods to apply all decorators in the correct order
- Serialization/deserialization for storage or transmission
- Integration with LLM APIs

## Extension Points

The framework is designed to be extensible:

- Custom decorators can be created by inheriting from `BaseDecorator`
- New decorator types can be added to the registry
- Custom parameter types and constraints can be defined
- Integration with different LLM providers is supported

## Next Steps

- See the [Quick Start Guide](quickstart.md) for practical examples
- Explore the [API Reference](api/index.md) for detailed documentation
- Learn about [Creating Custom Decorators](guide/advanced-usage.md)

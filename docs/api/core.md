# Core API

This page provides an overview of the core API components of the Prompt Decorators framework. For detailed documentation of each component, please refer to the specific module pages.

## Base Module

The Base module provides the fundamental classes and interfaces for the Prompt Decorators framework:

- [BaseDecorator](modules/core/base.md#core-base-api-reference): The base class for all decorators
- [DecoratorProcessor](modules/core/base.md#core-base-api-reference): Processes and applies multiple decorators to prompts
- [ParameterDefinition](modules/core/base.md#core-base-api-reference): Defines parameters for decorators

## Request Module

The Request module provides functionality for handling decorated requests:

- [DecoratedRequest](modules/core/request.md#core-request-api-reference): Represents a request with decorators
- [RequestProcessor](modules/core/request.md#core-request-api-reference): Processes decorated requests

## Validation Module

The Validation module provides utilities for validating decorator syntax, parameters, and compatibility:

- [DecoratorValidator](modules/core/validation.md#core-validation-api-reference): Validates decorator syntax and parameters
- [ParameterValidator](modules/core/validation.md#core-validation-api-reference): Validates decorator parameters against their definitions
- [SchemaValidator](modules/core/validation.md#core-validation-api-reference): Validates decorator schemas against JSON Schema definitions

## Model-Specific Module

The Model-Specific module provides functionality for adapting decorators to specific language models:

- [ModelAdapter](modules/core/model_specific.md#core-model-specific-api-reference): Adapts decorators to specific language models
- [ModelCapabilities](modules/core/model_specific.md#core-model-specific-api-reference): Defines the capabilities of a language model
- [ModelRegistry](modules/core/model_specific.md#core-model-specific-api-reference): Registry of language models and their capabilities

## Registry Module

The Registry module provides functionality for registering and managing decorators:

- [DecoratorRegistry](modules/core/registry.md): Registry of available decorators
- [RegistryEntry](modules/core/registry.md): Entry in the decorator registry

## Exceptions Module

The Exceptions module provides exception classes for error handling:

- [DecoratorError](modules/core/exceptions.md): Base class for all decorator-related exceptions
- [ValidationError](modules/core/exceptions.md): Exception raised when validation fails
- [CompatibilityError](modules/core/exceptions.md): Exception raised when decorators are incompatible

# Glossary

This glossary defines key terms used throughout the Prompt Decorators documentation.

## A

### API Integration
The process of connecting the Prompt Decorators framework with various LLM provider APIs, such as OpenAI, Anthropic, or Hugging Face.

### Apply Method
The core method of a decorator that takes a prompt as input and returns a modified prompt as output. All decorators must implement this method.

## B

### BaseDecorator
The abstract base class that all decorators must inherit from. It defines the interface that all decorators must implement, including the `apply`, `to_dict`, and `from_dict` methods.

## C

### Chain of Thought
A prompt engineering technique that encourages the LLM to break down complex problems into steps and show its reasoning process. Implemented as the `ChainOfThought` decorator in the framework.

### CLI (Command Line Interface)
A text-based interface that allows users to interact with the Prompt Decorators framework through terminal commands.

### Compatibility
The ability of decorators to work together without conflicts. The framework includes tools to check decorator compatibility.

### Custom Decorator
A decorator created by a user that extends the BaseDecorator class to implement specific functionality not provided by the built-in decorators.

## D

### Decorator
In the context of this framework, a class that modifies a prompt to enhance its effectiveness with LLMs. Not to be confused with Python decorators (the `@decorator` syntax), although the concept is similar.

### Decorator Chain
A sequence of decorators applied one after another to a prompt. The order of application matters, as each decorator modifies the prompt based on its current state.

### Decorator Registry
A central repository that keeps track of all available decorators, their metadata, and provides methods to retrieve and instantiate them.

### DecoratedRequest
A class that encapsulates a prompt, a list of decorators to apply, and additional metadata like the target model and API parameters.

### Discovery
The process of automatically finding and registering decorators in the registry, typically by scanning specific directories for classes that inherit from BaseDecorator.

## F

### Few-Shot Learning
A technique where examples are provided in the prompt to help the LLM understand the desired output format or reasoning pattern.

## I

### Interactive Mode
A CLI mode that provides a step-by-step interface for selecting and configuring decorators, entering a prompt, and viewing the decorated result.

## J

### JSON Schema
A vocabulary that allows you to annotate and validate JSON documents. Used in the framework to define the structure of decorator parameters and validate them.

## L

### LLM (Large Language Model)
A type of AI model trained on vast amounts of text data that can generate human-like text based on prompts. Examples include GPT-4, Claude, and Llama.

## M

### Middleware
A component that sits between decorators and their application, allowing for additional processing or modification of the prompt before or after a decorator is applied.

### Model-Specific Adaptation
Modifications to decorators or their application based on the specific LLM being used, to account for differences in how various models respond to prompts.

## O

### OutputFormat
A decorator that specifies the desired format for the LLM's response, such as JSON, Markdown, or a custom structure.

## P

### Parameter
A configurable value that affects how a decorator modifies a prompt. Parameters are defined in a decorator's schema and can be set when instantiating the decorator.

### Persona
A decorator that adds characteristics of a specific role or personality to the prompt, influencing the tone and perspective of the LLM's response.

### Plugin
An extension mechanism that allows adding new functionality to the framework without modifying its core code.

### Prompt
The input text sent to an LLM to generate a response. In the context of this framework, prompts are modified by decorators to enhance their effectiveness.

### Prompt Engineering
The practice of designing and refining prompts to get better, more reliable responses from LLMs.

## R

### Reasoning
A decorator that encourages the LLM to use specific reasoning patterns or approaches when generating a response.

### Registry
See Decorator Registry.

## S

### Serialization
The process of converting decorator instances or decorated requests to a format (like JSON) that can be stored or transmitted, and later reconstructed.

### System Prompt
A special type of prompt that sets the overall behavior and context for an LLM session, separate from the user's specific query.

## T

### Template
A predefined structure for prompts with placeholders for variables. Templates can be used as a starting point before applying decorators.

### Token
The basic unit of text that LLMs process. A token can be as short as a character or as long as a word, depending on the model's tokenization scheme.

## V

### Validation
The process of checking that decorator parameters conform to their defined schema, ensuring they are of the correct type and within acceptable ranges.

### Versioning
A system for tracking and managing different versions of decorators, allowing for compatibility checks and updates.

## Next Steps

- Explore the [API Reference](api/index.md)
- Check out the [Examples](examples/basic.md)
- Read the [FAQ](faq.md) for answers to common questions

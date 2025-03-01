# Prompt Decorators: A Standard for Enhanced AI Interactions


[![Standard Status: Proposed](https://img.shields.io/badge/Standard%20Status-Proposed-yellow.svg)](https://github.com/prompt-decorators/spec)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A standardized framework for enhancing AI interactions through simple, composable prompt modifiers.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Quick Examples](#quick-examples)
- [Specification](#specification)
- [Implementation Guide](#implementation-guide)
- [Demo & Test Suite](#demo--test-suite)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

Prompt Decorators provide a standardized syntax for modifying how AI models process and respond to prompts. Inspired by function decorators in programming languages, this specification creates a consistent way to guide AI behavior across different models and platforms.

Instead of writing lengthy instructions in each prompt, users can simply add decorator prefixes like `+++Reasoning` or `+++StepByStep` to achieve specific response patterns.

## Key Features

- **Simple Syntax**: Easy-to-learn `+++Decorator(parameter=value)` format
- **Composable Behavior**: Stack multiple decorators to create complex interactions
- **Cross-Platform**: Designed to work across compatible LLM implementations
- **Extensible**: Framework for creating specialized decorators for different domains
- **Implementation Agnostic**: Can be applied at different integration levels (API, UI, middleware)

## Quick Examples

### Basic Example

```
+++Reasoning
What are the ethical implications of autonomous vehicles?
```

The AI will provide detailed reasoning before reaching conclusions.

### Multiple Decorators

```
+++StepByStep(numbered=true)
+++OutputFormat(format=markdown)
How do I build a simple React component?
```

The AI will provide numbered steps in Markdown format.

### Complex Example

```
+++Debate(perspectives=3)
+++DecisionMatrix(criteria=cost,feasibility,timeline,risks)
+++FactCheck
Should our startup migrate to a cloud-native architecture?
```

The AI will provide a balanced debate with multiple perspectives, structured as a decision matrix, with factual claims verified.

## Specification

The full specification is available in [prompt-decorators-specification-v1.0.md](prompt-decorators-specification-v1.0.md). 

Key sections include:

- [Core Syntax](docs/prompt-decorators-specification-v1.0.md#3-syntax-specification)
- [Standard Decorators](docs/prompt-decorators-specification-v1.0.md#4-categories-of-prompt-decorators)
- [Implementation Guidelines](docs/prompt-decorators-specification-v1.0.md#5-implementation-considerations)
- [Security & Privacy Considerations](docs/prompt-decorators-specification-v1.0.md#11-security-and-privacy-considerations)

### Core Decorators

| Decorator | Description | Example |
|-----------|-------------|---------|
| `+++Reasoning` | Show reasoning process | `+++Reasoning(depth=comprehensive)` |
| `+++StepByStep` | Break into sequential steps | `+++StepByStep(numbered=true)` |
| `+++OutputFormat` | Control response format | `+++OutputFormat(format=json)` |
| `+++Tone` | Adjust writing style | `+++Tone(style=technical)` |
| `+++Version` | Specify standard version | `+++Version(standard=1.0.0)` |

## Implementation Guide

Prompt Decorators can be implemented at various levels:

### For LLM Providers

```python
# Example implementation in a provider API
def process_decorators(user_prompt):
    # Extract decorators
    decorators = extract_decorators(user_prompt)
    cleaned_prompt = remove_decorators(user_prompt)
    
    # Generate system prompt from decorators
    system_prompt = generate_system_prompt(decorators)
    
    # Send to model
    response = query_model(system_prompt, cleaned_prompt)
    return response
```

### For Application Developers

```javascript
// Client-side decorator implementation example
const promptWithDecorators = decoratorManager
  .add("Reasoning", { depth: "comprehensive" })
  .add("OutputFormat", { format: "markdown" })
  .applyToPrompt(userInput);

// Send to API
const response = await api.sendPrompt(promptWithDecorators);
```

### For End Users

Add the following system prompt to instruct the model about decorators:

```
A "Prompt Decorator" is an instruction starting with +++ that modifies how you generate responses.
When you see +++Reasoning, begin your response with detailed reasoning before conclusions.
When you see +++StepByStep, structure your response as numbered steps.
[etc...]
```
## Getting Started

- [Read the full specification](docs/prompt-decorators-specification-v1.0.md)
- [Test suite](tests/)
- [Decorator registry](registry/)

## Acknowledgements

- Inspired by [Mostapha Kalami Heris](https://kalami.medium.com) article on [Prompt Decorators](https://kalami.medium.com/prompt-decorators-a-simple-way-to-improve-ai-responses-c3f3c2579a8c)
- Based on own research on prompt engineering and collection of curated prompt libraries
- Thanks to all contributors and community members who have provided feedback

## Current Status

This specification is currently a formal proposal. We invite implementations, feedback, and contributions from the AI community to help refine and improve the standard.
Any indudtry or domain specific decorators should be added to the [registry](registry/) for easy discovery and reuse.


## Contributing

We welcome contributions to the Prompt Decorators standard! Please see our [contribution guidelines](CONTRIBUTING.md) for details on how to participate.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

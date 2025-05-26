# Prompt Decorators

<div align="center">

<img src="https://synaptiai.github.io/prompt-decorators/assets/logo.png" alt="Prompt Decorators Logo" width="400"/>

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Documentation](https://img.shields.io/badge/docs-MkDocs-blue)](https://synaptiai.github.io/prompt-decorators/)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-black)](https://github.com/astral-sh/ruff)

[![Code Quality and Testing](https://github.com/synaptiai/prompt-decorators/workflows/Code%20Quality%20and%20Testing/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Code+Quality+and+Testing%22)
[![Documentation](https://github.com/synaptiai/prompt-decorators/workflows/Documentation/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Documentation%22)
[![Publish to PyPI](https://github.com/synaptiai/prompt-decorators/workflows/Publish%20to%20PyPI/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Publish+to+PyPI%22)

**Prompt Decorators is a comprehensive framework that standardizes how prompts for Large Language Models (LLMs) are enhanced, structured, and transformed. This repository contains both the official Prompt Decorators Specification and its complete Python reference implementation.**

[Documentation](https://synaptiai.github.io/prompt-decorators/) •
[Prompt Decorators Specification](https://synaptiai.github.io/prompt-decorators/prompt-decorators-specification-v1.0/)

</div>

## 📋 Table of Contents

- [Overview](#overview)
  - [What Are Prompt Decorators?](#what-are-prompt-decorators)
  - [Key Components](#key-components)
  - [Background & Motivation](#background--motivation)
  - [Challenges in Prompt Engineering](#challenges-in-prompt-engineering)
  - [Benefits of Prompt Decorators](#benefits-of-prompt-decorators)
  - [Key Features](#key-features)
- [Implementation Status](#implementation-status)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Basic Usage](#basic-usage)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## 🔍 Overview

### What Are Prompt Decorators?

Prompt Decorators introduces a standardized annotation system inspired by software design patterns that allows users to modify LLM behavior through simple, composable "decorators." By prefixing prompts with annotations like `+++Reasoning`, `+++StepByStep`, or `+++OutputFormat`, users can consistently control how AI models process and respond to their requests across different platforms and implementations.

This project addresses the growing complexity of AI interactions by providing:

1. **The Specification**: A formal standard that defines decorator syntax, behavior, and extension mechanisms
2. **The Python Implementation**: A production-ready reference implementation with comprehensive tooling
3. **MCP Integration**: A Model Context Protocol server that enables prompt decorator functionality in tools like Claude Desktop

### Key Components

- **📝 Specification**: The formal [Prompt Decorators Specification (v1.0)](https://synaptiai.github.io/prompt-decorators/prompt-decorators-specification-v1.0/) defining the standard
- **🛠️ Core Framework**: A Python implementation with registry-based decorator management
- **🧩 140+ Decorators**: A comprehensive library of pre-built decorators covering reasoning, formatting, and more
- **🔌 MCP Server**: Integration with the Model Context Protocol for use with desktop AI applications
- **📚 Extensive Documentation**: API references, guides, and examples for both users and developers

### Background & Motivation

As Large Language Models become increasingly integrated into workflows across industries, the need for standardized, consistent ways to interact with these systems has become apparent. Current prompt engineering approaches are largely ad-hoc, requiring extensive documentation, reinvention, and significant cognitive overhead when switching between systems or use cases.

Prompt Decorators address this challenge by providing a systematic approach to modifying AI behavior through simple, composable annotations. Inspired by the Decorator pattern in programming and Python's function decorators, they serve as a layer of abstraction that decouples the core prompt from instructions about how to process and present the response.

### Challenges in Prompt Engineering

Current prompt engineering suffers from several limitations:

- **Inconsistency**: Instructions vary widely between users, platforms, and models
- **Verbosity**: Detailed instructions consume token context that could be used for content
- **Cognitive Overhead**: Users must remember or document specific prompting techniques
- **Lack of Composability**: Combining different instruction paradigms is cumbersome
- **Undocumented Behavior**: Expected model behavior is often implicit rather than explicit

### Benefits of Prompt Decorators

Prompt Decorators solves key challenges in prompt engineering:

- **Inconsistency**: Provides a standard syntax and behavior across different LLM platforms
- **Verbosity**: Replaces lengthy instructions with concise annotations
- **Cognitive Overhead**: Simplifies prompt crafting with reusable patterns
- **Lack of Composability**: Enables clean combination of multiple instruction paradigms
- **Undocumented Behavior**: Explicitly defines expected model responses

Whether you're crafting prompts for specific reasoning patterns, structuring outputs in particular formats, or ensuring consistent responses across different models, Prompt Decorators provides a systematic approach that makes prompt engineering more modular, reusable, and maintainable.

The Prompt Decorators framework addresses these challenges through:

- **Standardization**: Common vocabulary and syntax across platforms and models
- **Efficiency**: Concise annotations that reduce token consumption
- **Reusability**: Consistent behaviors that can be reused across different contexts
- **Composability**: Ability to combine decorators for complex interaction patterns
- **Explicit Behavior**: Clear documentation of expected model responses
- **Reduced Cognitive Load**: Simple annotations instead of lengthy instructions

### Key Features

- **📚 Registry-based decorator management**: Centralized registry of decorators with metadata
- **✅ Parameter validation and type checking**: Robust validation of decorator parameters
- **🔢 Decorator versioning**: Support for semantic versioning of decorators
- **🔄 Compatibility checking**: Verification of decorator compatibility
- **📝 Documentation generation**: Automatic generation of documentation for decorators
- **🧩 Dynamic loading**: Runtime decorator loading from definition files
- **🔍 Runtime decorator discovery**: Dynamic discovery and registration of decorators

## 💡 Implementation Status

The Prompt Decorators project is currently in active development.

You can see the how prompt decorators work by testing out the [demo](/demo/README.md) or running the [MCP server implementation](https://synaptiai.github.io/prompt-decorators/integrations/mcp/) together with your Claude Desktop.

Or you can use the [.cursorrules](.cursorrules) in this repository as system instructions in Cursor (or chatGPT/Claude) to instruct it. Try it out and share your experiences!

### Implemented Functionality

- **✅ Core Decorator Registry**: Load decorators from standardized JSON definitions
- **✅ Decorator Application**: Apply decorators to prompts with parameter validation
- **✅ Sophisticated Transformation**: Convert decorator parameters into prompt adjustments
- **✅ Multiple Input Formats**: Support for Python functions, strings, and JSON
- **✅ Parameter validation and type checking**: Robust validation of decorator parameters
- **✅ Standard Decorators**: Implementation of the standard decorators defined in the specification
- **✅ Extension Framework**: Support for domain-specific decorator extensions
- **✅ Documentation Generation**: Automated documentation generation from decorator definitions

For a detailed breakdown of implementation status, see our [Implementation Status](https://synaptiai.github.io/prompt-decorators/implementation-status/) document.

### Roadmap

The roadmap for this project is outlined in the [ROADMAP](https://synaptiai.github.io/prompt-decorators/roadmap/) file.

## 🚀 Getting Started

### Installation

You can install the package from PyPI [https://pypi.org/project/prompt-decorators/](https://pypi.org/project/prompt-decorators/):

```bash
pip install prompt-decorators
```

For additional functionality, you can install optional dependencies:

```bash
# For Model Context Protocol (MCP) integration
pip install "prompt-decorators[mcp]"

# For development and testing
pip install "prompt-decorators[dev,test]"

# For documentation
pip install "prompt-decorators[docs]"

# For all optional dependencies
pip install "prompt-decorators[all]"
```

### Basic Usage

```python
import prompt_decorators as pd

# Load available decorators
pd.load_decorator_definitions()

# Create a decorator instance
reasoning = pd.create_decorator_instance("Reasoning", depth="comprehensive")

# Apply the decorator to a prompt
prompt = "Explain the concept of prompt engineering."
decorated_prompt = reasoning.apply(prompt)

print(decorated_prompt)
```

### Verifying Installation

After installation, verify that everything is working correctly:

```bash
# Verify the package is installed
python -c "import prompt_decorators; print(prompt_decorators.__version__)"

# Verify registry loading
python -m prompt_decorators verify
```

If you see "Registry verification successful" with a count of loaded decorators, you're ready to go!

For more detailed examples and usage instructions, please refer to the [official documentation](https://synaptiai.github.io/prompt-decorators/).

## 📝 License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more information.

## 🤝 Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## 🤖 Acknowledgments

This project would not be possible without the contributions of the following individuals and organizations:

- **[Mostapha Kalami Heris](https://kalami.medium.com)**: For his article on [Prompt Decorators: A Simple Way to Improve AI Responses](https://kalami.medium.com/prompt-decorators-a-simple-way-to-improve-ai-responses-c3f3c2579a8c), which inspired this specification and repository
- **[Synaptiai](https://synapti.ai)**: The creators and maintainers of this framework and specification
- **[Contributors](https://github.com/synaptiai/prompt-decorators/graphs/contributors)**: All the wonderful people who have contributed to this project

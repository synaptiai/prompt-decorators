# Prompt Decorators

<div align="center">

<img src="docs/assets/logo.png" alt="Prompt Decorators Logo" width="400"/>

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Documentation](https://img.shields.io/badge/docs-MkDocs-blue)](https://synaptiai.github.io/prompt-decorators/)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-black)](https://github.com/astral-sh/ruff)

[![Code Quality and Testing](https://github.com/synaptiai/prompt-decorators/workflows/Code%20Quality%20and%20Testing/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Code+Quality+and+Testing%22)
[![Documentation](https://github.com/synaptiai/prompt-decorators/workflows/Documentation/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Documentation%22)
[![Publish to PyPI](https://github.com/synaptiai/prompt-decorators/workflows/Publish%20to%20PyPI/badge.svg)](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Publish+to+PyPI%22)

**A Python framework implementing the Prompt Decorators Specification for enhancing interactions with Large Language Models (LLMs) through standardized, composable prompt modifications.**

[Documentation](https://synaptiai.github.io/prompt-decorators/) •
[Prompt Decorators Specification](/docs/prompt-decorators-specification-v1.0.md)

</div>

## 📋 Table of Contents

- [Overview](#overview)
- [Background & Motivation](#background--motivation)
- [Implemented Functionality](#implemented-functionality)
- [Implementation Status](#implementation-status)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Basic Usage](#basic-usage)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## 🔍 Overview

Prompt Decorators is a powerful and flexible framework that enables systematic modification of prompts to achieve specific behaviors in LLM responses. Based on the [Prompt Decorators Specification](docs/prompt-decorators-specification-v1.0.md), it provides a structured way to define, combine, and apply decorators to prompts.

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

## 💡 Implemented Functionality

- **✅ Core Decorator Registry**: Load decorators from standardized JSON definitions
- **✅ Decorator Application**: Apply decorators to prompts with parameter validation
- **✅ Sophisticated Transformation**: Convert decorator parameters into prompt adjustments
- **✅ Multiple Input Formats**: Support for Python functions, strings, and JSON
- **✅ Parameter validation and type checking**: Robust validation of decorator parameters
- **✅ Standard Decorators**: Implementation of the standard decorators defined in the specification
- **✅ Extension Framework**: Support for domain-specific decorator extensions
- **✅ Documentation Generation**: Automated documentation generation from decorator definitions

## 📊 Implementation Status

The Prompt Decorators project is currently in active development.

For a detailed breakdown of implementation status, see our [Implementation Status](docs/implementation-status.md) document.

### 🚧 Roadmap

The roadmap for this project is outlined in the [ROADMAP](ROADMAP.md) file.

## 🚀 Getting Started

### Installation

You can install the package from PyPI:

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

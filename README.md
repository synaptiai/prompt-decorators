# Prompt Decorators

<div align="center">

<img src="docs/assets/logo.png" alt="Prompt Decorators Logo" width="400"/>

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org/)
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
- [Implemented Functionality](#implemented-functionality)
- [Architecture](#architecture)
- [Example Usage](#example-usage)
- [Getting Started](#getting-started)
- [Prompt Decorators Specification](#prompt-decorators-specification)
- [Domain-Specific Extensions](#domain-specific-extensions)
- [Development](#development)
- [License](#license)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [Acknowledgments](#acknowledgments)
- [Code Quality](#code-quality)

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

## 🚀 Implemented Functionality

The framework currently implements:

1. **Core Decorators**:
   - `Reasoning`: Enhances reasoning capabilities in responses
   - `StepByStep`: Breaks down reasoning into sequential steps
   - `TreeOfThought`: Explores multiple reasoning paths
   - `FirstPrinciples`: Applies first principles reasoning
   - `OutputFormat`: Controls the format of the output (markdown, JSON, etc.)
   - `Tone`: Adjusts the tone of the response
   - And many more...

2. **Registry System**:
   - JSON-based decorator definitions
   - Metadata for documentation and compatibility
   - Versioning and dependency management

3. **Documentation System**:
   - Comprehensive markdown documentation
   - Integration with MkDocs for documentation site
   - API reference documentation

4. **Dynamic Implementation**:
   - Runtime loading of decorators from definitions
   - No code generation required
   - Flexible extension mechanism

5. **Integrations**:
   - **Model Context Protocol (MCP)**: Integration with the [Model Context Protocol](https://github.com/microsoft/model-context-protocol) for standardized LLM interactions
   - **Claude Desktop**: Specialized integration for Anthropic's Claude Desktop application
   - MCP tools for applying decorators and retrieving decorator information

## 🏗️ Architecture

The framework is organized into several key components:

1. **Core** (`prompt_decorators/core/`):
   - `base.py`: Contains `DecoratorBase` abstract base class that defines the decorator interface
   - `dynamic_decorator.py`: Implements the dynamic decorator functionality
   - `registry.py`: Manages the decorator registry
   - `parser.py`: Parses decorator annotations in text
   - `validation.py`: Validates decorator parameters
   - `model_specific.py`: Adapts decorators for specific LLM models
   - `request.py`: Handles API requests with decorators

2. **Schemas** (`prompt_decorators/schemas/`):
   - `decorator_schema.py`: Defines schemas for decorator definitions
   - JSON schemas for validation

3. **Utils** (`prompt_decorators/utils/`):
   - `discovery.py`: Runtime decorator discovery and registration
   - `compatibility.py`: Checks compatibility between decorators
   - `cache.py`: Caching utilities for decorator responses
   - `doc_gen.py`: Documentation generation utilities
   - `string_utils.py`: String manipulation utilities
   - `json_loader.py`: Loads decorator definitions from JSON files

4. **Integrations** (`prompt_decorators/integrations/`):
   - `mcp/`: Integration with the Model Context Protocol
   - `mcp/server.py`: MCP server implementation
   - `mcp/claude_desktop.py`: Integration with Claude Desktop

5. **Scripts** (`scripts/`):
   - Documentation scripts for generating, verifying, and enhancing documentation
   - Validation scripts for checking docstrings and code quality
   - Development tools for common tasks

The system uses a dynamic implementation approach where decorators are defined in registry files (typically JSON) and loaded at runtime, rather than generating code. This provides more flexibility and simplifies the extension process.

## 📝 License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more information.

## 🤝 Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

### Development Environment

To ensure code quality, the project uses strict type checking in CI. While the `demo/` directory is excluded from pre-commit hooks to reduce development friction, it's still validated in CI with stricter settings.

Before pushing changes:
1. Run `scripts/check_demo_types.py` to validate the demo directory with the same strict type checking used in CI
2. Alternatively, install the optional pre-push hook: `cp scripts/git-hooks/pre-push .git/hooks/pre-push && chmod +x .git/hooks/pre-push`

## 🚧 Roadmap

The roadmap for this project is outlined in the [ROADMAP](ROADMAP.md) file.

## 🤖 Acknowledgments

This project would not be possible without the contributions of the following individuals and organizations:

- **[Synaptiai](https://synaptiai.com)**: The original creators and maintainers of the framework
- **[Contributors](https://github.com/synaptiai/prompt-decorators/graphs/contributors)**: All the wonderful people who have contributed to this project

## 🔢 Code Quality

This project uses a variety of tools and practices to ensure high code quality:

- **[Code Style](https://github.com/astral-sh/ruff)**: Enforces consistent coding style
- **[Code Quality and Testing](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Code+Quality+and+Testing%22)**: Continuous integration and testing
- **[Documentation Verification](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Documentation+Verification%22)**: Ensures documentation accuracy
- **[Documentation](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Documentation%22)**: Comprehensive documentation site
- **[Publish to PyPI](https://github.com/synaptiai/prompt-decorators/actions?query=workflow%3A%22Publish+to+PyPI%22)**: Automated deployment to PyPI

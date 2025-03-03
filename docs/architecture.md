# Project Architecture

This document outlines the architecture of the Prompt Decorators framework, providing an overview of the code structure, key components, and design patterns.

## Directory Structure

The `prompt_decorators` package has the following main directories:

- **core/**: Contains the core functionality of the framework
  - `base.py`: Base classes for all decorators
  - `model_specific.py`: Model-specific decorator handling
  - `request.py`: API request handling
- **decorators/**: Contains the decorator implementations
  - **generated/**: Contains auto-generated decorator implementations based on registry definitions
- **generator/**: Contains code generation utilities
  - `code_gen.py`: Generates Python code from registry definitions
  - `test_gen.py`: Generates test files for decorators
  - `registry.py`: Scans and parses the registry files
  - `cli.py`: Command-line interface for the generator
- **utils/**: Contains utility functions
  - `cache.py`: Caching utilities
  - `compatibility.py`: Decorator compatibility checking
  - `discovery.py`: Runtime decorator discovery
  - `doc_gen.py`: Documentation generation
  - `json_loader.py`: JSON loading utilities
  - `model_detection.py`: LLM model detection and capability analysis
  - `plugins.py`: Plugin system for extensions
  - `telemetry.py`: Usage telemetry (optional)

## Key Components

### Core Module (10.3% of codebase)

The core module provides the foundation for all decorators:

1. **BaseDecorator**: The abstract base class for all decorators, defining:
   - Standard initialization
   - Parameter validation
   - Serialization/deserialization
   - The abstract `apply` method

2. **ModelSpecificDecorator**: Extends BaseDecorator with model-specific capabilities:
   - Model compatibility checking
   - Model-aware parameter validation
   - Model-specific application logic

3. **DecoratedRequest**: Handles API requests with decorators:
   - Decorator validation and compatibility checking
   - Decorator application to prompts
   - API parameter management

### Decorators Module (46.7% of codebase)

The decorators module contains:

1. **Generated Decorators**: Auto-generated from registry JSON files (44.2% of codebase)
   - Each decorator follows a consistent structure derived from the registry
   - Parameter validation based on registry specifications
   - Standardized application logic

2. **Custom Decorators**: Manually created decorators (2.5% of codebase)
   - More complex application logic
   - Specialized validation
   - Model-specific behaviors

### Generator Module (14.2% of codebase)

The generator module facilitates code generation:

1. **Registry Scanner**: Scans JSON files in the registry directory
   - Parses decorator definitions
   - Validates against schema
   - Groups by category

2. **Code Generator**: Generates Python code for decorators
   - Creates class definitions
   - Implements parameter validation
   - Generates property getters
   - Creates the apply method

3. **Test Generator**: Generates unit tests for decorators
   - Creates parameter validation tests
   - Implements apply method tests
   - Generates serialization tests

### Utils Module (24.7% of codebase)

The utils module provides supporting functionality:

1. **Registry Management**: Tools for working with the decorator registry
   - JSON loading and validation
   - Schema enforcement
   - Documentation generation

2. **Runtime Support**: Utilities for runtime operations
   - Decorator discovery
   - Caching
   - Compatibility checking
   - Model detection

3. **Plugin System**: Extensibility through plugins
   - Plugin loading and validation
   - Hook registration and execution
   - Custom decorator integration

## Architectural Patterns

### Registry-Driven Development

The framework employs a registry-driven approach:

1. **JSON Definitions**: Decorators are defined in JSON files in the registry
2. **Code Generation**: Python classes are generated from these definitions
3. **Test Generation**: Tests are generated from the same definitions
4. **Documentation Generation**: Documentation is generated from the registry and code

This approach ensures consistency and reduces duplication.

### Clean Layering

The codebase follows a clean layering pattern:

1. **Core Layer**: Provides the foundation and abstractions
2. **Decorators Layer**: Implements specific decorator behaviors
3. **Utils Layer**: Provides supporting functionality
4. **Generator Layer**: Handles code generation

Dependencies flow in one direction: decorators → core and utils → core.

### Factory Pattern

The framework uses factory patterns for decorator creation:

1. **Decorator Factories**: Create decorators from registry data
2. **Request Factories**: Create API requests with appropriate decorators
3. **Test Factories**: Create test instances with appropriate fixtures

### Strategy Pattern

The decorator application logic follows the strategy pattern:

1. **Common Interface**: All decorators implement the `apply` method
2. **Swappable Strategies**: Different decorators can be applied in different orders
3. **Compositional Approach**: Decorators can be composed in chains

## Code Metrics

### Lines of Code by Module

- **Total**: 13,384 lines
- **utils**: 3,304 lines (24.7%)
- **decorators/generated**: 5,913 lines (44.2%)
- **core**: 1,373 lines (10.3%)
- **generator**: 1,897 lines (14.2%)
- **decorators (non-generated)**: 329 lines (2.5%)
- **__init__ files**: 568 lines (4.2%)

### Key Files by Size

1. **utils/doc_gen.py**: 905 lines
2. **generator/test_gen.py**: 800 lines
3. **generator/code_gen.py**: 657 lines
4. **utils/plugins.py**: 625 lines
5. **core/base.py**: 620 lines

## Design Principles

The framework follows several key design principles:

1. **Modularity**: Each decorator focuses on a specific prompt engineering technique
2. **Extensibility**: The plugin system and registry-driven approach allow for easy extension
3. **Composability**: Decorators can be composed in different combinations
4. **Consistency**: Generated code follows consistent patterns
5. **Testability**: Generated tests ensure quality and functionality
6. **Documentation**: Generated documentation ensures accuracy and completeness

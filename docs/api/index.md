# API Reference

## Table of Contents

- [Overview](#overview)
- [API Structure](#api-structure)
  - [Modules](#modules)
    - [Core Modules](modules/index.md#core-modules)
    - [Schema Modules](modules/index.md#schema-modules)
    - [Utility Modules](modules/index.md#utility-modules)
    - [Integration Modules](modules/index.md#integration-modules)
    - [Other Modules](modules/index.md#other-modules)
  - [Decorators](#decorators)
    - [Minimal](decorators/index.md#minimal)
    - [Reasoning Process Decorators](decorators/index.md#reasoning-process-decorators)
    - [Output Structure Decorators](decorators/index.md#output-structure-decorators)
    - [Tone](decorators/index.md#tone)
    - [Verification](decorators/index.md#verification)
- [Usage Example](#usage-example)

## Overview

This section contains the API reference for the Prompt Decorators package. It provides detailed documentation for all modules, classes, functions, and properties in the package.

## API Structure

The API is organized into the following sections:

### Modules {#modules}

- **[Modules](modules/index.md)**: Documentation for all Python modules in the package
  - [Core Modules](modules/index.md#core-modules): Core functionality of prompt decorators
  - [Schema Modules](modules/index.md#schema-modules): Data models and schemas
  - [Utility Modules](modules/index.md#utility-modules): Helper functions and utilities
  - [Integration Modules](modules/index.md#integration-modules): Integrations with other systems

### Decorators {#decorators}

- **[Decorators](decorators/index.md)**: Documentation for all available prompt decorators
  - [Minimal Decorators](decorators/index.md#minimal): Essential decorators for basic functionality
  - [Reasoning Process Decorators](decorators/index.md#reasoning-process-decorators): Decorators for controlling reasoning processes
  - [Output Structure Decorators](decorators/index.md#output-structure-decorators): Decorators for controlling output structure
  - [And more...](decorators/index.md)

## Usage Example

```python
from prompt_decorators import transform_prompt

# Transform a prompt using decorators
transformed_prompt = transform_prompt(
    "What are the environmental impacts of electric vehicles?",
    ["+++StepByStep(numbered=true)", "+++Reasoning(depth=comprehensive)"]
)
```

For more examples, see the [Quick Start](../quickstart.md) guide.

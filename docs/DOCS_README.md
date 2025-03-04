# Documentation Overview

This directory contains the documentation for the Prompt Decorators project.

## Key Documentation Files

- [Getting Started](./installation.md)
- [Creating Decorators](./tutorials/creating_custom_decorator.md)
- [Extension Development](./tutorials/extension_development.md)
- [Domain-Specific Extensions](./guides/domain_specific_extensions.md)
- [API Reference](./api/index.md)

## Building the Documentation

The documentation is built using MkDocs with the Material theme and several plugins.
To build the documentation locally, run:

```bash
pip install -r docs/requirements.txt
mkdocs build
```

To serve the documentation locally, run:

```bash
mkdocs serve
```

## Documentation Structure

- `docs/`: Main documentation directory
  - `api/`: API reference documentation
  - `guides/`: User guides
  - `tutorials/`: Step-by-step tutorials
  - `examples/`: Example code and usage
  - `project_summaries/`: Documentation of project efforts

# Documentation Workflow

This document explains the workflow for generating and maintaining documentation for the Prompt Decorators project.

## Overview

The documentation for Prompt Decorators consists of:

1. **API Reference**: Automatically generated from docstrings and type annotations in the code
2. **User Guides**: Manually written Markdown files
3. **Examples**: Code examples with explanations
4. **Tutorials**: Step-by-step guides for common tasks

We use [MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/) to build the documentation website.

## Documentation Generation Process

The documentation generation process involves two main steps:

1. **Generate API Reference**: Extract docstrings and type annotations from the code to create Markdown files
2. **Build Documentation Website**: Use MkDocs to build a static website from all Markdown files

### Step 1: Generate API Reference

To generate the API reference documentation, use the `generate_docs.py` script:

```bash
# Generate Markdown documentation
python docs/generate_docs.py --format markdown

# Clean the output directory before generating documentation
python docs/generate_docs.py --format markdown --clean

# Generate both Markdown and HTML documentation
python docs/generate_docs.py --format both
```

This script:
- Extracts docstrings and type annotations from the code
- Loads decorator definitions from the registry
- Merges code and registry documentation
- Generates Markdown files in the `docs/api` directory

### Step 2: Build Documentation Website

To build the documentation website, use MkDocs:

```bash
# Serve documentation locally (with live reload)
mkdocs serve

# Build documentation
mkdocs build

# Deploy documentation to GitHub Pages
mkdocs gh-deploy
```

## Documentation Structure

The documentation is organized as follows:

- `docs/`: Root directory for documentation
  - `api/`: API reference documentation (auto-generated)
  - `examples/`: Code examples with explanations
  - `guide/`: User guides
  - `tutorials/`: Step-by-step tutorials
  - `project_summaries/`: Project overview and summaries
  - `guides/`: Domain-specific guides

## Maintaining Documentation

### Updating API Reference

When you make changes to the code:

1. Update docstrings and type annotations in the code
2. Run `python docs/generate_docs.py --format markdown --clean` to regenerate the API reference
3. Run `mkdocs serve` to preview the changes
4. Commit the changes to the repository

### Adding New Documentation

To add new documentation:

1. Create a new Markdown file in the appropriate directory
2. Add the file to the navigation in `mkdocs.yml`
3. Run `mkdocs serve` to preview the changes
4. Commit the changes to the repository

## Documentation Standards

Please follow these standards when writing documentation:

1. **Docstrings**: Use Google-style docstrings (see [DOCSTRING_STANDARDS.md](DOCSTRING_STANDARDS.md))
2. **Markdown**: Use consistent formatting and structure
3. **Examples**: Include runnable examples that demonstrate key features
4. **Links**: Ensure all links are valid and point to the correct location

## Troubleshooting

### Broken Links

If you encounter broken links in the documentation:

1. Run `mkdocs build` to see warnings about broken links
2. Fix the broken links in the source files
3. Regenerate the API reference if necessary
4. Run `mkdocs serve` to verify the fixes

### Missing Documentation

If you notice missing documentation:

1. Check if the code has proper docstrings and type annotations
2. Ensure the module or class is included in the documentation generation process
3. Update the docstrings and regenerate the API reference
4. Update the navigation in `mkdocs.yml` if necessary

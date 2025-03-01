# Prompt Decorators Examples

This directory contains examples of how to use the Prompt Decorators package.

## Available Examples

### 1. `register_all_decorators.py`

**Purpose**: Registers all decorators from the generated directory with the `DecoratorRegistry`.

**Features**:
- Clears the existing registry
- Discovers and registers all decorators from the generated directory
- Prints a summary of registered decorators

**Usage**:
```bash
python examples/register_all_decorators.py
```

**Example Output**:
```
================================================================================
========================== Registering All Decorators ==========================
================================================================================

Registry cleared. Current decorators: 0

Registering decorators from: /path/to/prompt-decorators/prompt_decorators/decorators/generated/decorators

  - Registered: Concise
  - Registered: RedTeam
  - Registered: TableFormat
  ...

Registered 70 decorators:

Total registered decorators: 70

Decorator categories (1):
  - Uncategorized: 70 decorators

================================================================================
============================ Registration Completed ============================
================================================================================
```

### 2. `use_registered_decorators.py`

**Purpose**: Demonstrates how to use registered decorators to modify prompts.

**Features**:
- Registers decorators directly within the script
- Lists available decorators and their versions
- Shows how to create and use a specific decorator (Concise)
- Demonstrates combining multiple decorators (ELI5 + Professional)
- Shows how to find decorators by category

**Usage**:
```bash
python examples/use_registered_decorators.py
```

**Example Output**:
```
================================================================================
============================= Available Decorators =============================
================================================================================

Total decorators available: 70
- Concise (Latest version: 1.0.0)
- RedTeam (Latest version: 1.0.0)
...

================================================================================
========================== Using a Specific Decorator ==========================
================================================================================

Created Concise decorator (v1.0.0)
Parameters: {...}

Original prompt:
'Explain the concept of quantum computing in detail...'

Decorated prompt:
'Instructions for Concise decorator: bulletPoints=False, level=2, 

Explain the concept of quantum computing in detail...'

================================================================================
========================= Combining Multiple Decorators =========================
================================================================================

Original prompt:
'Explain how neural networks work.'

With ELI5 decorator:
'Instructions for ELI5 decorator: strictness=False, 

Explain how neural networks work.'

With ELI5 + Professional decorators:
'Instructions for Professional decorator: industry=general, formality=ProfessionalFormalityEnum.STANDARD,

Instructions for ELI5 decorator: strictness=False, 

Explain how neural networks work.'
```

## Adding New Examples

To add a new example:

1. Create a new Python file in the `examples` directory
2. Import the necessary modules from the `prompt_decorators` package
3. Add a docstring explaining the purpose of the example
4. Add the example to this README.md file

Each example should be self-contained and demonstrate a specific feature or use case of the Prompt Decorators package. 
# Prompt Decorator Validator Tool

The validator tool provides a way to validate prompt decorator definitions against the official JSON schemas of the Prompt Decorators specification.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Validation Types](#validation-types)
- [Troubleshooting](#troubleshooting)

## Installation

The validator requires Python 3.6+ and the `jsonschema` package.

```bash
# Install the required dependency
pip install jsonschema
```

## Usage

The validator tool can be used to validate different types of artifacts:

```bash
# Basic usage
python validate_decorators.py [command] [file_or_directory_path] [options]
```

Available commands:

- `decorator`: Validate a decorator definition against the decorator schema
- `registry`: Validate a registry entry against the registry-entry schema
- `api`: Validate an API request against the api-request schema
- `package`: Validate an extension package against the extension-package schema
- `directory`: Validate all JSON files in a directory against a specific schema

## Examples

### Validating a Single Registry Entry

```bash
python validate_decorators.py registry registry/core/reasoning.json
```

### Validating All Decorators in a Directory

```bash
python validate_decorators.py directory registry/core --type registry
```

### Validating an API Request

```bash
python validate_decorators.py api examples/api-request.json
```

### Validating an Extension Package

```bash
python validate_decorators.py package extensions/core/package.json
```

### Validating Using a Custom Schemas Directory

```bash
python validate_decorators.py registry registry/core/reasoning.json --schemas-dir /path/to/schemas
```

## Validation Types

The validator supports four types of validation:

### 1. Decorator Validation

Validates a JSON file against the `decorator.schema.json` schema, which defines the structure of a single decorator instance.

Required fields:
- `name`: The name of the decorator
- `version`: The semantic version of the decorator implementation
- `parameters`: (Optional) Parameters for the decorator

### 2. Registry Entry Validation

Validates a JSON file against the `registry-entry.schema.json` schema, which defines how decorators are registered in the central registry.

Required fields:
- `decoratorName`: The name of the decorator
- `version`: The semantic version of the decorator
- `description`: Detailed description of what the decorator does
- `parameters`: List of parameters that the decorator accepts

### 3. API Request Validation

Validates a JSON file against the `api-request.schema.json` schema, which defines the structure of API requests when using decorators.

Required fields:
- `prompt`: The main prompt text to be processed
- `decorators`: (Optional) List of decorators to apply to the prompt

### 4. Extension Package Validation

Validates a JSON file against the `extension-package.schema.json` schema, which defines how decorator extensions are packaged.

Required fields:
- `name`: Name of the extension package
- `version`: Semantic version of the extension package
- `decorators`: List of decorators included in the package

## Troubleshooting

### Common Validation Errors

1. **Schema Not Found**

   ```
   Error: Schema decorator.schema.json not found
   ```

   This error occurs when the validator cannot find the schema files. Make sure the schemas directory exists and contains the required schema files.

2. **Missing Required Fields**

   ```
   ✗ Registry entry validation error in registry/core/reasoning.json:
     - 'description' is a required property
   ```

   This error indicates that a required field is missing. Add the missing field to your JSON file.

3. **Invalid Field Type**

   ```
   ✗ Decorator validation error in decorators/custom.json:
     - 'number' is not of type 'string'
     - Path: version
   ```

   This error indicates that a field has an incorrect type. Check the field and ensure it has the correct type.

### Tips

- The validator provides detailed error messages that include the path to the error in the JSON file.
- When validating a directory, all JSON files in that directory (and subdirectories) will be validated.
- The validator uses the `jsonschema` package to perform validation, which follows the JSON Schema Draft 7 specification.

## Contributing

Contributions to the validator tool are welcome! Please ensure your changes maintain backward compatibility and add appropriate tests.

See the [contribution guidelines](../CONTRIBUTING.md) for more information.

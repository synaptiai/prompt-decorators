# Validator Tool

The Prompt Decorators Validator Tool is a utility for validating decorator definitions, ensuring they conform to the framework's specifications, and helping detect issues before they affect your applications.

## Overview

The validator tool performs several key functions:

1. **Schema Validation**: Ensures decorator definitions match the expected schema
2. **Parameter Validation**: Verifies parameter types, names, and defaults
3. **Transform Function Analysis**: Checks for syntax errors and potential issues
4. **Compatibility Checking**: Identifies potential conflicts between decorators
5. **Performance Analysis**: Evaluates transform functions for efficiency concerns

## Installation

The validator tool is included with the prompt-decorators package:

```bash
pip install prompt-decorators
```

For the command-line interface, install with the CLI extras:

```bash
pip install "prompt-decorators[cli]"
```

## Using the Validator CLI

The validator can be used from the command line:

```bash
# Validate a single decorator JSON file
prompt-decorators validate my_decorator.json

# Validate all decorators in a directory
prompt-decorators validate --directory path/to/decorators

# Validate a decorator defined in Python code
prompt-decorators validate --module my_package.decorators

# Generate a report
prompt-decorators validate --report report.html path/to/decorators
```

### Available Commands

- `validate`: Validate decorator definitions
- `check-conflicts`: Check for conflicts between decorators
- `analyze`: Analyze transform functions for performance issues
- `verify`: Verify that decorators work with various LLM providers

### Options

- `--directory`, `-d`: Directory containing decorator definitions
- `--recursive`, `-r`: Recursively search directories
- `--module`, `-m`: Python module containing decorator definitions
- `--format`, `-f`: Output format (text, json, html)
- `--report`: Generate a detailed report file
- `--verbose`, `-v`: Show detailed validation information
- `--fix`: Attempt to fix issues automatically

## Using the Validator in Code

You can also use the validator programmatically in your Python code:

```python
from prompt_decorators.tools.validator import (
    validate_decorator_definition,
    validate_transform_function,
    check_decorator_conflicts
)

# Validate a decorator definition
from prompt_decorators import DecoratorDefinition

my_decorator = DecoratorDefinition(
    name="MyDecorator",
    description="A sample decorator",
    category="Custom",
    parameters=[
        {
            "name": "param1",
            "type": "string",
            "description": "A parameter",
            "default": "default value"
        }
    ],
    transform_function="return 'Modified: ' + text;"
)

# Validate against schema
validation_result = validate_decorator_definition(my_decorator)
if validation_result.is_valid:
    print("Decorator is valid!")
else:
    print(f"Validation errors: {validation_result.errors}")

# Validate transform function specifically
transform_result = validate_transform_function(my_decorator.transform_function)
if transform_result.is_valid:
    print("Transform function is valid!")
else:
    print(f"Transform function errors: {transform_result.errors}")

# Check for conflicts with existing decorators
conflicts = check_decorator_conflicts(my_decorator)
if conflicts:
    print(f"Potential conflicts with: {', '.join(conflicts)}")
```

## Validation Checks

The validator performs these checks:

### Schema Validation
- Ensures required fields are present (name, description, etc.)
- Validates structure conforms to the JSON schema
- Checks field types and formats

### Parameter Validation
- Verifies parameter names are unique
- Ensures enum parameters have valid options
- Checks default values match parameter types
- Validates parameter descriptions

### Transform Function Analysis
- Checks JavaScript syntax
- Verifies all parameters are used correctly
- Ensures function returns a string value
- Warns about potential security issues

### Compatibility Analysis
- Identifies conflicting parameter names
- Detects overlapping functionality
- Warns about parameters with similar names but different types

## Creating a Custom Validator

You can extend the validator for your specific needs:

```python
from prompt_decorators.tools.validator import DecoratorValidator, ValidationRule

# Create a custom validation rule
class CustomParameterRule(ValidationRule):
    """Rule that requires parameters to follow a naming convention."""

    def validate(self, decorator_def):
        """Check that all parameters follow snake_case convention."""
        issues = []

        for param in decorator_def.parameters:
            name = param.get("name", "")
            if not name.islower() or " " in name:
                issues.append(f"Parameter '{name}' should use snake_case")

        return issues

# Create a custom validator with your rule
class CustomValidator(DecoratorValidator):
    def __init__(self):
        super().__init__()
        self.add_rule(CustomParameterRule())

# Use your custom validator
validator = CustomValidator()
result = validator.validate(my_decorator)
```

## Continuous Integration

The validator tool can be integrated into your CI/CD pipeline:

```yaml
# GitHub Actions example
name: Validate Decorators

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install prompt-decorators[cli]
    - name: Validate decorators
      run: |
        prompt-decorators validate --directory ./decorators --report validation-report.html
    - name: Upload validation report
      uses: actions/upload-artifact@v2
      with:
        name: validation-report
        path: validation-report.html
```

## Common Validation Issues and Solutions

### Issue: Missing Required Fields

```
Error: Missing required field 'description' in decorator 'MyDecorator'
```

**Solution**: Add the missing field to your decorator definition.

### Issue: Invalid Parameter Type

```
Error: Parameter 'count' has invalid type 'integer'. Valid types are: string, number, boolean, enum
```

**Solution**: Change the parameter type to one of the supported types. Use `"type": "number"` instead of `"type": "integer"`.

### Issue: Transform Function Syntax Error

```
Error: Syntax error in transform function: Unexpected token 'return'
```

**Solution**: Fix the JavaScript syntax in your transform function. Make sure you're using valid JavaScript.

### Issue: Missing Parameter in Transform Function

```
Warning: Parameter 'format' is defined but not used in the transform function
```

**Solution**: Either use the parameter in your transform function or remove it from the parameter definitions.

### Issue: Potential Security Issue

```
Warning: Transform function uses 'eval', which can be a security risk
```

**Solution**: Avoid using `eval` or other unsafe JavaScript constructs in your transform functions.

## Performance Optimization

The validator can help identify performance issues in your decorators:

```bash
prompt-decorators analyze --performance my_decorator.json
```

This will analyze your transform functions for performance issues such as:

- Inefficient string concatenations
- Complex loops or recursion
- Excessive memory usage
- Potential performance bottlenecks

## Best Practices

1. **Validate Early and Often**: Run validation during development, not just before release
2. **Automate Validation**: Include validation in your CI/CD pipeline
3. **Fix All Errors**: Resolve all validation errors before using decorators in production
4. **Review Warnings**: Warnings may indicate future problems
5. **Use Reports**: Generate and review comprehensive validation reports

## Related Tools

- **Schema Generator**: Generate JSON schema files for your decorators
- **Documentation Generator**: Create documentation from decorator definitions
- **Test Generator**: Generate test cases for your decorators

## Next Steps

- Learn how to [create your own decorators](creating_decorators.md)
- Explore [custom decorators in the tutorials](tutorials/creating_custom_decorator.md)
- Check out the [decorator specification](prompt-decorators-specification-v1.0.md)

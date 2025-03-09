# Development Guide

This guide provides comprehensive information for developers working on the Prompt Decorators project. It covers best practices, workflows, and coding standards to ensure consistent, high-quality contributions.

## Development Philosophy

The Prompt Decorators project follows these core principles:

1. **Simplicity**: Keep the API and implementation as simple as possible
2. **Extensibility**: Design for future extensions and customizations
3. **Quality**: Maintain high-quality code through testing and review
4. **Documentation**: Provide thorough documentation for all components
5. **User Focus**: Prioritize developer experience and ease of use

## Development Workflow

### Feature Development Lifecycle

1. **Planning**:
   - Create an issue describing the feature
   - Discuss design and implementation approaches
   - Define acceptance criteria

2. **Implementation**:
   - Create a new branch (`feature/<feature-name>`)
   - Implement the feature with tests
   - Update documentation

3. **Review**:
   - Submit a pull request
   - Address feedback
   - Update implementation as needed

4. **Merge**:
   - Ensure all checks pass
   - Merge into main branch
   - Delete feature branch

### Bug Fix Workflow

1. **Reporting**:
   - Create an issue with steps to reproduce
   - Include expected vs. actual behavior
   - Add relevant logs or screenshots

2. **Analysis**:
   - Verify the bug
   - Identify the root cause
   - Determine the best approach to fix

3. **Implementation**:
   - Create a new branch (`bugfix/<bug-description>`)
   - Fix the bug and add tests to prevent regression
   - Update documentation if needed

4. **Review and Merge**:
   - Submit a pull request
   - Ensure all checks pass
   - Merge after approval

### Working with Issues

- Use descriptive titles and detailed descriptions
- Apply appropriate labels (bug, enhancement, documentation, etc.)
- Link related issues and pull requests
- Use task lists for tracking progress

### Pull Request Guidelines

- Reference the related issue(s) in the PR description
- Provide a clear summary of changes
- Include screenshots or examples for UI changes
- Add reviewers who are familiar with the affected code
- Respond to feedback promptly

## Code Organization

### Package Structure

```
prompt_decorators/
├── core/                   # Core decorator functionality
│   ├── __init__.py
│   ├── base.py             # Base decorator classes
│   ├── dynamic_decorator.py # Dynamic decorator implementation
│   └── registry.py         # Decorator registry
├── schemas/                # JSON schemas
│   ├── __init__.py
│   ├── decorator_schema.py # Decorator schema definitions
│   └── validation.py       # Schema validation utilities
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── string_utils.py     # String manipulation utilities
│   └── js_utils.py         # JavaScript-related utilities
├── integrations/           # Integration with other systems
│   ├── __init__.py
│   └── mcp/                # Model Context Protocol integration
├── __init__.py             # Public API
├── config.py               # Configuration
└── dynamic_decorators_module.py # Dynamic decorator implementation
```

### Key Modules and Components

#### Core Module

The `core` module contains the fundamental decorator classes and functionality:

- `base.py`: Contains the `DecoratorBase` abstract base class that all decorators inherit from
- `dynamic_decorator.py`: Contains the `DynamicDecorator` implementation
- `registry.py`: Manages the decorator registry

#### Schema Module

The `schemas` module handles schema definition and validation:

- `decorator_schema.py`: Contains the `DecoratorSchema` and `ParameterSchema` classes
- `validation.py`: Provides schema validation utilities

#### Utils Module

The `utils` module contains utility functions:

- `string_utils.py`: String manipulation, including decoration extraction
- `js_utils.py`: JavaScript-related utilities, including transform function evaluation

#### Integrations Module

The `integrations` module contains integrations with external systems:

- `mcp/`: Model Context Protocol integration

### Module Responsibilities

1. **Core**: Responsible for decorator definition, registration, and application
2. **Schemas**: Responsible for defining and validating decorator schemas
3. **Utils**: Provides utility functions for string manipulation and JavaScript execution
4. **Integrations**: Connects with external systems and tools

## Coding Standards

### Python Style Guidelines

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use `ruff` for formatting and linting
- Maximum line length of 100 characters
- Use 4 spaces for indentation (not tabs)
- Use snake_case for function and variable names
- Use CamelCase for class names
- Use UPPER_CASE for constants

### Type Annotations

- Use type annotations for all functions and methods
- Use `Optional[T]` for parameters that could be `None`
- Use `Union[T1, T2]` for parameters that could be multiple types
- Use `Any` only when absolutely necessary
- Use generics (`TypeVar`, `Generic`) for flexible typing

Example:

```python
from typing import Dict, List, Optional, TypeVar, Generic

T = TypeVar('T')

class Registry(Generic[T]):
    def get_item(self, name: str) -> Optional[T]:
        """Get an item from the registry by name."""
        # Implementation
```

### Documentation Guidelines

#### Docstrings

- Use Google-style docstrings for all classes, methods, and functions
- Include a brief description, parameters, return values, and exceptions
- Add examples for complex functions
- Document all public APIs

Example:

```python
def apply_dynamic_decorators(text: str) -> str:
    """
    Apply all dynamic decorators found in the text.

    This function extracts decorator annotations from the text, applies
    the corresponding transformations, and returns the modified text.

    Args:
        text: The input text containing decorator annotations.

    Returns:
        The transformed text with decorators applied and annotations removed.

    Raises:
        DecoratorNotFoundError: If a referenced decorator is not registered.

    Example:
        >>> apply_dynamic_decorators("+++StepByStep(numbered=true)\\nExplain quantum computing.")
        "Please break down your explanation into numbered steps.\\n\\nExplain quantum computing."
    """
    # Implementation
```

#### Code Comments

- Use comments to explain complex logic or non-obvious design decisions
- Avoid redundant comments that simply restate the code
- Use TODO, FIXME, or NOTE comments for future work

### Error Handling

- Use custom exception classes for specific error cases
- Provide clear error messages with context
- Handle exceptions at appropriate levels
- Use context managers for resource cleanup

Example:

```python
class DecoratorNotFoundError(Exception):
    """Raised when a referenced decorator is not found in the registry."""
    pass

def get_decorator(name: str) -> DecoratorBase:
    """Get a decorator from the registry by name."""
    if name not in _registry:
        raise DecoratorNotFoundError(f"Decorator '{name}' not found in registry")
    return _registry[name]
```

### Testing Guidelines

#### Test Organization

- Organize tests to mirror the package structure
- Use descriptive test names that explain what's being tested
- Group related tests in classes

#### Writing Tests

- Use pytest for unit and integration tests
- Write test cases for normal operation, edge cases, and error conditions
- Use fixtures for common setup
- Use parametrized tests for testing multiple inputs
- Aim for high test coverage

Example:

```python
import pytest
from prompt_decorators import apply_dynamic_decorators, register_decorator, DecoratorDefinition

@pytest.fixture
def example_decorator():
    """Fixture that provides a test decorator."""
    decorator_def = DecoratorDefinition(
        name="Example",
        description="Example decorator for testing",
        category="Test",
        parameters=[
            {
                "name": "prefix",
                "type": "string",
                "description": "Text to prepend",
                "default": "Prefix: "
            }
        ],
        transform_function="return prefix + text;"
    )
    register_decorator(decorator_def)
    return decorator_def

def test_apply_dynamic_decorators(example_decorator):
    """Test that decorators are correctly applied to text."""
    # Arrange
    prompt = """
    +++Example(prefix="Test: ")
    This is a test
    """

    # Act
    result = apply_dynamic_decorators(prompt)

    # Assert
    assert result.strip() == "Test: This is a test"
```

#### Mocking and Test Doubles

- Use `unittest.mock` or `pytest-mock` for mocking
- Create test doubles (mocks, stubs, fakes) for external dependencies
- Use mocking judiciously, preferring integration tests when possible

### Performance Considerations

- Minimize JavaScript evaluation overhead
- Cache expensive operations when appropriate
- Profile code to identify bottlenecks
- Be mindful of memory usage with large prompts

## Working with JavaScript

The Prompt Decorators framework uses JavaScript for transform functions. Here are some guidelines:

### Writing Transform Functions

- Keep transform functions simple and focused
- Avoid complex logic that is difficult to debug
- Use ES6 syntax (template literals, arrow functions, etc.)
- Test with multiple inputs, including edge cases

### JavaScript Best Practices

- Avoid using `eval` in transform functions
- Use template literals for string concatenation
- Handle potential errors (e.g., missing parameters)
- Keep functions pure when possible

Example:

```javascript
// Good
const result = `${prefix}${text}${suffix}`;

// Avoid
const result = prefix + text + suffix;
```

### Security Considerations

- Validate inputs before executing transform functions
- Sanitize user inputs to prevent injection attacks
- Implement timeout mechanisms for complex transforms
- Avoid exposing sensitive information in transform functions

## Working with Decorators

### Creating Decorators

- Choose clear, descriptive names
- Define sensible default parameter values
- Include comprehensive descriptions
- Use appropriate parameter types
- Test with various inputs and combinations

### Decorator Categories

- Assign decorators to appropriate categories
- Document category-specific behavior
- Consider compatibility between decorators in the same category

### Decorator Registry

- Register decorators at an appropriate time (import vs. runtime)
- Handle versioning and deprecation appropriately
- Document decorator dependencies

## Continuous Integration

### GitHub Actions

We use GitHub Actions for continuous integration:

- **Test Workflow**: Runs tests on multiple Python versions
- **Lint Workflow**: Checks code style and typing
- **Docs Workflow**: Builds and validates documentation
- **Release Workflow**: Publishes packages to PyPI

### Pre-commit Hooks

We use pre-commit hooks to ensure code quality:

- **ruff**: Checks formatting and linting
- **mypy**: Verifies type annotations
- **pytest**: Runs tests
- **doc8**: Validates documentation

## Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: Backwards-compatible feature additions
- **PATCH**: Backwards-compatible bug fixes

### Release Checklist

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md` with changes
3. Create a release commit and tag
4. Push to GitHub
5. Create a GitHub release
6. Build and publish to PyPI

### Changelog Maintenance

- Organize changes by type (Added, Changed, Deprecated, Removed, Fixed, Security)
- Include contributor acknowledgements
- Link to relevant issues and pull requests

## Advanced Development Topics

### Adding a New Integration

1. Create a new directory in `prompt_decorators/integrations/`
2. Implement the integration with clear interfaces
3. Add tests in `tests/integrations/`
4. Document the integration in `docs/integrations/`
5. Update `README.md` with the new integration

### Creating Custom Tools

1. Define the tool's purpose and interface
2. Implement the tool in an appropriate module
3. Add tests for the tool
4. Document the tool's usage
5. Integrate with the main package if appropriate

### Performance Optimization

1. Profile code to identify bottlenecks
2. Optimize critical paths
3. Add benchmarks to measure improvements
4. Document performance considerations

## Troubleshooting Development Issues

### Common Issues

#### Decorator Not Found

```
DecoratorNotFoundError: Decorator 'ExampleDecorator' not found in registry
```

- Ensure the decorator is registered before use
- Check for typos in the decorator name
- Verify the import order

#### JavaScript Errors

```
JavaScriptError: Unexpected token in transform_function
```

- Check JavaScript syntax in the transform function
- Ensure all variables are defined
- Test the transform function with different inputs

#### Type Checking Errors

```
mypy: error: Argument 1 to "apply_decorator" has incompatible type "str"; expected "DecoratorBase"
```

- Fix type annotations
- Update signature to match implementation
- Add appropriate type casts

### Debugging Strategies

- Use logging to trace execution flow
- Add debug prints for complex operations
- Use a debugger for step-by-step execution
- Isolate issues with minimal reproducible examples

## Additional Resources

- [Python Documentation Style Guide](https://developers.google.com/style/python-documentation)
- [JavaScript Best Practices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
- [Effective Pull Request Reviews](https://github.blog/2015-01-21-how-to-write-the-perfect-pull-request/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Next Steps

- Explore the [core concepts](concepts.md) to understand the framework's architecture
- Check the [API Reference](api/index.md) for detailed reference
- Read the [tutorials](tutorials/creating_custom_decorator.md) for practical examples

For detailed API documentation, see the [API Reference](api/index.md).

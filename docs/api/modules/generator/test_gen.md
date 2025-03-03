# Test Generation Module

The `test_gen` module provides functionality for generating tests for decorators. It automates the creation of test cases for decorator classes.

## TestGenerator

```python
class TestGenerator:
    """Generates tests for decorators.

    This class provides methods for generating tests for decorators,
    including unit tests, integration tests, and property-based tests.
    """
```

The `TestGenerator` class generates tests for decorators, including unit tests, integration tests, and property-based tests.

### Key Methods

- `generate_unit_tests(spec: dict) -> str`: Generate unit tests for a decorator
- `generate_integration_tests(spec: dict) -> str`: Generate integration tests for a decorator
- `generate_property_tests(spec: dict) -> str`: Generate property-based tests for a decorator

## TestCase

```python
class TestCase:
    """Represents a test case for a decorator.

    This class represents a test case for a decorator, including
    the input, expected output, and test parameters.
    """
```

The `TestCase` class represents a test case for a decorator, including the input, expected output, and test parameters.

### Key Attributes

- `decorator_name`: The name of the decorator being tested
- `parameters`: The parameters for the decorator
- `input_prompt`: The input prompt for the test
- `expected_output`: The expected output of the test
- `description`: A description of the test case

## TestSuite

```python
class TestSuite:
    """Collection of test cases for a decorator.

    This class represents a collection of test cases for a decorator,
    organized by test type.
    """
```

The `TestSuite` class represents a collection of test cases for a decorator, organized by test type.

### Key Attributes

- `decorator_name`: The name of the decorator being tested
- `unit_tests`: Unit tests for the decorator
- `integration_tests`: Integration tests for the decorator
- `property_tests`: Property-based tests for the decorator

### Key Methods

- `add_test_case(test_case: TestCase) -> None`: Add a test case to the suite
- `generate_test_file() -> str`: Generate a test file for the suite

## Usage Example

```python
from prompt_decorators.generator.test_gen import TestGenerator, TestCase, TestSuite

# Create test generator
generator = TestGenerator()

# Generate tests for a decorator
spec = {
    "name": "MyCustomDecorator",
    "parameters": [
        {"name": "style", "type": "str", "default": "detailed", "description": "Style of the decorator"}
    ],
    "description": "A custom decorator for demonstration purposes",
    "category": "custom",
    "behavior": "Adds custom behavior to the prompt"
}

unit_tests = generator.generate_unit_tests(spec)
integration_tests = generator.generate_integration_tests(spec)
property_tests = generator.generate_property_tests(spec)

# Create a test suite
suite = TestSuite(decorator_name="MyCustomDecorator")

# Add test cases
test_case = TestCase(
    decorator_name="MyCustomDecorator",
    parameters={"style": "detailed"},
    input_prompt="Explain quantum computing.",
    expected_output="Explain quantum computing.\n\nPlease provide a detailed explanation with examples.",
    description="Test with detailed style"
)
suite.add_test_case(test_case)

# Generate test file
test_file = suite.generate_test_file()

# Write to file
with open("test_my_custom_decorator.py", "w") as f:
    f.write(test_file)
```

## API Reference

::: prompt_decorators.generator.test_gen

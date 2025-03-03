# Prompt Decorators Testing Framework

This directory contains the automated testing infrastructure for the Prompt Decorators project. The framework is designed to validate the implementation of decorators, test their behavior with LLMs, and verify compatibility between different decorators.

## Overview

The testing infrastructure consists of:

1. **Auto-generated tests**: Tests automatically created from decorator JSON definitions
2. **Test utilities**: Helper functions for testing decorators
3. **Manual examples**: Specific test cases and real-world examples
4. **Response cache**: System to avoid redundant API calls during testing

## Directory Structure

```
tests/
├── auto/                  # Auto-generated tests from decorator schemas
│   ├── reasoning/         # Tests for reasoning decorators
│   ├── structure/         # Tests for structure decorators
│   ├── tone/              # Tests for tone decorators
│   ├── verification/      # Tests for verification decorators
│   └── meta/              # Tests for meta-decorators
├── cache/                 # Cached responses from LLM APIs
├── examples/              # Manual test examples and real-world use cases
├── utils/                 # Test utility functions and helpers
│   └── test_helpers.py    # Core test helpers
└── README.md              # This file
```

## Test Generation

Tests are automatically generated from decorator JSON definitions using the registry tools script:

```bash
# Method 1: Use registry_tools.py (recommended)
python scripts/registry_tools.py generate-tests

# Method 2: Use run_tests.py with --generate flag
python scripts/run_tests.py --generate
```

This process:
1. Reads all decorator JSON files from the registry
2. Extracts parameter information, examples, and compatibility requirements
3. Generates test files for each decorator in the `tests/auto` directory

## Running Tests

### Running All Tests

```bash
# Method 1: Use run_tests.py (recommended)
python scripts/run_tests.py

# Method 2: Use pytest directly
pytest tests/auto
```

### Running Tests for a Specific Category

```bash
pytest tests/auto/reasoning
```

### Running Tests for a Specific Decorator

```bash
pytest tests/auto/reasoning/reasoning_test.py
```

## Test Environment Options

The testing framework supports different modes of operation:

### Using Mock Responses (Default)

Tests use simulated LLM responses:

```bash
pytest tests/auto
```

### Using Real LLM API

Tests use actual LLM API calls:

```bash
USE_REAL_LLM=true pytest tests/auto
```

### Using Response Cache

To avoid redundant API calls, enable response caching:

```bash
USE_REAL_LLM=true USE_RESPONSE_CACHE=true pytest tests/auto
```

## Test Helpers

The `test_helpers.py` module provides utility functions for testing:

- `validate_decorator_in_prompt()`: Validates decorator syntax and parameters
- `check_expectation()`: Checks if a response meets specified expectations
- `LLMClient`: Client for generating responses (real or simulated)
- `combine_decorators()`: Checks compatibility between decorators

## Example Test

Here's an example of an auto-generated test for the Reasoning decorator:

```python
def test_reasoning_depth_enum_values():
    """Test that depth accepts only valid enum values."""
    # Valid values
    validate_decorator_in_prompt("+++Reasoning(depth=basic)\nTest prompt.")
    validate_decorator_in_prompt("+++Reasoning(depth=moderate)\nTest prompt.")
    validate_decorator_in_prompt("+++Reasoning(depth=comprehensive)\nTest prompt.")

    # Invalid value
    with pytest.raises(ValidationError):
        validate_decorator_in_prompt("+++Reasoning(depth=invalid_value)\nTest prompt.")
```

## Adding Custom Tests

While most tests are auto-generated, you can add custom tests for specific scenarios:

1. Create a new test file in the appropriate directory
2. Import the necessary test helpers
3. Write your test cases
4. Run the tests using pytest

## Integration Testing

Integration tests verify that different decorators work together properly:

```python
def test_reasoning_with_step_by_step():
    response = llm_client.generate("+++Reasoning\n+++StepByStep\nExplain quantum computing.")
    assert check_expectation(response, "contains_numbered_steps")
    # More assertions...
```

## Extending the Framework

To extend the testing framework:

1. Add new expectation checkers in `test_helpers.py`
2. Enhance the test generator in `generate_tests.py`
3. Improve the mock response generation in `LLMClient._generate_mock_response()`

## Continuous Integration

The test suite can be integrated into CI pipelines to automatically validate changes:

```yaml
# Example GitHub Actions workflow
name: Decorator Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Generate tests
        run: python scripts/generate_tests.py
      - name: Run tests
        run: pytest tests/auto
```

## Adding Real LLM API Support

To test with actual LLM APIs, implement the `_call_real_llm_api()` method in `LLMClient`:

```python
def _call_real_llm_api(self, prompt):
    # Example with OpenAI API
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

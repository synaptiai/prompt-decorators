# Prompt Decorators Python Reference Implementation

This is a reference implementation of the [Prompt Decorators](../../README.md) specification in Python. It provides a complete implementation of the core decorators, validation tools, and example usage.

## Features

- Implementation of all core decorators:
  - `+++Reasoning`
  - `+++StepByStep`
  - `+++OutputFormat`
  - `+++Tone`
  - `+++Version`
- JSON Schema validation
- Pydantic models for type safety
- Comprehensive test suite
- Example usage with pretty printing

## Installation

```bash
# Using Poetry (recommended)
poetry install

# Using pip
pip install .
```

## Usage

### Basic Example

```python
from prompt_decorators import (
    APIRequest,
    ReasoningDecorator,
    StepByStepDecorator,
    OutputFormatDecorator,
    OutputFormat,
)

# Create a request with decorators
request = APIRequest(
    prompt="Explain how nuclear fusion works",
    decorators=[
        ReasoningDecorator(
            version="1.0.0",
            parameters={"depth": "comprehensive"}
        ),
        StepByStepDecorator(
            version="1.0.0",
            parameters={"numbered": True}
        ),
        OutputFormatDecorator(
            version="1.0.0",
            parameters={"format": OutputFormat.MARKDOWN}
        )
    ]
)

# The above is equivalent to:
"""
+++Reasoning(depth=comprehensive)
+++StepByStep(numbered=true)
+++OutputFormat(format=markdown)
Explain how nuclear fusion works
"""
```

### Validation

```python
from pathlib import Path
from prompt_decorators import DecoratorValidator

# Initialize validator with schema directory
validator = DecoratorValidator(Path("../../schemas"))

# Validate request
errors = validator.validate_api_request(request)
if not errors:
    print("Request is valid!")
else:
    print("Validation errors:", errors)
```

### Running the Example

```bash
# Using Poetry
poetry run python -m prompt_decorators.example

# Direct Python execution
python -m prompt_decorators.example
```

## Development

### Running Tests

```bash
# Using Poetry
poetry run pytest

# Using pytest directly
pytest
```

### Code Quality

```bash
# Format code
poetry run black .

# Run linter
poetry run ruff check .

# Run type checker
poetry run mypy .
```

## Project Structure

```
prompt_decorators/
├── __init__.py      # Package initialization
├── models.py        # Core data models
├── validator.py     # Schema validation
└── example.py       # Usage example

tests/
└── test_decorators.py  # Test suite
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](../../LICENSE) file for details. 
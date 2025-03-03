# Request Module

The `request` module provides functionality for handling decorated requests. It manages the application of decorators to prompts and the processing of responses.

## DecoratedRequest

```python
class DecoratedRequest:
    """Represents a request with decorators.

    This class encapsulates a prompt and its associated decorators,
    providing methods for applying the decorators and processing the request.
    """
```

The `DecoratedRequest` class represents a request with decorators. It encapsulates a prompt and its associated decorators.

### Key Attributes

- `prompt`: The original prompt text
- `decorators`: The list of decorators to apply
- `metadata`: Additional metadata for the request

### Key Methods

- `apply_decorators() -> str`: Apply all decorators to the prompt
- `to_dict() -> dict`: Convert the request to a dictionary representation
- `from_dict(data: dict) -> DecoratedRequest`: Create a request from a dictionary representation

## RequestProcessor

```python
class RequestProcessor:
    """Processes decorated requests.

    This class handles the processing of decorated requests, including
    validation, application of decorators, and model-specific adaptations.
    """
```

The `RequestProcessor` class processes decorated requests, handling validation, application of decorators, and model-specific adaptations.

### Key Methods

- `process(request: DecoratedRequest) -> str`: Process a decorated request
- `validate(request: DecoratedRequest) -> bool`: Validate a decorated request
- `adapt_to_model(request: DecoratedRequest, model: str) -> DecoratedRequest`: Adapt a request to a specific model

## Usage Example

```python
from prompt_decorators.core.request import DecoratedRequest, RequestProcessor
from prompt_decorators.decorators import Reasoning, StepByStep

# Create request
request = DecoratedRequest(
    prompt="Explain how nuclear fusion works.",
    decorators=[
        Reasoning(depth="comprehensive"),
        StepByStep(numbered=True)
    ],
    metadata={"model": "gpt-4"}
)

# Process request
processor = RequestProcessor()
processed_prompt = processor.process(request)

# Convert to dictionary
request_dict = request.to_dict()

# Create from dictionary
new_request = DecoratedRequest.from_dict(request_dict)
```

## API Reference {: #core-request-api-reference }

::: prompt_decorators.core.request

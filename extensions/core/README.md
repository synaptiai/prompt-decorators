# Prompt Decorators Core Extension

This package provides a Python implementation of the Prompt Decorators Core extension, which includes decorators for reasoning, step-by-step instructions, output formatting, tone adjustment, and version specification.

## Installation

```bash
pip install prompt-decorators-core
```

Or with Poetry:

```bash
poetry add prompt-decorators-core
```

## Features

- **Reasoning Decorator**: Encourages the AI to show its thought process before reaching conclusions.
- **StepByStep Decorator**: Structures responses as a sequence of steps.
- **OutputFormat Decorator**: Controls the format of responses (plaintext, markdown, JSON, YAML, XML).
- **Tone Decorator**: Adjusts the writing style of responses (formal, casual, friendly, technical, humorous).
- **Version Decorator**: Specifies the version of the Prompt Decorators standard.

## Usage

### Creating API Requests with Decorator Objects

```python
from prompt_decorators_core import (
    APIRequest,
    Reasoning,
    ReasoningDepth,
    StepByStep,
    OutputFormat,
    OutputFormatType,
    Tone,
    ToneStyle,
    Version,
)

# Create decorators
decorators = [
    Version(standard="1.0.0"),
    Reasoning(depth=ReasoningDepth.COMPREHENSIVE),
    StepByStep(numbered=True),
    OutputFormat(format=OutputFormatType.MARKDOWN),
    Tone(style=ToneStyle.TECHNICAL),
]

# Create API request
request = APIRequest(
    model="gpt-4",
    prompt="Explain how nuclear fusion works and its potential as an energy source.",
    decorators=decorators,
    temperature=0.7,
)

# Get decorated prompt
decorated_prompt = request.get_decorated_prompt()
print(decorated_prompt)

# Get JSON representation
json_representation = request.to_json()
print(json_representation)

# Get system instructions
system_instructions = request.get_system_instructions()
print(system_instructions)
```

### Parsing Decorated Prompts

```python
from prompt_decorators_core import APIRequest

# Create decorated prompt
decorated_prompt = (
    '+++Version(standard="1.0.0")'
    '+++Reasoning(depth="comprehensive")'
    '+++StepByStep(numbered=true)'
    '+++OutputFormat(format="markdown")'
    '+++Tone(style="technical")'
    'Explain how nuclear fusion works and its potential as an energy source.'
)

# Create API request from decorated prompt
request = APIRequest.from_decorated_prompt(
    model="gpt-4",
    decorated_prompt=decorated_prompt,
    temperature=0.7,
)

# Get parsed prompt
print(request.prompt)

# Get system instructions
print(request.get_system_instructions())

# Get JSON representation
print(request.to_json())
```

### Command-Line Interface

The package includes a command-line interface for working with decorated prompts:

```bash
# Process a decorated prompt and output JSON
prompt-decorators "+++Reasoning(depth=\"comprehensive\")Explain nuclear fusion" --output json

# Read a prompt from a file
prompt-decorators @prompt.txt --model gpt-4 --temperature 0.8

# Output system instructions
prompt-decorators "+++StepByStep(numbered=true)How to make pasta" --output instructions

# Save output to a file
prompt-decorators "+++OutputFormat(format=\"markdown\")Python tutorial" --output-file output.json
```

Available options:
- `--model`, `-m`: Model to use (default: "gpt-4")
- `--temperature`, `-t`: Temperature for the request (default: 0.7)
- `--max-tokens`: Maximum number of tokens to generate
- `--output`, `-o`: Output format (json, decorated, instructions, prompt)
- `--output-file`, `-f`: Output file path

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/prompt-decorators/extensions.git
cd extensions/core

# Install dependencies
poetry install

# Run tests
poetry run pytest
```

### Running the Example

```bash
poetry run python -m prompt_decorators_core.example
```

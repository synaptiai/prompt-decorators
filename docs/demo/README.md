# Demoing the Prompt Decorators

This guide explains how to use the demo tools provided with the Prompt Decorators framework to showcase its capabilities. The demos help illustrate the power of decorators in enhancing LLM outputs for different use cases.

## Overview

The Prompt Decorators demo package includes:

1. A **CLI demo** for quick examples from the command line
2. An **interactive web demo** for visual experimentation
3. A collection of **example scripts** for different use cases
4. A **comparison tool** to see before/after decorator effects

## Installation

To use the demo tools, install the package with the demo extras:

```bash
pip install "prompt-decorators[demo]"
```

This installs the core package plus additional dependencies required for the demos.

## Command Line Demo

The CLI demo allows you to quickly experiment with decorators from the command line:

```bash
# Run a basic example
python -m prompt_decorators.demo.main basic step-by-step

# Try a custom prompt with decorators
python -m prompt_decorators.demo.dynamic_openai_demo run-custom-prompt \
  --prompt "Explain quantum computing" \
  --decorator "Audience(level=beginner)" \
  --decorator "StepByStep(numbered=true)"
```

### Available Commands

```bash
# List all available decorators
python -m prompt_decorators.demo.dynamic_openai_demo --list-decorators

# Run a predefined example
python -m prompt_decorators.demo.dynamic_openai_demo --example step_by_step

# Getting help
python -m prompt_decorators.demo.dynamic_openai_demo --help
```

### Basic Examples

```bash
# Basic reasoning and structure decorators
python -m prompt_decorators.demo.main basic reasoning                 # Use the Reasoning decorator
python -m prompt_decorators.demo.main basic step-by-step              # Use the StepByStep decorator
python -m prompt_decorators.demo.main basic output-format             # Use the OutputFormat decorator
python -m prompt_decorators.demo.main basic bullet                    # Use the Bullet decorator
python -m prompt_decorators.demo.main basic tree-of-thought           # Use the TreeOfThought decorator
```

### Advanced Examples

```bash
# Standard advanced compositions
python -m prompt_decorators.demo.main advanced compound-decorators     # Combines StepByStep, Reasoning, and OutputFormat
python -m prompt_decorators.demo.main advanced tech-tutorial           # Creates a technical tutorial using multiple decorators
python -m prompt_decorators.demo.main advanced decision-analysis       # Uses decorators for structured decision analysis
python -m prompt_decorators.demo.main advanced debate-topic            # Creates balanced debate analysis
```

## Interactive Web Demo

The web demo provides an interactive interface for exploring decorators:

```bash
# Start the web interface
python -m prompt_decorators.demo.web_app
```

Then open your browser to http://localhost:7860 to access the interface.

### Web Demo Features

- **Interactive Decorator Selection**: Choose from available decorators with a simple interface
- **Parameter Configuration**: Customize decorator parameters
- **Real-time Preview**: See the transformed prompt before sending to an LLM
- **Response Comparison**: Compare responses with and without decorators
- **Decorator Stacking**: Combine multiple decorators and adjust their order
- **Export Options**: Save your configurations and responses

## Example Scripts

The demo package includes example scripts that showcase different applications of prompt decorators:

### Basic Examples

Found in `demo/examples/basic.py`:

```python
from prompt_decorators.demo.examples.basic import run_example

# Run the reasoning example
run_example("reasoning")
```

### Advanced Examples

Found in `demo/examples/advanced.py`:

```python
from prompt_decorators.demo.examples.advanced import run_example

# Run the technical tutorial example
run_example("tech_tutorial")
```

### Domain-Specific Examples

Found in `demo/examples/domain_specific.py`:

```python
from prompt_decorators.demo.examples.domain_specific import run_example

# Run the data science example
run_example("data_science")
```

## Comparison Tool

The comparison tool helps visualize the difference between decorated and undecorated prompts:

```bash
python -m prompt_decorators.demo.compare \
  --prompt "Explain how nuclear fusion works" \
  --decorator "StepByStep(numbered=true)" \
  --decorator "Audience(level=beginner)" \
  --model "gpt-4"
```

This will:
1. Send the original prompt to the LLM
2. Send the decorated prompt to the LLM
3. Display both responses side by side for comparison

## Configuration

The demo tools can be configured through environment variables or a `.env` file:

```
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Model Configuration
DEFAULT_MODEL=gpt-4o-mini
MAX_TOKENS=2048
TEMPERATURE=0.7

# Logging Configuration
LOG_LEVEL=INFO
SAVE_LOGS=false
LOG_FILE=prompt_decorator_demo.log
```

## Creating Your Own Demos

You can create custom demos based on the provided examples:

```python
from prompt_decorators import apply_dynamic_decorators, create_decorator_instance
from prompt_decorators.demo.utils.llm_client import get_completion

# Define a custom demo
def my_custom_demo():
    # Create a decorated prompt
    prompt = """
    +++Persona(role="historian")
    +++StepByStep(numbered=true)
    +++OutputFormat(format="markdown")
    Explain the causes of World War I
    """

    # Apply decorators
    transformed_prompt = apply_dynamic_decorators(prompt)

    # Print the transformation
    print("Original prompt:")
    print(prompt)
    print("\nTransformed prompt:")
    print(transformed_prompt)

    # Get LLM response (if API key is configured)
    try:
        response = get_completion(transformed_prompt)
        print("\nLLM Response:")
        print(response)
    except Exception as e:
        print(f"Error getting LLM response: {e}")

if __name__ == "__main__":
    my_custom_demo()
```

## Demo Architecture

The demo code is structured as follows:

- `prompt_decorators/demo/main.py`: Main entry point for CLI
- `prompt_decorators/demo/dynamic_openai_demo.py`: OpenAI-specific demo
- `prompt_decorators/demo/web_app.py`: Web interface using Gradio
- `prompt_decorators/demo/compare.py`: Comparison tool
- `prompt_decorators/demo/examples/`: Example scripts
- `prompt_decorators/demo/utils/`: Utility functions

## Best Practices for Demonstrations

When using the demo tools to present Prompt Decorators:

1. **Start Simple**: Begin with basic decorators before moving to complex combinations
2. **Show Transformations**: Always display both the original and transformed prompts
3. **Use Real-World Examples**: Choose examples relevant to your audience
4. **Highlight Benefits**: Emphasize improved structure, clarity, or depth in responses
5. **Compare Results**: Show the difference between decorated and undecorated prompts
6. **Customize for Audience**: Adjust examples based on your audience's domain

## Troubleshooting

### API Key Issues

If you encounter authentication errors:

```
Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.
```

Make sure to set your API key:

```bash
export OPENAI_API_KEY=your_api_key_here
```

Or create a `.env` file in the demo directory.

### Model Availability

If you see:

```
Error: The model 'gpt-4' does not exist or you do not have access to it.
```

Try using a different model:

```bash
python -m prompt_decorators.demo.dynamic_openai_demo run-custom-prompt \
  --prompt "Hello world" \
  --model "gpt-3.5-turbo"
```

### Other Issues

For other common issues, check the troubleshooting section in the README.md file in the demo directory.

## Next Steps

- Explore the [tutorials](../tutorials/creating_custom_decorator.md) to create your own decorators
- Learn about [MCP integration](../integrations/mcp.md) to use decorators with Claude and other LLMs
- Read the [specification](../prompt-decorators-specification-v1.0.md) for detailed technical information

# Prompt Decorator Test Examples

This directory contains example scripts that demonstrate how to use various prompt decorators with actual AI models and test their behavior in real-world scenarios.

## Running the Examples

Most examples require an API key for the AI model service being used. Set the appropriate environment variables before running the examples:

```bash
# For OpenAI models (GPT-3.5, GPT-4)
export OPENAI_API_KEY="your-api-key-here"

# For Anthropic models (Claude)
export ANTHROPIC_API_KEY="your-api-key-here"

# To enable tests with GPT-4 (optional)
export USE_GPT4="true"
```

Then run the example scripts:

```bash
python tests/examples/tree_of_thought_example.py
python tests/examples/comparison_example.py
```

## Available Examples

### Reasoning Decorators
- `tree_of_thought_example.py` - Demonstrates the TreeOfThought decorator with various branching configurations

### Structure Decorators
- `comparison_example.py` - Demonstrates the Comparison decorator with different formats and aspect configurations

### Tone Decorators
- (Examples coming soon)

### Verification Decorators
- (Examples coming soon)

## Creating New Examples

When creating new test examples, follow these guidelines:

1. Name the file according to the decorator being tested (`decorator_name_example.py`)
2. Include multiple parameter configurations to show the decorator's flexibility
3. Test with at least 2-3 different prompts to demonstrate behavior across contexts
4. Include clear output formatting to make results easy to interpret
5. Add appropriate error handling and environment checks
6. Update this README when adding a new example

Each example should be self-contained and well-documented to serve as a learning resource. 
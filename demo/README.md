# OpenAI Prompt Decorator Demo

This demo showcases the power of prompt decorators with the OpenAI API. It demonstrates how to apply various decorators to enhance LLM outputs for different use cases using a dynamic decorator implementation.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up configuration
cp .env.sample .env
# Edit .env to add your OpenAI API key

# Run a basic example
python -m demo.main basic step-by-step

# Try a custom prompt with decorators
python -m demo.dynamic_openai_demo run-custom-prompt \
  --prompt "Explain quantum computing" \
  --decorator "Audience(level=beginner)" \
  --decorator "StepByStep(numbered=true)"
```

## Dynamic Decorator Implementation

This demo uses a dynamic decorator implementation that loads decorator definitions directly from JSON files at runtime, eliminating the need for code generation.

```bash
# List all available dynamic decorators
python -m demo.dynamic_openai_demo --list-decorators

# Run a predefined example
python -m demo.dynamic_openai_demo --example step_by_step

# Run a custom prompt with multiple decorators
python -m demo.dynamic_openai_demo run-custom-prompt \
  --prompt "Explain quantum computing" \
  --decorator "Audience(level=beginner)" \
  --decorator "StepByStep(numbered=true)"
```

## Overview

Prompt decorators are a pattern for structuring prompts for large language models. This demo shows how to use the `prompt-decorators` library with OpenAI models to:

- Apply individual decorators to basic prompts
- Compose multiple decorators for advanced use cases
- Use domain-specific decorator patterns for particular fields
- Create custom decorated prompts on the fly
- Visualize how decorators transform your original prompts

## How Prompt Decorators Work

Prompt decorators use a special syntax to modify how AI models process and respond to prompts. For example:

```python
# Single decorator
+++Reasoning(depth=comprehensive)
What are the environmental impacts of electric vehicles?

# Multiple decorators
+++StepByStep(numbered=true)
+++Audience(level=beginner)
Explain how neural networks work
```

This demo transforms these decorators into natural language instructions that the model can understand:

```
# Transformed from Reasoning decorator
Please provide detailed reasoning in your response. Show your thought process step by step before reaching a conclusion. Provide a very thorough and detailed analysis.

What are the environmental impacts of electric vehicles?

# Transformed from StepByStep and Audience decorators
Please break down your response into clear, sequential steps. Number each step sequentially (Step 1, Step 2, etc.).
Please tailor your response for a specific audience expertise level. Write for beginners with no prior knowledge of the subject. Use simple language, avoid jargon, and explain concepts from first principles.

Explain how neural networks work
```

The demo shows both the decorator syntax and the transformed instructions, helping you understand how decorators enhance AI interactions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/synaptiai/prompt-decorators.git
   cd prompt-decorators
   ```

2. Install the dependencies:
   ```bash
   pip install -r demo/requirements.txt
   ```

3. Set up your OpenAI API key:

   Create a `.env` file in the `demo` directory with the following content:
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

   You can customize these settings to use different models or parameters.

## Usage

The demo is organized as a command-line application with several subcommands:

### Basic Examples

Run basic decorator examples:

```bash
# Basic reasoning and structure decorators
python -m demo.main basic reasoning                 # Use the Reasoning decorator
python -m demo.main basic step-by-step              # Use the StepByStep decorator
python -m demo.main basic output-format             # Use the OutputFormat decorator
python -m demo.main basic bullet                    # Use the Bullet decorator
python -m demo.main basic tree-of-thought           # Use the TreeOfThought decorator

# Content style decorators
python -m demo.main basic tone                      # Use the Tone decorator
python -m demo.main basic audience                  # Use the Audience decorator
python -m demo.main basic concise                   # Use the Concise decorator
python -m demo.main basic detailed                  # Use the Detailed decorator

# Advanced thinking decorators
python -m demo.main basic negative-space            # Use the NegativeSpace decorator
```

### Advanced Examples

Run advanced decorator composition examples:

```bash
# Standard advanced compositions
python -m demo.main advanced compound-decorators     # Combines StepByStep, Reasoning, and OutputFormat
python -m demo.main advanced tech-tutorial           # Creates a technical tutorial using multiple decorators
python -m demo.main advanced decision-analysis       # Uses decorators for structured decision analysis
python -m demo.main advanced debate-topic            # Creates balanced debate analysis
python -m demo.main advanced layered-explanation     # Provides explanations at multiple levels of detail

# Advanced reasoning approaches
python -m demo.main advanced first-principles-analysis  # Uses first principles reasoning
python -m demo.main advanced critical-review            # Provides critical review of a topic

# Creative and strategic examples
python -m demo.main advanced creative-problem-solving   # Uses decorators for creative solutions
python -m demo.main advanced strategic-planning         # Creates a strategic plan using multiple decorators
```

### Domain-Specific Examples

Run domain-specific decorator examples:

```bash
# Technical domains
python -m demo.main domain data-science              # Data analysis approach with multiple decorators
python -m demo.main domain technical-documentation   # Technical documentation with structured format

# Business and strategy domains
python -m demo.main domain product-management        # Product management framework with decorators
python -m demo.main domain business-strategy         # Business strategy analysis

# Content creation domains
python -m demo.main domain educational-content       # Educational content with beginner-friendly format
python -m demo.main domain creative-writing          # Creative writing with specific style

# Specialized professional domains
python -m demo.main domain scientific-review         # Scientific analysis with academic style
python -m demo.main domain legal-analysis            # Legal analysis with structured format
python -m demo.main domain medical-explanation       # Medical explanation with audience consideration
```

### Custom Prompts

Run your own custom prompts with decorators using the dynamic implementation:

```bash
# Basic custom prompt with a single decorator
python -m demo.dynamic_openai_demo run-custom-prompt \
  --prompt "Explain how neural networks work" \
  --decorator "Audience(level=beginner)"

# Combining multiple decorators
python -m demo.dynamic_openai_demo run-custom-prompt \
  --prompt "Explain how neural networks work" \
  --decorator "Audience(level=beginner)" \
  --decorator "StepByStep(numbered=true)"

# Overriding the model and temperature
python -m demo.dynamic_openai_demo run-custom-prompt \
  --prompt "What is quantum computing?" \
  --decorator "Reasoning(depth=comprehensive)" \
  --model "gpt-4" \
  --temperature 0.8
```

If you don't specify a model or temperature, the values from your `.env` file will be used.

> **Note about decorator parameters**: When specifying parameters in the command line, use the exact parameter names from the decorator definition. For example, `StepByStep(numbered=true)` or `Concise(maxWords=300)`.

## Available Decorators

The demo supports a wide range of decorators that can be used individually or in combination. You can list all available decorators with:

```bash
python -m demo.dynamic_openai_demo --list-decorators
```

### Basic Decorators
- `Reasoning(depth=basic|moderate|comprehensive)` - Enhances response with detailed thought process
- `StepByStep(numbered=true|false)` - Organizes response in sequential steps
- `OutputFormat(format=markdown|json|html|csv)` - Formats output in specific style
- `Tone(style=formal|casual|friendly|technical|humorous)` - Sets the tone of the response
- `Audience(level=beginner|intermediate|expert|technical)` - Tailors response for specific audience level
- `Concise(level=moderate|high|extreme, maxWords=int, bulletPoints=true|false)` - Creates brief, to-the-point responses
- `Detailed(depth=basic|moderate|comprehensive, examples=true|false)` - Provides comprehensive, detailed responses
- `NegativeSpace(focus=constraints|limitations|counterarguments|risks)` - Explores what's not explicitly mentioned in the prompt

### Format Decorators
- `Bullet(style=dash|dot|arrow|star, indented=true|false, compact=true|false)` - Creates bullet point lists
- `TreeOfThought(branches=3, depth=3, pruning=true|false)` - Explores multiple reasoning paths

### Other Decorators
- Academic, AsExpert, FirstPrinciples, Persona, Prioritize, Professional, and many more! Use the `--list-decorators` command to see all available options.

## Configuration

You can configure the demo through environment variables or by editing the `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key
- `DEFAULT_MODEL`: The default model to use (e.g., `gpt-4o-mini`, `gpt-4`)
- `MAX_TOKENS`: Maximum tokens in the response
- `TEMPERATURE`: Sampling temperature (0.0-2.0)
- `LOG_LEVEL`: Logging level (INFO, DEBUG, etc.)
- `SAVE_LOGS`: Whether to save logs to a file
- `LOG_FILE`: Log file path

## Decorator Registry

The dynamic decorator implementation loads decorators from a registry of JSON files. The registry is organized into the following directories:

- `registry/core` - Core decorators for reasoning, structure, tone, etc.
- `registry/extensions` - Specialized decorators for specific domains

Each decorator file contains metadata, parameter definitions, transformation templates, and usage examples, allowing the system to validate parameters and apply transformations at runtime.

## Contributing

Feel free to contribute to this demo by:

1. Adding new examples
2. Improving existing examples
3. Enhancing the documentation
4. Fixing bugs

See the main repository's [CONTRIBUTING.md](../CONTRIBUTING.md) for more details on how to contribute.

## License

This demo is licensed under the Apache License 2.0. See the [LICENSE](../LICENSE) file for details.

# OpenAI Prompt Decorator Demo

This demo showcases the power of prompt decorators with the OpenAI API. It demonstrates how to apply various decorators to enhance LLM outputs for different use cases.

## Overview

Prompt decorators are a pattern for structuring prompts for large language models. This demo shows how to use the `prompt-decorators` library with OpenAI models to:

- Apply individual decorators to basic prompts
- Compose multiple decorators for advanced use cases
- Use domain-specific decorator patterns for particular fields
- Create custom decorated prompts on the fly
- Visualize how decorators transform your original prompts

## How Prompt Decorators Work

Prompt decorators use a special syntax to modify how AI models process and respond to prompts. For example:

```
Reasoning(depth='comprehensive')
What are the environmental impacts of electric vehicles?
```

This demo transforms these decorators into natural language instructions that the model can understand:

```
Please provide detailed reasoning in your response. Show your thought process step by step before reaching a conclusion. Provide a very thorough and detailed analysis.

What are the environmental impacts of electric vehicles?
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
python -m demo.main basic reasoning
python -m demo.main basic step-by-step
python -m demo.main basic output-format
python -m demo.main basic bullet
python -m demo.main basic tree-of-thought

# Content style decorators
python -m demo.main basic tone
python -m demo.main basic audience
python -m demo.main basic concise
python -m demo.main basic detailed

# Advanced thinking decorators
python -m demo.main basic negative-space
```

### Advanced Examples

Run advanced decorator composition examples:

```bash
# Standard advanced compositions
python -m demo.main advanced compound-decorators
python -m demo.main advanced tech-tutorial
python -m demo.main advanced decision-analysis
python -m demo.main advanced debate-topic
python -m demo.main advanced layered-explanation

# Advanced reasoning approaches
python -m demo.main advanced first-principles-analysis
python -m demo.main advanced critical-review

# Creative and strategic examples
python -m demo.main advanced creative-problem-solving
python -m demo.main advanced strategic-planning
```

### Domain-Specific Examples

Run domain-specific decorator examples:

```bash
# Technical domains
python -m demo.main domain data-science
python -m demo.main domain technical-documentation

# Business and strategy domains
python -m demo.main domain product-management
python -m demo.main domain business-strategy

# Content creation domains
python -m demo.main domain educational-content
python -m demo.main domain creative-writing

# Specialized professional domains
python -m demo.main domain scientific-review
python -m demo.main domain legal-analysis
python -m demo.main domain medical-explanation
```

### Custom Prompts

Run your own custom prompts with decorators:

```bash
python -m demo.main custom run-custom-prompt --prompt "Explain how neural networks work" --decorator "Audience(level='beginner')" --decorator "StepByStep(numbered='true')"
```

You can also override the default model and temperature:

```bash
python -m demo.main custom run-custom-prompt --prompt "What is quantum computing?" --decorator "Reasoning(depth='comprehensive')" --model "gpt-4" --temperature 0.8
```

If you don't specify a model or temperature, the values from your `.env` file will be used.

> **Note about decorator parameters**: When using the CLI, string values should be enclosed in quotes, and boolean values should be specified as `true` or `false` (lowercase, without quotes). For example: `StepByStep(numbered='true')`.

## Available Decorators

The demo supports a wide range of decorators that can be used individually or in combination:

### Basic Decorators
- `Reasoning(depth='basic'|'moderate'|'comprehensive')` - Enhances response with detailed thought process
- `StepByStep(numbered='true'|'false')` - Organizes response in sequential steps
- `OutputFormat(format='markdown'|'json'|'html'|'csv')` - Formats output in specific style
- `Tone(style='formal'|'casual'|'friendly'|'technical'|'humorous')` - Sets the tone of the response
- `Audience(level='beginner'|'intermediate'|'expert'|'technical')` - Tailors response for specific audience level
- `Concise(level='minimal'|'moderate'|'balanced', max_words=int, bullet_points='true'|'false')` - Creates brief, to-the-point responses
- `Detailed(depth='basic'|'moderate'|'comprehensive', examples='true'|'false')` - Provides comprehensive, detailed responses
- `NegativeSpace(focus='constraints'|'limitations'|'counterarguments'|'risks')` - Explores what's not explicitly mentioned in the prompt

### Format Decorators
- `Bullet(style='dash'|'dot'|'arrow'|'star', indented=true|false, compact=true|false)` - Creates bullet point lists
- `TreeOfThought(branches=3, depth=3, pruning='true'|'false')` - Explores multiple reasoning paths

## Examples of Combined Decorators

Decorators can be powerful when combined. Here are some examples:

### Technical Documentation
```bash
python -m demo.main domain technical-documentation
```

This applies the following decorators:
```
StepByStep()
Audience(level='technical')
OutputFormat(format='markdown')
```

### Debate Analysis
```bash
python -m demo.main advanced debate-topic
```

This applies the following decorators:
```
Reasoning(depth='comprehensive')
StepByStep(numbered='true')
OutputFormat(format='markdown')
```

## Configuration

You can configure the demo through environment variables or by editing the `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key
- `DEFAULT_MODEL`: The default model to use (e.g., `gpt-4o-mini`, `gpt-4`)
- `MAX_TOKENS`: Maximum tokens in the response
- `TEMPERATURE`: Sampling temperature (0.0-2.0)
- `LOG_LEVEL`: Logging level (INFO, DEBUG, etc.)
- `SAVE_LOGS`: Whether to save logs to a file
- `LOG_FILE`: Log file path

## Decorator Structure

Each decorator follows a standard structure:

```
DecoratorName(parameter1='value1', parameter2='value2')
```

Parameters should be properly formatted with:
- String values in quotes (e.g., `level='beginner'`)
- Boolean values without quotes (e.g., `numbered='true'` or `numbered='false'`)
- Integer values without quotes (e.g., `max_words=150` or `branches=3`)

## Contributing

Feel free to contribute to this demo by:

1. Adding new examples
2. Improving existing examples
3. Enhancing the documentation
4. Fixing bugs

See the main repository's [CONTRIBUTING.md](../CONTRIBUTING.md) for more details on how to contribute.

## License

This demo is licensed under the Apache License 2.0. See the [LICENSE](../LICENSE) file for details.

### Known Issues with Boolean Parameters

**Important Note**: There is currently an issue with boolean parameters in the command line interface. The decorator implementations expect actual boolean values, but the command line parser does not convert string values to booleans.

**Workaround**: For now, please avoid using decorators with boolean parameters in the command line interface. Instead, use decorators that only require string parameters, such as:

- `Reasoning(depth='comprehensive')`
- `Audience(level='beginner')`
- `OutputFormat(format='markdown')`
- `Tone(style='technical')`

If you need to use decorators with boolean parameters, you can modify the code in `demo/openai_demo.py` to convert string values to appropriate types before passing them to the decorator constructor.

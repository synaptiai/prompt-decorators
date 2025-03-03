# Command Line Interface (CLI)

The Prompt Decorators framework provides a command-line interface (CLI) that allows you to interact with the framework without writing Python code. This guide covers the available commands and how to use them effectively.

## Installation

The CLI is automatically installed when you install the Prompt Decorators package:

```bash
pip install prompt-decorators
```

## Basic Usage

After installation, you can access the CLI using the `prompt-decorators` command:

```bash
prompt-decorators --help
```

This will display the available commands and options.

## Available Commands

### List Decorators

To list all available decorators in the registry:

```bash
prompt-decorators list
```

To list decorators by category:

```bash
prompt-decorators list --category reasoning
```

### Apply Decorators

To apply a decorator to a prompt:

```bash
prompt-decorators apply --decorator Reasoning --prompt "Explain quantum mechanics."
```

To apply multiple decorators:

```bash
prompt-decorators apply --decorator Reasoning --decorator OutputFormat --prompt "Explain quantum mechanics."
```

You can also specify decorator parameters:

```bash
prompt-decorators apply --decorator "Reasoning:style=detailed,show_working=true" --prompt "Explain quantum mechanics."
```

### Generate Code

To generate code for a new decorator:

```bash
prompt-decorators generate --name CustomDecorator --category custom --output ./my_decorators
```

This will generate the necessary Python files for a new decorator.

### Validate Decorators

To validate a decorator JSON definition:

```bash
prompt-decorators validate --file ./decorators/custom_decorator.json
```

### Interactive Mode

The CLI also provides an interactive mode where you can apply decorators and see the results in real-time:

```bash
prompt-decorators interactive
```

This will start an interactive session where you can:
- Select decorators from a list
- Configure decorator parameters
- Enter a prompt
- See the decorated prompt
- Save the decorated prompt to a file

## Using with Pipes

You can use the CLI with Unix pipes to integrate with other tools:

```bash
echo "Explain quantum mechanics." | prompt-decorators apply --decorator Reasoning | openai api completions.create -m gpt-4
```

## Environment Variables

The CLI respects the following environment variables:

- `PROMPT_DECORATORS_REGISTRY_PATH`: Path to a custom registry directory
- `PROMPT_DECORATORS_CONFIG_PATH`: Path to a custom configuration file

Example:

```bash
export PROMPT_DECORATORS_REGISTRY_PATH=./my_decorators
prompt-decorators list
```

## Configuration File

You can create a configuration file at `~/.prompt-decorators/config.json` to set default values for the CLI:

```json
{
  "default_decorators": ["Reasoning", "OutputFormat"],
  "default_parameters": {
    "Reasoning": {
      "style": "detailed",
      "show_working": true
    },
    "OutputFormat": {
      "format_type": "markdown",
      "pretty_print": true
    }
  },
  "registry_path": "./my_decorators"
}
```

## Examples

### Example 1: Basic Decorator Application

```bash
prompt-decorators apply --decorator Reasoning --prompt "Explain the theory of relativity."
```

Output:
```
I need to explain the theory of relativity.

Let me think through this step by step:

1. First, I'll explain what the theory of relativity is
2. Then, I'll cover the key principles
3. Finally, I'll discuss its significance and implications

Now, I'll explain the theory of relativity:

The theory of relativity, developed by Albert Einstein, consists of two related theories: special relativity (1905) and general relativity (1915)...
```

### Example 2: Combining Multiple Decorators

```bash
prompt-decorators apply --decorator "Persona:role=physicist,tone=educational" --decorator "OutputFormat:format_type=markdown" --prompt "Explain quantum entanglement."
```

Output:
```
# Quantum Entanglement Explanation

As a physicist, I'm pleased to provide an educational explanation of quantum entanglement.

Quantum entanglement is a phenomenon in quantum physics where two or more particles become correlated in such a way that the quantum state of each particle cannot be described independently of the others...
```

### Example 3: Using the Interactive Mode

```bash
prompt-decorators interactive
```

This will start an interactive session with prompts to:
1. Select decorators from a list
2. Configure parameters for each decorator
3. Enter your prompt
4. View the decorated prompt
5. Optionally save the result to a file

### Example 4: Generating Code for a New Decorator

```bash
prompt-decorators generate --name EthicalConsiderations --category ethics --output ./my_decorators
```

This will generate:
- A Python file for the decorator implementation
- A JSON file for the decorator definition
- Test files for the decorator

## Next Steps

- Explore the [API Reference](../api/index.md)
- Learn about [API Integration](../guide/api-integration.md)
- Check out [Advanced Usage](../guide/advanced-usage.md)

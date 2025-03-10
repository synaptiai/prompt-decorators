# Frequently Asked Questions

This document answers common questions about the Prompt Decorators framework.

## General Questions

### What is Prompt Decorators?

Prompt Decorators is a Python framework for enhancing prompts sent to Large Language Models (LLMs). It provides a standardized way to modify how AI models process and respond to requests using a decorator pattern.

### How does it work?

The framework uses a simple syntax where decorators are prefixed with `+++` followed by a decorator name and optional parameters. These decorators are transformed into natural language instructions that LLMs can understand.

### What problem does it solve?

Prompt Decorators addresses several challenges:

1. **Consistency**: Provides a standardized way to enhance prompts across different LLMs
2. **Reusability**: Allows prompt enhancements to be reused across projects
3. **Composability**: Enables combining multiple enhancements for complex behaviors
4. **Maintainability**: Makes prompt engineering more structured and maintainable

### Which LLM providers are supported?

The framework is designed to work with any LLM provider, including:

- OpenAI (gpt-4, gpt-4o, etc.)
- Anthropic Claude
- Google Gemini
- Mistral AI
- Hugging Face models
- Local models

### Is it open source?

Yes, Prompt Decorators is open source under the MIT License, which allows for both personal and commercial use.

## Installation and Setup

### How do I install Prompt Decorators?

Install using pip:

```bash
pip install prompt-decorators
```

For additional features, you can install with extras:

```bash
# For MCP integration
pip install "prompt-decorators[mcp]"

# For development
pip install "prompt-decorators[dev,test,docs]"
```

### What are the system requirements?

- Python 3.11 or higher
- No special hardware requirements
- Works on Windows, macOS, and Linux

### How do I verify my installation?

```python
import prompt_decorators
print(prompt_decorators.__version__)
```

### Do I need API keys for LLM providers?

Yes, you'll need API keys for any LLM providers you want to use. The framework itself doesn't provide access to LLMs.

## Using Decorators

### How do I use decorators in my prompts?

Use the inline syntax directly in your prompts:

```python
prompt = """
+++StepByStep(numbered=true)
+++Audience(level="beginner")
Explain quantum computing.
"""

from prompt_decorators import apply_dynamic_decorators
transformed_prompt = apply_dynamic_decorators(prompt)
```

### Can I use decorators programmatically?

Yes, you can create and use decorator instances in your code:

```python
from prompt_decorators import create_decorator_instance

step_by_step = create_decorator_instance("StepByStep", numbered=True)
audience = create_decorator_instance("Audience", level="beginner")

original_prompt = "Explain quantum computing."
transformed_prompt = step_by_step(audience(original_prompt))
```

### How do I combine multiple decorators?

You can stack decorators either inline:

```
+++Persona(role="scientist")
+++StepByStep(numbered=true)
+++Audience(level="beginner")
Explain quantum computing.
```

Or programmatically:

```python
persona = create_decorator_instance("Persona", role="scientist")
step_by_step = create_decorator_instance("StepByStep", numbered=True)
audience = create_decorator_instance("Audience", level="beginner")

transformed_prompt = persona(step_by_step(audience(original_prompt)))
```

### What happens if decorators conflict?

When decorators have conflicting behaviors, the later decorator in the sequence takes precedence. For example, if you use both `Concise` and `Detailed`, the one that appears later will have more influence on the result.

### How many decorators can I use at once?

There's no hard limit on the number of decorators you can use, but consider:

1. **Token Usage**: Each decorator adds instructions that count toward token limits
2. **Clarity**: Too many decorators might create conflicting or confusing instructions
3. **Performance**: More decorators mean more processing time

A practical limit is typically 3-5 decorators per prompt.

## Available Decorators

### What decorators are included?

The framework includes over 140 pre-defined decorators in categories such as:

- **Reasoning**: Enhance logical thinking and problem-solving
- **Format**: Control output format and structure
- **Style**: Modify tone, voice, and writing style
- **Audience**: Target specific audiences
- **Persona**: Adopt specific roles or personalities
- **Domain**: Focus on specific knowledge domains
- **Length**: Control response length

### How do I see all available decorators?

```python
from prompt_decorators import get_available_decorators

decorators = get_available_decorators()
for decorator in decorators:
    print(f"{decorator.name}: {decorator.description}")
```

### What are the most commonly used decorators?

Some of the most popular decorators include:

- `StepByStep`: Breaks down responses into sequential steps
- `Reasoning`: Enhances logical reasoning in responses
- `Audience`: Adapts content for specific audience levels
- `Persona`: Adopts a specific role or personality
- `OutputFormat`: Controls the format of the output (markdown, JSON, etc.)
- `Concise`: Creates brief, to-the-point responses
- `Detailed`: Provides comprehensive, detailed responses

## Custom Decorators

### Can I create my own decorators?

Yes, you can create custom decorators using the `DecoratorDefinition` class:

```python
from prompt_decorators import DecoratorDefinition, register_decorator

my_decorator_def = DecoratorDefinition(
    name="MyCustomDecorator",
    description="A custom decorator that adds a prefix and suffix",
    category="Custom",
    parameters=[
        {"name": "prefix", "type": "string", "description": "Text to add before", "default": "START: "},
        {"name": "suffix", "type": "string", "description": "Text to add after", "default": " :END"}
    ],
    transform_function="return prefix + text + suffix;"
)

register_decorator(my_decorator_def)
```

### What language are transform functions written in?

Transform functions are written in JavaScript, which is executed in a sandboxed environment.

### Can I share my custom decorators?

Yes, you can share custom decorators by:

1. Creating a Python package with your decorator definitions
2. Sharing JSON files containing decorator definitions
3. Contributing to the main project

### How do I validate my custom decorators?

Use the validator tool to check your decorators:

```bash
python -m prompt_decorators.tools.validator validate my_decorator.json
```

You can also use the more comprehensive unified validator script:

```bash
# Validate decorator syntax in a prompt
python scripts/prompt_validator.py syntax -t "+++Reasoning(depth=comprehensive)\nExplain quantum computing."

# Validate a decorator schema file
python scripts/prompt_validator.py schema -f registry/core/reasoning/deductive.json
```

## Integrations

### How do I use Prompt Decorators with Claude Desktop?

1. Install the MCP integration:
   ```bash
   pip install "prompt-decorators[mcp]"
   ```

2. Run the Claude Desktop integration:
   ```bash
   python -m prompt_decorators.integrations.mcp.claude_desktop
   ```

3. In Claude Desktop, you'll see new tools available for working with decorators.

### What is MCP?

MCP (Model Context Protocol) is a protocol for integrating tools with LLM clients. Prompt Decorators provides an MCP integration that allows any MCP-compatible client to use decorators.

### Can I use Prompt Decorators in a web application?

Yes, you can integrate Prompt Decorators into web applications:

```python
from fastapi import FastAPI, Request
from prompt_decorators import apply_dynamic_decorators

app = FastAPI()

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    # Apply decorators
    transformed_prompt = apply_dynamic_decorators(prompt)

    # Send to LLM (implementation depends on your LLM client)
    response = your_llm_client.generate(transformed_prompt)

    return {"response": response}
```

## Performance and Limitations

### What is the performance impact?

The framework adds minimal overhead to prompt processing:

- Parsing decorators: microseconds to milliseconds
- Executing transform functions: milliseconds
- Overall impact: negligible compared to LLM API call time

### Are there token limits?

The framework itself doesn't impose token limits, but:

1. Each decorator adds instructions that count toward your LLM's token limits
2. More complex decorators add more tokens
3. Consider the token limits of your LLM provider

### Can decorators access external resources?

No, transform functions run in a sandboxed JavaScript environment and cannot access external resources like files, networks, or databases.

### Is there a rate limit?

The framework itself doesn't impose rate limits, but your LLM provider might have rate limits on API calls.

## Troubleshooting

### Why isn't my decorator being applied?

Common issues include:

1. **Syntax Errors**: Check that your decorator syntax is correct (`+++DecoratorName(param=value)`)
2. **Missing Registration**: Ensure the decorator is registered before use
3. **Name Typos**: Verify the decorator name is spelled correctly (case-sensitive)
4. **Parameter Errors**: Check that parameter names and values are correct

### How do I debug decorator transformations?

Print the transformed prompt to see what's happening:

```python
from prompt_decorators import apply_dynamic_decorators

prompt = """
+++StepByStep(numbered=true)
Explain quantum computing.
"""

transformed_prompt = apply_dynamic_decorators(prompt)
print("Original prompt:", prompt)
print("Transformed prompt:", transformed_prompt)
```

### Why am I getting a "Decorator not found" error?

This error occurs when you reference a decorator that isn't registered. Ensure:

1. You've imported the decorator correctly
2. The decorator name is spelled correctly (case-sensitive)
3. Any custom decorators are registered before use

### How do I fix JavaScript errors in transform functions?

If you're getting JavaScript errors in your transform functions:

1. Check the syntax of your JavaScript code
2. Ensure all variables used in the function are defined
3. Verify that the function returns a string
4. Test the function with different inputs

## Contributing and Support

### How can I contribute to the project?

You can contribute by:

1. Submitting bug reports and feature requests on GitHub
2. Creating pull requests with bug fixes or new features
3. Improving documentation
4. Creating and sharing custom decorators
5. Helping answer questions in the community

### Where can I get help?

- **Documentation**: [https://synaptiai.github.io/prompt-decorators/](https://synaptiai.github.io/prompt-decorators/)
- **GitHub Issues**: [https://github.com/synaptiai/prompt-decorators/issues](https://github.com/synaptiai/prompt-decorators/issues)
- **Discussions**: [https://github.com/synaptiai/prompt-decorators/discussions](https://github.com/synaptiai/prompt-decorators/discussions)

### Is there commercial support available?

For commercial support, please contact the maintainers through GitHub.

### How do I report a bug?

Report bugs on GitHub:

1. Go to [https://github.com/synaptiai/prompt-decorators/issues](https://github.com/synaptiai/prompt-decorators/issues)
2. Click "New Issue"
3. Select "Bug Report"
4. Fill in the template with details about the bug
5. Submit the issue

## Advanced Topics

### Can I use Prompt Decorators with streaming responses?

Yes, since the decorators are applied to the prompt before sending it to the LLM, streaming responses work normally.

### How do I handle versioning of decorators?

For versioning custom decorators:

1. Include version information in decorator names or descriptions
2. Use semantic versioning for your decorator packages
3. Document compatibility between versions

### Can I use Prompt Decorators in production?

Yes, the framework is designed for production use:

1. It's well-tested and has a comprehensive test suite
2. It follows best practices for security and performance
3. It's used in production by multiple organizations

### How do I optimize token usage?

To minimize token usage:

1. Use concise decorators that add minimal instructions
2. Combine related decorators into custom composite decorators
3. Use parameter defaults when possible
4. Consider creating specialized decorators for your specific needs

# Frequently Asked Questions (FAQ)

## General Questions

### What is Prompt Decorators?

Prompt Decorators is a Python framework that provides a structured way to enhance prompts for Large Language Models (LLMs). It allows you to apply various "decorators" to your prompts, each adding specific functionality or behavior, such as reasoning patterns, output formatting, or persona characteristics.

### Why should I use Prompt Decorators?

Prompt Decorators offers several benefits:

- **Modularity**: Apply specific prompt engineering techniques independently
- **Reusability**: Create a library of prompt techniques that can be reused across projects
- **Standardization**: Establish consistent prompt patterns across your organization
- **Experimentation**: Easily test different prompt engineering approaches
- **Compatibility**: Work with multiple LLM providers using the same decorator patterns

### Is Prompt Decorators free to use?

Yes, Prompt Decorators is open-source software released under the MIT License, which allows for free use, modification, and distribution.

### Which Python versions are supported?

Prompt Decorators supports Python 3.8 and higher.

### Does Prompt Decorators work with all LLM providers?

Yes, Prompt Decorators is designed to be provider-agnostic. You can use it with any LLM API, including OpenAI, Anthropic, Hugging Face, and others. The framework focuses on enhancing the prompts themselves, which can then be sent to any LLM provider.

## Technical Questions

### How do decorators work?

Decorators in this framework are Python classes that implement an `apply` method, which takes a prompt string as input and returns a modified prompt string as output. Each decorator adds specific enhancements to the prompt, such as reasoning instructions, output formatting requirements, or persona characteristics.

### Can I chain multiple decorators?

Yes, you can apply multiple decorators in sequence. The order of application matters, as each decorator modifies the prompt based on its current state. For example:

```python
from prompt_decorators.decorators import Reasoning, OutputFormat

reasoning = Reasoning(style="detailed")
output_format = OutputFormat(format_type="markdown")

prompt = "Explain quantum entanglement."
decorated_prompt = output_format.apply(reasoning.apply(prompt))
```

### Are there any limitations on the number of decorators I can use?

There's no hard limit on the number of decorators you can apply, but consider these practical limitations:

1. Each decorator adds to the prompt length, which may approach token limits of LLMs
2. Too many decorators might create conflicting instructions
3. Performance may degrade with a large number of decorators

### How do I create my own custom decorator?

To create a custom decorator, you need to:

1. Create a class that inherits from `BaseDecorator`
2. Implement the `apply`, `to_dict`, and `from_dict` methods
3. Register your decorator with the `DecoratorRegistry`

See the [Advanced Usage Guide](guide/advanced-usage.md) for a detailed example.

### Can I use Prompt Decorators with frameworks like LangChain?

Yes, Prompt Decorators can be integrated with LangChain and other LLM frameworks. You can apply decorators to prompts before passing them to LangChain components, or create custom LangChain prompt templates that incorporate Prompt Decorators. See the [API Integration Guide](guide/api-integration.md) for examples.

## Usage Questions

### How do I install Prompt Decorators?

You can install Prompt Decorators using pip:

```bash
pip install prompt-decorators
```

For development or to include optional dependencies:

```bash
pip install prompt-decorators[dev]  # Development dependencies
pip install prompt-decorators[cli]  # CLI dependencies
pip install prompt-decorators[all]  # All dependencies
```

### What's the difference between a decorator and a prompt template?

- **Prompt Templates** are static structures with placeholders for variables. They define the overall structure of a prompt.
- **Decorators** are dynamic modifiers that enhance prompts with specific behaviors or patterns. They can be applied to any prompt, including those generated from templates.

You can use both together: create a template for your base prompt structure, then apply decorators to enhance it with specific behaviors.

### How do I find available decorators?

You can list all available decorators using the registry:

```python
from prompt_decorators.registry import DecoratorRegistry

registry = DecoratorRegistry()
decorators = registry.get_all_decorators()
print(decorators)
```

Or using the CLI:

```bash
prompt-decorators list
```

### Can I use Prompt Decorators in production?

Yes, Prompt Decorators is designed for production use. It includes features like:

- Serialization/deserialization for storing and retrieving decorated prompts
- Compatibility checking to ensure decorators work well together
- Error handling and validation
- Performance optimizations like caching

### How do I contribute to Prompt Decorators?

Contributions are welcome! See the [Contributing Guide](contributing.md) for details on how to contribute to the project.

## Troubleshooting

### Why isn't my decorator modifying the prompt as expected?

Common reasons include:

1. Decorators are applied in the wrong order
2. The decorator parameters aren't set correctly
3. There might be compatibility issues between decorators
4. The LLM might not be following the decorated instructions

See the [Troubleshooting Guide](guide/troubleshooting.md) for more detailed help.

### How do I debug issues with decorators?

You can enable debug logging to see what's happening:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("prompt_decorators")
```

You can also print the decorated prompt before sending it to the LLM:

```python
decorated_prompt = decorator.apply(prompt)
print(decorated_prompt)
```

### Why am I getting a "Decorator not found" error?

This usually means the decorator isn't registered or the name is misspelled. Check:

1. That you're using the correct decorator name
2. That the decorator is properly registered
3. That you've installed any extensions that might contain the decorator

### Can decorators increase my API costs?

Decorators add text to your prompts, which increases the token count sent to the LLM API. This can increase costs, especially if you're using many decorators or complex ones. However, the improved quality and consistency of responses often outweighs the marginal cost increase.

## Advanced Questions

### How does versioning work for decorators?

Decorators support versioning to manage compatibility:

1. Each decorator can have a version number
2. The registry can track different versions of decorators
3. Compatibility checks can ensure decorators work together
4. You can specify version requirements when retrieving decorators

### Can I use Prompt Decorators with non-English languages?

Yes, Prompt Decorators works with any language supported by the underlying LLM. However, some decorators might be optimized for English and may need adaptation for other languages.

### Is there a way to measure the effectiveness of decorators?

You can implement evaluation metrics to compare the quality of responses with and without specific decorators. The framework doesn't include built-in evaluation tools, but you can:

1. Create A/B tests with different decorator combinations
2. Implement metrics like response quality, relevance, or accuracy
3. Use human evaluation to assess the impact of decorators

### How do I handle model-specific adaptations?

Some decorators might work differently with different LLMs. You can:

1. Create model-specific versions of decorators
2. Use conditional logic within decorators based on the target model
3. Implement middleware that adapts decorators for specific models

See the [Advanced Usage Guide](guide/advanced-usage.md) for examples.

## Next Steps

- Explore the [Basic Usage Guide](guide/basic-usage.md)
- Check out the [API Reference](api/index.md)
- See [Examples](examples/basic.md) of Prompt Decorators in action

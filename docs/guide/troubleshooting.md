# Troubleshooting

This guide provides solutions to common issues you might encounter when using the Prompt Decorators framework.

## Installation Issues

### Package Not Found

**Problem**: `pip install prompt-decorators` fails with "Package not found" error.

**Solution**:
- Verify that you're using the correct package name.
- Check your internet connection.
- Try using a different PyPI mirror: `pip install prompt-decorators --index-url https://pypi.org/simple/`
- If you're installing from a GitHub repository, ensure the repository URL is correct.

### Dependency Conflicts

**Problem**: Installation fails due to dependency conflicts.

**Solution**:
- Create a fresh virtual environment: `python -m venv venv` and activate it.
- Try installing with the `--no-dependencies` flag and then manually install dependencies: `pip install prompt-decorators --no-dependencies`
- Check if any of your existing packages conflict with the requirements of Prompt Decorators.

## Import Errors

### Module Not Found

**Problem**: `ImportError: No module named 'prompt_decorators'`

**Solution**:
- Verify that the package is installed: `pip list | grep prompt-decorators`
- Check that you're running Python from the correct environment where the package is installed.
- If using a Jupyter notebook, restart the kernel after installation.

### Cannot Import Name

**Problem**: `ImportError: cannot import name 'SomeDecorator' from 'prompt_decorators.decorators'`

**Solution**:
- Check that you're using the correct import path.
- Verify that the decorator exists in the version you have installed.
- Update to the latest version: `pip install --upgrade prompt-decorators`

## Decorator Registry Issues

### Decorator Not Found

**Problem**: `ValueError: Decorator 'SomeDecorator' not found in registry`

**Solution**:
- Check that the decorator name is spelled correctly.
- List available decorators: `from prompt_decorators.registry import DecoratorRegistry; print(DecoratorRegistry().get_all_decorators())`
- If it's a custom decorator, ensure it's properly registered.

### Custom Decorator Not Discovered

**Problem**: Custom decorators aren't being discovered by the registry.

**Solution**:
- Ensure your custom decorators follow the required structure.
- Check that the decorator class inherits from `BaseDecorator`.
- Verify that the decorator is in a location that's included in the discovery paths.
- Manually register the decorator: `registry.register(MyCustomDecorator)`

## Decorator Application Issues

### Unexpected Decorator Behavior

**Problem**: A decorator doesn't modify the prompt as expected.

**Solution**:
- Check the decorator parameters to ensure they're set correctly.
- Print the decorated prompt to see what's happening: `print(decorator.apply(prompt))`
- Verify that decorators are being applied in the correct order.
- Check if the decorator has any model-specific behavior that might be affecting its output.

### Decorator Compatibility Issues

**Problem**: Error message about incompatible decorators.

**Solution**:
- Check the compatibility requirements of each decorator.
- Use the compatibility checker: `from prompt_decorators.registry.compatibility import check_compatibility; check_compatibility(decorator1, decorator2)`
- Try changing the order of decorators.
- Consider using different decorators that serve similar purposes but are compatible.

## API Integration Issues

### API Authentication Errors

**Problem**: API calls fail with authentication errors.

**Solution**:
- Verify that your API key is correct and properly set.
- Check if the API key has the necessary permissions.
- Ensure the API key is being passed correctly in the request.

### Unexpected API Responses

**Problem**: The LLM API returns unexpected or error responses.

**Solution**:
- Check that the decorated prompt isn't exceeding the model's maximum token limit.
- Verify that the API parameters (temperature, max_tokens, etc.) are set appropriately.
- Ensure the prompt format is compatible with the specific LLM API you're using.
- Try with a simpler prompt to isolate the issue.

## CLI Issues

### Command Not Found

**Problem**: `prompt-decorators` command not found.

**Solution**:
- Ensure the package is installed with the CLI dependencies: `pip install prompt-decorators[cli]`
- Check that the installation directory is in your PATH.
- Try using `python -m prompt_decorators.cli` instead.

### CLI Parameter Errors

**Problem**: CLI commands fail with parameter errors.

**Solution**:
- Check the command syntax: `prompt-decorators --help`
- Ensure parameter values are properly quoted if they contain spaces.
- For decorator parameters, use the correct format: `--decorator "Reasoning:style=detailed,show_working=true"`

## Performance Issues

### Slow Decorator Application

**Problem**: Applying decorators is taking too long.

**Solution**:
- Reduce the number of decorators being applied.
- Check if any decorators are performing expensive operations.
- Consider using caching for frequently used decorator combinations.

### High Memory Usage

**Problem**: The application uses too much memory when applying decorators.

**Solution**:
- Limit the number of decorators used simultaneously.
- Check for memory leaks in custom decorators.
- Consider processing prompts in smaller batches.

## Serialization Issues

### JSON Serialization Errors

**Problem**: Errors when trying to serialize decorators to JSON.

**Solution**:
- Ensure all decorator attributes are JSON-serializable.
- Check for circular references in custom decorators.
- Use the built-in serialization methods: `decorator.to_dict()` and `DecoratedRequest.to_dict()`

### Deserialization Errors

**Problem**: Errors when trying to deserialize decorators from JSON.

**Solution**:
- Verify that the JSON structure matches what the decorator expects.
- Ensure all required fields are present in the JSON.
- Use the built-in deserialization methods: `Decorator.from_dict(data)` and `DecoratedRequest.from_dict(data)`

## Common Error Messages and Solutions

### "Decorator parameters validation failed"

**Problem**: The parameters provided to a decorator don't match its schema.

**Solution**:
- Check the decorator's documentation for the expected parameters.
- Verify the parameter types and values.
- Use the validator: `from prompt_decorators.registry.validation import validate_decorator_params; validate_decorator_params(decorator_class, params)`

### "Maximum recursion depth exceeded"

**Problem**: Infinite recursion when applying decorators.

**Solution**:
- Check for circular references in your decorator chain.
- Ensure that custom decorators don't call themselves recursively without a base case.
- Limit the depth of decorator nesting.

### "Incompatible decorator chain"

**Problem**: The chain of decorators contains incompatible decorators.

**Solution**:
- Check the compatibility matrix in the documentation.
- Use the compatibility checker before creating chains.
- Try different combinations or orders of decorators.

## Debugging Tips

### Enabling Debug Logging

To get more detailed information about what's happening:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("prompt_decorators")
```

### Inspecting Decorators

To inspect a decorator's structure and parameters:

```python
from pprint import pprint
decorator = Reasoning(style="detailed")
pprint(decorator.to_dict())
```

### Testing Decorator Application

To test how a decorator modifies a prompt:

```python
original_prompt = "Explain quantum mechanics."
decorated_prompt = decorator.apply(original_prompt)
print(f"Original: {original_prompt}")
print(f"Decorated: {decorated_prompt}")
```

## Getting Help

If you're still experiencing issues:

1. Check the [GitHub Issues](https://github.com/yourusername/prompt-decorators/issues) to see if others have encountered the same problem.
2. Search the [Discussions](https://github.com/yourusername/prompt-decorators/discussions) for related topics.
3. Create a new issue with:
   - A clear description of the problem
   - Steps to reproduce
   - Expected vs. actual behavior
   - Your environment details (Python version, OS, package version)
   - Any relevant error messages or logs

## Next Steps

- Return to the [Basic Usage Guide](./basic-usage.md)
- Explore the [API Reference](../api/index.md)
- Check out [Advanced Examples](../examples/advanced.md)

# Advanced Usage

This guide covers advanced usage patterns for the Prompt Decorators framework.

## Creating Custom Decorators

You can create custom decorators by inheriting from the `BaseDecorator` class:

```python
from prompt_decorators.core.base import BaseDecorator
from typing import Dict, Any, Optional

class CustomDecorator(BaseDecorator):
    """A custom decorator that adds specific instructions to a prompt."""

    def __init__(
        self,
        instructions: str,
        priority: int = 1,
        version: str = "1.0.0"
    ):
        """Initialize the custom decorator.

        Args:
            instructions: The instructions to add to the prompt.
            priority: The priority of the decorator (higher values are applied later).
            version: The semantic version of the decorator.
        """
        super().__init__(version=version)
        self.instructions = instructions
        self.priority = priority

    def apply(self, prompt: str) -> str:
        """Apply the decorator to the prompt.

        Args:
            prompt: The prompt to decorate.

        Returns:
            The decorated prompt.
        """
        return f"{prompt}\n\nAdditional instructions: {self.instructions}"

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            A dictionary representation of the decorator.
        """
        return {
            "type": self.__class__.__name__,
            "version": self.version,
            "parameters": {
                "instructions": self.instructions,
                "priority": self.priority
            }
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CustomDecorator":
        """Create a decorator from a dictionary.

        Args:
            data: The dictionary representation of the decorator.

        Returns:
            A new decorator instance.
        """
        return cls(
            instructions=data["parameters"]["instructions"],
            priority=data["parameters"].get("priority", 1),
            version=data["version"]
        )
```

## Registering Custom Decorators

You can register your custom decorators with the registry:

```python
from prompt_decorators.utils.discovery import DecoratorRegistry

# Get the registry instance
registry = DecoratorRegistry()

# Register your custom decorator
registry.register_decorator(CustomDecorator)

# Now you can get it by name
custom_decorator_class = registry.get_decorator("CustomDecorator")
```

## Working with Decorator Chains

You can create chains of decorators to apply multiple decorators in a specific order:

```python
from prompt_decorators.decorators.generated.decorators.chain import Chain
from prompt_decorators.decorators import Reasoning, OutputFormat, Concise

# Create individual decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)
concise = Concise(maxWords=200, bulletPoints=False)

# Create a chain of decorators
chain = Chain(
    decorators=[reasoning, concise, output_format],
    name="DetailedConciseMarkdown"
)

# Apply the chain to a prompt
prompt = "Explain quantum mechanics."
decorated_prompt = chain.apply(prompt)

print(decorated_prompt)
```

## Conditional Decorators

You can use conditional decorators to apply different decorators based on conditions:

```python
from prompt_decorators.decorators.generated.decorators.conditional import Conditional
from prompt_decorators.decorators import Detailed, Concise

# Create individual decorators
detailed = Detailed(depth=3, examples=True)
concise = Concise(maxWords=100, bulletPoints=True)

# Create a conditional decorator
def is_complex_topic(prompt: str) -> bool:
    complex_topics = ["quantum", "relativity", "philosophy", "consciousness"]
    return any(topic in prompt.lower() for topic in complex_topics)

conditional = Conditional(
    condition_func=is_complex_topic,
    true_decorator=detailed,
    false_decorator=concise,
    description="Use detailed for complex topics, concise for simple ones"
)

# Apply to different prompts
complex_prompt = "Explain quantum entanglement."
simple_prompt = "List the primary colors."

complex_result = conditional.apply(complex_prompt)  # Will use detailed
simple_result = conditional.apply(simple_prompt)    # Will use concise

print(f"Complex result: {complex_result[:100]}...")
print(f"Simple result: {simple_result[:100]}...")
```

## Model-Specific Adaptations

You can adapt decorators for specific LLM models:

```python
from prompt_decorators.core.model_specific import adapt_for_model
from prompt_decorators.decorators import Reasoning

# Create a decorator
reasoning = Reasoning(style="detailed", show_working=True)

# Adapt it for a specific model
gpt4_reasoning = adapt_for_model(reasoning, "gpt-4")
claude_reasoning = adapt_for_model(reasoning, "claude-2")

# Apply to a prompt
prompt = "Explain quantum entanglement."
gpt4_prompt = gpt4_reasoning.apply(prompt)
claude_prompt = claude_reasoning.apply(prompt)

print(f"GPT-4 prompt: {gpt4_prompt[:100]}...")
print(f"Claude prompt: {claude_prompt[:100]}...")
```

## Versioning and Compatibility

You can work with different versions of decorators and check compatibility:

```python
from prompt_decorators.utils.compatibility import get_compatibility_checker
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create decorators with specific versions
reasoning_v1 = Reasoning(style="detailed", show_working=True, version="1.0.0")
reasoning_v2 = Reasoning(style="detailed", show_working=True, version="2.0.0")
output_format = OutputFormat(format_type="markdown", pretty_print=True, version="1.5.0")

# Get the compatibility checker
checker = get_compatibility_checker()

# Check compatibility
issues_v1 = checker.check_compatibility(reasoning_v1, output_format)
issues_v2 = checker.check_compatibility(reasoning_v2, output_format)

print(f"Compatibility issues v1: {issues_v1}")
print(f"Compatibility issues v2: {issues_v2}")
```

## Serialization and Deserialization

You can serialize decorators to JSON and deserialize them:

```python
import json
from prompt_decorators.decorators import Reasoning
from prompt_decorators.core.base import BaseDecorator

# Create a decorator
reasoning = Reasoning(style="detailed", show_working=True)

# Serialize to dictionary
reasoning_dict = reasoning.to_dict()

# Serialize to JSON
reasoning_json = json.dumps(reasoning_dict, indent=2)
print(reasoning_json)

# Deserialize from dictionary
deserialized_reasoning = BaseDecorator.from_dict(reasoning_dict)
print(type(deserialized_reasoning))
```

## Working with Decorator Plugins

You can extend the framework with plugins:

```python
from prompt_decorators.utils.plugins import load_plugin, register_plugin

# Define a plugin
class MyPlugin:
    def __init__(self, name):
        self.name = name

    def process(self, prompt):
        return f"[Processed by {self.name}] {prompt}"

# Register the plugin
register_plugin("my_plugin", MyPlugin("CustomProcessor"))

# Use the plugin
plugin = load_plugin("my_plugin")
processed_prompt = plugin.process("Explain quantum entanglement.")
print(processed_prompt)
```

<a id="compliance"></a>
## Compliance and Regulatory Considerations

When using prompt decorators in regulated industries, you may need to consider compliance requirements:

```python
from prompt_decorators.decorators import CiteSources, FactCheck, Limitations
from prompt_decorators.decorators.generated.decorators.chain import Chain

# Create compliance-focused decorators
cite_sources = CiteSources(required=True, format="apa")
fact_check = FactCheck(level="rigorous", highlight_uncertainties=True)
limitations = Limitations(scope="comprehensive", include_alternatives=True)

# Create a compliance chain
compliance_chain = Chain(
    decorators=[cite_sources, fact_check, limitations],
    name="ComplianceChain"
)

# Apply to a prompt in a healthcare context
medical_prompt = "Explain the latest treatments for type 2 diabetes."
compliant_prompt = compliance_chain.apply(medical_prompt)

print(compliant_prompt)
```

### Healthcare Compliance

For healthcare applications, consider:

1. **HIPAA Compliance**: Ensure no PHI (Protected Health Information) is included in prompts
2. **Medical Accuracy**: Use fact-checking decorators to verify medical information
3. **Disclaimers**: Add appropriate medical disclaimers using the `Limitations` decorator
4. **Source Citation**: Always cite medical sources using the `CiteSources` decorator
5. **Audit Trails**: Maintain records of all prompts and responses for compliance auditing

### Financial Services Compliance

For financial applications, consider:

1. **Regulatory Disclosures**: Include required disclosures using custom decorators
2. **Investment Advice**: Clearly mark limitations when discussing investments
3. **Risk Statements**: Include appropriate risk statements
4. **Factual Accuracy**: Verify financial information with fact-checking decorators

## Next Steps

- Learn about [API Integration](api-integration.md)
- Explore the [API Reference](../api/index.md)
- Check out [Advanced Examples](../examples/advanced.md)

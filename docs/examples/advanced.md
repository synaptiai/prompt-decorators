# Advanced Examples

This page provides advanced examples of using the Prompt Decorators framework for more complex scenarios.

## Custom Decorator Implementation

This example shows how to create a custom decorator that implements a specific prompt engineering technique:

```python
from typing import Dict, Any, Optional
from prompt_decorators.core.base import BaseDecorator

class FewShotDecorator(BaseDecorator):
    """A decorator that adds few-shot examples to a prompt."""

    def __init__(
        self,
        examples: list[Dict[str, str]],
        example_format: str = "{input} -> {output}",
        separator: str = "\n\n",
        intro_text: Optional[str] = "Here are some examples:"
    ):
        """Initialize the FewShotDecorator.

        Args:
            examples: List of dictionaries containing input/output pairs
            example_format: Format string for each example
            separator: Separator between examples
            intro_text: Text to introduce the examples
        """
        self.examples = examples
        self.example_format = example_format
        self.separator = separator
        self.intro_text = intro_text

    def apply(self, prompt: str) -> str:
        """Apply the few-shot decorator to the prompt.

        Args:
            prompt: The original prompt

        Returns:
            The prompt with few-shot examples added
        """
        # Format each example
        formatted_examples = [
            self.example_format.format(**example)
            for example in self.examples
        ]

        # Join examples with separator
        examples_text = self.separator.join(formatted_examples)

        # Construct the full prompt
        if self.intro_text:
            full_prompt = f"{prompt}\n\n{self.intro_text}\n\n{examples_text}\n\nNow your turn:"
        else:
            full_prompt = f"{prompt}\n\n{examples_text}\n\nNow your turn:"

        return full_prompt

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "type": "FewShotDecorator",
            "examples": self.examples,
            "example_format": self.example_format,
            "separator": self.separator,
            "intro_text": self.intro_text
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FewShotDecorator':
        """Create a decorator from a dictionary.

        Args:
            data: Dictionary representation of the decorator

        Returns:
            A new FewShotDecorator instance
        """
        return cls(
            examples=data.get("examples", []),
            example_format=data.get("example_format", "{input} -> {output}"),
            separator=data.get("separator", "\n\n"),
            intro_text=data.get("intro_text")
        )

# Example usage
examples = [
    {"input": "Classify this review: 'This movie was fantastic!'", "output": "Positive"},
    {"input": "Classify this review: 'Terrible service and food.'", "output": "Negative"},
    {"input": "Classify this review: 'The experience was okay.'", "output": "Neutral"}
]

few_shot = FewShotDecorator(examples=examples)
prompt = "Classify this review: 'I really enjoyed the concert but the venue was too small.'"
decorated_prompt = few_shot.apply(prompt)

print(decorated_prompt)
```

## Conditional Decorator Chain

This example demonstrates how to create a conditional chain of decorators based on the content of the prompt:

```python
from prompt_decorators.decorators import Reasoning, OutputFormat, Persona
from prompt_decorators.core.request import DecoratedRequest
import re

def create_conditional_chain(prompt: str) -> DecoratedRequest:
    """Create a conditional chain of decorators based on prompt content.

    Args:
        prompt: The user's prompt

    Returns:
        A DecoratedRequest with appropriate decorators
    """
    decorators = []

    # Add a persona decorator based on topic
    if re.search(r'math|equation|calculus|algebra', prompt, re.IGNORECASE):
        decorators.append(Persona(
            role="mathematician",
            background="PhD in Mathematics with expertise in various mathematical fields",
            tone="educational"
        ))
    elif re.search(r'physics|quantum|relativity|mechanics', prompt, re.IGNORECASE):
        decorators.append(Persona(
            role="physicist",
            background="Theoretical physicist with expertise in quantum mechanics and relativity",
            tone="educational"
        ))
    elif re.search(r'code|program|function|algorithm', prompt, re.IGNORECASE):
        decorators.append(Persona(
            role="software engineer",
            background="Senior software engineer with 15 years of experience",
            tone="technical"
        ))

    # Add reasoning for complex questions
    if len(prompt.split()) > 15 or '?' in prompt or re.search(r'explain|how|why', prompt, re.IGNORECASE):
        decorators.append(Reasoning(style="detailed", show_working=True))

    # Add output format based on content
    if re.search(r'code|program|function', prompt, re.IGNORECASE):
        decorators.append(OutputFormat(format_type="code"))
    elif re.search(r'list|steps|bullet', prompt, re.IGNORECASE):
        decorators.append(OutputFormat(format_type="markdown", pretty_print=True))
    elif re.search(r'json|api|data', prompt, re.IGNORECASE):
        decorators.append(OutputFormat(format_type="json"))
    else:
        decorators.append(OutputFormat(format_type="markdown", pretty_print=True))

    # Create and return the decorated request
    return DecoratedRequest(
        prompt=prompt,
        decorators=decorators,
        model="gpt-4",
        api_params={"temperature": 0.7, "max_tokens": 1000}
    )

# Example usage
prompt1 = "Explain the quadratic formula and its applications in algebra."
request1 = create_conditional_chain(prompt1)
print(f"Prompt: {prompt1}")
print(f"Decorators: {[d.__class__.__name__ for d in request1.decorators]}")
print(f"Decorated prompt: {request1.apply_decorators()[:100]}...\n")

prompt2 = "Write a Python function to find the nth Fibonacci number using recursion."
request2 = create_conditional_chain(prompt2)
print(f"Prompt: {prompt2}")
print(f"Decorators: {[d.__class__.__name__ for d in request2.decorators]}")
print(f"Decorated prompt: {request2.apply_decorators()[:100]}...\n")
```

## Dynamic Decorator Registry

This example shows how to dynamically discover, load, and apply decorators from a custom registry:

```python
import os
import json
from typing import Dict, List, Any, Optional
from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.registry.discovery import discover_decorators
from prompt_decorators.registry.registry import DecoratorRegistry

class DynamicDecoratorManager:
    """A manager for dynamically discovering and applying decorators."""

    def __init__(self, registry_paths: List[str]):
        """Initialize the manager with paths to decorator registries.

        Args:
            registry_paths: List of paths to search for decorators
        """
        self.registry = DecoratorRegistry()
        self.registry_paths = registry_paths
        self.load_decorators()

    def load_decorators(self) -> None:
        """Discover and load decorators from registry paths."""
        for path in self.registry_paths:
            if os.path.exists(path):
                decorators = discover_decorators(path)
                for decorator_class in decorators:
                    self.registry.register(decorator_class)

    def get_decorators_by_category(self, category: str) -> List[str]:
        """Get decorator names by category.

        Args:
            category: Category to filter by

        Returns:
            List of decorator names in the category
        """
        return [
            name for name, info in self.registry.get_all_decorators().items()
            if info.get("category") == category
        ]

    def create_decorator(self, name: str, params: Optional[Dict[str, Any]] = None) -> BaseDecorator:
        """Create a decorator instance by name.

        Args:
            name: Name of the decorator
            params: Parameters for the decorator

        Returns:
            An instance of the decorator

        Raises:
            ValueError: If decorator not found
        """
        if params is None:
            params = {}

        decorator_class = self.registry.get_decorator_class(name)
        if decorator_class is None:
            raise ValueError(f"Decorator '{name}' not found in registry")

        return decorator_class(**params)

    def apply_decorators_from_config(self, prompt: str, config_file: str) -> str:
        """Apply decorators based on a configuration file.

        Args:
            prompt: The original prompt
            config_file: Path to a JSON configuration file

        Returns:
            The decorated prompt

        Raises:
            FileNotFoundError: If config file not found
        """
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Config file '{config_file}' not found")

        with open(config_file, 'r') as f:
            config = json.load(f)

        decorated_prompt = prompt
        for decorator_config in config.get("decorators", []):
            name = decorator_config.get("name")
            params = decorator_config.get("params", {})

            decorator = self.create_decorator(name, params)
            decorated_prompt = decorator.apply(decorated_prompt)

        return decorated_prompt

# Example usage
manager = DynamicDecoratorManager([
    "./decorators",
    "~/.prompt-decorators/custom"
])

# List decorators by category
reasoning_decorators = manager.get_decorators_by_category("reasoning")
print(f"Reasoning decorators: {reasoning_decorators}\n")

# Create and apply a decorator
reasoning = manager.create_decorator("Reasoning", {"style": "detailed", "show_working": True})
prompt = "Explain the concept of recursion in programming."
decorated_prompt = reasoning.apply(prompt)
print(f"Decorated prompt: {decorated_prompt[:100]}...\n")

# Apply decorators from a config file
config_content = {
    "decorators": [
        {"name": "Persona", "params": {"role": "teacher", "tone": "educational"}},
        {"name": "Reasoning", "params": {"style": "step_by_step"}},
        {"name": "OutputFormat", "params": {"format_type": "markdown"}}
    ]
}

with open("decorator_config.json", "w") as f:
    json.dump(config_content, f)

decorated_prompt = manager.apply_decorators_from_config(
    "Explain how photosynthesis works.",
    "decorator_config.json"
)
print(f"Decorated prompt from config: {decorated_prompt[:100]}...")
```

## Decorator Composition with Middleware

This example demonstrates how to implement a middleware pattern for decorator composition:

```python
from typing import Callable, List, Dict, Any
from prompt_decorators.core.base import BaseDecorator

class DecoratorMiddleware:
    """Middleware for intercepting and modifying decorator behavior."""

    def __init__(self, pre_hooks: List[Callable] = None, post_hooks: List[Callable] = None):
        """Initialize the middleware.

        Args:
            pre_hooks: Functions to call before decorator application
            post_hooks: Functions to call after decorator application
        """
        self.pre_hooks = pre_hooks or []
        self.post_hooks = post_hooks or []

    def apply(self, decorator: BaseDecorator, prompt: str) -> str:
        """Apply the middleware and decorator to a prompt.

        Args:
            decorator: The decorator to apply
            prompt: The original prompt

        Returns:
            The decorated prompt after middleware processing
        """
        # Apply pre-hooks
        modified_prompt = prompt
        for hook in self.pre_hooks:
            modified_prompt = hook(decorator, modified_prompt)

        # Apply the decorator
        decorated_prompt = decorator.apply(modified_prompt)

        # Apply post-hooks
        for hook in self.post_hooks:
            decorated_prompt = hook(decorator, decorated_prompt)

        return decorated_prompt

# Example hooks
def log_decorator_application(decorator: BaseDecorator, prompt: str) -> str:
    """Log decorator application."""
    print(f"Applying {decorator.__class__.__name__} to prompt: {prompt[:30]}...")
    return prompt

def validate_prompt_length(decorator: BaseDecorator, prompt: str) -> str:
    """Validate prompt length and truncate if necessary."""
    max_length = 1000
    if len(prompt) > max_length:
        print(f"Warning: Prompt exceeds {max_length} characters. Truncating...")
        return prompt[:max_length] + "..."
    return prompt

def add_decorator_metadata(decorator: BaseDecorator, prompt: str) -> str:
    """Add metadata about the applied decorator."""
    metadata = f"\n\n[Processed with {decorator.__class__.__name__}]"
    return prompt + metadata

# Example usage
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create middleware
middleware = DecoratorMiddleware(
    pre_hooks=[log_decorator_application, validate_prompt_length],
    post_hooks=[add_decorator_metadata]
)

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators with middleware
prompt = "Explain the concept of neural networks in artificial intelligence."
decorated_prompt = middleware.apply(reasoning, prompt)
decorated_prompt = middleware.apply(output_format, decorated_prompt)

print("\nFinal decorated prompt:")
print(decorated_prompt)
```

## Decorator Versioning and Compatibility

This example shows how to implement versioning and compatibility checks for decorators:

```python
from typing import Dict, Any, List, Optional, Set, Tuple
from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.registry.compatibility import check_compatibility
import semver

class VersionedDecorator(BaseDecorator):
    """A decorator with versioning support."""

    def __init__(self, version: str = "1.0.0", **kwargs):
        """Initialize the versioned decorator.

        Args:
            version: Semantic version of the decorator
            **kwargs: Additional parameters for the decorator
        """
        self.version = version
        self.params = kwargs

    def apply(self, prompt: str) -> str:
        """Apply the decorator to the prompt.

        Args:
            prompt: The original prompt

        Returns:
            The decorated prompt
        """
        # Implementation would depend on the specific decorator
        return prompt

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "type": self.__class__.__name__,
            "version": self.version,
            **self.params
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'VersionedDecorator':
        """Create a decorator from a dictionary.

        Args:
            data: Dictionary representation of the decorator

        Returns:
            A new VersionedDecorator instance
        """
        version = data.pop("version", "1.0.0")
        return cls(version=version, **data)

    def is_compatible_with(self, other: 'VersionedDecorator') -> Tuple[bool, Optional[str]]:
        """Check if this decorator is compatible with another.

        Args:
            other: Another decorator to check compatibility with

        Returns:
            Tuple of (is_compatible, reason)
        """
        # Check if decorators are of the same type
        if self.__class__.__name__ != other.__class__.__name__:
            return True, None  # Different types are assumed compatible

        # Check version compatibility
        try:
            this_version = semver.VersionInfo.parse(self.version)
            other_version = semver.VersionInfo.parse(other.version)

            # Major version must match for compatibility
            if this_version.major != other_version.major:
                return False, f"Major version mismatch: {self.version} vs {other.version}"

            return True, None
        except ValueError:
            return False, "Invalid version format"

class DecoratorChain:
    """A chain of versioned decorators with compatibility checking."""

    def __init__(self, decorators: Optional[List[VersionedDecorator]] = None):
        """Initialize the decorator chain.

        Args:
            decorators: List of decorators to chain
        """
        self.decorators = decorators or []

    def add_decorator(self, decorator: VersionedDecorator) -> Tuple[bool, Optional[str]]:
        """Add a decorator to the chain if compatible.

        Args:
            decorator: Decorator to add

        Returns:
            Tuple of (success, error_message)
        """
        # Check compatibility with existing decorators
        for existing in self.decorators:
            is_compatible, reason = existing.is_compatible_with(decorator)
            if not is_compatible:
                return False, f"Incompatible with {existing.__class__.__name__}: {reason}"

        # Add the decorator if compatible
        self.decorators.append(decorator)
        return True, None

    def apply(self, prompt: str) -> str:
        """Apply all decorators in the chain.

        Args:
            prompt: The original prompt

        Returns:
            The decorated prompt
        """
        decorated_prompt = prompt
        for decorator in self.decorators:
            decorated_prompt = decorator.apply(decorated_prompt)
        return decorated_prompt

    def to_dict(self) -> Dict[str, Any]:
        """Convert the chain to a dictionary.

        Returns:
            Dictionary representation of the chain
        """
        return {
            "decorators": [d.to_dict() for d in self.decorators]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DecoratorChain':
        """Create a chain from a dictionary.

        Args:
            data: Dictionary representation of the chain

        Returns:
            A new DecoratorChain instance
        """
        chain = cls()
        for decorator_data in data.get("decorators", []):
            decorator_type = decorator_data.pop("type", None)
            if decorator_type:
                # In a real implementation, you would look up the decorator class
                # based on the type name
                decorator = VersionedDecorator.from_dict(decorator_data)
                chain.add_decorator(decorator)
        return chain

# Example usage
class ReasoningV1(VersionedDecorator):
    def apply(self, prompt: str) -> str:
        return f"{prompt}\n\nLet me think through this step by step..."

class ReasoningV2(VersionedDecorator):
    def apply(self, prompt: str) -> str:
        return f"{prompt}\n\nI'll analyze this systematically:\n1. First, I'll understand the problem\n2. Then, I'll develop a solution approach\n3. Finally, I'll implement and verify the solution"

# Create a chain
chain = DecoratorChain()

# Add compatible decorators
reasoning_v1 = ReasoningV1(version="1.0.0", style="basic")
success, error = chain.add_decorator(reasoning_v1)
print(f"Adding ReasoningV1: {'Success' if success else f'Failed - {error}'}")

# Try to add an incompatible decorator
reasoning_v2 = ReasoningV2(version="2.0.0", style="advanced")
success, error = chain.add_decorator(reasoning_v2)
print(f"Adding ReasoningV2: {'Success' if success else f'Failed - {error}'}")

# Apply the chain
prompt = "Explain the concept of blockchain."
decorated_prompt = chain.apply(prompt)
print(f"\nDecorated prompt: {decorated_prompt}")
```

## Next Steps

- Explore the [API Reference](../api/index.md)
- Learn about [API Integration](../guide/api-integration.md)
- Check out [Provider Examples](../examples/providers.md)

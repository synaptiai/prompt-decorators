# Creating Your First Custom Decorator

This tutorial walks you through the process of creating a custom decorator for the Prompt Decorators framework, from concept to implementation and testing.

## Prerequisites

Before starting, make sure you have:
- The Prompt Decorators framework installed
- Basic understanding of Python classes and inheritance
- Familiarity with the basic concepts of the framework

## Step 1: Plan Your Decorator

Every good decorator begins with a clear purpose. Let's design a `PoliteDecorator` that makes LLM responses more polite and courteous.

Our decorator will have the following parameters:
- `politeness_level`: An integer from 1-3 determining how polite the response should be
- `use_honorifics`: A boolean indicating whether to use formal honorifics
- `culture`: An optional string specifying cultural norms to follow (e.g., "Japanese", "British")

## Step 2: Create the Decorator Class

Create a new file named `polite_decorator.py` in your project:

```python
from prompt_decorators.core import BaseDecorator
from typing import Optional, Dict, Any, List
from enum import Enum


class PolitenessLevel(Enum):
    COURTEOUS = 1
    VERY_POLITE = 2
    EXTREMELY_FORMAL = 3


class PoliteDecorator(BaseDecorator):
    """
    A decorator that makes responses more polite and courteous.

    This decorator adds instructions to generate responses with appropriate
    levels of politeness, optionally using honorifics and following
    specific cultural norms of courtesy.
    """

    name = "Polite"
    version = "1.0.0"
    category = "tone"

    def __init__(
        self,
        politeness_level: int = 1,
        use_honorifics: bool = False,
        culture: Optional[str] = None
    ):
        """
        Initialize the polite decorator.

        Args:
            politeness_level: Level of politeness (1-3), higher means more formal
            use_honorifics: Whether to use formal honorifics in the response
            culture: Optional cultural context for politeness norms
        """
        super().__init__()
        # Validate and assign parameters
        self.politeness_level = max(1, min(3, politeness_level))  # Clamp between 1-3
        self.use_honorifics = use_honorifics
        self.culture = culture

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.

        This method adds instructions for politeness to the prompt.

        Args:
            prompt: The prompt to decorate

        Returns:
            The decorated prompt with politeness instructions
        """
        # Create the politeness instruction based on level
        if self.politeness_level == 1:
            instruction = "Please respond in a courteous and polite manner."
        elif self.politeness_level == 2:
            instruction = "Please respond in a very polite and respectful manner."
        else:  # level == 3
            instruction = "Please respond with extreme formality and the utmost courtesy."

        # Add honorific instruction if requested
        if self.use_honorifics:
            instruction += " Use appropriate honorifics and formal address."

        # Add cultural context if specified
        if self.culture:
            instruction += f" Follow the politeness norms typical in {self.culture} culture."

        # Return the decorated prompt
        return f"{instruction}\n\n{prompt}"
```

## Step 3: Register Your Decorator

To make your decorator available through the registry system, you need to register it:

```python
from prompt_decorators.utils import get_registry

# Get the registry instance
registry = get_registry()

# Register your decorator
registry.register_decorator(PoliteDecorator)
```

You can add this code to your application's initialization, or create a separate script to handle registration.

## Step 4: Create JSON Definition (Optional)

For better integration with the framework, you can create a JSON definition for your decorator:

```json
{
  "name": "Polite",
  "description": "A decorator that makes responses more polite and courteous",
  "version": "1.0.0",
  "category": "tone",
  "parameters": [
    {
      "name": "politeness_level",
      "type": "integer",
      "description": "Level of politeness (1-3), higher means more formal",
      "required": false,
      "default": 1,
      "constraints": {
        "minimum": 1,
        "maximum": 3
      }
    },
    {
      "name": "use_honorifics",
      "type": "boolean",
      "description": "Whether to use formal honorifics in the response",
      "required": false,
      "default": false
    },
    {
      "name": "culture",
      "type": "string",
      "description": "Optional cultural context for politeness norms",
      "required": false,
      "default": null
    }
  ],
  "examples": [
    {
      "name": "Basic politeness",
      "parameters": {
        "politeness_level": 1
      },
      "input": "Tell me about climate change.",
      "output": "Please respond in a courteous and polite manner.\n\nTell me about climate change."
    },
    {
      "name": "Formal Japanese style",
      "parameters": {
        "politeness_level": 3,
        "use_honorifics": true,
        "culture": "Japanese"
      },
      "input": "Explain the concept of artificial intelligence.",
      "output": "Please respond with extreme formality and the utmost courtesy. Use appropriate honorifics and formal address. Follow the politeness norms typical in Japanese culture.\n\nExplain the concept of artificial intelligence."
    }
  ],
  "compatibility": {
    "incompatible_with": ["Informal", "Sarcastic"],
    "caution_with": ["Technical", "Academic"]
  },
  "author": "Your Name",
  "contact": "your.email@example.com"
}
```

Save this as `polite.json` in your registry directory.

## Step 5: Add Model-Specific Behavior (Advanced)

For more advanced usage, you can create a model-specific version of your decorator:

```python
from prompt_decorators.core import ModelSpecificDecorator

class ModelSpecificPoliteDecorator(ModelSpecificDecorator):
    """
    A model-specific version of the polite decorator.

    This decorator adapts the politeness instructions based on the model's
    capabilities and characteristics.
    """

    name = "PoliteModelSpecific"
    version = "1.0.0"

    def __init__(
        self,
        model_id: str,
        politeness_level: int = 1,
        use_honorifics: bool = False,
        culture: Optional[str] = None
    ):
        """Initialize with model ID and parameters."""
        super().__init__(model_id)
        self.politeness_level = max(1, min(3, politeness_level))
        self.use_honorifics = use_honorifics
        self.culture = culture

    def apply_for_model(self, prompt: str) -> str:
        """Apply model-specific politeness instructions."""
        # Adapt based on model capabilities
        if self.model_capabilities.supports_feature("tone_control"):
            # Advanced models can handle nuanced tone instructions
            if self.politeness_level == 1:
                instruction = "Please respond in a courteous and polite manner."
            elif self.politeness_level == 2:
                instruction = "Please respond in a very polite and respectful manner."
            else:  # level == 3
                instruction = "Please respond with extreme formality and the utmost courtesy."

            if self.use_honorifics:
                instruction += " Use appropriate honorifics and formal address."

            if self.culture:
                instruction += f" Follow the politeness norms typical in {self.culture} culture."
        else:
            # For simpler models, use a more basic instruction
            instruction = "Please be polite and respectful in your response."

        return f"{instruction}\n\n{prompt}"

    def apply_fallback(self, prompt: str) -> str:
        """Fallback for unknown models."""
        return f"Please be polite in your response.\n\n{prompt}"
```

## Step 6: Test Your Decorator

Create a simple test script to verify your decorator works as expected:

```python
#!/usr/bin/env python
"""
Test script for the PoliteDecorator.
"""

import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from polite_decorator import PoliteDecorator

def main():
    """Test the PoliteDecorator with different parameters."""
    # Create a sample prompt
    prompt = "Explain the concept of quantum computing."
    print(f"Original prompt: \"{prompt}\"\n")

    # Test with basic politeness
    basic = PoliteDecorator()
    decorated_prompt = basic.apply(prompt)
    print("Basic politeness:")
    print(f"\"{decorated_prompt}\"\n")

    # Test with higher politeness level
    formal = PoliteDecorator(politeness_level=3, use_honorifics=True)
    decorated_prompt = formal.apply(prompt)
    print("Formal with honorifics:")
    print(f"\"{decorated_prompt}\"\n")

    # Test with cultural context
    cultural = PoliteDecorator(politeness_level=2, culture="British")
    decorated_prompt = cultural.apply(prompt)
    print("British politeness:")
    print(f"\"{decorated_prompt}\"\n")

if __name__ == "__main__":
    main()
```

Save this as `test_polite_decorator.py` and run it to see your decorator in action.

## Step 7: Document Your Decorator

Good documentation is crucial for others (and your future self) to understand your decorator. Create a documentation file `docs/api/decorators/Polite.md`:

```markdown
# Polite Decorator

A decorator that makes responses more polite and courteous.

## Description

The `Polite` decorator adds instructions to generate responses with appropriate levels of politeness, optionally using honorifics and following specific cultural norms of courtesy.

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| politeness_level | int | No | 1 | Level of politeness (1-3), higher means more formal |
| use_honorifics | bool | No | False | Whether to use formal honorifics in the response |
| culture | str | No | None | Optional cultural context for politeness norms |

## Examples

### Basic Politeness

```python
from prompt_decorators.decorators import Polite

decorator = Polite(politeness_level=1)
prompt = "Tell me about climate change."
decorated_prompt = decorator.apply(prompt)
```

**Result:**
```
Please respond in a courteous and polite manner.

Tell me about climate change.
```

### Formal Japanese Style

```python
from prompt_decorators.decorators import Polite

decorator = Polite(
    politeness_level=3,
    use_honorifics=True,
    culture="Japanese"
)
prompt = "Explain the concept of artificial intelligence."
decorated_prompt = decorator.apply(prompt)
```

**Result:**
```
Please respond with extreme formality and the utmost courtesy. Use appropriate honorifics and formal address. Follow the politeness norms typical in Japanese culture.

Explain the concept of artificial intelligence.
```

## Compatibility

- **Incompatible with**: Informal, Sarcastic
- **Use with caution**: Technical, Academic

## See Also

- [Professional Decorator](Professional.md)
- [Formal Decorator](Formal.md)
- [Audience Decorator](Audience.md)
```

## Conclusion

Congratulations! You've created a custom decorator for the Prompt Decorators framework. Your decorator can now be used standalone, registered with the decorator registry, or defined in JSON for dynamic loading.

To further enhance your decorator:

1. Add more parameters for finer control
2. Create unit tests for comprehensive testing
3. Add type hints and thorough docstrings
4. Consider edge cases and parameter validation
5. Define compatibility with other decorators

The Prompt Decorators framework makes it easy to create and share custom decorators that enhance LLM interactions in specific ways, allowing for more controlled and consistent prompting across applications.

# Tutorial: Developing Extensions for Prompt Decorators

This tutorial will guide you through the process of developing extensions for the Prompt Decorators framework. By the end, you'll understand how to create custom decorators, extend the registry, and contribute your extensions to the community.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Types of Extensions](#types-of-extensions)
- [Creating a Custom Decorator](#creating-a-custom-decorator)
- [Registry Integration](#registry-integration)
- [Testing Your Extension](#testing-your-extension)
- [Extension Distribution](#extension-distribution)
- [Advanced Extension Techniques](#advanced-extension-techniques)
- [Creating Domain-Specific Extensions](#creating-domain-specific-extensions)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before starting this tutorial, ensure you have:

1. Installed the Prompt Decorators framework:
   ```bash
   pip install prompt-decorators
   ```

2. Basic understanding of:
   - Python decorators
   - The Prompt Decorators core concepts
   - JSON schema validation (for registry extensions)

3. Development environment:
   - Python 3.10+
   - A code editor (VS Code, PyCharm, etc.)
   - pytest for testing

## Types of Extensions

The Prompt Decorators framework supports several types of extensions:

1. **Custom Decorators**: New prompt decorators with unique functionality
2. **Registry Extensions**: Adding new decorators to the registry system
3. **Integration Extensions**: Adapters for specific LLM APIs or frameworks
4. **Utility Extensions**: Tools and helpers that enhance the framework

This tutorial will primarily focus on creating custom decorators and integrating them with the registry.

## Creating a Custom Decorator

Let's create a custom decorator that formats text with specific colors for highlighting important information.

### Step 1: Basic Decorator Structure

Start by creating a new Python file named `color_highlight.py`:

```python
from typing import Callable, Optional, Union, List, Dict, Any
from prompt_decorators.base import BaseDecorator

class ColorHighlight(BaseDecorator):
    """Decorator that highlights text with specific colors.

    This decorator adds HTML-like color tags to highlight specific words or
    phrases in the prompt text.

    Args:
        highlight_words: Words or phrases to highlight
        color: Color to use for highlighting (default: "yellow")
        case_sensitive: Whether matching should be case-sensitive (default: False)
    """

    def __init__(
        self,
        highlight_words: Union[str, List[str]],
        color: str = "yellow",
        case_sensitive: bool = False
    ) -> None:
        """Initialize the ColorHighlight decorator."""
        super().__init__()
        self.highlight_words = [highlight_words] if isinstance(highlight_words, str) else highlight_words
        self.color = color
        self.case_sensitive = case_sensitive

    def __call__(self, text: str) -> str:
        """Apply the color highlighting to the text.

        Args:
            text: The input text to be highlighted

        Returns:
            The text with color highlighting applied
        """
        if not self.highlight_words:
            return text

        result = text
        for word in self.highlight_words:
            if self.case_sensitive:
                result = result.replace(
                    word,
                    f"<span style='background-color: {self.color}'>{word}</span>"
                )
            else:
                # Case-insensitive replacement requires more complex logic
                import re
                pattern = re.compile(re.escape(word), re.IGNORECASE)
                result = pattern.sub(
                    lambda m: f"<span style='background-color: {self.color}'>{m.group(0)}</span>",
                    result
                )

        return result

    @property
    def metadata(self) -> Dict[str, Any]:
        """Return metadata about this decorator instance."""
        return {
            "name": "ColorHighlight",
            "highlight_words": self.highlight_words,
            "color": self.color,
            "case_sensitive": self.case_sensitive
        }
```

### Step 2: Add Additional Functionality

Let's enhance our decorator with more functionality:

```python
class ColorHighlight(BaseDecorator):
    # ... existing code ...

    def add_highlight_word(self, word: str) -> 'ColorHighlight':
        """Add a new word to highlight.

        Args:
            word: The new word to highlight

        Returns:
            Self for method chaining
        """
        if word not in self.highlight_words:
            self.highlight_words.append(word)
        return self

    def change_color(self, new_color: str) -> 'ColorHighlight':
        """Change the highlight color.

        Args:
            new_color: The new color to use

        Returns:
            Self for method chaining
        """
        self.color = new_color
        return self

    def toggle_case_sensitivity(self) -> 'ColorHighlight':
        """Toggle case sensitivity.

        Returns:
            Self for method chaining
        """
        self.case_sensitive = not self.case_sensitive
        return self
```

### Step 3: Create Factory Methods

Factory methods make it easier to create common variants of your decorator:

```python
@classmethod
def important(cls, highlight_words: Union[str, List[str]]) -> 'ColorHighlight':
    """Factory method for highlighting important information in red.

    Args:
        highlight_words: Words to highlight as important

    Returns:
        ColorHighlight instance configured for important highlighting
    """
    return cls(highlight_words=highlight_words, color="red", case_sensitive=True)

@classmethod
def casual(cls, highlight_words: Union[str, List[str]]) -> 'ColorHighlight':
    """Factory method for casual highlighting in light yellow.

    Args:
        highlight_words: Words to highlight casually

    Returns:
        ColorHighlight instance configured for casual highlighting
    """
    return cls(highlight_words=highlight_words, color="lightyellow", case_sensitive=False)
```

## Registry Integration

Next, let's integrate our custom decorator with the Prompt Decorators registry.

### Step 1: Create a Registry JSON Definition

Create a file named `color_highlight.json` in a directory called `registry_extensions`:

```json
{
  "name": "ColorHighlight",
  "category": "formatting",
  "description": "Highlights specific words or phrases with color formatting",
  "version": "1.0.0",
  "author": "Your Name",
  "parameters": [
    {
      "name": "highlight_words",
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Words or phrases to highlight",
      "required": true
    },
    {
      "name": "color",
      "type": "string",
      "description": "Color to use for highlighting",
      "default": "yellow",
      "required": false
    },
    {
      "name": "case_sensitive",
      "type": "boolean",
      "description": "Whether matching should be case-sensitive",
      "default": false,
      "required": false
    }
  ],
  "examples": [
    {
      "input": "This is an important message about security.",
      "parameters": {
        "highlight_words": ["important", "security"],
        "color": "yellow"
      },
      "output": "This is an <span style='background-color: yellow'>important</span> message about <span style='background-color: yellow'>security</span>."
    }
  ],
  "factory_methods": [
    {
      "name": "important",
      "description": "Highlights important information in red",
      "parameters": [
        {
          "name": "highlight_words",
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Words to highlight as important",
          "required": true
        }
      ]
    },
    {
      "name": "casual",
      "description": "Casual highlighting in light yellow",
      "parameters": [
        {
          "name": "highlight_words",
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Words to highlight casually",
          "required": true
        }
      ]
    }
  ],
  "compatibility": {
    "models": ["all"],
    "decorators": {
      "compatible": ["all"],
      "incompatible": []
    }
  }
}
```

### Step 2: Register Your Decorator

Now, let's create a module to register our decorator with the registry system:

```python
# extensions_loader.py
from prompt_decorators.registry import DecoratorRegistry
from color_highlight import ColorHighlight
import os
import json

def register_extensions(registry: DecoratorRegistry) -> None:
    """Register extensions with the decorator registry.

    Args:
        registry: The decorator registry instance
    """
    # Register the ColorHighlight decorator
    registry.register_decorator_class(ColorHighlight)

    # Load registry metadata from JSON
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "registry_extensions", "color_highlight.json")

    with open(json_path, 'r') as f:
        metadata = json.load(f)

    # Update registry with metadata
    registry.update_decorator_metadata("ColorHighlight", metadata)

    print(f"Registered ColorHighlight decorator with the registry")
```

### Step 3: Use Your Decorator

You can now use your custom decorator:

```python
from prompt_decorators.registry import DecoratorRegistry
from extensions_loader import register_extensions

# Initialize the registry and register extensions
registry = DecoratorRegistry()
register_extensions(registry)

# Create a decorator instance directly
highlight = ColorHighlight(["important", "critical"], color="orange")
result = highlight("This is an important message with critical information.")
print(result)

# Or create it through the registry
highlight_factory = registry.get_decorator_factory("ColorHighlight")
highlight_instance = highlight_factory(highlight_words=["warning", "alert"], color="red")
result = highlight_instance("This is a warning message with an alert.")
print(result)

# Or use a factory method
important_highlight = ColorHighlight.important(["urgent", "immediate attention"])
result = important_highlight("This requires urgent action and immediate attention.")
print(result)
```

## Testing Your Extension

Testing is crucial for ensuring your decorator works correctly. Let's create a basic test file:

```python
# test_color_highlight.py
import pytest
from color_highlight import ColorHighlight

def test_basic_highlighting():
    """Test basic word highlighting functionality."""
    highlighter = ColorHighlight(["important", "critical"], color="yellow")
    result = highlighter("This is an important message with critical information.")
    expected = "This is an <span style='background-color: yellow'>important</span> message with <span style='background-color: yellow'>critical</span> information."
    assert result == expected

def test_case_sensitivity():
    """Test case sensitivity settings."""
    # Case sensitive
    highlighter = ColorHighlight(["Important"], color="yellow", case_sensitive=True)
    result = highlighter("This is an Important message, not important.")
    expected = "This is an <span style='background-color: yellow'>Important</span> message, not important."
    assert result == expected

    # Case insensitive
    highlighter = ColorHighlight(["Important"], color="yellow", case_sensitive=False)
    result = highlighter("This is an Important message, also important.")
    expected = "This is an <span style='background-color: yellow'>Important</span> message, also <span style='background-color: yellow'>important</span>."
    assert result == expected

def test_factory_methods():
    """Test factory methods."""
    # Important factory
    highlighter = ColorHighlight.important(["warning"])
    result = highlighter("This is a warning message.")
    expected = "This is a <span style='background-color: red'>warning</span> message."
    assert result == expected

    # Casual factory
    highlighter = ColorHighlight.casual(["note"])
    result = highlighter("Please note this information.")
    expected = "Please <span style='background-color: lightyellow'>note</span> this information."
    assert result == expected

def test_method_chaining():
    """Test method chaining API."""
    highlighter = ColorHighlight(["initial"])
    result = (highlighter
               .add_highlight_word("added")
               .change_color("green")
               .toggle_case_sensitivity()
               ("This has an initial word and an ADDED emphasis."))

    # With case sensitivity toggled to True
    expected = "This has an <span style='background-color: green'>initial</span> word and an <span style='background-color: green'>added</span> emphasis."
    assert result == expected
```

Run the tests with pytest:

```bash
pytest test_color_highlight.py -v
```

## Extension Distribution

You can distribute your extension in several ways:

### Option 1: Stand-alone Package

Create a separate Python package:

```
color-highlight-extension/
├── pyproject.toml
├── setup.py
├── README.md
├── color_highlight/
│   ├── __init__.py
│   ├── extension.py
│   └── registry_extensions/
│       └── color_highlight.json
└── tests/
    └── test_color_highlight.py
```

### Option 2: Contribution to Main Repository

1. Fork the Prompt Decorators repository
2. Add your extension to the appropriate directories
3. Submit a pull request with your changes

### Option 3: Local Extension

For personal use, simply use your extension code directly in your project.

## Advanced Extension Techniques

### Extending Core Functionality

You can extend core classes for more complex integrations:

```python
from prompt_decorators.base import BaseDecorator
from prompt_decorators.registry import DecoratorRegistry
from typing import Any, Dict, Optional, Type

class ExtendedRegistry(DecoratorRegistry):
    """Extended registry with additional features."""

    def register_with_dependencies(
        self,
        decorator_class: Type[BaseDecorator],
        dependencies: Dict[str, Any]
    ) -> None:
        """Register a decorator with its dependencies.

        Args:
            decorator_class: The decorator class to register
            dependencies: Dependencies required by the decorator
        """
        self.register_decorator_class(decorator_class)
        # Store dependencies for later use
        self._dependencies[decorator_class.__name__] = dependencies

    def get_decorator_with_dependencies(
        self,
        decorator_name: str
    ) -> Optional[BaseDecorator]:
        """Get a decorator instance with its dependencies injected.

        Args:
            decorator_name: Name of the decorator to get

        Returns:
            Decorator instance with dependencies or None if not found
        """
        factory = self.get_decorator_factory(decorator_name)
        if not factory:
            return None

        dependencies = self._dependencies.get(decorator_name, {})
        return factory(**dependencies)
```

### Creating Component Decorators

For complex extensions, break functionality into smaller components:

```python
class MarkerComponent:
    """Component for marking text."""

    def mark_text(self, text, marker, pattern):
        # Implementation
        pass

class HighlightComponent:
    """Component for highlighting text."""

    def highlight_text(self, text, color):
        # Implementation
        pass

class AdvancedHighlighter(BaseDecorator, MarkerComponent, HighlightComponent):
    """Advanced highlighter using composition of components."""

    def __call__(self, text):
        # Use components to implement functionality
        marked_text = self.mark_text(text, marker="*", pattern=self.pattern)
        highlighted_text = self.highlight_text(marked_text, color=self.color)
        return highlighted_text
```

## Creating Domain-Specific Extensions

Domain-specific extensions allow you to create specialized decorators tailored to particular fields or industries. This section will guide you through the process of creating a cohesive set of decorators for a specific domain.

### Planning Your Domain Extension

1. **Identify Domain Needs**: Determine the unique requirements of your domain:
   - What specialized behaviors would benefit practitioners in this field?
   - What domain-specific terminology or formats are commonly used?
   - What output structures are most valuable for domain experts?

2. **Map Domain Concepts to Decorators**: Create a mapping between domain concepts and potential decorators:
   - Identify key workflows that could be enhanced
   - Determine parameters that domain experts would understand
   - Consider how domain-specific decorators might interact with core decorators

### Example: Medical Domain Extension

Let's create a simple extension package for the medical domain:

```python
# medical_decorators.py
from prompt_decorators.base import BaseDecorator
from typing import List, Optional, Union

class MedicalEvidence(BaseDecorator):
    """Decorator that ensures responses cite medical evidence according to standards.

    Args:
        level: The level of evidence required (systematic, rct, cohort, case, expert)
        recency: Maximum age of cited research in years
    """

    def __init__(
        self,
        level: str = "systematic",
        recency: int = 5
    ) -> None:
        super().__init__()
        self.level = level
        self.recency = recency

    def __call__(self, text: str) -> str:
        # Implementation would modify the prompt to request evidence-based responses
        # This is a simplified example
        return f"{text}\n\nPlease provide {self.level}-level medical evidence " \
               f"from the past {self.recency} years to support all claims."

class PatientFriendly(BaseDecorator):
    """Decorator that adapts medical information for patient understanding.

    Args:
        reading_level: Target reading comprehension level
        include_glossary: Whether to include a glossary of medical terms
    """

    def __init__(
        self,
        reading_level: str = "middle",
        include_glossary: bool = True
    ) -> None:
        super().__init__()
        self.reading_level = reading_level
        self.include_glossary = include_glossary

    def __call__(self, text: str) -> str:
        # Implementation would modify the prompt to request patient-friendly responses
        # This is a simplified example
        result = f"{text}\n\nPlease explain this in patient-friendly language " \
                f"at a {self.reading_level} school reading level."

        if self.include_glossary:
            result += " Include a brief glossary for any medical terms used."

        return result
```

### Creating the Extension Package

Now, let's create the extension package JSON file:

```json
{
  "name": "medical-decorators",
  "version": "1.0.0",
  "description": "Prompt decorators for medical and healthcare applications",
  "author": {
    "name": "Healthcare AI Team",
    "email": "healthcare@example.com",
    "url": "https://healthcare-ai.example.com"
  },
  "license": "MIT",
  "keywords": ["medical", "healthcare", "evidence-based-medicine", "patient-education"],
  "repository": {
    "type": "git",
    "url": "https://github.com/example/medical-decorators"
  },
  "decorators": [
    {
      "decoratorName": "MedicalEvidence",
      "version": "1.0.0",
      "description": "Ensures responses cite medical evidence according to evidence-based medicine standards",
      "parameters": [
        {
          "name": "level",
          "type": "enum",
          "description": "The level of evidence required",
          "enum": ["systematic", "rct", "cohort", "case", "expert"],
          "default": "systematic",
          "required": false
        },
        {
          "name": "recency",
          "type": "number",
          "description": "Maximum age of cited research in years",
          "default": 5,
          "required": false
        }
      ],
      "examples": [
        {
          "description": "Request for treatment information with high-quality evidence",
          "usage": "+++MedicalEvidence(level=systematic, recency=3)\nWhat are the current treatments for type 2 diabetes?",
          "result": "Provides treatment information citing systematic reviews and meta-analyses from the last 3 years"
        }
      ],
      "compatibility": {
        "requires": ["CiteSources"],
        "conflicts": [],
        "models": ["gpt-4"]
      }
    },
    {
      "decoratorName": "PatientFriendly",
      "version": "1.0.0",
      "description": "Adapts medical information to be understandable by patients without medical background",
      "parameters": [
        {
          "name": "readingLevel",
          "type": "enum",
          "description": "Target reading comprehension level",
          "enum": ["elementary", "middle", "high", "college"],
          "default": "middle",
          "required": false
        },
        {
          "name": "includeGlossary",
          "type": "boolean",
          "description": "Whether to include a glossary of medical terms",
          "default": true,
          "required": false
        }
      ],
      "examples": [
        {
          "description": "Explaining a medical condition to a patient",
          "usage": "+++PatientFriendly(readingLevel=middle, includeGlossary=true)\nExplain what hypertension is and how it affects the body.",
          "result": "Provides an explanation of hypertension at a middle school reading level with a glossary of medical terms"
        }
      ],
      "compatibility": {
        "requires": [],
        "conflicts": ["Technical"],
        "models": ["gpt-4", "gpt-3.5-turbo"]
      }
    }
  ],
  "dependencies": {
    "standard": {
      "version": "1.0.0"
    }
  }
}
```

### Packaging and Distribution

To package your domain-specific extension:

1. **Create a Package Structure**:
   ```
   medical-decorators/
   ├── pyproject.toml
   ├── setup.py
   ├── README.md
   ├── medical_decorators/
   │   ├── __init__.py
   │   ├── decorators.py
   │   └── registry_extensions/
   │       └── medical_decorators.json
   └── tests/
       └── test_medical_decorators.py
   ```

2. **Create a Registration Module**:
   ```python
   # __init__.py
   from prompt_decorators.registry import DecoratorRegistry
   from .decorators import MedicalEvidence, PatientFriendly
   import os
   import json

   def register_extensions(registry: DecoratorRegistry) -> None:
       """Register medical extensions with the decorator registry."""
       # Register decorator classes
       registry.register_decorator_class(MedicalEvidence)
       registry.register_decorator_class(PatientFriendly)

       # Load registry metadata from JSON
       current_dir = os.path.dirname(os.path.abspath(__file__))
       json_path = os.path.join(current_dir, "registry_extensions", "medical_decorators.json")

       with open(json_path, 'r') as f:
           metadata = json.load(f)

       # Update registry with metadata
       for decorator in metadata["decorators"]:
           registry.update_decorator_metadata(decorator["decoratorName"], decorator)

       print(f"Registered medical domain decorators with the registry")
   ```

3. **Document Domain-Specific Usage**:
   Create comprehensive documentation that explains:
   - The domain-specific concepts your decorators address
   - How to use the decorators in domain-specific workflows
   - Examples of common use cases in your domain
   - Any domain-specific best practices

### Using Domain-Specific Extensions

Users can incorporate your domain-specific extensions:

```python
from prompt_decorators.registry import DecoratorRegistry
from medical_decorators import register_extensions

# Initialize registry and register medical extensions
registry = DecoratorRegistry()
register_extensions(registry)

# Create a prompt with medical decorators
prompt = """
+++MedicalEvidence(level=rct, recency=3)
+++PatientFriendly(readingLevel=elementary, includeGlossary=true)
What are the treatment options for childhood asthma?
"""

# Process the prompt
processed_prompt = registry.process_prompt(prompt)
```

### Domain-Specific Extension Best Practices

1. **Use Domain Terminology**: Name decorators and parameters using familiar domain terminology
2. **Consult Domain Experts**: Work with experts in the field to identify valuable decorator functionality
3. **Document Domain Context**: Provide context about why certain decorators are valuable in the domain
4. **Consider Workflows**: Design decorators that fit into existing domain workflows
5. **Test with Domain Users**: Validate your extensions with actual practitioners in the field

## Best Practices

When developing extensions, follow these best practices:

1. **Follow the Core Design Principles**
   - Your extension should be composable with other decorators
   - Maintain immutability of input text
   - Provide clear documentation

2. **Parameter Handling**
   - Validate parameters in `__init__`
   - Provide sensible defaults
   - Use type annotations

3. **Testing**
   - Test edge cases (empty strings, long text, etc.)
   - Test composition with other decorators
   - Test factory methods

4. **Registry Integration**
   - Provide complete and accurate JSON metadata
   - Include examples in the registry JSON
   - Specify compatibility with other decorators

5. **Code Quality**
   - Follow PEP 8 standards
   - Document your code with docstrings
   - Handle errors gracefully

## Troubleshooting

Common issues and solutions:

### Decorator Not Found in Registry

**Problem**: Your decorator isn't available in the registry after registration.

**Solution**:
- Ensure you've called `register_decorator_class` with the correct class
- Check that the class name matches the name in your JSON metadata
- Verify that your registration code is being executed

### Unexpected Behavior When Composing Decorators

**Problem**: Your decorator doesn't work well when combined with others.

**Solution**:
- Ensure your decorator preserves the structure expected by other decorators
- Test with common decorators to identify compatibility issues
- Update your compatibility matrix in the registry JSON

### Extension Not Working with Specific LLMs

**Problem**: Your extension works with some LLMs but not others.

**Solution**:
- Check if the LLM has specific formatting requirements
- Add LLM-specific logic to handle different API formats
- Document compatibility limitations in your metadata

## Conclusion

You've now learned how to create custom extensions for the Prompt Decorators framework. By following this tutorial, you can develop decorators that meet your specific needs, integrate them with the registry system, and distribute them to the community.

Remember that the power of the Prompt Decorators framework comes from its extensibility and composability. Your contributions can help expand the ecosystem and provide valuable tools for other developers.

## Next Steps

Now that you've learned how to create and distribute extensions for Prompt Decorators, you might want to explore:

- [Creating more complex decorators](./creating_decorators.md)
- [Developing domain-specific extensions](../guides/domain_specific_extensions.md)
- [Integrating with specific LLM APIs](../api_reference.md)
- [Contributing to the Prompt Decorators project](../../CONTRIBUTING.md)

Happy decorating!

# Creating Domain-Specific Extensions

This guide provides a comprehensive walkthrough for creating domain-specific extensions for the Prompt Decorators framework. Domain-specific extensions allow you to create specialized decorators tailored to particular fields or industries, making AI interactions more effective for specific use cases.

## Table of Contents

- [Introduction](#introduction)
- [Why Create Domain-Specific Extensions?](#why-create-domain-specific-extensions)
- [Planning Your Domain Extension](#planning-your-domain-extension)
- [Step-by-Step Implementation Guide](#step-by-step-implementation-guide)
- [Example: Medical Domain Extension](#example-medical-domain-extension)
- [Example: Legal Domain Extension](#example-legal-domain-extension)
- [Testing Domain-Specific Extensions](#testing-domain-specific-extensions)
- [Distribution and Sharing](#distribution-and-sharing)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Introduction

Domain-specific extensions enhance the Prompt Decorators framework by providing specialized behaviors tailored to particular fields or industries. These extensions make AI interactions more effective by incorporating domain knowledge, terminology, and workflows directly into the prompt engineering process.

## Why Create Domain-Specific Extensions?

Domain-specific extensions offer several advantages:

1. **Specialized Behavior**: Implement behaviors that address unique requirements of your domain
2. **Domain Terminology**: Use familiar terminology that domain experts understand
3. **Workflow Integration**: Fit AI interactions into existing domain workflows
4. **Consistency**: Ensure consistent AI responses for domain-specific tasks
5. **Knowledge Encapsulation**: Embed domain knowledge into reusable components
6. **Quality Control**: Enforce domain-specific standards and best practices

## Planning Your Domain Extension

Before implementing your domain extension, careful planning is essential:

### 1. Domain Analysis

- **Identify Key Tasks**: What are the common tasks in your domain that could benefit from AI assistance?
- **Analyze Workflows**: How do practitioners in your domain currently work?
- **Identify Pain Points**: What aspects of AI interaction are currently challenging for domain experts?
- **Review Terminology**: What specialized language is used in your domain?

### 2. Decorator Mapping

Create a mapping between domain concepts and potential decorators:

| Domain Concept | Potential Decorator | Parameters | Description |
|----------------|---------------------|------------|-------------|
| Concept 1 | Decorator1 | param1, param2 | How this decorator helps with the concept |
| Concept 2 | Decorator2 | param1, param2 | How this decorator helps with the concept |

### 3. Compatibility Analysis

- **Core Decorators**: Which core decorators would complement your domain-specific decorators?
- **Conflicts**: Are there any potential conflicts with existing decorators?
- **Dependencies**: Do your decorators depend on other decorators?

### 4. User Personas

Define the users who will benefit from your extension:

- **Primary Users**: Who are the main users of your extension?
- **Skill Level**: What is their technical expertise with AI and prompt engineering?
- **Use Cases**: What specific problems will they solve with your extension?

## Step-by-Step Implementation Guide

Follow these steps to implement your domain-specific extension:

### Step 1: Set Up Your Project Structure

Create a directory structure for your extension:

```
your-domain-extension/
├── pyproject.toml
├── setup.py
├── README.md
├── your_domain_extension/
│   ├── __init__.py
│   ├── decorators.py
│   └── registry_extensions/
│       └── your_domain_extension.json
└── tests/
    └── test_your_domain_extension.py
```

### Step 2: Define Your Decorator Classes

Create your decorator classes in `decorators.py`:

```python
from prompt_decorators.base import BaseDecorator
from typing import List, Optional, Union

class YourDomainDecorator(BaseDecorator):
    """Decorator that implements domain-specific behavior.

    Args:
        param1: Description of parameter 1
        param2: Description of parameter 2
    """

    def __init__(
        self,
        param1: str = "default",
        param2: int = 5
    ) -> None:
        super().__init__()
        self.param1 = param1
        self.param2 = param2

    def __call__(self, text: str) -> str:
        # Implementation of your domain-specific behavior
        return f"{text}\n\nApply domain-specific transformation with {self.param1} and {self.param2}."
```

### Step 3: Create Registry Entries

Create a JSON file in the `registry_extensions` directory:

```json
{
  "decoratorName": "YourDomainDecorator",
  "version": "1.0.0",
  "description": "Detailed description of your domain-specific decorator",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "url": "https://yourwebsite.com"
  },
  "parameters": [
    {
      "name": "param1",
      "type": "string",
      "description": "Description of parameter 1",
      "default": "default",
      "required": false
    },
    {
      "name": "param2",
      "type": "number",
      "description": "Description of parameter 2",
      "default": 5,
      "required": false
    }
  ],
  "examples": [
    {
      "description": "Example usage in your domain",
      "usage": "+++YourDomainDecorator(param1=value, param2=10)\nYour domain-specific prompt here.",
      "result": "Expected result description"
    }
  ],
  "compatibility": {
    "requires": [],
    "conflicts": [],
    "models": ["gpt-4", "gpt-3.5-turbo"]
  }
}
```

### Step 4: Create an Extension Package

Create an extension package JSON file:

```json
{
  "name": "your-domain-extension",
  "version": "1.0.0",
  "description": "A collection of decorators for your specific domain",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "url": "https://yourwebsite.com"
  },
  "license": "MIT",
  "keywords": ["your-domain", "prompt-decorators", "ai"],
  "repository": {
    "type": "git",
    "url": "https://github.com/yourusername/your-domain-extension"
  },
  "decorators": [
    // Include your registry entries here
  ],
  "dependencies": {
    "standard": {
      "version": "1.0.0"
    },
    "extensions": []
  }
}
```

### Step 5: Implement Registration

Create registration code in `__init__.py`:

```python
from prompt_decorators.utils.discovery import DecoratorRegistry
from .decorators import YourDomainDecorator
import os
import json

def register_extensions(registry: DecoratorRegistry) -> None:
    """Register domain-specific extensions with the decorator registry."""
    # Register decorator classes
    registry.register_decorator(YourDomainDecorator)

    # Note: The registry doesn't currently support updating metadata directly
    # The metadata is in registry_extensions/your_domain_extension.json for reference

    print(f"Registered domain-specific decorators with the registry")
```

### Step 6: Write Tests

Create tests in `tests/test_your_domain_extension.py`:

```python
import pytest
from your_domain_extension.decorators import YourDomainDecorator

def test_your_domain_decorator():
    """Test your domain-specific decorator."""
    decorator = YourDomainDecorator(param1="test", param2=10)
    result = decorator("Test prompt")
    assert "test" in result
    assert "10" in result
```

### Step 7: Package Your Extension

Create a `setup.py` file:

```python
from setuptools import setup, find_packages

setup(
    name="your-domain-extension",
    version="1.0.0",
    description="Domain-specific extensions for Prompt Decorators",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "prompt-decorators>=1.0.0",
    ],
    include_package_data=True,
    package_data={
        "your_domain_extension": ["registry_extensions/*.json"],
    },
)
```

## Example: Medical Domain Extension

Let's create a simple extension package for the medical domain:

### Medical Decorator Classes

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
        result = f"{text}\n\nPlease explain this in patient-friendly language " \
                f"at a {self.reading_level} school reading level."

        if self.include_glossary:
            result += " Include a brief glossary for any medical terms used."

        return result
```

### Medical Extension Package

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

### Usage Example

```python
from prompt_decorators.utils.discovery import DecoratorRegistry
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

# Send to LLM API
response = llm_api.generate(processed_prompt)
```

## Example: Legal Domain Extension

Here's another example for the legal domain:

### Legal Decorator Classes

```python
# legal_decorators.py
from prompt_decorators.base import BaseDecorator

class LegalCitation(BaseDecorator):
    """Decorator that ensures proper legal citations in responses.

    Args:
        jurisdiction: The legal jurisdiction (us, uk, eu, international)
        format: Citation format (bluebook, alwd, oscola)
    """

    def __init__(
        self,
        jurisdiction: str = "us",
        format: str = "bluebook"
    ) -> None:
        super().__init__()
        self.jurisdiction = jurisdiction
        self.format = format

    def __call__(self, text: str) -> str:
        return f"{text}\n\nPlease include proper legal citations in {self.format} format " \
               f"for {self.jurisdiction} jurisdiction."

class LegalAnalysis(BaseDecorator):
    """Decorator that structures responses as legal analysis.

    Args:
        framework: Analysis framework to use (irac, creac, firac)
        depth: Depth of analysis (brief, standard, comprehensive)
    """

    def __init__(
        self,
        framework: str = "irac",
        depth: str = "standard"
    ) -> None:
        super().__init__()
        self.framework = framework
        self.depth = depth

    def __call__(self, text: str) -> str:
        return f"{text}\n\nPlease structure your response as a {self.depth} legal analysis " \
               f"using the {self.framework.upper()} framework."
```

## Testing Domain-Specific Extensions

Testing is crucial for ensuring your domain-specific extensions work correctly:

### 1. Unit Tests

Test each decorator individually:

```python
def test_medical_evidence_decorator():
    """Test the MedicalEvidence decorator."""
    decorator = MedicalEvidence(level="rct", recency=3)
    result = decorator("What are the treatments for diabetes?")
    assert "rct-level medical evidence" in result
    assert "past 3 years" in result
```

### 2. Integration Tests

Test how your decorators work with the registry:

```python
def test_registry_integration():
    """Test integration with the decorator registry."""
    registry = DecoratorRegistry()
    register_extensions(registry)

    # Test decorator retrieval
    decorator_factory = registry.get_decorator_factory("MedicalEvidence")
    assert decorator_factory is not None

    # Test prompt processing
    prompt = "+++MedicalEvidence(level=rct)\nWhat are the treatments for diabetes?"
    processed = registry.process_prompt(prompt)
    assert "rct-level medical evidence" in processed
```

### 3. Domain Expert Validation

Have domain experts review your decorators:

- Are the parameters intuitive for domain experts?
- Do the decorators address real domain needs?
- Is the terminology correct and appropriate?
- Do the examples reflect realistic use cases?

## Distribution and Sharing

There are several ways to distribute your domain-specific extensions:

### 1. Python Package

Publish your extension as a Python package:

```bash
# Build the package
python setup.py sdist bdist_wheel

# Upload to PyPI
twine upload dist/*
```

### 2. GitHub Repository

Host your extension on GitHub:

- Include comprehensive documentation
- Provide installation instructions
- Include examples specific to your domain
- Add badges for build status, test coverage, etc.

### 3. Contribution to Main Repository

Consider contributing to the main Prompt Decorators repository:

1. Fork the repository
2. Add your extension to the appropriate directories
3. Submit a pull request with your changes

## Best Practices

Follow these best practices when creating domain-specific extensions:

### 1. Domain-Specific Considerations

- **Use Domain Terminology**: Name decorators and parameters using familiar domain terminology
- **Consult Domain Experts**: Work with experts in the field to identify valuable decorator functionality
- **Document Domain Context**: Provide context about why certain decorators are valuable in the domain
- **Consider Workflows**: Design decorators that fit into existing domain workflows
- **Test with Domain Users**: Validate your extensions with actual practitioners in the field

### 2. Technical Considerations

- **Follow Core Design Principles**: Ensure your decorators are composable with other decorators
- **Maintain Immutability**: Don't modify the input text directly
- **Validate Parameters**: Check parameter values and provide helpful error messages
- **Document Thoroughly**: Include comprehensive docstrings and examples
- **Test Edge Cases**: Test with various inputs, including edge cases

### 3. Usability Considerations

- **Intuitive Defaults**: Provide sensible default values for parameters
- **Clear Examples**: Include examples that demonstrate common use cases
- **Comprehensive Documentation**: Document how your decorators address domain-specific needs
- **Versioning**: Follow semantic versioning for your extensions
- **Backward Compatibility**: Maintain backward compatibility when updating your extensions

## Troubleshooting

Common issues and solutions:

### Decorator Not Working with LLM

**Problem**: Your domain-specific decorator doesn't affect the LLM's response.

**Solution**:
- Ensure your decorator is properly registered with the registry
- Check that the decorator's `__call__` method is modifying the prompt correctly
- Verify that the LLM supports the behavior you're trying to achieve

### Compatibility Issues

**Problem**: Your decorator conflicts with other decorators.

**Solution**:
- Update your compatibility information in the registry JSON
- Modify your decorator to work better with others
- Document known conflicts and provide workarounds

### Domain Experts Find It Difficult to Use

**Problem**: Domain experts struggle to use your decorators effectively.

**Solution**:
- Simplify parameter names and values
- Provide more examples of common use cases
- Create templates for common workflows
- Develop a simple UI for applying decorators

## Conclusion

Creating domain-specific extensions for Prompt Decorators allows you to tailor AI interactions to the unique needs of your field. By following the guidelines in this document, you can create powerful, reusable decorators that make AI more accessible and effective for domain experts.

Remember that the most valuable domain-specific extensions are those that truly understand and address the specific challenges of the domain. Work closely with domain experts throughout the development process to ensure your extensions meet their needs.

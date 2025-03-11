# Tutorial: Combining Decorators

This tutorial will guide you through the process of combining multiple decorators to create sophisticated prompt transformations. By stacking decorators, you can achieve complex behaviors that would be difficult to implement with a single decorator.

## Prerequisites

Before starting this tutorial, ensure you have:

1. Installed the Prompt Decorators package (`pip install prompt-decorators`)
2. Completed the [Creating Custom Decorators](creating_custom_decorator.md) tutorial
3. Familiarity with the core concepts of the framework

## Why Combine Decorators?

Combining decorators allows you to:

- Apply multiple enhancements to a single prompt
- Create modular transformations that can be mixed and matched
- Separate concerns, making each decorator focused on a specific task
- Build complex behaviors from simple building blocks

## Methods for Combining Decorators

There are three main ways to combine decorators:

1. **Inline stacking**: Using multiple decorator annotations in your prompt text
2. **Programmatic chaining**: Applying decorators in sequence in your code
3. **Composite decorators**: Creating new decorators that internally use other decorators

Let's explore each approach.

## 1. Inline Stacking

The simplest way to combine decorators is by stacking them in your prompt using the inline syntax:

```python
from prompt_decorators import apply_dynamic_decorators

# Create a prompt with multiple stacked decorators
prompt = """
+++Persona(role="data scientist")
+++Reasoning(depth="comprehensive")
+++OutputFormat(format="markdown")
Analyze this dataset and identify key trends:
[dataset description...]
"""

# Apply all decorators at once
transformed_prompt = apply_dynamic_decorators(prompt)
```

When using inline stacking:
- Decorators are applied in order, from top to bottom
- Each decorator transforms the text that results from previous decorators
- Later decorators can modify or override effects of earlier ones

### Example: Technical Analysis with Multiple Decorators

Here's an example that combines decorators for a technical analysis:

```python
from prompt_decorators import apply_dynamic_decorators
import openai

# Multi-decorator prompt for technical analysis
prompt = """
+++Persona(role="data scientist")
+++Reasoning(depth="comprehensive")
+++StepByStep(numbered=true)
+++OutputFormat(format="markdown")
+++Audience(level="technical")

Analyze the following dataset of customer churn and identify the key factors that predict churn:

Customer ID, Age, Tenure (months), Monthly Contract, Services Subscribed, Monthly Charges, Churn
1, 42, 24, Yes, Internet+Phone, 89.90, No
2, 27, 3, No, Internet only, 45.50, Yes
3, 35, 18, Yes, Full package, 120.30, No
4, 51, 36, Yes, Internet+TV, 95.75, No
5, 23, 1, No, Phone only, 25.10, Yes
...
"""

transformed_prompt = apply_dynamic_decorators(prompt)

# Send to an LLM
openai.api_key = "your-api-key-here"
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": transformed_prompt}],
    temperature=0.7
)
```

The resulting transformation applies multiple effects:
1. Adopts the persona of a data scientist
2. Provides comprehensive reasoning
3. Structures the response as numbered steps
4. Formats the output in markdown
5. Targets a technical audience

## 2. Programmatic Chaining

You can also chain decorators programmatically in your code:

```python
from prompt_decorators import create_decorator_instance

# Create individual decorator instances
persona = create_decorator_instance("Persona", role="teacher")
step_by_step = create_decorator_instance("StepByStep", numbered=True)
audience = create_decorator_instance("Audience", level="beginner")

# Original prompt
original_prompt = "Explain how photosynthesis works."

# Apply decorators in sequence (order matters!)
transformed_prompt = persona(step_by_step(audience(original_prompt)))

# The order is: audience -> step_by_step -> persona
```

When using programmatic chaining:
- You have more control over the order of application
- You can conditionally apply decorators based on runtime conditions
- You can reuse decorator instances across multiple prompts

### Example: Conditional Decorator Application

Here's an example that applies decorators conditionally:

```python
from prompt_decorators import create_decorator_instance

def generate_educational_content(topic, audience_level, include_steps=True, use_markdown=False):
    """Generate educational content with appropriate decorators."""
    prompt = f"Explain {topic}."

    # Start with audience adaptation
    audience = create_decorator_instance("Audience", level=audience_level)
    prompt = audience(prompt)

    # Add steps if requested
    if include_steps:
        step_by_step = create_decorator_instance("StepByStep", numbered=True)
        prompt = step_by_step(prompt)

    # Add markdown formatting if requested
    if use_markdown:
        output_format = create_decorator_instance("OutputFormat", format="markdown")
        prompt = output_format(prompt)

    # Always add a suitable persona for educational content
    if audience_level in ["beginner", "intermediate"]:
        persona = create_decorator_instance("Persona", role="teacher")
    else:
        persona = create_decorator_instance("Persona", role="professor")

    prompt = persona(prompt)

    return prompt

# Example usage
beginner_content = generate_educational_content(
    "photosynthesis",
    audience_level="beginner",
    include_steps=True
)

expert_content = generate_educational_content(
    "quantum computing",
    audience_level="expert",
    include_steps=False,
    use_markdown=True
)
```

## 3. Composite Decorators

For reusable combinations of decorators, you can create composite decorators that encapsulate multiple transformations. Here's how to implement one in Python:

```python
from prompt_decorators import DecoratorDefinition, register_decorator, create_decorator_instance

def technical_tutorial_transform(text, format="markdown", examples=True):
    """
    Transform function for the TechnicalTutorial decorator.

    Args:
        text (str): The original prompt text
        format (str): Output format
        examples (bool): Whether to include examples

    Returns:
        str: The transformed prompt text
    """
    # Create instances of the component decorators
    persona = create_decorator_instance('Persona', role='senior developer')
    steps = create_decorator_instance('StepByStep', numbered=True)
    audience = create_decorator_instance('Audience', level='technical')
    output_format = create_decorator_instance('OutputFormat', format=format)

    # Apply decorators in sequence
    result = persona(steps(audience(text)))
    result = output_format(result)

    # Add examples instruction if needed
    if examples:
        result = "Please include practical code examples for each step.\n\n" + result

    return result

# Define the composite decorator
technical_tutorial = DecoratorDefinition(
    name="TechnicalTutorial",
    description="Creates a technical tutorial with steps, reasoning, and technical details",
    category="Composite",
    parameters=[
        {
            "name": "format",
            "type": "enum",
            "description": "Output format",
            "enum": ["markdown", "plaintext"],
            "default": "markdown"
        },
        {
            "name": "examples",
            "type": "boolean",
            "description": "Include examples",
            "default": True
        }
    ],
    transform_function=technical_tutorial_transform
)

# Register the composite decorator
register_decorator(technical_tutorial)

# Use the composite decorator
tutorial = create_decorator_instance("TechnicalTutorial", format="markdown", examples=True)
transformed = tutorial("Explain how to implement a binary search algorithm.")
```

When creating composite decorators:
- You encapsulate complexity behind a simpler interface
- You ensure consistent application of multiple decorators
- You can provide parameters that control the internal decorators

## 4. Decorator Composition with Classes

If you prefer a more object-oriented approach, you can create a class-based composite decorator:

```python
from prompt_decorators import DecoratorBase, register_decorator

class CompositeTutorialDecorator(DecoratorBase):
    """A class-based composite decorator for generating tutorials."""

    def __init__(self, format="markdown", examples=True, audience="technical"):
        """Initialize the composite decorator."""
        super().__init__()
        self.format = format
        self.examples = examples
        self.audience = audience

    def transform(self, text):
        """Apply multiple transformations in sequence."""
        from prompt_decorators import create_decorator_instance

        # Create instances of component decorators
        persona = create_decorator_instance('Persona', role='senior developer')
        steps = create_decorator_instance('StepByStep', numbered=True)
        audience = create_decorator_instance('Audience', level=self.audience)
        output_format = create_decorator_instance('OutputFormat', format=self.format)

        # Apply the transformations in sequence
        result = persona(steps(audience(text)))
        result = output_format(result)

        # Add examples instruction if needed
        if self.examples:
            result = "Please include practical code examples for each step.\n\n" + result

        return result

# Register the composite class decorator
register_decorator(CompositeTutorialDecorator,
                  name="ClassTutorial",
                  description="Class-based tutorial decorator",
                  category="Composite")
```

## Conclusion

In this tutorial, you've learned how to:

1. Combine decorators using inline stacking in the prompt
2. Chain decorators programmatically in your code
3. Create composite decorators that encapsulate multiple transformations
4. Implement class-based composite decorators

By combining decorators, you can create powerful, flexible prompt transformations that would be difficult to achieve with a single decorator. This modular approach allows you to build complex behaviors from simple, reusable components.

## Next Steps

- Experiment with different combinations of decorators
- Create domain-specific composite decorators for your use cases
- Develop an extension with multiple related decorators (see the [Extension Development](extension_development.md) tutorial)
- Contribute your most useful decorator combinations to the community

# Tutorial: Creating a Custom Decorator

This tutorial will guide you through the process of creating a custom decorator with the Prompt Decorators framework. We'll create a practical, reusable decorator that you can adapt for your own use cases.

## Prerequisites

Before starting this tutorial, ensure you have:

1. Installed the Prompt Decorators package (`pip install prompt-decorators`)
2. Basic understanding of Python
3. Familiarity with the core concepts of the framework

## What We'll Build

We'll create a `CodeReview` decorator that transforms a prompt into instructions for conducting a code review of the provided code. This is useful for:

- Getting more consistent code reviews from LLMs
- Focusing the LLM on specific aspects of the code
- Ensuring best practices are checked

## Step 1: Import the Required Modules

First, let's import the necessary components:

```python
from prompt_decorators import (
    DecoratorDefinition,
    register_decorator,
    create_decorator_instance,
    apply_dynamic_decorators
)
```

## Step 2: Define the Decorator

Now, we'll define our `CodeReview` decorator:

```python
def code_review_transform(text, focus="all", severity="all", suggest_fixes=True):
    """
    Transform function for the CodeReview decorator.

    Args:
        text (str): The original prompt text
        focus (str): What aspects to focus on in the review
        severity (str): Whether to include only issues of specific severity
        suggest_fixes (bool): Whether to suggest specific fixes for issues

    Returns:
        str: The transformed prompt text
    """
    instruction = "Please perform a code review on the following code. "

    # Add focus-specific instructions
    if focus == "security":
        instruction += "Focus primarily on security issues such as injection vulnerabilities, " \
            "authentication problems, data exposure, and other security concerns. "
    elif focus == "performance":
        instruction += "Focus primarily on performance issues such as inefficient algorithms, " \
            "resource leaks, unnecessary operations, and optimization opportunities. "
    elif focus == "readability":
        instruction += "Focus primarily on code readability including naming conventions, " \
            "documentation, code organization, and adherence to style guidelines. "
    else:
        instruction += "Evaluate all aspects including security, performance, readability, " \
            "maintainability, and adherence to best practices. "

    # Add severity-specific instructions
    if severity == "critical":
        instruction += "Only highlight critical issues that could lead to serious vulnerabilities or failures. "
    elif severity == "major":
        instruction += "Focus on major and critical issues, ignoring minor stylistic concerns. "
    else:
        instruction += "Include issues of all severity levels, from critical to minor. "

    # Add fix suggestion instructions
    if suggest_fixes:
        instruction += "For each issue identified, suggest a specific fix with example code. "
    else:
        instruction += "Identify issues without providing specific fix implementations. "

    # Formatting instructions
    instruction += "Format your review as follows:\n" \
        "1. Summary of findings\n" \
        "2. Issues (grouped by type/severity)\n" \
        "3. Recommendations\n\n"

    # Append the original prompt
    return instruction + text

code_review_decorator = DecoratorDefinition(
    name="CodeReview",
    description="Transforms a prompt into instructions for conducting a code review",
    category="Development",
    parameters=[
        {
            "name": "focus",
            "type": "enum",
            "description": "What aspects to focus on in the review",
            "enum": ["security", "performance", "readability", "all"],
            "default": "all"
        },
        {
            "name": "severity",
            "type": "enum",
            "description": "Whether to include only issues of specific severity",
            "enum": ["critical", "major", "all"],
            "default": "all"
        },
        {
            "name": "suggest_fixes",
            "type": "boolean",
            "description": "Whether to suggest specific fixes for issues",
            "default": True
        }
    ],
    transform_function=code_review_transform
)

# Register the custom decorator
register_decorator(code_review_decorator)
```

## Step 3: Use the Decorator

Now that we've defined and registered our decorator, let's use it:

```python
# Method 1: Using create_decorator_instance
code_review = create_decorator_instance(
    "CodeReview",
    focus="security",
    severity="critical",
    suggest_fixes=True
)

code_to_review = """
def validate_user(username, password):
    """Validate a user's credentials."""
    if username == 'admin' and password == 'password123':
        return True
    return False
"""

transformed_prompt = code_review(code_to_review)
print(transformed_prompt)

# Method 2: Using inline syntax with apply_dynamic_decorators
prompt_with_inline = f"""
+++CodeReview(focus="security", severity="critical", suggest_fixes=true)
{code_to_review}
"""

transformed_prompt_inline = apply_dynamic_decorators(prompt_with_inline)
print(transformed_prompt_inline)
```

## Step 4: Test with an LLM

Finally, let's test our decorator with an LLM:

```python
import openai

openai.api_key = "your-api-key-here"

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": transformed_prompt}
    ],
    temperature=0.7,
    max_tokens=1000
)

print(response.choices[0].message.content)
```

## Alternative: Using Class-Based Decorators

For more complex decorators, you might prefer to use a class-based approach:

```python
from prompt_decorators import DecoratorBase

class CodeReviewDecorator(DecoratorBase):
    """A decorator for conducting code reviews."""

    def __init__(self, focus="all", severity="all", suggest_fixes=True):
        """
        Initialize the CodeReview decorator.

        Args:
            focus (str): What aspects to focus on in the review
            severity (str): Whether to include only issues of specific severity
            suggest_fixes (bool): Whether to suggest specific fixes for issues
        """
        super().__init__()  # Initialize the base class
        self.focus = focus
        self.severity = severity
        self.suggest_fixes = suggest_fixes

    def transform(self, text):
        """Transform the input text into a code review prompt."""
        instruction = "Please perform a code review on the following code. "

        # Add focus-specific instructions
        if self.focus == "security":
            instruction += "Focus primarily on security issues. "
        elif self.focus == "performance":
            instruction += "Focus primarily on performance issues. "
        # ... other focus options ...

        # Add the rest of the instruction logic

        return instruction + text

# Register the class-based decorator
from prompt_decorators import register_decorator

# Note: There's no separate register_decorator_class function,
# use the regular register_decorator function
register_decorator(CodeReviewDecorator,
                  name="ClassBasedCodeReview",
                  description="Class-based code review decorator",
                  category="Development")
```

## Conclusion

In this tutorial, you've learned how to:

1. Define a custom decorator with parameters
2. Implement a transform function in Python
3. Register the decorator with the framework
4. Use the decorator both programmatically and with inline syntax
5. Create class-based decorators for more complex scenarios

Your `CodeReview` decorator can now be used consistently across your applications to get better code reviews from LLMs. You can extend this pattern to create other specialized decorators for your specific needs.

## Next Steps

- Try creating decorators for other development tasks (e.g., documentation generation, unit test creation)
- Explore combining multiple decorators for more complex scenarios
- Consider developing decorator extensions for specific domains

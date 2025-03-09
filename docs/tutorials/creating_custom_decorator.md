# Tutorial: Creating a Custom Decorator

This tutorial will guide you through the process of creating a custom decorator with the Prompt Decorators framework. We'll create a practical, reusable decorator that you can adapt for your own use cases.

## Prerequisites

Before starting this tutorial, ensure you have:

1. Installed the Prompt Decorators package (`pip install prompt-decorators`)
2. Basic understanding of Python
3. Familiarity with the [core concepts](../concepts.md) of the framework

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
    transform_function="""
    let instruction = "Please perform a code review on the following code. ";

    // Add focus-specific instructions
    if (focus === "security") {
        instruction += "Focus primarily on security issues such as injection vulnerabilities, " +
            "authentication problems, data exposure, and other security concerns. ";
    } else if (focus === "performance") {
        instruction += "Focus primarily on performance issues such as inefficient algorithms, " +
            "resource leaks, unnecessary operations, and optimization opportunities. ";
    } else if (focus === "readability") {
        instruction += "Focus primarily on code readability including naming conventions, " +
            "documentation, code organization, and adherence to style guidelines. ";
    } else {
        instruction += "Evaluate all aspects including security, performance, readability, " +
            "maintainability, and adherence to best practices. ";
    }

    // Add severity-specific instructions
    if (severity === "critical") {
        instruction += "Only highlight critical issues that could lead to serious vulnerabilities or failures. ";
    } else if (severity === "major") {
        instruction += "Focus on major and critical issues, ignoring minor stylistic concerns. ";
    } else {
        instruction += "Include issues of all severity levels, from critical to minor. ";
    }

    // Add fix suggestion instructions
    if (suggest_fixes) {
        instruction += "For each issue identified, suggest a specific fix with example code. ";
    } else {
        instruction += "Identify issues without providing specific fix implementations. ";
    }

    // Formatting instructions
    instruction += "Format your review as follows:\\n" +
        "1. Summary of the code and its purpose (based on the code itself)\\n" +
        "2. Overall assessment\\n" +
        "3. Issues identified (with severity level for each)";

    if (suggest_fixes) {
        instruction += "\\n4. Suggested fixes with code examples";
    }

    instruction += "\\n\\nHere's the code to review:\\n\\n";

    return instruction + text;
    """
)
```

## Step 3: Register the Decorator

Next, register the decorator to make it available:

```python
register_decorator(code_review_decorator)
```

## Step 4: Test the Decorator

Now let's test our decorator with a simple code snippet:

```python
# Sample code for review
code_to_review = """
def calculate_discount(price, discount_percent):
    # Calculate discounted price
    discounted = price * (1 - discount_percent / 100)
    return discounted

# Apply discount to all products
product_prices = [100, 200, 300, -50, 500]
discounted_prices = []
for price in product_prices:
    new_price = calculate_discount(price, 10)
    discounted_prices.append(new_price)
print("Discounted prices:", discounted_prices)
"""

# Test the decorator programmatically
code_review = create_decorator_instance("CodeReview", focus="security", severity="all", suggest_fixes=True)
transformed_prompt = code_review(code_to_review)

print("Transformed Prompt:")
print("-" * 80)
print(transformed_prompt)
print("-" * 80)
```

## Step 5: Test with an LLM

Finally, let's send our decorated prompt to an LLM (this example uses OpenAI, but you can use any provider):

```python
import openai

openai.api_key = "your-api-key-here"

response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an expert code reviewer with years of experience."},
        {"role": "user", "content": transformed_prompt}
    ],
    temperature=0.7,
    max_tokens=1500
)

print("\nLLM Response:")
print("-" * 80)
print(response.choices[0].message.content)
```

## Complete Example

Here's the complete example that you can run:

```python
from prompt_decorators import (
    DecoratorDefinition,
    register_decorator,
    create_decorator_instance,
    apply_dynamic_decorators
)
import openai

# Define the CodeReview decorator
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
    transform_function="""
    let instruction = "Please perform a code review on the following code. ";

    // Add focus-specific instructions
    if (focus === "security") {
        instruction += "Focus primarily on security issues such as injection vulnerabilities, " +
            "authentication problems, data exposure, and other security concerns. ";
    } else if (focus === "performance") {
        instruction += "Focus primarily on performance issues such as inefficient algorithms, " +
            "resource leaks, unnecessary operations, and optimization opportunities. ";
    } else if (focus === "readability") {
        instruction += "Focus primarily on code readability including naming conventions, " +
            "documentation, code organization, and adherence to style guidelines. ";
    } else {
        instruction += "Evaluate all aspects including security, performance, readability, " +
            "maintainability, and adherence to best practices. ";
    }

    // Add severity-specific instructions
    if (severity === "critical") {
        instruction += "Only highlight critical issues that could lead to serious vulnerabilities or failures. ";
    } else if (severity === "major") {
        instruction += "Focus on major and critical issues, ignoring minor stylistic concerns. ";
    } else {
        instruction += "Include issues of all severity levels, from critical to minor. ";
    }

    // Add fix suggestion instructions
    if (suggest_fixes) {
        instruction += "For each issue identified, suggest a specific fix with example code. ";
    } else {
        instruction += "Identify issues without providing specific fix implementations. ";
    }

    // Formatting instructions
    instruction += "Format your review as follows:\\n" +
        "1. Summary of the code and its purpose (based on the code itself)\\n" +
        "2. Overall assessment\\n" +
        "3. Issues identified (with severity level for each)";

    if (suggest_fixes) {
        instruction += "\\n4. Suggested fixes with code examples";
    }

    instruction += "\\n\\nHere's the code to review:\\n\\n";

    return instruction + text;
    """
)

# Register the decorator
register_decorator(code_review_decorator)

# Sample code for review
code_to_review = """
def calculate_discount(price, discount_percent):
    # Calculate discounted price
    discounted = price * (1 - discount_percent / 100)
    return discounted

# Apply discount to all products
product_prices = [100, 200, 300, -50, 500]
discounted_prices = []
for price in product_prices:
    new_price = calculate_discount(price, 10)
    discounted_prices.append(new_price)
print("Discounted prices:", discounted_prices)
"""

# Test inline decorator syntax
inline_prompt = f"""
+++CodeReview(focus=security, severity=all, suggest_fixes=true)
{code_to_review}
"""

transformed_prompt = apply_dynamic_decorators(inline_prompt)

# Send to OpenAI (replace with your API key)
openai.api_key = "your-api-key-here"

response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an expert code reviewer with years of experience."},
        {"role": "user", "content": transformed_prompt}
    ],
    temperature=0.7,
    max_tokens=1500
)

print("LLM Response:")
print("-" * 80)
print(response.choices[0].message.content)
```

## Variations and Extensions

Here are some ways you can modify and extend this decorator:

### Add Language-Specific Reviews

Extend the decorator to handle different programming languages:

```python
code_review_decorator = DecoratorDefinition(
    name="CodeReview",
    description="Transforms a prompt into instructions for conducting a code review",
    category="Development",
    parameters=[
        # ... other parameters ...
        {
            "name": "language",
            "type": "enum",
            "description": "Programming language of the code",
            "enum": ["python", "javascript", "java", "csharp", "go", "auto"],
            "default": "auto"
        }
    ],
    transform_function="""
    let instruction = "Please perform a code review on the following code. ";

    // Language-specific instructions
    if (language !== "auto") {
        instruction += `This is ${language} code. Apply best practices specific to ${language}. `;
    } else {
        instruction += "Determine the language from the code and apply appropriate best practices. ";
    }

    // ... rest of the transformation function ...
    """
)
```

### Add Team Standards

Customize the decorator for your team's specific standards:

```python
code_review_decorator = DecoratorDefinition(
    name="TeamCodeReview",
    description="Transforms a prompt into instructions for conducting a code review using team standards",
    category="Development",
    parameters=[
        # ... other parameters ...
        {
            "name": "team_standards",
            "type": "enum",
            "description": "Which team's standards to apply",
            "enum": ["backend", "frontend", "data", "devops"],
            "default": "backend"
        }
    ],
    transform_function="""
    let instruction = "Please perform a code review on the following code. ";

    // Add team-specific standards
    if (team_standards === "backend") {
        instruction += "Apply our backend team standards: " +
            "1. All functions must have type annotations. " +
            "2. Use meaningful variable names. " +
            "3. Functions should do one thing well. " +
            "4. Include error handling for all external calls. ";
    } else if (team_standards === "frontend") {
        instruction += "Apply our frontend team standards: " +
            "1. Components should be reusable. " +
            "2. Use consistent naming conventions. " +
            "3. Ensure accessibility compliance. " +
            "4. Avoid direct DOM manipulation. ";
    }
    // ... other team standards ...

    // ... rest of the transformation function ...
    """
)
```

## Best Practices

When creating your decorators, keep these best practices in mind:

1. **Keep Transforms Focused**: Each decorator should do one thing well
2. **Provide Good Defaults**: Make your decorators usable without requiring parameters
3. **Document Thoroughly**: Include clear descriptions for your decorator and its parameters
4. **Handle Edge Cases**: Consider how your decorator behaves with unusual inputs
5. **Test with Multiple Models**: Different LLMs may respond differently to the same instructions

## Next Steps

Now that you've created your first custom decorator, you can:

1. [Combine decorators](combining_decorators.md) for more complex behaviors
2. Develop [domain-specific decorator packages](extension_development.md)
3. Share your decorator with the community
4. Explore the [MCP integration](../integrations/mcp.md) to use your decorators with Claude Desktop

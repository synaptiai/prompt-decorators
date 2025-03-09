# Creating Decorators

This guide explains how to create your own custom decorators with the Prompt Decorators framework.

## Overview

Custom decorators allow you to extend the framework with your own specialized behaviors. This is useful for:

- Creating domain-specific decorators for your field
- Building organization-specific prompt enhancements
- Optimizing decorators for particular LLM providers
- Implementing novel prompt engineering techniques

## Decorator Structure

Each decorator consists of:

1. A **name** that uniquely identifies it
2. A **description** explaining its purpose
3. A **category** for organizational purposes
4. A set of **parameters** that control its behavior
5. A **transform function** that applies the decoration

## Creating a Basic Decorator

### Using DecoratorDefinition

The simplest way to create a custom decorator is using the `DecoratorDefinition` class:

```python
from prompt_decorators import (
    DecoratorDefinition,
    register_decorator,
    create_decorator_instance
)

# Define a custom decorator
my_decorator_def = DecoratorDefinition(
    name="CustomPrefix",
    description="Adds a custom prefix to the prompt",
    category="Format",
    parameters=[
        {
            "name": "prefix",
            "type": "string",
            "description": "Text to add before the prompt",
            "default": "IMPORTANT: "
        }
    ],
    transform_function="return prefix + text;"
)

# Register the decorator for use
register_decorator(my_decorator_def)

# Create and use an instance of your decorator
custom_prefix = create_decorator_instance("CustomPrefix", prefix="ATTENTION: ")
result = custom_prefix("Please review this document carefully.")
print(result)  # "ATTENTION: Please review this document carefully."
```

### Transform Function

The `transform_function` is the heart of your decorator. It's a JavaScript function (as a string) that takes the input text and applies the decoration. The function has access to:

- All defined parameters (e.g., `prefix` in the example above)
- The input text as `text`
- Must return the transformed text

Examples of transform functions:

```javascript
// Simple addition of prefix and suffix
"return prefix + text + suffix;"

// Conditional transformation
"if (style === 'formal') { return 'Formally: ' + text; } else { return 'Casually: ' + text; }"

// Text manipulation
"return text.split('.').join('.\n').trim();"
```

### Parameters

Parameters allow your decorator to be customized. Each parameter has these properties:

- `name`: The parameter's identifier
- `type`: Data type (`string`, `boolean`, `number`, `enum`)
- `description`: Documentation for the parameter
- `default`: Default value if not specified
- `enum` (optional): List of allowed values for enum types

Example of complex parameters:

```python
parameters=[
    {
        "name": "style",
        "type": "enum",
        "description": "The style of formatting to apply",
        "enum": ["formal", "casual", "technical"],
        "default": "formal"
    },
    {
        "name": "include_timestamp",
        "type": "boolean",
        "description": "Whether to include a timestamp",
        "default": False
    },
    {
        "name": "indent_level",
        "type": "number",
        "description": "Level of indentation (0-4)",
        "default": 0
    }
]
```

## Advanced Decorator Creation

### Composition of Decorators

You can create decorators that compose other decorators:

```python
composite_decorator_def = DecoratorDefinition(
    name="FormalSteps",
    description="Combines formal tone with step-by-step instructions",
    category="Composite",
    parameters=[
        {
            "name": "numbered",
            "type": "boolean",
            "description": "Whether to number the steps",
            "default": True
        }
    ],
    # First apply Tone(style=formal), then StepByStep with the numbered parameter
    transform_function="""
    const toneDecorator = createDecoratorInstance('Tone', { style: 'formal' });
    const stepDecorator = createDecoratorInstance('StepByStep', { numbered: numbered });
    return stepDecorator(toneDecorator(text));
    """
)
```

### Conditional Logic

You can use conditional logic in your transform function:

```python
conditional_decorator_def = DecoratorDefinition(
    name="AdaptiveResponse",
    description="Adapts the response based on complexity",
    category="Adaptive",
    parameters=[
        {
            "name": "complexity",
            "type": "enum",
            "description": "Complexity level of the input",
            "enum": ["simple", "moderate", "complex"],
            "default": "moderate"
        }
    ],
    transform_function="""
    if (complexity === 'simple') {
        const eli5 = createDecoratorInstance('ELI5');
        return eli5(text);
    } else if (complexity === 'moderate') {
        const audience = createDecoratorInstance('Audience', { level: 'intermediate' });
        return audience(text);
    } else {
        const detailed = createDecoratorInstance('Detailed', { depth: 'comprehensive' });
        return detailed(text);
    }
    """
)
```

### Advanced Text Processing

For more complex transformations, you can perform detailed text processing:

```python
text_processor_def = DecoratorDefinition(
    name="QueryFocus",
    description="Focuses a query on specific aspects",
    category="Query",
    parameters=[
        {
            "name": "aspects",
            "type": "string",
            "description": "Comma-separated list of aspects to focus on",
            "default": "pros,cons"
        }
    ],
    transform_function="""
    const aspectList = aspects.split(',').map(a => a.trim());
    let result = "Please focus your analysis on the following aspects:\\n";

    for (let i = 0; i < aspectList.length; i++) {
        result += `${i+1}. ${aspectList[i]}\\n`;
    }

    result += "\\n" + text;
    return result;
    """
)
```

## Best Practices

### Parameter Design

1. **Default Values**: Always provide sensible default values for parameters
2. **Clear Names**: Use descriptive, self-explanatory parameter names
3. **Limited Options**: For enum types, limit options to a manageable set
4. **Documentation**: Thoroughly document each parameter's purpose and effect

### Transform Function

1. **Keep It Simple**: Prefer simple transforms that do one thing well
2. **Error Handling**: Include error handling for unexpected inputs
3. **Performance**: Avoid unnecessary complexity that could impact performance
4. **Testability**: Create transforms that can be easily tested

### Documentation

1. **Clear Description**: Provide a concise, clear description of what your decorator does
2. **Examples**: Include examples of how to use your decorator
3. **Category**: Choose an appropriate category that matches your decorator's purpose
4. **Compatibility**: Document any known conflicts with other decorators

## Testing Your Decorators

To test your custom decorators:

```python
# Define and register your decorator
my_decorator_def = DecoratorDefinition(...)
register_decorator(my_decorator_def)

# Test with different inputs
test_cases = [
    "Simple test case",
    "Another test with different format",
    "Edge case with special characters: @#$%^&*()"
]

my_decorator = create_decorator_instance("MyDecorator", param1="value1")

for test in test_cases:
    transformed = my_decorator(test)
    print(f"Original: {test}")
    print(f"Transformed: {transformed}")
    print("-" * 50)
```

## Loading Decorators from Files

For reusability, you can define decorators in JSON files:

```json
{
  "name": "BulletedSummary",
  "description": "Creates a bulleted summary format",
  "category": "Format",
  "parameters": [
    {
      "name": "points",
      "type": "number",
      "description": "Number of bullet points to request",
      "default": 5
    },
    {
      "name": "style",
      "type": "enum",
      "description": "Bullet point style",
      "enum": ["dash", "star", "arrow"],
      "default": "dash"
    }
  ],
  "transform_function": "return `Please summarize the following into ${points} key points using ${style === 'dash' ? '-' : style === 'star' ? '*' : '→'} as bullet points:\\n\\n${text}`;"
}
```

Load and register this decorator:

```python
import json
from prompt_decorators import DecoratorDefinition, register_decorator

# Load from a JSON file
with open("path/to/my_decorators.json", "r") as f:
    decorators_data = json.load(f)

# If it's a single decorator
decorator_def = DecoratorDefinition(**decorators_data)
register_decorator(decorator_def)

# If it's an array of decorators
for decorator_data in decorators_data:
    decorator_def = DecoratorDefinition(**decorator_data)
    register_decorator(decorator_def)
```

## Decorator Registry Management

### Listing Decorators

```python
from prompt_decorators import get_available_decorators

# Get all decorators
all_decorators = get_available_decorators()

# Filter by category
format_decorators = [d for d in all_decorators if d.category == "Format"]

# Find a specific decorator
reasoning_decorator = next((d for d in all_decorators if d.name == "Reasoning"), None)
```

### Decorator Persistence

To persist your custom decorators across sessions, you can:

1. Save them to JSON files
2. Load and register them at application startup
3. Organize them into decorator packages

## Domain-Specific Examples

### Scientific Research Decorator

```python
scientific_method_def = DecoratorDefinition(
    name="ScientificMethod",
    description="Structures response according to scientific method",
    category="Domain",
    parameters=[
        {
            "name": "include_abstract",
            "type": "boolean",
            "description": "Whether to include an abstract section",
            "default": True
        }
    ],
    transform_function="""
    let result = "Please structure your response according to the scientific method with the following sections:\\n";

    if (include_abstract) {
        result += "1. Abstract: A brief summary of the entire analysis\\n";
    }

    result += `${include_abstract ? "2" : "1"}. Question/Problem: Clearly define the research question\\n`;
    result += `${include_abstract ? "3" : "2"}. Hypothesis: Formulate a testable hypothesis\\n`;
    result += `${include_abstract ? "4" : "3"}. Methodology: Describe how to test the hypothesis\\n`;
    result += `${include_abstract ? "5" : "4"}. Results: Present the expected findings\\n`;
    result += `${include_abstract ? "6" : "5"}. Discussion: Interpret the results and their implications\\n`;
    result += `${include_abstract ? "7" : "6"}. Conclusion: Summarize the findings and suggest next steps\\n\\n`;

    result += text;
    return result;
    """
)
```

### Business Analysis Decorator

```python
business_analysis_def = DecoratorDefinition(
    name="BusinessAnalysis",
    description="Structures response as a business analysis",
    category="Domain",
    parameters=[
        {
            "name": "framework",
            "type": "enum",
            "description": "Business analysis framework to use",
            "enum": ["SWOT", "Porter", "PESTEL"],
            "default": "SWOT"
        }
    ],
    transform_function="""
    let result = `Please analyze the following using a ${framework} framework:\\n\\n`;

    if (framework === "SWOT") {
        result += "Structure your analysis with these sections:\\n";
        result += "1. Strengths: Internal positive factors\\n";
        result += "2. Weaknesses: Internal negative factors\\n";
        result += "3. Opportunities: External positive factors\\n";
        result += "4. Threats: External negative factors\\n\\n";
    } else if (framework === "Porter") {
        result += "Structure your analysis using Porter's Five Forces:\\n";
        result += "1. Threat of new entrants\\n";
        result += "2. Bargaining power of buyers\\n";
        result += "3. Bargaining power of suppliers\\n";
        result += "4. Threat of substitute products or services\\n";
        result += "5. Intensity of competitive rivalry\\n\\n";
    } else if (framework === "PESTEL") {
        result += "Structure your analysis using PESTEL framework:\\n";
        result += "1. Political factors\\n";
        result += "2. Economic factors\\n";
        result += "3. Social factors\\n";
        result += "4. Technological factors\\n";
        result += "5. Environmental factors\\n";
        result += "6. Legal factors\\n\\n";
    }

    result += text;
    return result;
    """
)
```

## Next Steps

- Explore the [Tutorial: Creating a Custom Decorator](tutorials/creating_custom_decorator.md) for step-by-step examples
- Learn about [Tutorial: Combining Decorators](tutorials/combining_decorators.md) for advanced use cases
- See the [specification](prompt-decorators-specification-v1.0.md) for technical details of the decorator system

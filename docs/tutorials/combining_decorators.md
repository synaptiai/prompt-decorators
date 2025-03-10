# Tutorial: Combining Decorators

This tutorial will guide you through the process of combining multiple decorators to create sophisticated prompt transformations. By stacking decorators, you can achieve complex behaviors that would be difficult to implement with a single decorator.

## Prerequisites

Before starting this tutorial, ensure you have:

1. Installed the Prompt Decorators package (`pip install prompt-decorators`)
2. Completed the [Creating Custom Decorators](creating_custom_decorator.md) tutorial
3. Familiarity with the [core concepts](../concepts.md) of the framework

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

For reusable combinations of decorators, you can create composite decorators that encapsulate multiple transformations:

```python
from prompt_decorators import DecoratorDefinition, register_decorator

# Define a composite decorator
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
    transform_function="""
    // Create instances of the component decorators
    const persona = createDecoratorInstance('Persona', { role: 'senior developer' });
    const steps = createDecoratorInstance('StepByStep', { numbered: true });
    const audience = createDecoratorInstance('Audience', { level: 'technical' });
    const outputFormat = createDecoratorInstance('OutputFormat', { format: format });

    // Apply conditional decorators
    let result = persona(steps(audience(text)));
    result = outputFormat(result);

    // Add examples instruction if needed
    if (examples) {
        result = "Please include practical code examples for each step.\\n\\n" + result;
    }

    return result;
    """
)

# Register the composite decorator
register_decorator(technical_tutorial)

# Use the composite decorator
from prompt_decorators import create_decorator_instance

tutorial = create_decorator_instance("TechnicalTutorial", format="markdown", examples=True)
transformed = tutorial("Explain how to implement a binary search algorithm.")
```

When creating composite decorators:
- You encapsulate complexity behind a simpler interface
- You ensure consistent application of multiple decorators
- You can provide parameters that control the internal decorators

### Example: Educational Content Generator

Here's a more advanced composite decorator for educational content:

```python
from prompt_decorators import DecoratorDefinition, register_decorator, create_decorator_instance

educational_content = DecoratorDefinition(
    name="EducationalContent",
    description="Creates educational content with appropriate structure and style",
    category="Education",
    parameters=[
        {
            "name": "level",
            "type": "enum",
            "description": "Target audience level",
            "enum": ["elementary", "middle_school", "high_school", "undergraduate", "graduate"],
            "default": "high_school"
        },
        {
            "name": "structure",
            "type": "enum",
            "description": "Content structure",
            "enum": ["steps", "outline", "narrative", "q_and_a"],
            "default": "steps"
        },
        {
            "name": "visuals",
            "type": "boolean",
            "description": "Include descriptions of visual aids",
            "default": True
        },
        {
            "name": "assessment",
            "type": "boolean",
            "description": "Include assessment questions",
            "default": False
        }
    ],
    transform_function="""
    // Map education level to audience level
    let audienceLevel = "intermediate";
    if (level === "elementary" || level === "middle_school") {
        audienceLevel = "beginner";
    } else if (level === "graduate") {
        audienceLevel = "expert";
    }

    // Map structure to appropriate decorator
    let structureDecorator;
    if (structure === "steps") {
        structureDecorator = createDecoratorInstance('StepByStep', { numbered: true });
    } else if (structure === "outline") {
        structureDecorator = createDecoratorInstance('Outline', { depth: 3 });
    } else if (structure === "narrative") {
        structureDecorator = createDecoratorInstance('Narrative', { structure: 'classic' });
    } else if (structure === "q_and_a") {
        structureDecorator = createDecoratorInstance('QAndA');
    }

    // Create audience and persona decorators
    const audience = createDecoratorInstance('Audience', { level: audienceLevel });

    // Create appropriate persona based on level
    let personaRole = "teacher";
    if (level === "undergraduate" || level === "graduate") {
        personaRole = "professor";
    } else if (level === "elementary") {
        personaRole = "elementary teacher";
    }
    const persona = createDecoratorInstance('Persona', { role: personaRole });

    // Apply the basic transformations
    let result = persona(structureDecorator(audience(text)));

    // Add instructions for visuals if requested
    if (visuals) {
        result = "Please include descriptions of appropriate visual aids or diagrams that would help explain the concepts.\\n\\n" + result;
    }

    // Add assessment questions if requested
    if (assessment) {
        const assessmentDecorator = createDecoratorInstance('Assessment', { questionCount: 5, includeAnswers: true });
        result = assessmentDecorator(result);
    }

    return result;
    """
)

# Register the composite decorator
register_decorator(educational_content)

# Example usage
educational = create_decorator_instance(
    "EducationalContent",
    level="high_school",
    structure="steps",
    visuals=True,
    assessment=True
)

lesson = educational("Explain the process of cell division (mitosis).")
```

## Advanced Topics: Handling Decorator Conflicts

When combining decorators, you may encounter conflicts. The framework handles conflicts by giving precedence to later decorators, but you can also explicitly manage them:

### Incompatible Decorators

Some decorators are inherently incompatible:

```python
# These decorators have conflicting behaviors
prompt = """
+++Concise(level="high")
+++Detailed(depth="comprehensive")
Explain quantum computing.
"""
```

In this case, `Detailed` will win because it appears later. To manage this:

1. Be aware of potential conflicts (see [Compatibility](../compatibility.md))
2. Order your decorators carefully, with higher priority decorators later in the sequence
3. Consider using composite decorators that are designed to work together

### Parameter Conflicts

Parameter conflicts can occur when decorators modify the same aspect:

```python
# Parameter conflict example
prompt = """
+++OutputFormat(format="json")
+++OutputFormat(format="markdown")
Provide a list of popular programming languages.
"""
```

Again, the later parameter (`format="markdown"`) will override the earlier one.

## Real-World Example: Research Paper Generator

Let's build a comprehensive example that combines multiple decorators to generate research paper outlines:

```python
from prompt_decorators import (
    DecoratorDefinition,
    register_decorator,
    create_decorator_instance,
    apply_dynamic_decorators
)
import openai

# Define a composite decorator for research papers
research_paper = DecoratorDefinition(
    name="ResearchPaper",
    description="Generates research paper content with appropriate academic structure and style",
    category="Academic",
    parameters=[
        {
            "name": "field",
            "type": "enum",
            "description": "Academic field",
            "enum": ["computer_science", "biology", "psychology", "physics", "economics"],
            "default": "computer_science"
        },
        {
            "name": "paper_section",
            "type": "enum",
            "description": "Which section of the paper to generate",
            "enum": ["abstract", "introduction", "methodology", "results", "discussion", "conclusion", "outline"],
            "default": "outline"
        },
        {
            "name": "citation_style",
            "type": "enum",
            "description": "Citation style",
            "enum": ["APA", "MLA", "Chicago", "IEEE", "Harvard"],
            "default": "APA"
        },
        {
            "name": "include_citations",
            "type": "boolean",
            "description": "Whether to include citations",
            "default": True
        }
    ],
    transform_function="""
    // Map field to persona role
    const fieldMap = {
        computer_science: "computer scientist",
        biology: "biologist",
        psychology: "psychologist",
        physics: "physicist",
        economics: "economist"
    };
    const role = fieldMap[field] || "researcher";

    // Basic decorators
    const persona = createDecoratorInstance('Persona', { role: role });
    const academic = createDecoratorInstance('Academic', { style: 'scientific' });
    const outputFormat = createDecoratorInstance('OutputFormat', { format: 'markdown' });

    // Section-specific decorators
    let sectionDecorator;
    let instruction = "";

    if (paper_section === "abstract") {
        sectionDecorator = createDecoratorInstance('Concise', { level: 'high' });
        instruction = "Please write an abstract for a research paper on the following topic. " +
            "Keep it between 150-250 words and focus on the research question, methodology, " +
            "key findings, and implications.\\n\\n";
    } else if (paper_section === "introduction") {
        sectionDecorator = createDecoratorInstance('FirstPrinciples', { depth: 3 });
        instruction = "Please write an introduction section for a research paper on the following topic. " +
            "Include background information, the research gap being addressed, the research question, " +
            "and the significance of the study.\\n\\n";
    } else if (paper_section === "methodology") {
        sectionDecorator = createDecoratorInstance('StepByStep', { numbered: true });
        instruction = "Please write a methodology section for a research paper on the following topic. " +
            "Detail the research design, participants/data sources, procedures, measures, and analysis methods.\\n\\n";
    } else if (paper_section === "results") {
        sectionDecorator = createDecoratorInstance('Detailed', { depth: 'comprehensive' });
        instruction = "Please write a results section for a research paper on the following topic. " +
            "Present the findings without interpretation, using appropriate organizational structure.\\n\\n";
    } else if (paper_section === "discussion") {
        sectionDecorator = createDecoratorInstance('Reasoning', { depth: 'comprehensive' });
        instruction = "Please write a discussion section for a research paper on the following topic. " +
            "Interpret the results, relate them to prior work, address limitations, and suggest future directions.\\n\\n";
    } else if (paper_section === "conclusion") {
        sectionDecorator = createDecoratorInstance('Concise', { level: 'moderate' });
        instruction = "Please write a conclusion section for a research paper on the following topic. " +
            "Summarize the main findings and their implications without introducing new information.\\n\\n";
    } else {
        // Default: outline
        sectionDecorator = createDecoratorInstance('Outline', { depth: 3 });
        instruction = "Please create a detailed outline for a research paper on the following topic. " +
            "Include all major sections and subsections with brief descriptions of their content.\\n\\n";
    }

    // Citation decorator if requested
    let citationDecorator = null;
    if (include_citations) {
        citationDecorator = createDecoratorInstance('CiteSources', { style: citation_style });
    }

    // Apply transformations in sequence
    let result = instruction + text;
    result = academic(result);
    result = sectionDecorator(result);
    if (citationDecorator) {
        result = citationDecorator(result);
    }
    result = persona(result);
    result = outputFormat(result);

    return result;
    """
)

# Register the decorator
register_decorator(research_paper)

# Create a research paper outline
research = create_decorator_instance(
    "ResearchPaper",
    field="computer_science",
    paper_section="outline",
    citation_style="IEEE",
    include_citations=True
)

topic = "The impact of transformer architectures on natural language processing tasks"
paper_outline = research(topic)

# Send to an LLM
openai.api_key = "your-api-key-here"
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": paper_outline}],
    temperature=0.7
)

print(response.choices[0].message.content)
```

## Best Practices for Combining Decorators

When combining decorators, follow these best practices:

1. **Consider Order Carefully**: The sequence of decorators affects the final result
2. **Minimize Conflicts**: Avoid combining inherently contradictory decorators
3. **Create Composites for Common Patterns**: If you frequently use a specific combination, create a composite decorator
4. **Test Thoroughly**: Different LLMs may handle combinations differently
5. **Watch Token Limits**: Multiple decorators increase instruction length, which counts against token limits
6. **Document Combinations**: Keep track of effective decorator combinations for different tasks

## Next Steps

Now that you've learned how to combine decorators, you can:

1. Explore [extension development](extension_development.md) to create decorator packages
2. Dive into advanced techniques like conditional decorator application
3. Create domain-specific composite decorators for your use case
4. Experiment with the [MCP integration](../integrations/mcp.md) to use decorator combinations with Claude Desktop

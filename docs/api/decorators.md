# Decorators API

The Prompt Decorators framework provides a rich collection of built-in decorators that can be used to enhance prompt engineering for Large Language Models (LLMs). This page provides an overview of all available decorators and how to use them.

## About Decorators

Decorators are reusable components that apply specific transformations to prompts. They can enhance prompts by adding structure, guiding the model's reasoning, or specifying output formats. Decorators can be combined to create complex prompt engineering patterns.

## Using Decorators

Basic usage of decorators involves importing the desired decorator from the `prompt_decorators.decorators` module, instantiating it with appropriate parameters, and applying it to a prompt:

```python
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to a prompt
prompt = "Explain quantum entanglement."
decorated_prompt = output_format.apply(reasoning.apply(prompt))
```

You can also use the DecoratedRequest class for more convenient handling:

```python
from prompt_decorators.core.request import DecoratedRequest
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create a decorated request
request = DecoratedRequest(
    prompt="Explain quantum mechanics.",
    decorators=[
        Reasoning(style="detailed", show_working=True),
        OutputFormat(format_type="markdown", pretty_print=True)
    ],
    model="gpt-4",
    api_params={
        "temperature": 0.7,
        "max_tokens": 1000
    }
)

# Apply all decorators
decorated_prompt = request.apply_decorators()
```

## Available Decorators

The framework provides numerous decorators organized into different categories:

### Reasoning Decorators

These decorators focus on improving the reasoning process of the LLM:

- [Reasoning](decorators/Reasoning.md): Structures the model's reasoning process
- [Abductive](decorators/Abductive.md): Applies abductive reasoning (inference to best explanation)
- [Deductive](decorators/Deductive.md): Applies deductive reasoning (from general to specific)
- [Inductive](decorators/Inductive.md): Applies inductive reasoning (patterns to general principles)
- [FirstPrinciples](decorators/FirstPrinciples.md): Applies first principles reasoning
- [StepByStep](decorators/StepByStep.md): Break down problem solving into sequential steps
- [TreeOfThought](decorators/TreeOfThought.md): Explores multiple reasoning paths

### Output Format Decorators

These decorators control how information is presented:

- [OutputFormat](decorators/OutputFormat.md): Specifies output format (markdown, JSON, etc.)
- [TableFormat](decorators/TableFormat.md): Presents information in tabular format
- [Bullet](decorators/Bullet.md): Organizes output as bullet points
- [Schema](decorators/Schema.md): Enforces a specific data schema

### Analysis Decorators

These decorators focus on detailed analysis:

- [Detailed](decorators/Detailed.md): Enhances analysis with more details
- [Concise](decorators/Concise.md): Provides focused, brief responses
- [Balanced](decorators/Balanced.md): Presents balanced viewpoints
- [RootCause](decorators/RootCause.md): Performs root cause analysis
- [Comparison](decorators/Comparison.md): Compares multiple items or concepts
- [Extremes](decorators/Extremes.md): Explores extreme cases or boundaries
- [FindGaps](decorators/FindGaps.md): Identifies gaps in analysis or reasoning
- [Limitations](decorators/Limitations.md): Explicitly states limitations
- [NegativeSpace](decorators/NegativeSpace.md): Considers unexplored or implicit aspects
- [Summary](decorators/Summary.md): Provides a concise summary

### Perspective Decorators

These decorators inject specific viewpoints:

- [Contrarian](decorators/Contrarian.md): Presents opposing viewpoints
- [Steelman](decorators/Steelman.md): Presents the strongest form of opposing arguments
- [Debate](decorators/Debate.md): Structures response as a debate
- [PeerReview](decorators/PeerReview.md): Evaluates as if conducting peer review
- [RedTeam](decorators/RedTeam.md): Critical analysis seeking vulnerabilities
- [AsExpert](decorators/AsExpert.md): Responds from expertise in a specific domain
- [Audience](decorators/Audience.md): Tailors content for specific audiences
- [Persona](decorators/Persona.md): Adopts a specific persona or character
- [ELI5](decorators/ELI5.md): Explains Like I'm 5 (simplifies complex topics)

### Creativity & Style Decorators

These decorators modify tone and creativity:

- [Creative](decorators/Creative.md): Enhances creative elements
- [ForcedAnalogy](decorators/ForcedAnalogy.md): Uses analogies to explain concepts
- [Analogical](decorators/Analogical.md): Applies analogical reasoning
- [Narrative](decorators/Narrative.md): Structures content as a narrative
- [Tone](decorators/Tone.md): Adjusts the tone of the response
- [StyleShift](decorators/StyleShift.md): Changes writing or explanation style
- [Professional](decorators/Professional.md): Ensures a professional tone
- [Academic](decorators/Academic.md): Uses academic writing style
- [Motivational](decorators/Motivational.md): Adds motivational elements

### Critical Thinking Decorators

These decorators enhance critical evaluation:

- [FactCheck](decorators/FactCheck.md): Verifies factual accuracy
- [BlindSpots](decorators/BlindSpots.md): Identifies potential blind spots
- [StressTest](decorators/StressTest.md): Tests ideas under challenging conditions
- [Confidence](decorators/Confidence.md): States confidence levels in assertions
- [Uncertainty](decorators/Uncertainty.md): Explicitly deals with uncertainty
- [QualityMetrics](decorators/QualityMetrics.md): Evaluates using quality metrics
- [Socratic](decorators/Socratic.md): Uses Socratic questioning

### Organization Decorators

These decorators add structure and organization:

- [Prioritize](decorators/Prioritize.md): Prioritizes information by importance
- [Priority](decorators/Priority.md): Similar to Prioritize with different parameters
- [Outline](decorators/Outline.md): Structures content as an outline
- [MECE](decorators/MECE.md): Ensures Mutually Exclusive, Collectively Exhaustive categories
- [Timeline](decorators/Timeline.md): Organizes information chronologically
- [Layered](decorators/Layered.md): Presents information in layers of detail

### Meta Decorators

These decorators focus on the decorator system itself:

- [Custom](decorators/Custom.md): Creates custom decorator behaviors
- [Chain](decorators/Chain.md): Chains multiple decorators together
- [Conditional](decorators/Conditional.md): Applies decorators conditionally
- [Extension](decorators/Extension.md): Extends decorator functionality
- [Nested](decorators/Nested.md): Nests decorators within each other
- [Override](decorators/Override.md): Overrides default decorator behavior
- [Context](decorators/Context.md): Provides additional context
- [Constraints](decorators/Constraints.md): Adds constraints to model responses
- [BuildOn](decorators/BuildOn.md): Builds on previous interactions
- [Version](decorators/Version.md): Specifies version compatibility
- [CiteSources](decorators/CiteSources.md): Requires citation of sources

## Creating Custom Decorators

You can create custom decorators by extending the BaseDecorator class:

```python
from prompt_decorators.core import BaseDecorator

class MyCustomDecorator(BaseDecorator):
    def __init__(self, param1=None, param2=True):
        self.param1 = param1
        self.param2 = param2

    def apply_to_prompt(self, prompt):
        # Implement your custom transformation logic
        modified_prompt = f"My custom transformation ({self.param1}): {prompt}"
        if self.param2:
            modified_prompt += "\nAdditional instructions based on param2."
        return modified_prompt
```

For more details on creating custom decorators, see the [Creating Custom Decorators tutorial](../tutorials/creating_custom_decorator.md).

## Decorator Registry

The decorator registry provides a centralized way to register and access decorators:

```python
from prompt_decorators.core.registry import DecoratorRegistry

# Get the global registry
registry = DecoratorRegistry()

# Register a custom decorator
registry.register("MyCustomDecorator", MyCustomDecorator)

# Get a decorator by name
decorator_class = registry.get("MyCustomDecorator")
instance = decorator_class(param1="value", param2=True)
```

For more information on the decorator registry, see the [Decorator Registry documentation](../DECORATOR_REGISTRY.md).

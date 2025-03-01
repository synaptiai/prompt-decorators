# Combining Decorators Effectively

This tutorial provides guidance on how to combine multiple decorators in the Prompt Decorators framework to achieve sophisticated prompt enhancements while avoiding conflicts.

## Understanding Decorator Composition

When you apply multiple decorators to a prompt, they are composed in sequence. This means the order of application matters significantly.

Consider this example:

```python
from prompt_decorators.decorators.generated.decorators.concise import Concise
from prompt_decorators.decorators.generated.decorators.technical import Technical

concise = Concise(max_words=100)
technical = Technical(domain="computer_science")

prompt = "Explain neural networks."

# These two approaches yield different results:
result1 = concise.apply(technical.apply(prompt))  # Technical first, then Concise
result2 = technical.apply(concise.apply(prompt))  # Concise first, then Technical
```

In `result1`, the model is first instructed to provide a technical explanation, and then that instruction is modified to be concise. In `result2`, the model is first instructed to be concise, and then that instruction is modified to be technical.

## The Decorator Stack Concept

Think of decorator combination as building a stack of instructions. Each new decorator adds another layer of instructions on top of the existing ones. The last decorator applied will be the "outermost" instruction the model sees first.

### General Rules for Decorator Order

1. **Format/Structure decorators should be applied last** - These control the final output format
2. **Reasoning decorators should be applied first** - These set the thinking process
3. **Style/Tone decorators should be in the middle** - These control how the content is communicated

```
[Original Prompt] → [Reasoning] → [Style/Tone] → [Format/Structure] → [Final Prompt]
```

## Common Decorator Combinations

Here are some effective decorator combinations for common scenarios:

### For Technical Explanations

```python
from prompt_decorators.decorators.generated.decorators.reasoning import Reasoning
from prompt_decorators.decorators.generated.decorators.technical import Technical
from prompt_decorators.decorators.generated.decorators.bullet import Bullet

# Create decorators
reasoning = Reasoning(depth="comprehensive")
technical = Technical(domain="physics", expertise_level="expert")
bullet = Bullet(style="numbered")

# Apply in effective order
prompt = "Explain quantum entanglement."
decorated_prompt = bullet.apply(technical.apply(reasoning.apply(prompt)))
```

This combination:
1. First asks the model to use comprehensive reasoning
2. Then specifies to use technical language at an expert level in physics
3. Finally formats the output as a numbered bullet list

### For Educational Content

```python
from prompt_decorators.decorators.generated.decorators.eli5 import ELI5
from prompt_decorators.decorators.generated.decorators.analogical import Analogical
from prompt_decorators.decorators.generated.decorators.summary import Summary

# Create decorators
analogical = Analogical(domains=["everyday_life", "nature"])
eli5 = ELI5(age=12)
summary = Summary(include_key_points=True, max_length=3)

# Apply in effective order
prompt = "Explain how the internet works."
decorated_prompt = summary.apply(eli5.apply(analogical.apply(prompt)))
```

This combination:
1. First asks the model to use analogical reasoning with everyday life examples
2. Then specifies to explain at a 12-year-old's level
3. Finally asks for a summary with key points at the end

### For Decision Making

```python
from prompt_decorators.decorators.generated.decorators.step_by_step import StepByStep
from prompt_decorators.decorators.generated.decorators.alternatives import Alternatives
from prompt_decorators.decorators.generated.decorators.decision_matrix import DecisionMatrix

# Create decorators
step_by_step = StepByStep(show_reasoning=True)
alternatives = Alternatives(min_alternatives=3, max_alternatives=5)
decision_matrix = DecisionMatrix(criteria=["cost", "time", "quality"])

# Apply in effective order
prompt = "What's the best approach for implementing a recommendation system?"
decorated_prompt = decision_matrix.apply(
    alternatives.apply(step_by_step.apply(prompt))
)
```

This combination creates a structured decision-making prompt that:
1. First walks through the problem step by step
2. Then generates multiple alternative approaches
3. Finally evaluates those alternatives using a decision matrix

## Using the Compatibility Checker

To avoid conflicts between decorators, use the built-in compatibility checker:

```python
from prompt_decorators.utils import get_compatibility_checker
from prompt_decorators.decorators.generated.decorators.concise import Concise
from prompt_decorators.decorators.generated.decorators.detailed import Detailed

checker = get_compatibility_checker()

concise = Concise(max_words=100)
detailed = Detailed(min_detail_level=3)

# Check compatibility
issues = checker.check_compatibility(concise, detailed)

if issues:
    print("These decorators may conflict:")
    for issue in issues:
        print(f"- {issue}")
else:
    # Apply decorators if compatible
    prompt = "Explain neural networks."
    decorated_prompt = detailed.apply(concise.apply(prompt))
```

## Advanced Decorator Patterns

Here are some advanced patterns for combining decorators:

### The Chain Pattern

Use the `Chain` meta-decorator to apply multiple decorators in sequence:

```python
from prompt_decorators.decorators.generated.decorators.meta.chain import Chain
from prompt_decorators.decorators.generated.decorators.reasoning import Reasoning
from prompt_decorators.decorators.generated.decorators.technical import Technical
from prompt_decorators.decorators.generated.decorators.bullet import Bullet

# Create decorators
reasoning = Reasoning(depth="comprehensive") 
technical = Technical(domain="physics")
bullet = Bullet()

# Chain them together
chain = Chain(decorators=[reasoning, technical, bullet])

# Apply the chain
prompt = "Explain quantum entanglement."
decorated_prompt = chain.apply(prompt)
```

### The Conditional Pattern

Use the `Conditional` meta-decorator to apply decorators based on conditions:

```python
from prompt_decorators.decorators.generated.decorators.meta.conditional import Conditional
from prompt_decorators.decorators.generated.decorators.eli5 import ELI5
from prompt_decorators.decorators.generated.decorators.technical import Technical

# Create condition function
def is_technical_topic(prompt: str) -> bool:
    technical_keywords = ["algorithm", "quantum", "neural network", "compiler"]
    return any(keyword in prompt.lower() for keyword in technical_keywords)

# Create decorators
eli5 = ELI5(age=10)
technical = Technical()

# Create conditional decorator
conditional = Conditional(
    condition_func=is_technical_topic,
    true_decorator=technical,
    false_decorator=eli5
)

# Apply conditionally
prompt1 = "Explain how quantum computers work."  # Will apply Technical
prompt2 = "Explain how rainbows form."  # Will apply ELI5

decorated_prompt1 = conditional.apply(prompt1)
decorated_prompt2 = conditional.apply(prompt2)
```

### The Priority Pattern

Use the `Priority` meta-decorator to resolve conflicts between decorators:

```python
from prompt_decorators.decorators.generated.decorators.meta.priority import Priority
from prompt_decorators.decorators.generated.decorators.concise import Concise
from prompt_decorators.decorators.generated.decorators.detailed import Detailed

# Create potentially conflicting decorators
concise = Concise(max_words=150)
detailed = Detailed(min_detail_level=2)

# Create priority decorator (concise takes precedence)
priority = Priority(
    decorators=[detailed, concise],
    priority_order=[1, 0]  # Lower index = higher priority
)

# Apply with priority resolution
prompt = "Explain how GPT models work."
decorated_prompt = priority.apply(prompt)
```

## Domain-Specific Decorator Combinations

Different domains may benefit from specific decorator combinations:

### Healthcare Domain

```python
from prompt_decorators.decorators.generated.decorators.professional import Professional
from prompt_decorators.decorators.generated.decorators.fact_check import FactCheck
from prompt_decorators.decorators.generated.decorators.limitations import Limitations

# Create healthcare-focused decorators
professional = Professional(industry="healthcare")
fact_check = FactCheck(verification_level=3)
limitations = Limitations(highlight_uncertainties=True)

# Apply in effective order
prompt = "Explain the benefits and risks of immunotherapy."
decorated_prompt = limitations.apply(
    fact_check.apply(professional.apply(prompt))
)
```

### Financial Analysis

```python
from prompt_decorators.decorators.generated.decorators.balanced import Balanced
from prompt_decorators.decorators.generated.decorators.professional import Professional
from prompt_decorators.decorators.generated.decorators.schema import Schema

# Create finance-focused decorators
balanced = Balanced()
professional = Professional(industry="finance")
schema = Schema(schema={
    "analysis": "string",
    "risks": ["string"],
    "opportunities": ["string"],
    "recommendation": "string"
})

# Apply in effective order
prompt = "Analyze the current market trends for renewable energy investments."
decorated_prompt = schema.apply(
    professional.apply(balanced.apply(prompt))
)
```

## Common Pitfalls to Avoid

1. **Decorator Overload**: Using too many decorators can create conflicting or confusing instructions. Limit to 3-4 for best results.

2. **Conflicting Instructions**: Be careful with opposing decorators (e.g., Concise + Detailed). Use the compatibility checker or Priority meta-decorator.

3. **Wrong Order**: Applying decorators in a suboptimal order can diminish their effectiveness. Follow the general ordering principles.

4. **Parameter Conflicts**: Parameters across decorators may conflict (e.g., max_words in one, min_words in another). Be mindful of parameter coherence.

5. **Ignoring Model Limitations**: Some models may not handle complex instruction combinations well. Consider using ModelSpecificDecorator for adaptation.

## Best Practices

1. **Start Simple**: Begin with 1-2 decorators and add more as needed.

2. **Test Combinations**: Always test your decorator combinations with different prompts.

3. **Use Meta-Decorators**: Chain, Conditional, and Priority meta-decorators can help manage complex combinations.

4. **Check Compatibility**: Use the compatibility checker to identify potential conflicts.

5. **Be Consistent**: Maintain consistent parameter values across decorators (e.g., domain terminology).

6. **Monitor Results**: Different models may respond differently to decorator combinations. Monitor and adjust as needed.

## Conclusion

Effective decorator combinations can significantly enhance the quality and consistency of LLM responses. By understanding the interaction between decorators and following best practices, you can create sophisticated prompt engineering solutions tailored to your specific needs.

Next steps:
- Try the examples in this tutorial with your own prompts
- Explore the [Compatibility Matrix](../compatibility.md) for more information
- Check out the [Decorator Catalog](../api/decorators/) for all available decorators 
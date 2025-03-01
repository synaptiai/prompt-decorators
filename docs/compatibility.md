# Decorator Compatibility Guide

This document provides information about decorator compatibility in the Prompt Decorators framework.

## Introduction

When combining multiple decorators, it's important to understand which decorators work well together and which ones might conflict. This guide will help you make informed decisions when combining decorators.

## Compatibility Matrix

The following table shows the compatibility between common decorator categories:

| Category        | Reasoning | Format | Style | Verification | Meta     |
|-----------------|-----------|--------|-------|--------------|----------|
| **Reasoning**   | ✓         | ✓      | ✓     | ✓            | ✓        |
| **Format**      | ✓         | ⚠️      | ✓     | ✓            | ✓        |
| **Style**       | ✓         | ✓      | ⚠️     | ✓            | ✓        |
| **Verification**| ✓         | ✓      | ✓     | ✓            | ✓        |
| **Meta**        | ✓         | ✓      | ✓     | ✓            | ✓        |

Legend:
- ✓: Generally compatible
- ⚠️: May have conflicts, use with caution
- ❌: Generally incompatible

## Known Incompatibilities

The following specific decorator combinations are known to have conflicts:

1. **ELI5 + Technical**: These decorators have contradictory goals (simplicity vs. technical complexity).
2. **Concise + Detailed**: These decorators have opposing constraints on response length.
3. **Bullet + TableFormat**: These decorators specify conflicting output formats.
4. **Academic + Humorous**: These decorators define incompatible tones.
5. **FirstPrinciples + StepByStep**: These decorators provide different structured reasoning approaches that may conflict.

## Best Practices

When combining decorators, follow these best practices:

1. **Apply in the right order**: Decorators are applied in sequence, so put the most specific or format-related decorators last.
2. **Limit the number**: Using too many decorators can lead to conflicting instructions. Limit to 2-3 decorators.
3. **Test combinations**: Always test decorator combinations to ensure they produce the desired effect.
4. **Handle conflicts**: When using potentially conflicting decorators, be explicit about which aspect should take precedence.

## Example Combinations

Here are some effective decorator combinations:

### For Technical Documentation
```python
technical = Technical(domain="computing", expertise_level="expert")
code_examples = CodeExamples(language="python", count=3)
formatted = OutputFormat(format_type="markdown")

# Good order: domain → specifics → format
decorated_prompt = formatted.apply(code_examples.apply(technical.apply(prompt)))
```

### For Explanations
```python
reasoning = Reasoning(depth="comprehensive")
eli5 = ELI5(age=12)
bullet = Bullet(style="dash")

# Good order: reasoning → audience adaptation → format
decorated_prompt = bullet.apply(eli5.apply(reasoning.apply(prompt)))
```

### For Creative Content
```python
creative = Creative(genre="narrative")
motivational = Motivational(intensity=2)
persona = Persona(role="marketing")

# Good order: role → style → intensity
decorated_prompt = motivational.apply(creative.apply(persona.apply(prompt)))
```

## Using Compatibility Checker

You can use the built-in compatibility checker to verify compatibility:

```python
from prompt_decorators.utils import get_compatibility_checker

checker = get_compatibility_checker()
issues = checker.check_compatibility(decorator1, decorator2)

if issues:
    for issue in issues:
        print(f"Warning: {issue}")
else:
    print("Decorators are compatible!")
```

## Model-Specific Considerations

Some decorators may behave differently depending on the model being used. Use the model-specific adapters to handle these cases:

```python
from prompt_decorators.core import ModelSpecificDecoratorFactory

model_specific_decorator = ModelSpecificDecoratorFactory.create_for_model(
    decorator_class=Reasoning,
    model_id="gpt-4",
    depth="comprehensive"
)
```

## Getting Help

If you encounter incompatibilities not listed here or have questions about specific combinations, please:

1. Check the documentation for each decorator in the `docs/api/decorators/` directory.
2. Look at the examples in the `examples/` directory.
3. Open an issue on the GitHub repository if you've discovered a new incompatibility.

Remember that while some combinations are generally incompatible, the specific behavior may depend on the exact parameter values and the LLM model being used. 
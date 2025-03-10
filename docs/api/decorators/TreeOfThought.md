# TreeOfThought Decorator

Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `branches` | number | Number of different reasoning branches to explore | 3 |
| `depth` | number | Maximum depth of reasoning in each branch | 3 |
| `pruning` | boolean | Whether to eliminate less promising branches early | False |

## Examples

### Multi-branch problem solving for a complex question

```
+++TreeOfThought
What might explain the Fermi Paradox?
```

Explores three different reasoning branches about potential explanations for the Fermi Paradox, developing each path to moderate depth

### Deep, focused exploration with pruning

```
+++TreeOfThought(branches=5, depth=5, pruning=true)
How might we solve the climate change crisis?
```

Starts with five different approaches to climate change, explores each in depth, and eliminates less promising branches to focus on the most viable solutions

## Model-Specific Implementations

### gpt-4

**Instruction:** Consider {branches} distinct approaches to this problem. For each approach, think step-by-step to a depth of {depth} levels. Label each branch clearly (e.g., 'Approach 1', 'Approach 2') and use subheadings to indicate depth levels. {pruning}

**Notes:** This model handles complex branching reasoning well, but benefits from clear formatting instructions

### gpt-3.5-turbo

**Instruction:** Explore {branches} different ways to approach this problem. Be very explicit about which approach you're discussing, and break down each approach into {depth} levels of detailed analysis. Start each approach with a clear label and keep them separated.

**Notes:** This model may need additional structure to manage multiple reasoning branches effectively


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **StepByStep**: Enhances TreeOfThought StepByStep can help organize the reasoning within each branch of the tree
- **Debate**: Enhances TreeOfThought TreeOfThought and Debate work well together to explore multiple perspectives with structured reasoning

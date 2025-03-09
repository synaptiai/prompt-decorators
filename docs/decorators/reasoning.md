# Reasoning Decorators

This section documents decorators that enhance reasoning capabilities in the Prompt Decorators framework.

## Reasoning

The `Reasoning` decorator specifies a particular reasoning approach to be used in the response.

**Category**: Reasoning

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `approach` | string | The reasoning approach to use (e.g., "deductive", "inductive") | "general" |
| `depth` | string | The depth of reasoning to apply (e.g., "basic", "detailed", "comprehensive") | "detailed" |
| `steps` | integer | Number of reasoning steps to include | 3 |

**Example**:

```
+++Reasoning(approach="deductive", depth="comprehensive")
Explain the relationship between exercise and mental health.
```

**Compatible with**: `StepByStep`, `OutputFormat`, `Tone`

## StepByStep

The `StepByStep` decorator encourages step-by-step problem solving, breaking down complex problems into manageable steps.

**Category**: Reasoning

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `numbered` | boolean | Whether to number the steps | true |
| `detailed` | boolean | Whether to include detailed explanations for each step | true |
| `min_steps` | integer | Minimum number of steps to include | 3 |
| `max_steps` | integer | Maximum number of steps to include | 10 |

**Example**:

```
+++StepByStep(numbered=true, detailed=true)
How to solve a quadratic equation?
```

**Compatible with**: `Reasoning`, `OutputFormat`, `Tone`

## TreeOfThought

The `TreeOfThought` decorator implements the Tree of Thought reasoning approach, exploring multiple reasoning paths.

**Category**: Reasoning

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `branches` | integer | Number of reasoning branches to explore | 3 |
| `depth` | integer | Depth of reasoning in each branch | 2 |
| `show_pruning` | boolean | Whether to show pruned reasoning paths | false |
| `evaluation_criteria` | string | Criteria for evaluating branches | "logical_consistency" |

**Example**:

```
+++TreeOfThought(branches=3, depth=3)
What are the possible outcomes of increasing interest rates on the housing market?
```

**Compatible with**: `OutputFormat`, `Tone`

## FirstPrinciples

The `FirstPrinciples` decorator encourages reasoning from first principles, breaking down complex problems to their fundamental truths.

**Category**: Reasoning

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `depth` | string | Depth of first principles analysis | "detailed" |
| `axioms` | boolean | Whether to explicitly state axioms | true |
| `context` | string | Domain context for principles (e.g., "physics", "economics") | "general" |

**Example**:

```
+++FirstPrinciples(axioms=true, context="economics")
Why do markets tend toward equilibrium?
```

**Compatible with**: `StepByStep`, `OutputFormat`

## ForcedAnalogy

The `ForcedAnalogy` decorator uses analogical reasoning, comparing the problem to a different domain to gain insights.

**Category**: Reasoning

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `domain` | string | Domain for the analogy (e.g., "nature", "technology") | "nature" |
| `detail` | string | Level of detail in the analogy | "moderate" |
| `creative` | boolean | Whether to use creative analogies | true |

**Example**:

```
+++ForcedAnalogy(domain="nature")
Explain how social networks spread information.
```

**Compatible with**: `Reasoning`, `OutputFormat`

## Inductive

The `Inductive` decorator applies inductive reasoning, drawing general conclusions from specific observations.

**Category**: Reasoning

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `examples` | integer | Number of examples to use in reasoning | 3 |
| `confidence` | string | Confidence level in inductive conclusions | "moderate" |
| `caveats` | boolean | Whether to include caveats about inductive reasoning | true |

**Example**:

```
+++Inductive(examples=5, caveats=true)
Based on current technology trends, how might mobile devices evolve in the next decade?
```

**Compatible with**: `StepByStep`, `OutputFormat`

## RootCause

The `RootCause` decorator focuses on identifying root causes of problems or phenomena.

**Category**: Reasoning

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `depth` | integer | How many levels deep to analyze causes | 3 |
| `systemic` | boolean | Whether to focus on systemic causes | true |
| `diagram` | boolean | Whether to include a cause-effect diagram | false |

**Example**:

```
+++RootCause(depth=4, systemic=true)
Why do software projects often exceed their initial time estimates?
```

**Compatible with**: `StepByStep`, `OutputFormat`

## Analogical

The `Analogical` decorator uses analogical reasoning to compare the current problem with similar ones.

**Category**: Reasoning

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `sources` | integer | Number of analogical sources to draw from | 2 |
| `detail` | string | Level of detail in mapping analogies | "detailed" |
| `domain` | string | Domain restriction for analogies | "general" |

**Example**:

```
+++Analogical(sources=3, domain="biology")
How is a company's organizational structure similar to other systems?
```

**Compatible with**: `Reasoning`, `OutputFormat`

## Abductive

The `Abductive` decorator uses abductive reasoning to form the most likely explanation for observations.

**Category**: Reasoning

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `hypotheses` | integer | Number of hypotheses to consider | 3 |
| `ranking` | boolean | Whether to rank hypotheses by likelihood | true |
| `evidence_focus` | string | Focus on evidence (e.g., "contradictory", "supporting") | "balanced" |

**Example**:

```
+++Abductive(hypotheses=4, ranking=true)
What might explain the sudden decline in bee populations?
```

**Compatible with**: `OutputFormat`, `Limitations`

## Deductive

The `Deductive` decorator applies deductive reasoning, drawing specific conclusions from general premises.

**Category**: Reasoning

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `premises` | integer | Number of premises to state | 3 |
| `formal` | boolean | Whether to use formal logic notation | false |
| `validity_check` | boolean | Whether to check argument validity | true |

**Example**:

```
+++Deductive(premises=2, validity_check=true)
Is artificial intelligence conscious?
```

**Compatible with**: `StepByStep`, `OutputFormat`

## Using Reasoning Decorators Together

Reasoning decorators can often be combined with each other or with decorators from other categories to create more powerful transformations. For example:

```
+++Reasoning(approach="deductive")
+++StepByStep(numbered=true)
+++OutputFormat(format="markdown")
Analyze the impact of remote work on urban development.
```

This combines a deductive reasoning approach with step-by-step problem solving and markdown formatting.

## See Also

- Format Decorators (coming soon)
- Style Decorators (coming soon)
- [Creating Custom Reasoning Decorators](../tutorials/creating_custom_decorator.md)

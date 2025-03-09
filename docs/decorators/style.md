# Style Decorators

This section documents decorators that modify the style, tone, and presentation of responses in the Prompt Decorators framework.

## Tone

The `Tone` decorator adjusts the tone of the response to match a specified style.

**Category**: Style

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `style` | enum | The tone style to use (e.g., "formal", "casual", "technical", "friendly", "enthusiastic", "professional") | "professional" |
| `intensity` | string | The intensity of the tone adjustment (e.g., "mild", "moderate", "strong") | "moderate" |

**Example**:

```
+++Tone(style="friendly", intensity="strong")
Explain the concept of object-oriented programming.
```

**Compatible with**: Most other decorators, particularly well with `Audience` and `Persona`

## Persona

The `Persona` decorator instructs the model to adopt a specific persona or role when generating a response.

**Category**: Style

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `role` | string | The role or persona to adopt (e.g., "teacher", "scientist", "coach") | "expert" |
| `style` | string | Additional styling for the persona (e.g., "enthusiastic", "dry", "methodical") | "neutral" |
| `background` | string | Optional background context for the persona | "" |

**Example**:

```
+++Persona(role="experienced software engineer", style="pragmatic")
What are the most important principles of good software design?
```

**Compatible with**: `Tone`, `OutputFormat`, most reasoning decorators

## Audience

The `Audience` decorator adapts the content for a specific audience or expertise level.

**Category**: Style

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `level` | enum | The expertise level of the audience (e.g., "beginner", "intermediate", "advanced", "expert") | "intermediate" |
| `domain` | string | Specific domain knowledge or context for the audience | "general" |
| `adapt_terminology` | boolean | Whether to adapt terminology to the audience level | true |

**Example**:

```
+++Audience(level="beginner", domain="programming")
Explain how databases work.
```

**Compatible with**: `Tone`, `ELI5`, `OutputFormat`

## ELI5

The `ELI5` ("Explain Like I'm 5") decorator simplifies explanations to be understandable by someone with minimal background knowledge.

**Category**: Style

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `use_analogies` | boolean | Whether to use simple analogies in explanations | true |
| `simplified_vocabulary` | boolean | Whether to use simplified vocabulary | true |
| `visual_descriptions` | boolean | Whether to use visual descriptions and examples | true |

**Example**:

```
+++ELI5(use_analogies=true)
How does the internet work?
```

**Compatible with**: `OutputFormat`, `StepByStep`

## Concise

The `Concise` decorator generates brief, to-the-point responses.

**Category**: Style

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `level` | enum | The level of conciseness (e.g., "minimal", "moderate", "extreme") | "moderate" |
| `retain_examples` | boolean | Whether to retain illustrative examples | false |
| `bullet_points` | boolean | Whether to use bullet points for brevity | true |

**Example**:

```
+++Concise(level="extreme", bullet_points=true)
What are the key features of Python?
```

**Compatible with**: `OutputFormat`, incompatible with `Detailed`

## Detailed

The `Detailed` decorator produces comprehensive, in-depth responses with thorough explanations.

**Category**: Style

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `depth` | enum | The level of detail (e.g., "moderate", "comprehensive", "exhaustive") | "comprehensive" |
| `include_examples` | boolean | Whether to include examples | true |
| `include_context` | boolean | Whether to include background context | true |

**Example**:

```
+++Detailed(depth="exhaustive", include_examples=true)
How do neural networks learn?
```

**Compatible with**: Most reasoning decorators, incompatible with `Concise`

## Professional

The `Professional` decorator ensures responses have a professional, business-appropriate tone and format.

**Category**: Style

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `formality` | enum | The level of formality (e.g., "standard", "highly formal") | "standard" |
| `industry` | string | Specific industry context, if applicable | "general" |
| `include_citations` | boolean | Whether to include citations and references | false |

**Example**:

```
+++Professional(formality="highly formal", industry="finance")
What are the key considerations for regulatory compliance?
```

**Compatible with**: `OutputFormat`, `Detailed`, most reasoning decorators

## StyleShift

The `StyleShift` decorator transforms the style of text to match a specified genre, author, or cultural style.

**Category**: Style

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `target_style` | string | The style to emulate (e.g., "academic", "journalistic", "literary") | "academic" |
| `example_source` | string | An example source or author to imitate | "" |
| `maintain_content` | boolean | Whether to maintain all content while shifting style | true |

**Example**:

```
+++StyleShift(target_style="journalistic", example_source="The Economist")
Explain the implications of quantum computing for cryptography.
```

**Compatible with**: Most other decorators, may conflict with `Tone` if using contradictory styles

## Motivational

The `Motivational` decorator adds inspirational and encouraging elements to the response.

**Category**: Style

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `intensity` | enum | The intensity of motivational language (e.g., "subtle", "moderate", "strong") | "moderate" |
| `emphasize_progress` | boolean | Whether to emphasize progress and growth | true |
| `include_quotes` | boolean | Whether to include motivational quotes | false |

**Example**:

```
+++Motivational(intensity="strong", include_quotes=true)
How can I improve my programming skills?
```

**Compatible with**: Most other decorators

## Using Style Decorators Together

Style decorators can be combined with other decorators to create more nuanced responses. For example:

```
+++Persona(role="teacher")
+++Audience(level="beginner")
+++OutputFormat(format="markdown")
Explain how gravity works.
```

This combines a teacher persona with beginner-friendly explanations in markdown format.

## See Also

- [Reasoning Decorators](reasoning.md)
- [Output Format Decorators](format.md) (coming soon)
- [Creating Custom Style Decorators](../tutorials/creating_custom_decorator.md)

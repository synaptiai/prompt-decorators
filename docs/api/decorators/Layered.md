# Layered Decorator

Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `levels` | enum | The granularity of explanation levels to include | summary-detail-technical |
| `count` | number | Number of distinct explanation layers to provide | 3 |
| `progression` | enum | How to structure the progression between layers | separate |

## Levels Options

- `sentence-paragraph-full`: Structure the explanation in three distinct formats: first a one-sentence summary, then a single paragraph overview, and finally a full comprehensive explanation.
- `basic-intermediate-advanced`: Provide explanations at three knowledge levels: a basic explanation for beginners, an intermediate explanation with more domain-specific concepts, and an advanced explanation for specialists.
- `summary-detail-technical`: Present the information in increasing technical depth: first a high-level summary, then a detailed explanation, and finally a technical deep-dive with specialized terminology and concepts.

## Progression Options

- `separate`: Present each explanation layer as a separate, clearly labeled section with its own heading.
- `nested`: Structure the explanation as a hierarchical nested format, where each layer builds upon and includes the previous layer.
- `incremental`: Present the information incrementally, adding new details and concepts with each layer while referencing previous information.

## Examples

### Basic three-level explanation of a complex concept

```
+++Layered
Explain how blockchain technology works.
```

Provides a summary-level explanation of blockchain, followed by a detailed explanation, and finally a technical deep dive with implementation details

### Multi-layered nested progression with custom levels

```
+++Layered(levels=basic-intermediate-advanced, count=4, progression=nested)
Describe the principles of quantum computing.
```

Delivers a nested explanation of quantum computing with four progressive layers of understanding, each building on the previous and increasing in complexity from basic to advanced

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Provide {count} different levels of explanation about this topic. Use the {levels} approach, with each layer getting progressively more detailed. Structure these {progression}. Make sure to clearly label each layer so readers can choose their preferred depth.

**Notes:** This model sometimes needs explicit reminders to create sufficiently distinct layers with meaningful differences in detail


## Implementation Guidance

### Three-level explanation of blockchain technology

**Original Prompt:**
```
Explain how blockchain technology works.
```

**Transformed Prompt:**
```
Please present the information at multiple levels of explanation depth, allowing readers to engage with the content at their preferred level of detail. Present the information in increasing technical depth: first a high-level summary, then a detailed explanation, and finally a technical deep-dive with specialized terminology and concepts. Provide exactly 3 distinct layers of explanation, each with increasing depth and detail. Present each explanation layer as a separate, clearly labeled section with its own heading.

Explain how blockchain technology works.
```

### Multi-layered nested explanation of quantum computing

**Original Prompt:**
```
Describe the principles of quantum computing.
```

**Transformed Prompt:**
```
Please present the information at multiple levels of explanation depth, allowing readers to engage with the content at their preferred level of detail. Provide explanations at three knowledge levels: a basic explanation for beginners, an intermediate explanation with more domain-specific concepts, and an advanced explanation for specialists. Provide exactly 4 distinct layers of explanation, each with increasing depth and detail. Structure the explanation as a hierarchical nested format, where each layer builds upon and includes the previous layer.

Describe the principles of quantum computing.
```

## Transformation Details

**Base Instruction:** Please present the information at multiple levels of explanation depth, allowing readers to engage with the content at their preferred level of detail.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `levels`:
  - When set to `sentence-paragraph-full`: Structure the explanation in three distinct formats: first a one-sentence summary, then a single paragraph overview, and finally a full comprehensive explanation.
  - When set to `basic-intermediate-advanced`: Provide explanations at three knowledge levels: a basic explanation for beginners, an intermediate explanation with more domain-specific concepts, and an advanced explanation for specialists.
  - When set to `summary-detail-technical`: Present the information in increasing technical depth: first a high-level summary, then a detailed explanation, and finally a technical deep-dive with specialized terminology and concepts.

- `count`:
  - Format: Provide exactly {value} distinct layers of explanation, each with increasing depth and detail.

- `progression`:
  - When set to `separate`: Present each explanation layer as a separate, clearly labeled section with its own heading.
  - When set to `nested`: Structure the explanation as a hierarchical nested format, where each layer builds upon and includes the previous layer.
  - When set to `incremental`: Present the information incrementally, adding new details and concepts with each layer while referencing previous information.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Audience**: Enhances Layered Layered works well with Audience to further tailor each layer to different expertise levels
- **ELI5**: Enhances Layered ELI5 can be effectively used for the initial layer in a layered explanation
- **Technical**: Enhances Layered Technical can be used for the deepest layer in a layered explanation

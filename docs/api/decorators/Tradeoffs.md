# Tradeoffs Decorator

Analyzes design tradeoffs across multiple dimensions.

**Category**: Architecture And Design

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `axes` | enum | Dimensions to analyze | performance,cost,complexity,maintainability |
| `format` | enum | Presentation format | decision-matrix |
| `depth` | enum | Analysis depth | detailed |

## Axes Options

- `performance`: Option: performance
- `cost`: Option: cost
- `complexity`: Option: complexity
- `maintainability`: Option: maintainability
- `security`: Option: security
- `time-to-market`: Option: time-to-market

## Format Options

- `table`: Present your analysis in a tabular format with options as rows and dimensions as columns.
- `prose`: Present your analysis as a structured prose discussion of each option across the dimensions.
- `radar-chart`: Describe how a radar chart would represent these tradeoffs, with each axis representing one dimension.
- `decision-matrix`: Create a decision matrix that scores each option across the dimensions, with a final recommendation based on the overall scores.

## Depth Options

- `overview`: Provide a high-level overview of the key tradeoffs without detailed analysis.
- `detailed`: Provide a thorough analysis with specific examples and reasoning for each dimension.
- `quantitative`: Where possible, include quantitative metrics and measurements to support your analysis.

## Examples

### Analyzing database hosting options

```
+++Tradeoffs(axes=performance,cost,security,maintainability, format=decision-matrix)
Analyze the tradeoffs between using a managed database service versus self-hosted for a financial application.
```

A decision matrix comparing managed vs. self-hosted database options across performance, cost, security, and maintainability dimensions, with scores and a final recommendation.

### Comparing programming languages

```
+++Tradeoffs(axes=performance,complexity,time-to-market, format=table, depth=overview)
Compare Python, Java, and Rust for developing a new data processing pipeline.
```

A table showing a high-level overview of how Python, Java, and Rust compare across performance, complexity, and time-to-market dimensions.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a detailed comparison of the options across multiple dimensions. For each dimension, explain the tradeoffs between the different approaches.

**Notes:** Simpler instruction for models with less analytical capability.


## Implementation Guidance

### Software architecture decision

**Original Prompt:**
```
Compare microservices vs monolithic architecture for our e-commerce platform.
```

**Transformed Prompt:**
```
Analyze the tradeoffs between different options considering the specified dimensions. Present a balanced assessment that highlights the advantages and disadvantages of each approach. Analyze the following dimensions: performance,cost,complexity,maintainability. Create a decision matrix that scores each option across the dimensions, with a final recommendation based on the overall scores. Provide a thorough analysis with specific examples and reasoning for each dimension.

Compare microservices vs monolithic architecture for our e-commerce platform.
```

**Notes:** The decorator adds structure to the comparison by specifying dimensions and format.

## Transformation Details

**Base Instruction:** Analyze the tradeoffs between different options considering the specified dimensions. Present a balanced assessment that highlights the advantages and disadvantages of each approach.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `axes`:
  - Format: Analyze the following dimensions: {value}.

- `format`:
  - When set to `table`: Present your analysis in a tabular format with options as rows and dimensions as columns.
  - When set to `prose`: Present your analysis as a structured prose discussion of each option across the dimensions.
  - When set to `radar-chart`: Describe how a radar chart would represent these tradeoffs, with each axis representing one dimension.
  - When set to `decision-matrix`: Create a decision matrix that scores each option across the dimensions, with a final recommendation based on the overall scores.

- `depth`:
  - When set to `overview`: Provide a high-level overview of the key tradeoffs without detailed analysis.
  - When set to `detailed`: Provide a thorough analysis with specific examples and reasoning for each dimension.
  - When set to `quantitative`: Where possible, include quantitative metrics and measurements to support your analysis.

## Compatibility

- **Requires**: None
- **Conflicts**: Pros
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **Reasoning**: Enhances Tradeoffs Tradeoffs works well with Reasoning to provide more structured analytical thinking.
- **Pros**: Conflicts with Tradeoffs Tradeoffs provides a more comprehensive analysis than simple pros/cons and should not be used together.

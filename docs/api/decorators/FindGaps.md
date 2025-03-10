# FindGaps Decorator

Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `aspects` | enum | The specific types of gaps to focus on finding | comprehensive |
| `depth` | enum | How thoroughly to analyze for gaps | thorough |
| `solutions` | boolean | Whether to suggest solutions or approaches for addressing the identified gaps | True |

## Aspects Options

- `questions`: Focus specifically on identifying unanswered questions and unresolved issues that need clarification.
- `resources`: Focus specifically on identifying missing resources, tools, skills, or capabilities needed for implementation or success.
- `stakeholders`: Focus specifically on identifying overlooked stakeholders, individuals, or groups whose perspectives or needs are not adequately addressed.
- `risks`: Focus specifically on identifying potential risks, threats, and vulnerabilities that have not been adequately considered.
- `dependencies`: Focus specifically on identifying overlooked dependencies, prerequisites, or contingencies that could affect implementation or outcomes.
- `comprehensive`: Comprehensively identify gaps across multiple dimensions, including questions, resources, stakeholders, risks, and dependencies.

## Depth Options

- `basic`: Conduct a focused analysis to identify the most obvious and critical gaps.
- `thorough`: Conduct a detailed analysis to identify both obvious and subtle gaps that might significantly impact outcomes.
- `exhaustive`: Conduct an extremely comprehensive analysis to identify all possible gaps, including edge cases and minor considerations.

## Examples

### Basic comprehensive gap analysis of a business plan

```
+++FindGaps
We plan to launch our SaaS product with these features and marketing channels...
```

First identifies gaps across various aspects of the SaaS product launch plan, then suggests solutions for addressing each gap

### Exhaustive stakeholder-focused gap analysis without solutions

```
+++FindGaps(aspects=stakeholders, depth=exhaustive, solutions=false)
Here's our urban redevelopment proposal...
```

Provides an exhaustive analysis of overlooked or inadequately considered stakeholders in the urban redevelopment proposal, without suggesting solutions

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** First analyze this content carefully. Then identify missing or overlooked {aspects} using a {depth} approach. For each gap found, clearly explain why it matters and how it could impact outcomes. {solutions} Be specific and constructive in your gap analysis.

**Notes:** This model sometimes needs more explicit instruction to go beyond surface-level analysis and identify non-obvious gaps


## Implementation Guidance

### Basic comprehensive gap analysis of a business plan

**Original Prompt:**
```
We plan to launch our SaaS product with these features and marketing channels...
```

**Transformed Prompt:**
```
Please first analyze the main content, then methodically identify missing elements, unanswered questions, or overlooked considerations that need addressing. Comprehensively identify gaps across multiple dimensions, including questions, resources, stakeholders, risks, and dependencies. Conduct a detailed analysis to identify both obvious and subtle gaps that might significantly impact outcomes. For each identified gap, suggest potential solutions, approaches, or strategies to address it.

We plan to launch our SaaS product with these features and marketing channels...
```

### Exhaustive stakeholder-focused gap analysis without solutions

**Original Prompt:**
```
Here's our urban redevelopment proposal...
```

**Transformed Prompt:**
```
Please first analyze the main content, then methodically identify missing elements, unanswered questions, or overlooked considerations that need addressing. Focus specifically on identifying overlooked stakeholders, individuals, or groups whose perspectives or needs are not adequately addressed. Conduct an extremely comprehensive analysis to identify all possible gaps, including edge cases and minor considerations. Focus solely on identifying gaps without suggesting solutions or remedies.

Here's our urban redevelopment proposal...
```

## Transformation Details

**Base Instruction:** Please first analyze the main content, then methodically identify missing elements, unanswered questions, or overlooked considerations that need addressing.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `aspects`:
  - When set to `questions`: Focus specifically on identifying unanswered questions and unresolved issues that need clarification.
  - When set to `resources`: Focus specifically on identifying missing resources, tools, skills, or capabilities needed for implementation or success.
  - When set to `stakeholders`: Focus specifically on identifying overlooked stakeholders, individuals, or groups whose perspectives or needs are not adequately addressed.
  - When set to `risks`: Focus specifically on identifying potential risks, threats, and vulnerabilities that have not been adequately considered.
  - When set to `dependencies`: Focus specifically on identifying overlooked dependencies, prerequisites, or contingencies that could affect implementation or outcomes.
  - When set to `comprehensive`: Comprehensively identify gaps across multiple dimensions, including questions, resources, stakeholders, risks, and dependencies.

- `depth`:
  - When set to `basic`: Conduct a focused analysis to identify the most obvious and critical gaps.
  - When set to `thorough`: Conduct a detailed analysis to identify both obvious and subtle gaps that might significantly impact outcomes.
  - When set to `exhaustive`: Conduct an extremely comprehensive analysis to identify all possible gaps, including edge cases and minor considerations.

- `solutions`:
  - When set to `true`: For each identified gap, suggest potential solutions, approaches, or strategies to address it.
  - When set to `false`: Focus solely on identifying gaps without suggesting solutions or remedies.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Limitations**: Enhances FindGaps Limitations and FindGaps complement each other by identifying both inherent constraints and missing elements
- **BreakAndBuild**: Enhances FindGaps FindGaps can help identify issues that BreakAndBuild can then address in its reconstruction phase
- **StressTest**: Enhances FindGaps FindGaps plus StressTest provides a comprehensive approach to identifying both missing elements and potential breaking points

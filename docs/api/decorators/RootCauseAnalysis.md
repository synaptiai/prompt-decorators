# RootCauseAnalysis Decorator

Guides a methodical approach to identify the fundamental cause of an issue.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `depth` | `enum` | Analysis depth | `deep` |
| `method` | `enum` | Analysis method | `systematic` |
| `approach` | `enum` | Investigation approach | `isolation` |

## Depth Options

- `surface`: Conduct a basic analysis to identify immediate causes.
- `intermediate`: Investigate beyond immediate causes to identify contributing factors.
- `deep`: Perform a thorough analysis to uncover underlying systemic issues.
- `comprehensive`: Conduct an exhaustive investigation examining all possible factors and their interactions.

## Method Options

- `5-whys`: Use the 5 Whys technique, repeatedly asking why to drill down to the root cause.
- `fishbone`: Apply the fishbone (Ishikawa) diagram approach to categorize potential causes.
- `fault-tree`: Employ fault tree analysis to identify combinations of events leading to the issue.
- `systematic`: Follow a structured, step-by-step approach to eliminate possible causes.

## Approach Options

- `elimination`: Systematically rule out potential causes until the root cause is identified.
- `reproduction`: Attempt to reproduce the issue under controlled conditions to identify triggers.
- `isolation`: Isolate components or variables to determine their contribution to the issue.
- `comparison`: Compare working and non-working systems to identify differences.

## Examples

### Basic root cause analysis for a technical issue

```
+++RootCauseAnalysis()
Why does our database connection fail intermittently?
```

A systematic analysis using default parameters (deep depth, systematic method, isolation approach) to identify the fundamental cause of database connection issues.

### Comprehensive analysis using the 5-whys method

```
+++RootCauseAnalysis(depth=comprehensive, method=5-whys, approach=isolation)
Determine the root cause of the data inconsistency issue that occurs during concurrent updates.
```

An exhaustive investigation using the 5-whys technique and isolation approach to identify the fundamental cause of data inconsistency during concurrent updates.

### Surface-level analysis for quick troubleshooting

```
+++RootCauseAnalysis(depth=surface, method=fishbone)
Why is the customer checkout process failing?
```

A basic analysis using the fishbone diagram approach to categorize potential immediate causes of checkout failures.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Analyze the root cause of this problem systematically. Don't just address symptoms. {depth_instruction} {method_instruction} {approach_instruction}

**Notes:** Simplified instruction format for models with more limited context windows.


## Implementation Guidance

### Software debugging

**Original Prompt:**
```
Why is my application crashing when multiple users log in simultaneously?
```

**Transformed Prompt:**
```
Perform a root cause analysis to identify the fundamental cause of the issue. Focus on methodical investigation rather than symptoms. Perform a thorough analysis to uncover underlying systemic issues. Follow a structured, step-by-step approach to eliminate possible causes. Isolate components or variables to determine their contribution to the issue.

Why is my application crashing when multiple users log in simultaneously?
```

**Notes:** The decorator adds structured analysis guidance before the original question.

### Business process troubleshooting

**Original Prompt:**
```
Help me understand why our order fulfillment process is experiencing delays.
```

**Transformed Prompt:**
```
Perform a root cause analysis to identify the fundamental cause of the issue. Focus on methodical investigation rather than symptoms. Conduct an exhaustive investigation examining all possible factors and their interactions. Use the 5 Whys technique, repeatedly asking why to drill down to the root cause. Systematically rule out potential causes until the root cause is identified.

Help me understand why our order fulfillment process is experiencing delays.
```

**Notes:** Parameters are set to comprehensive depth, 5-whys method, and elimination approach.

## Transformation Details

**Base Instruction:** Perform a root cause analysis to identify the fundamental cause of the issue. Focus on methodical investigation rather than symptoms.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `depth`:
  - When set to `surface`: Conduct a basic analysis to identify immediate causes.
  - When set to `intermediate`: Investigate beyond immediate causes to identify contributing factors.
  - When set to `deep`: Perform a thorough analysis to uncover underlying systemic issues.
  - When set to `comprehensive`: Conduct an exhaustive investigation examining all possible factors and their interactions.

- `method`:
  - When set to `5-whys`: Use the 5 Whys technique, repeatedly asking why to drill down to the root cause.
  - When set to `fishbone`: Apply the fishbone (Ishikawa) diagram approach to categorize potential causes.
  - When set to `fault-tree`: Employ fault tree analysis to identify combinations of events leading to the issue.
  - When set to `systematic`: Follow a structured, step-by-step approach to eliminate possible causes.

- `approach`:
  - When set to `elimination`: Systematically rule out potential causes until the root cause is identified.
  - When set to `reproduction`: Attempt to reproduce the issue under controlled conditions to identify triggers.
  - When set to `isolation`: Isolate components or variables to determine their contribution to the issue.
  - When set to `comparison`: Compare working and non-working systems to identify differences.

## Compatibility

- **Requires**: None
- **Conflicts**: QuickFix, SimpleAnswer
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **SystematicThinking**: Enhances RootCauseAnalysis RootCauseAnalysis works well with SystematicThinking as both promote structured problem-solving approaches.
- **QuickFix**: Conflicts with RootCauseAnalysis RootCauseAnalysis focuses on finding underlying causes rather than quick solutions.

# RootCauseAnalysis Decorator

Guides a methodical approach to identify the fundamental cause of an issue.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `depth` | enum | Analysis depth | deep |
| `method` | enum | Analysis method | systematic |
| `approach` | enum | Investigation approach | isolation |

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

### gpt-3.5-turbo

**Instruction:** Analyze the root cause of this problem systematically. Don't just address symptoms. {depth_instruction} {method_instruction} {approach_instruction}

**Notes:** Simplified instruction format for models with more limited context windows.


## Compatibility

- **Requires**: None
- **Conflicts**: QuickFix, SimpleAnswer
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **SystematicThinking**: Enhances RootCauseAnalysis RootCauseAnalysis works well with SystematicThinking as both promote structured problem-solving approaches.
- **QuickFix**: Conflicts with RootCauseAnalysis RootCauseAnalysis focuses on finding underlying causes rather than quick solutions.

# FactCheck Decorator

Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `confidence` | boolean | Whether to include explicit confidence levels for claims | True |
| `uncertain` | enum | How to handle uncertain information | mark |
| `strictness` | enum | The threshold for considering information verified | moderate |

## Uncertain Options

- `mark`: Clearly mark any uncertain or speculative information with appropriate qualifiers (e.g., 'may be', 'some evidence suggests', 'it is theorized').
- `exclude`: Only include well-established or highly likely information, omitting speculative or highly uncertain claims entirely.
- `qualify`: Include uncertain information but qualify it extensively with context about the limitations of current knowledge.

## Strictness Options

- `low`: Apply a lenient standard for verification, allowing inclusion of generally accepted information even without definitive proof.
- `moderate`: Apply a balanced verification standard, requiring reliable sources for claims but accepting well-supported consensus views.
- `high`: Apply a stringent verification standard, requiring strong evidence and multiple reliable sources for all claims.

## Examples

### Basic fact checking with confidence indicators

```
+++FactCheck
Explain the history and effectiveness of vaccines.
```

Provides information about vaccines with clear indications of confidence levels for different claims

### High-strictness fact checking that excludes uncertain information

```
+++FactCheck(strictness=high, uncertain=exclude)
Describe what we know about dark matter.
```

Presents only well-established scientific facts about dark matter, excluding speculative or uncertain information

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Carefully distinguish between facts with strong evidence, facts with moderate evidence, and speculative information. Label your confidence level for each claim (Established fact, Likely, Uncertain). Be precise about what is and isn't well-supported by evidence.

**Notes:** This model benefits from more explicit instructions about the need to clearly signal confidence levels


## Implementation Guidance

### Basic fact checking with confidence indicators

**Original Prompt:**
```
Explain the history and effectiveness of vaccines.
```

**Transformed Prompt:**
```
Please verify the factual claims in your response and clearly distinguish between well-established facts, likely facts, and uncertain or speculative information. For each factual claim, include an explicit indication of your confidence level (e.g., 'Established fact:', 'Likely:', 'Uncertain:'). Clearly mark any uncertain or speculative information with appropriate qualifiers (e.g., 'may be', 'some evidence suggests', 'it is theorized'). Apply a balanced verification standard, requiring reliable sources for claims but accepting well-supported consensus views.

Explain the history and effectiveness of vaccines.
```

### High-strictness fact checking excluding uncertain information

**Original Prompt:**
```
Describe what we know about dark matter.
```

**Transformed Prompt:**
```
Please verify the factual claims in your response and clearly distinguish between well-established facts, likely facts, and uncertain or speculative information. For each factual claim, include an explicit indication of your confidence level (e.g., 'Established fact:', 'Likely:', 'Uncertain:'). Only include well-established or highly likely information, omitting speculative or highly uncertain claims entirely. Apply a stringent verification standard, requiring strong evidence and multiple reliable sources for all claims.

Describe what we know about dark matter.
```

## Transformation Details

**Base Instruction:** Please verify the factual claims in your response and clearly distinguish between well-established facts, likely facts, and uncertain or speculative information.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `confidence`:
  - When set to `true`: For each factual claim, include an explicit indication of your confidence level (e.g., 'Established fact:', 'Likely:', 'Uncertain:').
  - When set to `false`: Maintain factual accuracy but do not explicitly label confidence levels for individual claims.

- `uncertain`:
  - When set to `mark`: Clearly mark any uncertain or speculative information with appropriate qualifiers (e.g., 'may be', 'some evidence suggests', 'it is theorized').
  - When set to `exclude`: Only include well-established or highly likely information, omitting speculative or highly uncertain claims entirely.
  - When set to `qualify`: Include uncertain information but qualify it extensively with context about the limitations of current knowledge.

- `strictness`:
  - When set to `low`: Apply a lenient standard for verification, allowing inclusion of generally accepted information even without definitive proof.
  - When set to `moderate`: Apply a balanced verification standard, requiring reliable sources for claims but accepting well-supported consensus views.
  - When set to `high`: Apply a stringent verification standard, requiring strong evidence and multiple reliable sources for all claims.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CiteSource**: Enhances FactCheck CiteSource pairs well with FactCheck by providing references for verified claims
- **Uncertainty**: Enhances FactCheck Uncertainty complements FactCheck by providing detailed probabilistic assessment of uncertain claims

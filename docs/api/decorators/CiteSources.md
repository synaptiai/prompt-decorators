# CiteSources Decorator

Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `style` | enum | The placement and format of citations within the response | inline |
| `format` | enum | The citation format to use | APA |
| `comprehensive` | boolean | Whether to cite every claim (true) or only major claims (false) | False |

## Style Options

- `inline`: Add citations directly in the text using parenthetical references.
- `footnote`: Use numbered footnotes for citations, with footnotes appearing at the bottom of relevant sections.
- `endnote`: Use numbered endnotes for citations, with all notes appearing in a References section at the end.

## Format Options

- `APA`: Format citations according to APA style guidelines.
- `MLA`: Format citations according to MLA style guidelines.
- `Chicago`: Format citations according to Chicago Manual of Style guidelines.
- `Harvard`: Format citations according to Harvard referencing style guidelines.
- `IEEE`: Format citations according to IEEE citation style guidelines.

## Examples

### Basic inline citations for a scientific topic

```
+++CiteSources
Explain the evidence for climate change.
```

Explains climate change with inline citations to scientific sources in APA format

### Comprehensive footnote citations in Chicago style

```
+++CiteSources(style=footnote, format=Chicago, comprehensive=true)
Describe the major events of World War II.
```

Delivers a detailed account of WWII with comprehensive footnote citations in Chicago style for all factual claims

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Your response should include citations for the claims you make. For each significant fact or statistic, provide a citation to a credible source.

**Notes:** This model may need more explicit instructions about proper citation formatting


## Implementation Guidance

### Standard implementation with APA inline citations

**Original Prompt:**
```
Explain the evidence for climate change.
```

**Transformed Prompt:**
```
Please include citations for factual claims in your response to enhance credibility and enable verification. Add citations directly in the text using parenthetical references. Format citations according to APA style guidelines. Only cite major claims, specialized knowledge, statistics, and direct quotes.

Explain the evidence for climate change.
```

### Comprehensive Chicago footnotes

**Original Prompt:**
```
Describe the major events of World War II.
```

**Transformed Prompt:**
```
Please include citations for factual claims in your response to enhance credibility and enable verification. Use numbered footnotes for citations, with footnotes appearing at the bottom of relevant sections. Format citations according to Chicago Manual of Style guidelines. Cite every factual claim, including commonly known facts.

Describe the major events of World War II.
```

## Transformation Details

**Base Instruction:** Please include citations for factual claims in your response to enhance credibility and enable verification.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `style`:
  - When set to `inline`: Add citations directly in the text using parenthetical references.
  - When set to `footnote`: Use numbered footnotes for citations, with footnotes appearing at the bottom of relevant sections.
  - When set to `endnote`: Use numbered endnotes for citations, with all notes appearing in a References section at the end.

- `format`:
  - When set to `APA`: Format citations according to APA style guidelines.
  - When set to `MLA`: Format citations according to MLA style guidelines.
  - When set to `Chicago`: Format citations according to Chicago Manual of Style guidelines.
  - When set to `Harvard`: Format citations according to Harvard referencing style guidelines.
  - When set to `IEEE`: Format citations according to IEEE citation style guidelines.

- `comprehensive`:
  - When set to `true`: Cite every factual claim, including commonly known facts.
  - When set to `false`: Only cite major claims, specialized knowledge, statistics, and direct quotes.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **FactCheck**: Enhances CiteSources CiteSources pairs well with FactCheck for highly reliable information
- **Concise**: Conflicts with CiteSources Comprehensive citations may conflict with concise output requirements

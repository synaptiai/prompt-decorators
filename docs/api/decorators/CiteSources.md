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

### gpt-3.5-turbo

**Instruction:** Your response should include citations for the claims you make. For each significant fact or statistic, provide a citation to a credible source.

**Notes:** This model may need more explicit instructions about proper citation formatting


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **FactCheck**: Enhances CiteSources CiteSources pairs well with FactCheck for highly reliable information
- **Concise**: Conflicts with CiteSources Comprehensive citations may conflict with concise output requirements

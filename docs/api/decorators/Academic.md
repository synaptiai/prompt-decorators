# Academic Decorator

Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `style` | enum | The academic discipline style to follow | scientific |
| `format` | enum | The citation format to use for references | APA |

## Style Options

- `humanities`: Use conventions typical of humanities scholarship, including interpretive analysis, theoretical frameworks, and engagement with cultural, historical, or philosophical contexts.
- `scientific`: Follow scientific writing conventions, including clear methodology descriptions, evidence-based claims, objective tone, and precise technical terminology.
- `legal`: Adopt legal academic writing style, including careful statutory interpretation, case analysis, precedent citation, and attention to doctrinal frameworks.

## Format Options

- `APA`: Format all citations and references according to APA (American Psychological Association) style, 7th edition.
- `MLA`: Format all citations and references according to MLA (Modern Language Association) style, 9th edition.
- `Chicago`: Format all citations and references according to Chicago style (Chicago Manual of Style), 17th edition.
- `Harvard`: Format all citations and references according to Harvard referencing style.
- `IEEE`: Format all citations and references according to IEEE citation style used in engineering and computer science.

## Examples

### Scientific academic response with APA citations

```
+++Academic
Discuss the evidence for climate change.
```

Produces a scholarly analysis of climate change evidence using formal scientific language and proper APA citations

### Humanities-focused academic response with MLA citations

```
+++Academic(style=humanities, format=MLA)
Analyze the themes in Shakespeare's Hamlet.
```

Provides a literary analysis of Hamlet using humanities-appropriate terminology and MLA citation format

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Write this response as a scholarly {style} academic paper with formal language, precise terminology, and proper structure (introduction, literature review, analysis/discussion, conclusion). Use {format} citations for all factual claims. Include appropriate academic vocabulary, transitional phrases, and maintain an objective, analytical stance.

**Notes:** This model sometimes needs more explicit guidance to maintain consistent academic tone and proper citation formats throughout


## Compatibility

- **Requires**: None
- **Conflicts**: ELI5, Creative, Motivational
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CiteSources**: Enhances Academic CiteSources complements Academic by ensuring thorough citation practices consistent with academic standards
- **ELI5**: Conflicts with Academic ELI5's simplified language directly conflicts with Academic's scholarly language requirements
- **Creative**: Conflicts with Academic Creative's artistic expression conflicts with Academic's formal scholarly conventions
- **PeerReview**: Enhances Academic PeerReview pairs well with Academic to simulate scholarly publication review processes

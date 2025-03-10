# Creative Decorator

Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `level` | enum | The degree of creative thinking to apply | high |
| `elements` | array | Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative) |  |
| `constraints` | array | Optional creative constraints to work within |  |

## Level Options

- `moderate`: Use creativity to make the content engaging while ensuring it remains accessible and practical. Incorporate creative elements that enhance understanding without overshadowing the substance.
- `high`: Apply significant creative thinking to present the information in fresh, surprising ways. Use vivid language, unexpected angles, and novel framing to create an engaging and memorable response.
- `unconventional`: Push far beyond conventional thinking to create a truly original response. Break traditional patterns, challenge assumptions, and explore highly unusual perspectives or approaches.

## Examples

### Basic creative response to a standard question

```
+++Creative
Explain how the internet works.
```

Provides an imaginative explanation of the internet using unexpected metaphors and creative language while maintaining accuracy

### Highly creative response with specific elements

```
+++Creative(level=unconventional, elements=[metaphor,narrative,wordplay], constraints=[must reference nature])
Describe the principles of quantum computing.
```

Delivers an unconventional explanation of quantum computing through an engaging narrative filled with nature metaphors and clever wordplay

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Be creative, original and imaginative in your response. Use {level} levels of creativity and incorporate {elements} in your writing. Work within these constraints: {constraints}. Focus on making the response engaging, unexpected, and thought-provoking while still addressing the core question.

**Notes:** This model sometimes needs explicit encouragement to break from conventional patterns in its responses


## Compatibility

- **Requires**: None
- **Conflicts**: Academic, Professional
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Academic**: Conflicts with Creative Creative's imaginative expression conflicts with Academic's formal scholarly conventions
- **Professional**: Conflicts with Creative Creative's playful approach conflicts with Professional's business-oriented formality
- **Analogical**: Enhances Creative Analogical reasoning works well with Creative to develop rich, imaginative comparisons
- **Narrative**: Enhances Creative Narrative structure pairs excellently with Creative to build engaging storylines

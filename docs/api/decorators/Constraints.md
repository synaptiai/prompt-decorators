# Constraints Decorator

Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `wordCount` | number | Maximum number of words allowed in the response |  |
| `timeframe` | string | Maximum time required to implement or consume the response (e.g., '5min', '1hr', '1week') |  |
| `vocabulary` | enum | Constraints on vocabulary usage |  |
| `custom` | string | Custom constraint to apply (e.g., 'no negatives', 'use only questions', 'each sentence starts with consecutive letters of the alphabet') |  |

## Vocabulary Options

- `simple`: Use only simple, everyday vocabulary that would be understood by elementary school students. Avoid jargon, technical terms, and complex words.
- `technical`: Use precise technical vocabulary appropriate to the subject matter, including field-specific terminology and concepts.
- `domain-specific`: Employ specialized vocabulary from the relevant domain or field, using terms of art and professional language.
- `creative`: Use varied, vivid, and evocative vocabulary that enhances engagement, including metaphors, sensory language, and uncommon word choices.

## Examples

### Word count constraint for a complex topic

```
+++Constraints(wordCount=100)
Explain quantum computing principles.
```

Provides a concise explanation of quantum computing, carefully limiting the response to exactly 100 words

### Multiple constraints for a creative response

```
+++Constraints(wordCount=200, vocabulary=creative, custom=each paragraph must contain exactly three sentences)
Describe a futuristic city.
```

Delivers a 200-word description of a futuristic city using creative vocabulary, with each paragraph containing exactly three sentences

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** You must follow these exact constraints: {wordCount} {timeframe} {vocabulary} {custom}. These are hard requirements - your response will only be valuable if it strictly adheres to these constraints.

**Notes:** This model sometimes needs stronger emphasis on constraints to ensure they are followed precisely


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Concise**: Enhances Constraints Constraints with wordCount and Concise work well together to enforce brevity in different ways
- **Detailed**: Conflicts with Constraints Constraints with low wordCount may conflict with Detailed's aim for comprehensiveness
- **Creative**: Enhances Constraints Constraints often enhance creativity by forcing innovative solutions within limitations

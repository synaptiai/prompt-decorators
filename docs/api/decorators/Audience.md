# Audience Decorator

Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `level` | enum | The expertise level of the target audience | intermediate |
| `domain` | string | Specific knowledge domain or field for domain-specific terminology adaptation | general |
| `examples` | boolean | Whether to include additional examples for clarity | True |

## Level Options

- `beginner`: Write for beginners with no prior knowledge of the subject. Use simple language, avoid jargon, and explain all technical terms. Start with fundamental concepts.
- `intermediate`: Write for an audience with basic familiarity of the subject. You can use some field-specific terms, but explain more advanced concepts.
- `expert`: Write for a knowledgeable audience with extensive experience in the field. You can use specialized terminology and discuss advanced concepts directly.
- `technical`: Write for technical professionals who need precise, detailed information. Use proper technical terminology, reference standards, and provide implementation details where relevant.

## Examples

### Technical explanation for experts in a specific field

```
+++Audience(level=technical, domain=cybersecurity)
Explain zero-knowledge proofs.
```

Provides an in-depth technical explanation of zero-knowledge proofs using cybersecurity-specific terminology and concepts

### Beginner-friendly explanation with examples

```
+++Audience(level=beginner, examples=true)
How does machine learning work?
```

Explains machine learning concepts in simple terms with multiple illustrative examples suitable for complete beginners

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Adapt your language, terminology, and examples for a specific audience:

**Notes:** This model benefits from more direct instructions about audience adaptation


## Implementation Guidance

### Technical audience in cybersecurity

**Original Prompt:**
```
Explain zero-knowledge proofs.
```

**Transformed Prompt:**
```
Please tailor your response for a specific audience expertise level. Write for technical professionals who need precise, detailed information. Use proper technical terminology, reference standards, and provide implementation details where relevant. The audience has specific interest in the cybersecurity field, so use appropriate concepts and examples from this domain. Include multiple concrete examples to illustrate key points and enhance understanding.

Explain zero-knowledge proofs.
```

### Beginner audience with examples

**Original Prompt:**
```
How does machine learning work?
```

**Transformed Prompt:**
```
Please tailor your response for a specific audience expertise level. Write for beginners with no prior knowledge of the subject. Use simple language, avoid jargon, and explain all technical terms. Start with fundamental concepts. The audience has specific interest in the general field, so use appropriate concepts and examples from this domain. Include multiple concrete examples to illustrate key points and enhance understanding.

How does machine learning work?
```

## Transformation Details

**Base Instruction:** Please tailor your response for a specific audience expertise level.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `level`:
  - When set to `beginner`: Write for beginners with no prior knowledge of the subject. Use simple language, avoid jargon, and explain all technical terms. Start with fundamental concepts.
  - When set to `intermediate`: Write for an audience with basic familiarity of the subject. You can use some field-specific terms, but explain more advanced concepts.
  - When set to `expert`: Write for a knowledgeable audience with extensive experience in the field. You can use specialized terminology and discuss advanced concepts directly.
  - When set to `technical`: Write for technical professionals who need precise, detailed information. Use proper technical terminology, reference standards, and provide implementation details where relevant.

- `domain`:
  - Format: The audience has specific interest in the {value} field, so use appropriate concepts and examples from this domain.

- `examples`:
  - When set to `true`: Include multiple concrete examples to illustrate key points and enhance understanding.
  - When set to `false`: Focus on clear explanations without requiring numerous examples.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ELI5**: Conflicts with Audience ELI5 targets a specific audience level that may contradict the level specified in Audience
- **Technical**: Enhances Audience Technical can be combined with Audience when level=technical for enhanced technical details

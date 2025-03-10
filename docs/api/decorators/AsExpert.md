# AsExpert Decorator

Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `domain` | `string` | The specific field or discipline the expert specializes in | `Required` |
| `experience` | `enum` | The experience level of the expert | `senior` |
| `technical` | `boolean` | Whether to use highly technical language and domain-specific terminology | `True` |

## Experience Options

- `junior`: Adopt the perspective of a junior expert with foundational training and some practical experience in the field.
- `senior`: Adopt the perspective of a senior expert with extensive experience and deep knowledge of the field's established principles and practices.
- `leading`: Adopt the perspective of a leading authority in the field with comprehensive expertise and recognition for significant contributions.
- `pioneering`: Adopt the perspective of a pioneering innovator in the field who is at the cutting edge of new developments and paradigm-shifting approaches.

## Examples

### Basic response as a domain expert

```
+++AsExpert(domain=neuroscience)
Explain how memories are formed in the brain.
```

Provides an explanation of memory formation from the perspective of a senior neuroscientist, using appropriate terminology and references to relevant research

### Highly technical response as pioneering expert

```
+++AsExpert(domain=cryptography, experience=pioneering, technical=true)
Assess the security implications of quantum computing for current encryption standards.
```

Delivers a technically sophisticated assessment of quantum computing's encryption impacts from the perspective of a pioneering cryptography expert, using advanced terminology and nuanced analysis

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Adopt the perspective of a {experience} expert in {domain}. Use your specialized knowledge to provide an authoritative response that demonstrates deep expertise. {technical} Make sure to incorporate relevant frameworks, methodologies, and current understandings from the field.

**Notes:** This model sometimes needs stronger prompting to maintain consistent expert perspective and appropriate level of technical terminology


## Implementation Guidance

### Senior neuroscientist explanation of memory formation

**Original Prompt:**
```
Explain how memories are formed in the brain.
```

**Transformed Prompt:**
```
Please respond from the perspective of a domain expert in the specified field, providing authoritative content that reflects expert knowledge, terminology, and analytical approach. Respond as a specialist in neuroscience, incorporating field-specific knowledge, methodologies, and frameworks. Adopt the perspective of a senior expert with extensive experience and deep knowledge of the field's established principles and practices. Use domain-specific terminology, technical language, and specialized concepts appropriate for communication between experts in the field.

Explain how memories are formed in the brain.
```

### Pioneering cryptography expert on quantum computing implications

**Original Prompt:**
```
Assess the security implications of quantum computing for current encryption standards.
```

**Transformed Prompt:**
```
Please respond from the perspective of a domain expert in the specified field, providing authoritative content that reflects expert knowledge, terminology, and analytical approach. Respond as a specialist in cryptography, incorporating field-specific knowledge, methodologies, and frameworks. Adopt the perspective of a pioneering innovator in the field who is at the cutting edge of new developments and paradigm-shifting approaches. Use domain-specific terminology, technical language, and specialized concepts appropriate for communication between experts in the field.

Assess the security implications of quantum computing for current encryption standards.
```

## Transformation Details

**Base Instruction:** Please respond from the perspective of a domain expert in the specified field, providing authoritative content that reflects expert knowledge, terminology, and analytical approach.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `domain`:
  - Format: Respond as a specialist in {value}, incorporating field-specific knowledge, methodologies, and frameworks.

- `experience`:
  - When set to `junior`: Adopt the perspective of a junior expert with foundational training and some practical experience in the field.
  - When set to `senior`: Adopt the perspective of a senior expert with extensive experience and deep knowledge of the field's established principles and practices.
  - When set to `leading`: Adopt the perspective of a leading authority in the field with comprehensive expertise and recognition for significant contributions.
  - When set to `pioneering`: Adopt the perspective of a pioneering innovator in the field who is at the cutting edge of new developments and paradigm-shifting approaches.

- `technical`:
  - When set to `true`: Use domain-specific terminology, technical language, and specialized concepts appropriate for communication between experts in the field.
  - When set to `false`: Use more accessible language while maintaining accuracy, minimizing technical jargon but preserving the essential expert insights.

## Compatibility

- **Requires**: None
- **Conflicts**: ELI5
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ELI5**: Conflicts with AsExpert AsExpert (especially with technical=true) directly conflicts with ELI5's simplified approach
- **Academic**: Enhances AsExpert Academic complements AsExpert by adding scholarly conventions to expert knowledge
- **Technical**: Enhances AsExpert Technical works well with AsExpert to emphasize precision and deep domain terminology

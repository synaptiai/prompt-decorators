# AsExpert Decorator

Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `domain` | string | The specific field or discipline the expert specializes in | Required |
| `experience` | enum | The experience level of the expert | senior |
| `technical` | boolean | Whether to use highly technical language and domain-specific terminology | True |

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

### gpt-3.5-turbo

**Instruction:** Adopt the perspective of a {experience} expert in {domain}. Use your specialized knowledge to provide an authoritative response that demonstrates deep expertise. {technical} Make sure to incorporate relevant frameworks, methodologies, and current understandings from the field.

**Notes:** This model sometimes needs stronger prompting to maintain consistent expert perspective and appropriate level of technical terminology


## Compatibility

- **Requires**: None
- **Conflicts**: ELI5
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ELI5**: Conflicts with AsExpert AsExpert (especially with technical=true) directly conflicts with ELI5's simplified approach
- **Academic**: Enhances AsExpert Academic complements AsExpert by adding scholarly conventions to expert knowledge
- **Technical**: Enhances AsExpert Technical works well with AsExpert to emphasize precision and deep domain terminology

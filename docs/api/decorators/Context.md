# Context Decorator

A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.

**Category**: Meta

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `domain` | string | The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education') | Required |
| `scope` | enum | Which aspects of decorators to contextualize | all |
| `level` | enum | The expertise level to target within the domain | mixed |

## Scope Options

- `terminology`: Use domain-specific terminology and vocabulary from this field, but keep other aspects generalized.
- `examples`: Use domain-specific examples and cases to illustrate concepts, but keep terminology and structure generalized.
- `structure`: Organize the information according to standard frameworks and structures used in this domain, but keep terminology and examples generalized.
- `all`: Apply domain-specific terminology, examples, and structural organization throughout the entire response.

## Level Options

- `beginner`: Target the response for newcomers to the field with limited domain knowledge or expertise.
- `intermediate`: Target the response for individuals with moderate familiarity and experience in the domain.
- `expert`: Target the response for specialists and experts with advanced knowledge in the domain.
- `mixed`: Structure the response to be accessible to beginners while also including deeper insights for experts.

## Examples

### Basic domain-specific adaptation of decorators

```
+++Context(domain=medicine)
+++StepByStep
+++Detailed
Explain how vaccines are developed.
```

Applies the StepByStep and Detailed decorators with medical context-awareness, using appropriate medical terminology, examples, and structures for explaining vaccine development

### Targeted contextualization for specific expertise level

```
+++Context(domain=programming, scope=examples, level=beginner)
+++Reasoning
+++ELI5
Explain how databases work.
```

Uses the Reasoning and ELI5 decorators with programming-appropriate examples specifically tailored for beginners, while keeping general terminology and structure accessible

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Interpret this request within the context of the {domain} field. Use knowledge, terminology, and standards specific to this domain at a {level} level. Focus particularly on domain-appropriate {scope}.

**Notes:** This model sometimes needs more explicit reminders to maintain consistent domain-specific focus throughout longer responses

### gpt-4

**Instruction:** Frame your response specifically for the {domain} domain. Adjust your {scope} to match domain conventions and target a {level} expertise level.

**Notes:** This model handles domain adaptation well but benefits from clear guidance about which aspects to contextualize


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Audience**: Enhances Context Audience complements Context by further refining the target expertise level within the domain context
- **Professional**: Enhances Context Professional works well with Context to ensure appropriate formal language for the specific domain context
- **Custom**: Enhances Context Custom can provide additional specialized behaviors for particular domain contexts beyond standard adaptations

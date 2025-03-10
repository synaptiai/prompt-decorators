# Professional Decorator

Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `industry` | string | The specific industry context to adapt the language for | general |
| `formality` | enum | The level of formality to maintain in the response | standard |

## Formality Options

- `standard`: Use standard professional business language that is clear, concise, and respectful without being overly formal.
- `high`: Use a high level of formality with careful attention to precise language, proper business terminology, and structured communication.
- `executive`: Use executive-level communication style with strategic framing, high-level insights, and language appropriate for senior leadership or board presentations.

## Examples

### Standard professional business communication

```
+++Professional
Explain the benefits of implementing a CRM system.
```

Delivers a clear, professional explanation of CRM benefits using business-appropriate language and structure

### Industry-specific executive-level communication

```
+++Professional(industry=healthcare, formality=executive)
Summarize the impact of telehealth adoption on patient outcomes.
```

Produces an executive-level analysis of telehealth impacts using healthcare industry terminology and highly formal business language

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Use formal business language appropriate for a professional {industry} context. Maintain {formality} level of formality. Ensure proper structure, avoid colloquialisms, and use industry-appropriate terminology where relevant.

**Notes:** This model sometimes needs explicit reminders to maintain consistent professional tone throughout longer responses


## Compatibility

- **Requires**: None
- **Conflicts**: ELI5, Creative
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ELI5**: Conflicts with Professional Professional's formal business language directly conflicts with ELI5's simplified explanations
- **Creative**: Conflicts with Professional Professional's structured business approach conflicts with Creative's artistic expression
- **Audience**: Enhances Professional Professional works well with Audience to further refine the target business context

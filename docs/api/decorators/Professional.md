# Professional Decorator

Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `industry` | `string` | The specific industry context to adapt the language for | `general` |
| `formality` | `enum` | The level of formality to maintain in the response | `standard` |

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

### gpt-4-turbo

**Instruction:** Use formal business language appropriate for a professional {industry} context. Maintain {formality} level of formality. Ensure proper structure, avoid colloquialisms, and use industry-appropriate terminology where relevant.

**Notes:** This model sometimes needs explicit reminders to maintain consistent professional tone throughout longer responses


## Implementation Guidance

### Standard professional response about business systems

**Original Prompt:**
```
Explain the benefits of implementing a CRM system.
```

**Transformed Prompt:**
```
Please respond using professional, business-oriented language appropriate for formal workplace communication. Use standard professional business language that is clear, concise, and respectful without being overly formal. Adapt the language and terminology to be appropriate for the general industry, using relevant terminology and frameworks where applicable.

Explain the benefits of implementing a CRM system.
```

### Executive-level healthcare industry communication

**Original Prompt:**
```
Summarize the impact of telehealth adoption on patient outcomes.
```

**Transformed Prompt:**
```
Please respond using professional, business-oriented language appropriate for formal workplace communication. Use executive-level communication style with strategic framing, high-level insights, and language appropriate for senior leadership or board presentations. Adapt the language and terminology to be appropriate for the healthcare industry, using relevant terminology and frameworks where applicable.

Summarize the impact of telehealth adoption on patient outcomes.
```

## Transformation Details

**Base Instruction:** Please respond using professional, business-oriented language appropriate for formal workplace communication.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `industry`:
  - Format: Adapt the language and terminology to be appropriate for the {value} industry, using relevant terminology and frameworks where applicable.

- `formality`:
  - When set to `standard`: Use standard professional business language that is clear, concise, and respectful without being overly formal.
  - When set to `high`: Use a high level of formality with careful attention to precise language, proper business terminology, and structured communication.
  - When set to `executive`: Use executive-level communication style with strategic framing, high-level insights, and language appropriate for senior leadership or board presentations.

## Compatibility

- **Requires**: None
- **Conflicts**: ELI5, Creative
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ELI5**: Conflicts with Professional Professional's formal business language directly conflicts with ELI5's simplified explanations
- **Creative**: Conflicts with Professional Professional's structured business approach conflicts with Creative's artistic expression
- **Audience**: Enhances Professional Professional works well with Audience to further refine the target business context

# Persona Decorator

Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `role` | `string` | The specific persona or stakeholder role to adopt | `Required` |
| `traits` | `array` | Key personality traits or characteristics of the persona | `` |
| `goals` | `array` | Primary goals or concerns of the persona | `` |

## Examples

### Response from the perspective of a specific stakeholder

```
+++Persona(role=customer)
What are the implications of implementing a new subscription model?
```

Analyzes the subscription model from a customer's perspective, focusing on value, convenience, and potential concerns

### Detailed persona with specific traits and goals

```
+++Persona(role=senior software engineer, traits=[pragmatic,detail-oriented,experienced], goals=[code quality,maintainability,efficiency])
Evaluate the proposal to switch from monolith to microservices.
```

Provides a detailed analysis of the monolith-to-microservices transition from the perspective of a pragmatic, detail-oriented senior engineer who prioritizes code quality and maintainability

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Respond as a {role} with these characteristics: {traits}. Your main priorities are: {goals}. Think about how someone in this position with these traits and goals would naturally approach this topic. Use appropriate vocabulary, concerns, and priorities for this persona.

**Notes:** This model sometimes needs reminders to maintain consistent persona characteristics throughout longer responses


## Implementation Guidance

### Customer perspective on subscription model

**Original Prompt:**
```
What are the implications of implementing a new subscription model?
```

**Transformed Prompt:**
```
Please respond from the perspective of the specified persona, adapting your analysis and viewpoint to reflect how this persona would naturally view and respond to the situation or topic. Adopt the perspective and viewpoint of a customer, considering how someone in this role would approach the topic.

What are the implications of implementing a new subscription model?
```

### Detailed senior engineer persona evaluating architecture change

**Original Prompt:**
```
Evaluate the proposal to switch from monolith to microservices.
```

**Transformed Prompt:**
```
Please respond from the perspective of the specified persona, adapting your analysis and viewpoint to reflect how this persona would naturally view and respond to the situation or topic. Adopt the perspective and viewpoint of a senior software engineer, considering how someone in this role would approach the topic. Incorporate these key personality traits into the persona: [pragmatic,detail-oriented,experienced]. Let these characteristics influence how the persona perceives and reacts to the topic. Prioritize these primary goals and concerns that drive the persona's thinking: [code quality,maintainability,efficiency]. Ensure these priorities shape the perspective and recommendations offered.

Evaluate the proposal to switch from monolith to microservices.
```

## Transformation Details

**Base Instruction:** Please respond from the perspective of the specified persona, adapting your analysis and viewpoint to reflect how this persona would naturally view and respond to the situation or topic.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `role`:
  - Format: Adopt the perspective and viewpoint of a {value}, considering how someone in this role would approach the topic.

- `traits`:
  - Format: Incorporate these key personality traits into the persona: {value}. Let these characteristics influence how the persona perceives and reacts to the topic.

- `goals`:
  - Format: Prioritize these primary goals and concerns that drive the persona's thinking: {value}. Ensure these priorities shape the perspective and recommendations offered.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **AsExpert**: Enhances Persona Persona can be combined with AsExpert to create a character who is both in a specific role and has domain expertise
- **Audience**: Enhances Persona Persona (for the speaker) works well with Audience (for the listener) to create targeted communication
- **Balanced**: Conflicts with Persona Persona intentionally presents a single perspective, which may conflict with Balanced's goal of presenting multiple viewpoints

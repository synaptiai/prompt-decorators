# RedTeam Decorator

Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `strength` | enum | How aggressive or challenging the red team analysis should be | moderate |
| `focus` | array | Specific aspects to focus the red team analysis on |  |
| `constructive` | boolean | Whether to include constructive suggestions for improvement after critiques | True |

## Strength Options

- `moderate`: Apply a balanced adversarial analysis that identifies significant issues while maintaining a fair and reasonable perspective.
- `aggressive`: Apply an intensely critical adversarial analysis that aggressively challenges all aspects of the content, including fundamental assumptions and approaches.
- `steelman`: Apply the most sophisticated possible critique by first strengthening the argument to its best form, then finding its most substantive vulnerabilities.

## Examples

### Basic red team analysis of a business proposal

```
+++RedTeam
Here's our plan to launch a new subscription service...
```

Analyzes the subscription service plan from an adversarial perspective, identifying potential weaknesses, oversights, and challenges

### Aggressive red team analysis with specific focus areas

```
+++RedTeam(strength=aggressive, focus=[security,scalability,market-fit], constructive=true)
Review our new authentication system design.
```

Aggressively challenges the authentication system design, specifically targeting security, scalability, and market-fit concerns, followed by constructive improvement suggestions

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Act as a {strength} critic examining this content. Look for all possible problems, weaknesses, and vulnerabilities. {focus} Challenge underlying assumptions. Think about what could go wrong, what's missing, and why this might fail. {constructive} Be thorough and consider multiple angles of attack.

**Notes:** This model may need more explicit direction to maintain a consistently critical stance throughout the analysis


## Implementation Guidance

### Moderate red team analysis of a subscription service plan

**Original Prompt:**
```
Here's our plan to launch a new subscription service...
```

**Transformed Prompt:**
```
Please analyze the content from an adversarial perspective, actively looking for flaws, vulnerabilities, and weak points. Simulate how a critic or opponent would evaluate and challenge the ideas, plans, or arguments presented. Apply a balanced adversarial analysis that identifies significant issues while maintaining a fair and reasonable perspective. After identifying vulnerabilities and weaknesses, provide constructive suggestions for addressing each issue and strengthening the overall approach.

Here's our plan to launch a new subscription service...
```

### Aggressive focused red team analysis of an authentication system

**Original Prompt:**
```
Review our new authentication system design.
```

**Transformed Prompt:**
```
Please analyze the content from an adversarial perspective, actively looking for flaws, vulnerabilities, and weak points. Simulate how a critic or opponent would evaluate and challenge the ideas, plans, or arguments presented. Apply an intensely critical adversarial analysis that aggressively challenges all aspects of the content, including fundamental assumptions and approaches. Focus your adversarial analysis specifically on these aspects: [security,scalability,market-fit]. After identifying vulnerabilities and weaknesses, provide constructive suggestions for addressing each issue and strengthening the overall approach.

Review our new authentication system design.
```

## Transformation Details

**Base Instruction:** Please analyze the content from an adversarial perspective, actively looking for flaws, vulnerabilities, and weak points. Simulate how a critic or opponent would evaluate and challenge the ideas, plans, or arguments presented.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `strength`:
  - When set to `moderate`: Apply a balanced adversarial analysis that identifies significant issues while maintaining a fair and reasonable perspective.
  - When set to `aggressive`: Apply an intensely critical adversarial analysis that aggressively challenges all aspects of the content, including fundamental assumptions and approaches.
  - When set to `steelman`: Apply the most sophisticated possible critique by first strengthening the argument to its best form, then finding its most substantive vulnerabilities.

- `focus`:
  - Format: Focus your adversarial analysis specifically on these aspects: {value}.

- `constructive`:
  - When set to `true`: After identifying vulnerabilities and weaknesses, provide constructive suggestions for addressing each issue and strengthening the overall approach.
  - When set to `false`: Focus solely on identifying weaknesses and vulnerabilities without providing suggestions for improvement.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Limitations**: Enhances RedTeam RedTeam and Limitations work together to identify both external challenges and inherent constraints
- **Steelman**: Enhances RedTeam When RedTeam is set to 'steelman' strength, it works particularly well with the Steelman decorator
- **FindGaps**: Enhances RedTeam FindGaps complements RedTeam by identifying missing elements while RedTeam challenges existing elements

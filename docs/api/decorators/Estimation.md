# Estimation Decorator

Helps with effort estimation for development tasks.

**Category**: Developer Workflow

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `method` | `enum` | Estimation approach | `fibonacci` |
| `confidence` | `enum` | Estimate type | `range` |
| `factors` | `enum` | Considerations to include | `all` |

## Method Options

- `t-shirt`: Use t-shirt sizing (XS, S, M, L, XL, XXL) for your estimation.
- `fibonacci`: Use Fibonacci sequence points (1, 2, 3, 5, 8, 13, 21, etc.) for your estimation.
- `hours`: Estimate the effort in hours of work required.
- `days`: Estimate the effort in days of work required.

## Confidence Options

- `best-case`: Provide a best-case scenario estimate assuming ideal conditions.
- `worst-case`: Provide a worst-case scenario estimate accounting for potential complications.
- `expected`: Provide your most realistic expected estimate.
- `range`: Provide a range from best-case to worst-case estimates.

## Factors Options

- `complexity`: Consider technical complexity in your estimation.
- `risk`: Consider risk factors in your estimation.
- `unknowns`: Consider unknown factors and learning curves in your estimation.
- `dependencies`: Consider dependencies on other systems or teams in your estimation.
- `all`: Consider all factors including complexity, risk, unknowns, and dependencies in your estimation.

## Examples

### Fibonacci estimation with confidence range for authentication system

```
+++Estimation(method=fibonacci, confidence=range, factors=all)
Estimate the effort required to implement a new authentication system with social login and MFA support.
```

Provides a structured estimation using Fibonacci points with a range of estimates, considering all relevant factors for implementing an authentication system.

### T-shirt sizing for a simple feature

```
+++Estimation(method=t-shirt, confidence=expected)
Estimate the effort to add a dark mode toggle to our web application.
```

Provides a t-shirt size estimation (likely S or M) for implementing a dark mode feature with explanation of the expected effort.

### Hourly estimation focusing on complexity

```
+++Estimation(method=hours, confidence=worst-case, factors=complexity)
Estimate the effort to refactor our payment processing module.
```

Provides an hourly worst-case estimate focusing specifically on the technical complexity aspects of refactoring a payment system.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Analyze this development task and provide a detailed effort estimation. Break down the components and explain your reasoning for each estimate.

**Notes:** More explicit instruction for models with less context understanding.


## Implementation Guidance

### Software development task estimation

**Original Prompt:**
```
Estimate the effort required to implement a new authentication system with social login and MFA support.
```

**Transformed Prompt:**
```
Provide an effort estimation for the development task described. Break down the task into components and explain your reasoning. Use Fibonacci sequence points (1, 2, 3, 5, 8, 13, 21, etc.) for your estimation. Provide a range from best-case to worst-case estimates. Consider all factors including complexity, risk, unknowns, and dependencies in your estimation.

Estimate the effort required to implement a new authentication system with social login and MFA support.
```

**Notes:** The decorator adds specific estimation guidance before the original prompt.

## Transformation Details

**Base Instruction:** Provide an effort estimation for the development task described. Break down the task into components and explain your reasoning.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `method`:
  - When set to `t-shirt`: Use t-shirt sizing (XS, S, M, L, XL, XXL) for your estimation.
  - When set to `fibonacci`: Use Fibonacci sequence points (1, 2, 3, 5, 8, 13, 21, etc.) for your estimation.
  - When set to `hours`: Estimate the effort in hours of work required.
  - When set to `days`: Estimate the effort in days of work required.

- `confidence`:
  - When set to `best-case`: Provide a best-case scenario estimate assuming ideal conditions.
  - When set to `worst-case`: Provide a worst-case scenario estimate accounting for potential complications.
  - When set to `expected`: Provide your most realistic expected estimate.
  - When set to `range`: Provide a range from best-case to worst-case estimates.

- `factors`:
  - When set to `complexity`: Consider technical complexity in your estimation.
  - When set to `risk`: Consider risk factors in your estimation.
  - When set to `unknowns`: Consider unknown factors and learning curves in your estimation.
  - When set to `dependencies`: Consider dependencies on other systems or teams in your estimation.
  - When set to `all`: Consider all factors including complexity, risk, unknowns, and dependencies in your estimation.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ProjectPlanning**: Enhances Estimation Works well with ProjectPlanning decorator to create comprehensive project plans with effort estimates.
- **TechnicalSpecification**: Enhances Estimation Can be combined with TechnicalSpecification to include effort estimates in technical documentation.

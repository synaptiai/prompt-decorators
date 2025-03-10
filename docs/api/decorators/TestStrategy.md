# TestStrategy Decorator

Designs comprehensive testing approaches for software components or systems.

**Category**: Testing And Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `level` | `enum` | Testing scope level | `unit` |
| `framework` | `enum` | Testing framework to use | `language-appropriate` |
| `approach` | `enum` | Testing methodology | `tdd` |

## Level Options

- `unit`: Focus on unit testing individual components in isolation.
- `integration`: Design integration tests that verify interactions between components.
- `e2e`: Create end-to-end tests that validate complete user workflows.
- `performance`: Develop performance tests to measure system responsiveness and stability under load.
- `security`: Implement security tests to identify vulnerabilities and ensure data protection.

## Framework Options

- `jest`: Use Jest as the testing framework.
- `pytest`: Implement tests using the pytest framework.
- `junit`: Develop tests with the JUnit framework.
- `mocha`: Create tests using the Mocha framework.
- `cypress`: Build tests with the Cypress framework.

## Approach Options

- `tdd`: Follow Test-Driven Development methodology (write tests before implementation).
- `bdd`: Use Behavior-Driven Development with descriptive scenarios that reflect user requirements.
- `property`: Implement property-based testing to verify invariants across many generated inputs.
- `snapshot`: Utilize snapshot testing to detect unexpected UI or data structure changes.

## Examples

### Integration testing strategy for an authentication service

```
+++TestStrategy(level=integration, framework=jest, approach=bdd)
Design a testing strategy for an authentication service with database and external API dependencies.
```

A comprehensive integration testing strategy using Jest and BDD approach, focusing on testing interactions between the authentication service, database, and external APIs.

### Unit testing strategy with default parameters

```
+++TestStrategy()
Design tests for a string manipulation utility library.
```

A unit testing strategy using TDD methodology with an appropriate framework for the implementation language, focusing on testing individual functions in isolation.

### Performance testing for a high-traffic API

```
+++TestStrategy(level=performance, framework=junit)
Create tests for a payment processing API that handles 1000 transactions per second.
```

A performance testing strategy using JUnit to measure throughput, response time, and stability of the payment API under high load conditions.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a detailed testing strategy that includes test cases, methodologies, and frameworks for the following scenario:

**Notes:** More explicit instruction for models with less context understanding.


## Implementation Guidance

### Web application testing

**Original Prompt:**
```
Design a testing strategy for an authentication service with database and external API dependencies.
```

**Transformed Prompt:**
```
Design a testing strategy for the following, considering best practices for software quality assurance. Focus on integration tests that verify interactions between components. Use Jest as the testing framework. Use Behavior-Driven Development with descriptive scenarios that reflect user requirements.

Design a testing strategy for an authentication service with database and external API dependencies.
```

**Notes:** This example shows how the decorator adds specific guidance for integration testing with Jest using BDD methodology.

## Transformation Details

**Base Instruction:** Design a testing strategy for the following, considering best practices for software quality assurance.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `level`:
  - When set to `unit`: Focus on unit testing individual components in isolation.
  - When set to `integration`: Design integration tests that verify interactions between components.
  - When set to `e2e`: Create end-to-end tests that validate complete user workflows.
  - When set to `performance`: Develop performance tests to measure system responsiveness and stability under load.
  - When set to `security`: Implement security tests to identify vulnerabilities and ensure data protection.

- `framework`:
  - When set to `jest`: Use Jest as the testing framework.
  - When set to `pytest`: Implement tests using the pytest framework.
  - When set to `junit`: Develop tests with the JUnit framework.
  - When set to `mocha`: Create tests using the Mocha framework.
  - When set to `cypress`: Build tests with the Cypress framework.
  - When set to `language-appropriate`: Select an appropriate testing framework based on the implementation language.

- `approach`:
  - When set to `tdd`: Follow Test-Driven Development methodology (write tests before implementation).
  - When set to `bdd`: Use Behavior-Driven Development with descriptive scenarios that reflect user requirements.
  - When set to `property`: Implement property-based testing to verify invariants across many generated inputs.
  - When set to `snapshot`: Utilize snapshot testing to detect unexpected UI or data structure changes.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances TestStrategy TestStrategy works well with CodeReview to ensure both testing strategy and implementation quality.
- **ArchitectureDesign**: Enhances TestStrategy Can be used after ArchitectureDesign to develop tests that validate the architectural requirements.

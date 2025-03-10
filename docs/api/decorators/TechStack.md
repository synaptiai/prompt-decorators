# TechStack Decorator

Recommends technology combinations based on requirements.

**Category**: Architecture And Design

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `for` | enum | Target application type | web |
| `constraints` | enum | Project limitations | none |
| `maturity` | enum | Technology maturity preference | modern-stable |

## For Options

- `web`: Focus on web development technologies, frameworks, and hosting solutions.
- `mobile`: Focus on mobile app development frameworks, languages, and deployment platforms.
- `desktop`: Focus on desktop application frameworks, languages, and distribution methods.
- `iot`: Focus on IoT device programming, connectivity solutions, and data processing.
- `data`: Focus on data storage, processing, analysis, and visualization technologies.
- `ai`: Focus on AI/ML frameworks, model deployment, and supporting infrastructure.
- `enterprise`: Focus on enterprise-grade technologies with strong support and integration capabilities.

## Constraints Options

- `budget`: Prioritize cost-effective or open-source solutions that minimize licensing and operational costs.
- `scale`: Prioritize technologies that can handle significant growth in users, data, or traffic.
- `team-size`: Consider the learning curve and required expertise for the recommended technologies.
- `performance`: Emphasize high-performance technologies and optimization strategies.
- `security`: Prioritize technologies with strong security features and established security practices.
- `timeline`: Recommend technologies that enable rapid development and deployment.

## Maturity Options

- `bleeding-edge`: Include cutting-edge technologies that may still be in beta or early adoption phases.
- `modern-stable`: Recommend modern technologies that are stable and have good community support.
- `established`: Focus on well-established technologies with proven track records.
- `enterprise-proven`: Recommend only technologies with enterprise support, extensive documentation, and long-term stability guarantees.

## Examples

### Web application tech stack for a startup

```
+++TechStack(for=web, constraints=budget, maturity=modern-stable)
Recommend a technology stack for a B2B SaaS application with emphasis on rapid development and scalability.
```

A detailed recommendation of web technologies suitable for a B2B SaaS application, focusing on cost-effective solutions that are modern and stable, with explanations for why each component is appropriate.

### Enterprise mobile application tech stack

```
+++TechStack(for=mobile, constraints=security, maturity=enterprise-proven)
What technologies should we use for a financial services mobile app that needs to comply with banking regulations?
```

A comprehensive recommendation of enterprise-proven mobile technologies with strong security features, suitable for financial services applications with regulatory requirements.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Recommend a technology stack for the following requirements. List specific technologies, frameworks, libraries, and tools that work well together. For each component, briefly explain why it's appropriate for the requirements.

**Notes:** More explicit instruction for models with less context understanding.


## Implementation Guidance

### Web application recommendation

**Original Prompt:**
```
Recommend a technology stack for a B2B SaaS application with emphasis on rapid development and scalability.
```

**Transformed Prompt:**
```
Recommend a technology stack that is appropriate for the specified requirements. Include specific technologies, frameworks, and tools that work well together. Explain why each component is suitable for the requirements. Focus on web development technologies, frameworks, and hosting solutions. Prioritize technologies that can handle significant growth in users, data, or traffic. Recommend modern technologies that are stable and have good community support.

Recommend a technology stack for a B2B SaaS application with emphasis on rapid development and scalability.
```

**Notes:** The decorator adds specific guidance about the type of application, constraints, and technology maturity preferences.

## Transformation Details

**Base Instruction:** Recommend a technology stack that is appropriate for the specified requirements. Include specific technologies, frameworks, and tools that work well together. Explain why each component is suitable for the requirements.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `for`:
  - When set to `web`: Focus on web development technologies, frameworks, and hosting solutions.
  - When set to `mobile`: Focus on mobile app development frameworks, languages, and deployment platforms.
  - When set to `desktop`: Focus on desktop application frameworks, languages, and distribution methods.
  - When set to `iot`: Focus on IoT device programming, connectivity solutions, and data processing.
  - When set to `data`: Focus on data storage, processing, analysis, and visualization technologies.
  - When set to `ai`: Focus on AI/ML frameworks, model deployment, and supporting infrastructure.
  - When set to `enterprise`: Focus on enterprise-grade technologies with strong support and integration capabilities.

- `constraints`:
  - When set to `budget`: Prioritize cost-effective or open-source solutions that minimize licensing and operational costs.
  - When set to `scale`: Prioritize technologies that can handle significant growth in users, data, or traffic.
  - When set to `team-size`: Consider the learning curve and required expertise for the recommended technologies.
  - When set to `performance`: Emphasize high-performance technologies and optimization strategies.
  - When set to `security`: Prioritize technologies with strong security features and established security practices.
  - When set to `timeline`: Recommend technologies that enable rapid development and deployment.

- `maturity`:
  - When set to `bleeding-edge`: Include cutting-edge technologies that may still be in beta or early adoption phases.
  - When set to `modern-stable`: Recommend modern technologies that are stable and have good community support.
  - When set to `established`: Focus on well-established technologies with proven track records.
  - When set to `enterprise-proven`: Recommend only technologies with enterprise support, extensive documentation, and long-term stability guarantees.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ArchitecturalPattern**: Enhances TechStack TechStack works well with ArchitecturalPattern to provide both high-level architecture and specific technology recommendations.
- **CodeGeneration**: Enhances TechStack TechStack can provide context for CodeGeneration to generate code in the appropriate languages and frameworks.

# Monitoring Decorator

Creates monitoring and alerting setups for systems.

**Category**: Devops And Infrastructure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `focus` | enum | Monitoring emphasis | comprehensive |
| `tools` | enum | Preferred monitoring tools | recommend |
| `implementation` | enum | Implementation depth | configuration |

## Focus Options

- `performance`: Emphasize performance metrics, throughput, and latency monitoring.
- `errors`: Prioritize error detection, logging, and exception tracking.
- `security`: Focus on security-related monitoring, intrusion detection, and vulnerability scanning.
- `business-metrics`: Concentrate on business KPIs and metrics that align with organizational goals.
- `user-experience`: Monitor user interactions, satisfaction metrics, and frontend performance.
- `comprehensive`: Provide a balanced monitoring approach covering all critical aspects of the system.

## Tools Options

- `datadog`: Implement the solution using Datadog as the primary monitoring platform.
- `prometheus`: Use Prometheus and associated tools for metrics collection and alerting.
- `cloudwatch`: Leverage AWS CloudWatch for monitoring and alerting capabilities.
- `newrelic`: Build the monitoring solution around New Relic's observability platform.
- `grafana`: Utilize Grafana for dashboarding, with appropriate data sources for collection.
- `elastic`: Implement using the Elastic Stack (Elasticsearch, Logstash, Kibana).
- `recommend`: Suggest the most appropriate monitoring tools based on the system requirements.

## Implementation Options

- `concepts`: Provide a high-level conceptual overview of the monitoring approach.
- `configuration`: Include specific configuration examples and implementation details.
- `full-setup`: Deliver comprehensive setup instructions with code samples and deployment guidance.

## Examples

### Performance monitoring for microservices

```
+++Monitoring(focus=performance, tools=prometheus, implementation=configuration)
Create a monitoring solution for our microservices architecture focusing on performance metrics and latency.
```

Provides a Prometheus-based monitoring configuration focused on performance metrics like request rates, latency distributions, and resource utilization for microservices.

### Security monitoring with comprehensive setup

```
+++Monitoring(focus=security, tools=elastic, implementation=full-setup)
We need to monitor our cloud infrastructure for potential security breaches.
```

Delivers a complete Elastic Stack setup with detailed implementation instructions for security monitoring, including log collection, SIEM rules, and security dashboards.

### Business metrics monitoring concepts

```
+++Monitoring(focus=business-metrics, implementation=concepts)
What should we monitor for our SaaS product?
```

Provides conceptual guidance on monitoring business KPIs for a SaaS product, including customer acquisition costs, churn rates, and lifetime value metrics.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create a monitoring setup for the system described below. Include specific tools, metrics to track, and alert configurations.

**Notes:** Simplified instruction for models with more limited context windows.


## Implementation Guidance

### Microservices Architecture

**Original Prompt:**
```
Create a monitoring solution for our microservices architecture focusing on performance metrics and latency.
```

**Transformed Prompt:**
```
Create a monitoring and alerting setup for the described system. Focus on providing practical, implementable monitoring solutions. Emphasize performance metrics, throughput, and latency monitoring. Use Prometheus and associated tools for metrics collection and alerting. Include specific configuration examples and implementation details.

Create a monitoring solution for our microservices architecture focusing on performance metrics and latency.
```

**Notes:** This example shows how the decorator adds specific guidance for performance monitoring in a microservices context using Prometheus.

### E-commerce Platform

**Original Prompt:**
```
How should we monitor our e-commerce platform?
```

**Transformed Prompt:**
```
Create a monitoring and alerting setup for the described system. Focus on providing practical, implementable monitoring solutions. Provide a balanced monitoring approach covering all critical aspects of the system. Suggest the most appropriate monitoring tools based on the system requirements. Include specific configuration examples and implementation details.

How should we monitor our e-commerce platform?
```

**Notes:** This example uses default values to provide a comprehensive monitoring approach with tool recommendations.

## Transformation Details

**Base Instruction:** Create a monitoring and alerting setup for the described system. Focus on providing practical, implementable monitoring solutions.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `focus`:
  - When set to `performance`: Emphasize performance metrics, throughput, and latency monitoring.
  - When set to `errors`: Prioritize error detection, logging, and exception tracking.
  - When set to `security`: Focus on security-related monitoring, intrusion detection, and vulnerability scanning.
  - When set to `business-metrics`: Concentrate on business KPIs and metrics that align with organizational goals.
  - When set to `user-experience`: Monitor user interactions, satisfaction metrics, and frontend performance.
  - When set to `comprehensive`: Provide a balanced monitoring approach covering all critical aspects of the system.

- `tools`:
  - When set to `datadog`: Implement the solution using Datadog as the primary monitoring platform.
  - When set to `prometheus`: Use Prometheus and associated tools for metrics collection and alerting.
  - When set to `cloudwatch`: Leverage AWS CloudWatch for monitoring and alerting capabilities.
  - When set to `newrelic`: Build the monitoring solution around New Relic's observability platform.
  - When set to `grafana`: Utilize Grafana for dashboarding, with appropriate data sources for collection.
  - When set to `elastic`: Implement using the Elastic Stack (Elasticsearch, Logstash, Kibana).
  - When set to `recommend`: Suggest the most appropriate monitoring tools based on the system requirements.

- `implementation`:
  - When set to `concepts`: Provide a high-level conceptual overview of the monitoring approach.
  - When set to `configuration`: Include specific configuration examples and implementation details.
  - When set to `full-setup`: Deliver comprehensive setup instructions with code samples and deployment guidance.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Infrastructure**: Enhances Monitoring Monitoring works well with Infrastructure decorator to provide complete infrastructure-as-code solutions with built-in monitoring.
- **Security**: Enhances Monitoring When combined with Security decorator, can create security-focused monitoring solutions.

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


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Infrastructure**: Enhances Monitoring Monitoring works well with Infrastructure decorator to provide complete infrastructure-as-code solutions with built-in monitoring.
- **Security**: Enhances Monitoring When combined with Security decorator, can create security-focused monitoring solutions.

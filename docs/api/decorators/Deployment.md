# Deployment Decorator

Generates deployment approaches for applications and services.

**Category**: Devops And Infrastructure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `platform` | enum | Deployment target | kubernetes |
| `strategy` | enum | Deployment methodology | rolling |
| `environment` | enum | Target environment | production |

## Platform Options

- `aws`: For AWS deployment, consider services like ECS, EKS, Lambda, or EC2 based on the application architecture.
- `azure`: For Azure deployment, consider services like AKS, App Service, Azure Functions, or Virtual Machines based on the application architecture.
- `gcp`: For GCP deployment, consider services like GKE, Cloud Run, Cloud Functions, or Compute Engine based on the application architecture.
- `kubernetes`: For Kubernetes deployment, detail the necessary manifests, namespace configuration, and resource requirements.
- `heroku`: For Heroku deployment, specify buildpacks, add-ons, and configuration variables needed.
- `netlify`: For Netlify deployment, include build settings, environment variables, and any required redirects or functions.
- `vercel`: For Vercel deployment, specify project configuration, environment variables, and any required serverless functions.
- `on-prem`: For on-premises deployment, detail hardware requirements, networking configuration, and installation procedures.

## Strategy Options

- `blue-green`: Implement a blue-green deployment strategy with two identical environments to minimize downtime and risk.
- `canary`: Implement a canary deployment strategy, gradually routing traffic to the new version to detect issues early.
- `rolling`: Implement a rolling deployment strategy, updating instances incrementally to maintain service availability.
- `recreate`: Implement a recreate deployment strategy, terminating the old version before deploying the new one (involves downtime).
- `custom`: Implement a custom deployment strategy tailored to the specific requirements of the application and infrastructure.

## Environment Options

- `dev`: Target the development environment with appropriate debugging capabilities and minimal resource allocation.
- `staging`: Target the staging environment, configured to mirror production for testing purposes.
- `production`: Target the production environment with full resource allocation, monitoring, and high availability considerations.
- `multi-region`: Target multiple geographic regions for redundancy and reduced latency, with appropriate data replication strategies.

## Examples

### Kubernetes blue-green deployment for production

```
+++Deployment(platform=kubernetes, strategy=blue-green, environment=production)
Create a deployment plan for our microservices architecture ensuring zero downtime.
```

A comprehensive deployment plan for Kubernetes using blue-green deployment strategy in production, with specific manifests, service configurations, and implementation steps to ensure zero downtime.

### AWS serverless deployment for development

```
+++Deployment(platform=aws, strategy=canary, environment=dev)
How should we deploy our Node.js API?
```

A deployment plan for AWS serverless services (like Lambda and API Gateway) using a canary deployment approach in the development environment, with appropriate IAM configurations and testing procedures.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a detailed deployment plan for the application with the following specifications:
- Platform: {platform}
- Deployment strategy: {strategy}
- Target environment: {environment}

Include configuration details, step-by-step implementation instructions, and best practices.

**Notes:** Simplified instruction with more explicit structure for models with less context understanding.


## Implementation Guidance

### Microservices architecture on Kubernetes

**Original Prompt:**
```
Create a deployment plan for our microservices architecture ensuring zero downtime.
```

**Transformed Prompt:**
```
Generate a deployment plan for the specified platform, using the appropriate deployment strategy and targeting the specified environment. Include necessary configuration, infrastructure requirements, and implementation steps.

For Kubernetes deployment, detail the necessary manifests, namespace configuration, and resource requirements.
Implement a blue-green deployment strategy with two identical environments to minimize downtime and risk.
Target the production environment with full resource allocation, monitoring, and high availability considerations.

Create a deployment plan for our microservices architecture ensuring zero downtime.
```

**Notes:** The decorator adds specific guidance for Kubernetes deployment using blue-green strategy in production, which aligns with the zero-downtime requirement.

## Transformation Details

**Base Instruction:** Generate a deployment plan for the specified platform, using the appropriate deployment strategy and targeting the specified environment. Include necessary configuration, infrastructure requirements, and implementation steps.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `platform`:
  - When set to `aws`: For AWS deployment, consider services like ECS, EKS, Lambda, or EC2 based on the application architecture.
  - When set to `azure`: For Azure deployment, consider services like AKS, App Service, Azure Functions, or Virtual Machines based on the application architecture.
  - When set to `gcp`: For GCP deployment, consider services like GKE, Cloud Run, Cloud Functions, or Compute Engine based on the application architecture.
  - When set to `kubernetes`: For Kubernetes deployment, detail the necessary manifests, namespace configuration, and resource requirements.
  - When set to `heroku`: For Heroku deployment, specify buildpacks, add-ons, and configuration variables needed.
  - When set to `netlify`: For Netlify deployment, include build settings, environment variables, and any required redirects or functions.
  - When set to `vercel`: For Vercel deployment, specify project configuration, environment variables, and any required serverless functions.
  - When set to `on-prem`: For on-premises deployment, detail hardware requirements, networking configuration, and installation procedures.

- `strategy`:
  - When set to `blue-green`: Implement a blue-green deployment strategy with two identical environments to minimize downtime and risk.
  - When set to `canary`: Implement a canary deployment strategy, gradually routing traffic to the new version to detect issues early.
  - When set to `rolling`: Implement a rolling deployment strategy, updating instances incrementally to maintain service availability.
  - When set to `recreate`: Implement a recreate deployment strategy, terminating the old version before deploying the new one (involves downtime).
  - When set to `custom`: Implement a custom deployment strategy tailored to the specific requirements of the application and infrastructure.

- `environment`:
  - When set to `dev`: Target the development environment with appropriate debugging capabilities and minimal resource allocation.
  - When set to `staging`: Target the staging environment, configured to mirror production for testing purposes.
  - When set to `production`: Target the production environment with full resource allocation, monitoring, and high availability considerations.
  - When set to `multi-region`: Target multiple geographic regions for redundancy and reduced latency, with appropriate data replication strategies.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Architecture**: Enhances Deployment The Architecture decorator can provide context about the application structure that informs the deployment approach.
- **Security**: Enhances Deployment The Security decorator can add security considerations to the deployment plan.

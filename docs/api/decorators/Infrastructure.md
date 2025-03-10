# Infrastructure Decorator

Generates infrastructure as code templates for environment provisioning.

**Category**: Devops And Infrastructure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `tool` | enum | Infrastructure as code tool | terraform |
| `environment` | enum | Target environment | multi-environment |
| `approach` | enum | Infrastructure philosophy | immutable |

## Tool Options

- `terraform`: Use Terraform HCL syntax and modules to define the infrastructure.
- `cloudformation`: Use AWS CloudFormation YAML/JSON templates to define the infrastructure.
- `arm`: Use Azure Resource Manager templates to define the infrastructure.
- `pulumi`: Use Pulumi with appropriate programming language to define the infrastructure.
- `cdk`: Use Cloud Development Kit with appropriate programming language to define the infrastructure.
- `ansible`: Use Ansible playbooks and roles to define the infrastructure.

## Environment Options

- `dev`: Optimize for development speed and cost efficiency.
- `staging`: Create a production-like environment with reduced resources.
- `prod`: Optimize for reliability, security, and performance.
- `multi-environment`: Design with environment promotion in mind, using variables or parameters to differentiate environments.

## Approach Options

- `immutable`: Design infrastructure to be replaced rather than modified when changes are needed.
- `mutable`: Design infrastructure that can be updated in place.
- `hybrid`: Use a combination of immutable and mutable approaches as appropriate.

## Examples

### Terraform infrastructure for a multi-environment web application

```
+++Infrastructure(tool=terraform, environment=multi-environment, approach=immutable)
Create infrastructure as code for a web application with frontend, API, and database tiers.
```

Generates Terraform code with modules for frontend (e.g., S3/CloudFront), API (e.g., ECS/Lambda), and database (e.g., RDS) with environment variables and immutable deployment strategy.

### CloudFormation template for a development environment

```
+++Infrastructure(tool=cloudformation, environment=dev, approach=mutable)
Create infrastructure for a data processing pipeline.
```

Generates AWS CloudFormation template optimized for development with cost-saving measures and the ability to update resources in place.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create infrastructure as code for the following requirements using {tool} for {environment} environments with an {approach} infrastructure approach:

**Notes:** Simplified instruction for models with less context capacity.


## Implementation Guidance

### Web application infrastructure

**Original Prompt:**
```
Create infrastructure as code for a web application with frontend, API, and database tiers.
```

**Transformed Prompt:**
```
Generate infrastructure as code using best practices for the specified tool, environment, and approach. Use Terraform HCL syntax and modules to define the infrastructure. Design with environment promotion in mind, using variables or parameters to differentiate environments. Design infrastructure to be replaced rather than modified when changes are needed.

Create infrastructure as code for a web application with frontend, API, and database tiers.
```

**Notes:** The decorator adds specific guidance based on the selected IaC tool, environment strategy, and infrastructure approach.

## Transformation Details

**Base Instruction:** Generate infrastructure as code using best practices for the specified tool, environment, and approach.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `tool`:
  - When set to `terraform`: Use Terraform HCL syntax and modules to define the infrastructure.
  - When set to `cloudformation`: Use AWS CloudFormation YAML/JSON templates to define the infrastructure.
  - When set to `arm`: Use Azure Resource Manager templates to define the infrastructure.
  - When set to `pulumi`: Use Pulumi with appropriate programming language to define the infrastructure.
  - When set to `cdk`: Use Cloud Development Kit with appropriate programming language to define the infrastructure.
  - When set to `ansible`: Use Ansible playbooks and roles to define the infrastructure.

- `environment`:
  - When set to `dev`: Optimize for development speed and cost efficiency.
  - When set to `staging`: Create a production-like environment with reduced resources.
  - When set to `prod`: Optimize for reliability, security, and performance.
  - When set to `multi-environment`: Design with environment promotion in mind, using variables or parameters to differentiate environments.

- `approach`:
  - When set to `immutable`: Design infrastructure to be replaced rather than modified when changes are needed.
  - When set to `mutable`: Design infrastructure that can be updated in place.
  - When set to `hybrid`: Use a combination of immutable and mutable approaches as appropriate.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, claude-instant
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CloudProvider**: Enhances Infrastructure CloudProvider can specify the target cloud platform, which complements the Infrastructure decorator.
- **Security**: Enhances Infrastructure Security decorator can add security-specific requirements to the infrastructure code.

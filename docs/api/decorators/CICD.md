# CICD Decorator

Designs continuous integration and delivery pipelines.

**Category**: Devops And Infrastructure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `tool` | enum | CI/CD platform or tool | github-actions |
| `complexity` | enum | Pipeline sophistication | standard |
| `focus` | enum | Pipeline emphasis | balanced |

## Tool Options

- `github-actions`: Option: github-actions
- `jenkins`: Option: jenkins
- `gitlab-ci`: Option: gitlab-ci
- `azure-devops`: Option: azure-devops
- `circle-ci`: Option: circle-ci
- `argocd`: Option: argocd

## Complexity Options

- `basic`: Create a simple pipeline with essential build and deploy steps.
- `standard`: Implement a standard pipeline with testing, building, and deployment stages.
- `comprehensive`: Design a comprehensive pipeline with extensive testing, security scanning, and multi-environment deployments.
- `enterprise`: Architect an enterprise-grade pipeline with advanced features including canary deployments, automated rollbacks, and detailed compliance reporting.

## Focus Options

- `speed`: Optimize the pipeline for fast feedback and rapid deployments.
- `reliability`: Prioritize reliability with robust testing and validation steps.
- `security`: Emphasize security with thorough scanning, vulnerability checks, and secure deployment practices.
- `compliance`: Ensure compliance with industry standards and regulations through appropriate checks and documentation.
- `balanced`: Balance speed, reliability, security, and compliance considerations.

## Examples

### Basic GitHub Actions pipeline for a web application

```
+++CICD(tool=github-actions, complexity=basic, focus=speed)
```

Generates a simple GitHub Actions workflow optimized for quick feedback and deployment.

### Comprehensive security-focused Jenkins pipeline

```
+++CICD(tool=jenkins, complexity=comprehensive, focus=security)
```

Creates a detailed Jenkins pipeline configuration with extensive security scanning and testing.

### Enterprise-grade GitLab CI pipeline with compliance focus

```
+++CICD(tool=gitlab-ci, complexity=enterprise, focus=compliance)
```

Designs an advanced GitLab CI/CD configuration with detailed compliance reporting and validation.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create a CI/CD pipeline with these requirements:

**Notes:** Simplified instruction for models with more limited context windows.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **SecurityRequirements**: Enhances CICD SecurityRequirements can provide detailed security specifications that complement the CICD decorator's security focus.
- **ComplianceFramework**: Enhances CICD ComplianceFramework can specify regulatory requirements that the CI/CD pipeline should address.

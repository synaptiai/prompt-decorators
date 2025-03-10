# CICD Decorator

Designs continuous integration and delivery pipelines.

**Category**: Devops And Infrastructure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `tool` | `enum` | CI/CD platform or tool | `github-actions` |
| `complexity` | `enum` | Pipeline sophistication | `standard` |
| `focus` | `enum` | Pipeline emphasis | `balanced` |

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

### gpt-4-turbo

**Instruction:** Create a CI/CD pipeline with these requirements:

**Notes:** Simplified instruction for models with more limited context windows.


## Implementation Guidance

### Web application development

**Original Prompt:**
```
Design a CI/CD pipeline for a financial services application with security scanning and compliance checks.
```

**Transformed Prompt:**
```
Design a CI/CD pipeline with the following specifications:
Using github-actions as the CI/CD platform
Design a comprehensive pipeline with extensive testing, security scanning, and multi-environment deployments.
Emphasize security with thorough scanning, vulnerability checks, and secure deployment practices.

Design a CI/CD pipeline for a financial services application with security scanning and compliance checks.
```

**Notes:** The decorator adds specific CI/CD tool information and emphasizes security aspects for financial applications.

## Transformation Details

**Base Instruction:** Design a CI/CD pipeline with the following specifications:

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `tool`:
  - Format: Using {value} as the CI/CD platform

- `complexity`:
  - When set to `basic`: Create a simple pipeline with essential build and deploy steps.
  - When set to `standard`: Implement a standard pipeline with testing, building, and deployment stages.
  - When set to `comprehensive`: Design a comprehensive pipeline with extensive testing, security scanning, and multi-environment deployments.
  - When set to `enterprise`: Architect an enterprise-grade pipeline with advanced features including canary deployments, automated rollbacks, and detailed compliance reporting.

- `focus`:
  - When set to `speed`: Optimize the pipeline for fast feedback and rapid deployments.
  - When set to `reliability`: Prioritize reliability with robust testing and validation steps.
  - When set to `security`: Emphasize security with thorough scanning, vulnerability checks, and secure deployment practices.
  - When set to `compliance`: Ensure compliance with industry standards and regulations through appropriate checks and documentation.
  - When set to `balanced`: Balance speed, reliability, security, and compliance considerations.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **SecurityRequirements**: Enhances CICD SecurityRequirements can provide detailed security specifications that complement the CICD decorator's security focus.
- **ComplianceFramework**: Enhances CICD ComplianceFramework can specify regulatory requirements that the CI/CD pipeline should address.

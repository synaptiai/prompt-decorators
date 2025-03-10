# Reproduce Decorator

Creates detailed steps to reproduce a reported issue.

**Category**: Testing And Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `environment` | `enum` | Target environment for reproduction | `local` |
| `detail` | `enum` | Level of detail in steps | `comprehensive` |
| `format` | `enum` | Output format | `steps` |

## Environment Options

- `local`: Provide reproduction steps for a local development environment.
- `staging`: Provide reproduction steps specifically for a staging environment.
- `prod`: Provide reproduction steps that can be safely executed in a production environment.
- `docker`: Provide reproduction steps using Docker containers.
- `specific-version`: Provide reproduction steps for a specific software version, noting version dependencies.

## Detail Options

- `minimal`: Provide only the essential steps needed to reproduce the issue.
- `comprehensive`: Provide detailed steps including setup, execution, and verification of the issue.
- `debug-oriented`: Provide extremely detailed steps with debugging information, logging points, and state verification throughout the process.

## Format Options

- `steps`: Format the reproduction as numbered steps with clear instructions.
- `script`: Format the reproduction as a script that can be executed to reproduce the issue.
- `docker-compose`: Format the reproduction as a docker-compose configuration and associated commands.
- `video-script`: Format the reproduction as a script for creating a demonstration video, including visual cues and narration points.

## Examples

### Creating Docker-based reproduction steps for a race condition

```
+++Reproduce(environment=docker, detail=comprehensive, format=script)
Create reproduction steps for a race condition we're seeing in our payment processing service.
```

A comprehensive script that can be executed to reproduce the race condition in a Docker environment, including setup, execution steps, and verification points.

### Minimal reproduction steps for a UI bug

```
+++Reproduce(detail=minimal)
Create steps to reproduce the dropdown menu disappearing in our admin panel.
```

A concise list of essential steps needed to observe the dropdown menu bug in a local environment.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create clear, step-by-step instructions to reproduce the reported issue. Be specific about environment setup, actions to take, and expected results.

**Notes:** Simpler instruction for models with less context capacity.


## Implementation Guidance

### Bug reproduction for web application

**Original Prompt:**
```
Create reproduction steps for a race condition we're seeing in our payment processing service.
```

**Transformed Prompt:**
```
Create detailed steps to reproduce the reported issue. Focus on clarity and completeness so that someone else can follow these steps to observe the same behavior. Provide reproduction steps using Docker containers. Provide detailed steps including setup, execution, and verification of the issue. Format the reproduction as a script that can be executed to reproduce the issue.

Create reproduction steps for a race condition we're seeing in our payment processing service.
```

**Notes:** The decorator adds specific instructions about environment (Docker), detail level (comprehensive), and format (script) to guide the reproduction creation.

## Transformation Details

**Base Instruction:** Create detailed steps to reproduce the reported issue. Focus on clarity and completeness so that someone else can follow these steps to observe the same behavior.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `environment`:
  - When set to `local`: Provide reproduction steps for a local development environment.
  - When set to `staging`: Provide reproduction steps specifically for a staging environment.
  - When set to `prod`: Provide reproduction steps that can be safely executed in a production environment.
  - When set to `docker`: Provide reproduction steps using Docker containers.
  - When set to `specific-version`: Provide reproduction steps for a specific software version, noting version dependencies.

- `detail`:
  - When set to `minimal`: Provide only the essential steps needed to reproduce the issue.
  - When set to `comprehensive`: Provide detailed steps including setup, execution, and verification of the issue.
  - When set to `debug-oriented`: Provide extremely detailed steps with debugging information, logging points, and state verification throughout the process.

- `format`:
  - When set to `steps`: Format the reproduction as numbered steps with clear instructions.
  - When set to `script`: Format the reproduction as a script that can be executed to reproduce the issue.
  - When set to `docker-compose`: Format the reproduction as a docker-compose configuration and associated commands.
  - When set to `video-script`: Format the reproduction as a script for creating a demonstration video, including visual cues and narration points.

## Compatibility

- **Requires**: None
- **Conflicts**: Summarize, Condense
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Debug**: Enhances Reproduce The Debug decorator can enhance Reproduce by adding specific debugging techniques to the reproduction steps.
- **Summarize**: Conflicts with Reproduce The Summarize decorator conflicts with Reproduce as it would condense the detailed steps needed for proper reproduction.

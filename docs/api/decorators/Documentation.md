# Documentation Decorator

Creates comprehensive documentation for various audiences.

**Category**: Developer Workflow

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `for` | enum | Documentation target | code |
| `format` | enum | Documentation format | markdown |
| `detail` | enum | Documentation comprehensiveness | standard |

## For Options

- `code`: Create code documentation that explains the implementation details, functions, classes, and methods.
- `api`: Create API documentation that includes endpoints, request/response formats, authentication, and error handling.
- `user`: Create user documentation that explains how to use the product or service from an end-user perspective.
- `admin`: Create administrator documentation that explains how to configure, manage, and troubleshoot the system.
- `architecture`: Create architecture documentation that explains the system design, components, and their interactions.

## Format Options

- `markdown`: Format the documentation in Markdown syntax.
- `javadoc`: Format the documentation in Javadoc syntax.
- `jsdoc`: Format the documentation in JSDoc syntax.
- `openapi`: Format the documentation following OpenAPI specification.
- `restructuredtext`: Format the documentation in reStructuredText syntax.
- `html`: Format the documentation in HTML.
- `jupyter`: Format the documentation as a Jupyter notebook with explanatory cells.

## Detail Options

- `minimal`: Include only essential information with brief descriptions.
- `standard`: Include standard level of detail with examples and explanations.
- `comprehensive`: Include exhaustive details, examples, edge cases, and cross-references.

## Examples

### Creating comprehensive API documentation in Markdown

```
+++Documentation(for=api, format=markdown, detail=comprehensive)
Create documentation for our payment processing API including authentication, endpoints, request/response formats, and error handling.
```

The model will generate comprehensive API documentation in Markdown format, covering all aspects of the payment processing API with detailed examples, error scenarios, and cross-references.

### Creating minimal user documentation

```
+++Documentation(for=user, format=html, detail=minimal)
Document how to use our photo editing application.
```

The model will generate concise user documentation in HTML format, covering only the essential features and workflows of the photo editing application.

### Creating standard code documentation

```
+++Documentation(for=code, format=jsdoc, detail=standard)
Document this JavaScript utility function library.
```

The model will generate standard JSDoc documentation for the JavaScript utility functions, including function signatures, parameters, return values, and basic usage examples.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Generate detailed documentation following these specifications:

**Notes:** For smaller models, be more explicit about documentation structure requirements.

### claude-2

**Instruction:** Please create well-structured documentation with the following characteristics:

**Notes:** Claude models respond well to clear structure guidance in documentation tasks.


## Compatibility

- **Requires**: None
- **Conflicts**: ELI5, Simplify
- **Compatible Models**: gpt-4, gpt-3.5-turbo, claude-2, llama-2, palm-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeAnalysis**: Enhances Documentation Documentation works well after CodeAnalysis to document the analyzed code.
- **ELI5**: Conflicts with Documentation ELI5 simplifies content while Documentation formalizes it, creating potential conflicts in tone and detail level.

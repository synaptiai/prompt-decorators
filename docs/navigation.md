# Documentation Navigation

This document defines the navigation structure for the Prompt Decorators documentation. It serves as a reference for generating a comprehensive sidebar and navigation elements across the documentation site.

## Sidebar Structure

```yaml
navigation:
  - title: Getting Started
    items:
      - title: Introduction
        path: /index.html
      - title: Installation
        path: /installation.html
      - title: Quickstart
        path: /tutorials/quickstart.html
      - title: Key Concepts
        path: /concepts.html
  
  - title: Core Documentation
    items:
      - title: Architecture Overview
        path: /architecture.html
      - title: BaseDecorator
        path: /api/modules/prompt_decorators.core.base.html
      - title: Request System
        path: /api/modules/prompt_decorators.core.request.html
      - title: Version Support
        path: /api/modules/prompt_decorators.core.version.html
  
  - title: Decorator Registry
    items:
      - title: Registry Overview
        path: /registry/overview.html
      - title: Using the Registry
        path: /registry/usage.html
      - title: Registry API
        path: /api/modules/prompt_decorators.utils.discovery.html
      - title: Available Decorators
        path: /registry/decorators.html

  - title: Built-in Decorators
    items:
      - title: Reasoning Decorators
        path: /decorators/reasoning.html
        children:
          - title: Reasoning
            path: /api/decorators/reasoning.html
          - title: StepByStep
            path: /api/decorators/stepbystep.html
          - title: FirstPrinciples
            path: /api/decorators/firstprinciples.html
      - title: Format Decorators
        path: /decorators/format.html
        children:
          - title: OutputFormat
            path: /api/decorators/outputformat.html
          - title: Bullet
            path: /api/decorators/bullet.html
          - title: Concise
            path: /api/decorators/concise.html
      - title: Style Decorators
        path: /decorators/style.html
        children:
          - title: Professional
            path: /api/decorators/professional.html
          - title: ELI5
            path: /api/decorators/eli5.html
          - title: Academic
            path: /api/decorators/academic.html
      - title: Verification Decorators
        path: /decorators/verification.html
        children:
          - title: FactCheck
            path: /api/decorators/factcheck.html
          - title: CiteSources
            path: /api/decorators/citesources.html
      - title: Meta Decorators
        path: /decorators/meta.html
        children:
          - title: Chain
            path: /api/decorators/chain.html
          - title: Conditional
            path: /api/decorators/conditional.html

  - title: Tutorials
    items:
      - title: Quickstart
        path: /tutorials/quickstart.html
      - title: Creating Custom Decorators
        path: /tutorials/creating_custom_decorator.html
      - title: Combining Decorators
        path: /tutorials/combining_decorators.html
      - title: Integration with LLM APIs
        path: /tutorials/llm_integration.html
      - title: Working with the Registry
        path: /tutorials/registry_usage.html

  - title: Advanced Topics
    items:
      - title: Compatibility Matrix
        path: /compatibility.html
      - title: Extension Development
        path: /advanced/extensions.html
      - title: Model-Specific Adaptations
        path: /advanced/model_specific.html
      - title: Performance Optimization
        path: /advanced/performance.html
      - title: Security Considerations
        path: /advanced/security.html

  - title: API Reference
    items:
      - title: Core API
        path: /api/modules/prompt_decorators.core.html
      - title: Utility API
        path: /api/modules/prompt_decorators.utils.html
      - title: Generator API
        path: /api/modules/prompt_decorators.generator.html
      - title: Decorators API
        path: /api/modules/prompt_decorators.decorators.html

  - title: Examples
    items:
      - title: Basic Examples
        path: /examples/basic.html
      - title: Advanced Usage
        path: /examples/advanced.html
      - title: Domain-Specific
        path: /examples/domains.html
        children:
          - title: Healthcare
            path: /examples/domains/healthcare.html
          - title: Finance
            path: /examples/domains/finance.html
          - title: Education
            path: /examples/domains/education.html
      - title: LLM Providers
        path: /examples/providers.html
        children:
          - title: OpenAI
            path: /examples/providers/openai.html
          - title: Anthropic
            path: /examples/providers/anthropic.html
          - title: Google Gemini
            path: /examples/providers/gemini.html

  - title: Community & Support
    items:
      - title: Contributing
        path: /community/contributing.html
      - title: Code of Conduct
        path: /community/code_of_conduct.html
      - title: Roadmap
        path: /community/roadmap.html
      - title: Changelog
        path: /community/changelog.html
```

## Breadcrumb Implementation

Each documentation page should include a breadcrumb navigation feature at the top of the page. The breadcrumb should reflect the hierarchical position of the current page in the navigation structure.

Example breadcrumb format:
```html
Home > Tutorials > Creating Custom Decorators
```

## Previous/Next Navigation

Each documentation page should include previous/next navigation links at the bottom of the page, based on the logical reading order defined in the navigation structure.

Example:
```html
Previous: Quickstart | Next: Combining Decorators
```

## Implementation Notes

1. The navigation structure should be implemented as a data file that can be consumed by the documentation generation system.
2. Each page should have appropriate metadata including:
   - Title
   - Description
   - Tags/Keywords
   - Last updated timestamp
   - Related pages

3. The sidebar should highlight the currently active page and expand the relevant section.
4. The navigation structure should be reflected in the URL structure for logical and predictable page access.

## Documentation Index

A separate index.md file should be created to serve as the search index and directory of all documentation pages, categorized according to the navigation structure and including a brief description of each page. 
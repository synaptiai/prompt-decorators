# API Reference

Welcome to the Prompt Decorators API Reference. This section provides detailed documentation for all components of the Prompt Decorators framework.

## Core Components

The [Core Module](modules/prompt_decorators.core.md) contains the foundational components of the Prompt Decorators framework:

- [Base](modules/prompt_decorators.core.base.md): Base classes for decorators
- [Registry](modules/prompt_decorators.core.registry.md): Registry management for decorators
- [Validation](modules/prompt_decorators.core.validation.md): Validation utilities for decorators
- [Request](modules/prompt_decorators.core.request.md): Request handling for decorators
- [Exceptions](modules/prompt_decorators.core.exceptions.md): Exception classes for error handling
- [Model Specific](modules/prompt_decorators.core.model_specific.md): Model-specific functionality

## Decorators

The [Decorators Module](modules/prompt_decorators.decorators.md) contains all the decorators available in the framework:

### Reasoning Decorators
- [Reasoning](decorators/Reasoning.md): Enhances reasoning capabilities
- [StepByStep](decorators/StepByStep.md): Breaks down reasoning into steps
- [TreeOfThought](decorators/TreeOfThought.md): Explores multiple reasoning paths
- [FirstPrinciples](decorators/FirstPrinciples.md): Reasons from first principles

### Output Structure Decorators
- [OutputFormat](decorators/OutputFormat.md): Controls output format
- [Schema](decorators/Schema.md): Structures output according to a schema
- [TableFormat](decorators/TableFormat.md): Formats output as a table
- [Bullet](decorators/Bullet.md): Formats output as bullet points
- [Outline](decorators/Outline.md): Formats output as an outline
- [MECE](decorators/MECE.md): Ensures output is mutually exclusive and collectively exhaustive
- [Comparison](decorators/Comparison.md): Formats output as a comparison
- [DecisionMatrix](decorators/DecisionMatrix.md): Formats output as a decision matrix
- [Timeline](decorators/Timeline.md): Formats output as a timeline
- [Summary](decorators/Summary.md): Summarizes output
- [Prioritize](decorators/Prioritize.md): Prioritizes items in output
- [Layered](decorators/Layered.md): Structures output in layers
- [Nested](decorators/Nested.md): Structures output in a nested format

### Tone and Style Decorators
- [Tone](decorators/Tone.md): Controls the tone of the output
- [Persona](decorators/Persona.md): Adopts a specific persona
- [Audience](decorators/Audience.md): Tailors output for a specific audience
- [Creative](decorators/Creative.md): Enhances creativity in output
- [Professional](decorators/Professional.md): Ensures professional tone
- [Academic](decorators/Academic.md): Adopts academic style
- [Concise](decorators/Concise.md): Makes output concise
- [Detailed](decorators/Detailed.md): Makes output detailed
- [ELI5](decorators/ELI5.md): Explains like I'm 5

### Meta Decorators
- [Context](decorators/Context.md): Provides context for the model
- [Custom](decorators/Custom.md): Creates custom decorators
- [Chain](decorators/Chain.md): Chains multiple decorators
- [Override](decorators/Override.md): Overrides decorator behavior
- [Conditional](decorators/Conditional.md): Applies decorators conditionally
- [Priority](decorators/Priority.md): Sets decorator priority
- [Version](decorators/Version.md): Specifies decorator version
- [Compatibility](decorators/Compatibility.md): Specifies decorator compatibility
- [Extension](decorators/Extension.md): Extends decorator functionality
- [BuildOn](decorators/BuildOn.md): Builds on existing decorators
- [Refine](decorators/Refine.md): Refines decorator output
- [Constraints](decorators/Constraints.md): Applies constraints to output

## Utilities

The [Utilities Module](modules/prompt_decorators.utils.md) contains utility functions and classes:

- [Cache](modules/prompt_decorators.utils.cache.md): Caching utilities
- [Compatibility](modules/prompt_decorators.utils.compatibility.md): Compatibility utilities
- [Discovery](modules/prompt_decorators.utils.discovery.md): Discovery utilities
- [Documentation](modules/prompt_decorators.utils.doc_gen.md): Documentation generation
- [Factory](modules/prompt_decorators.utils.factory.md): Factory utilities
- [JSON Loader](modules/prompt_decorators.utils.json_loader.md): JSON loading utilities
- [Model Detection](modules/prompt_decorators.utils.model_detection.md): Model detection utilities
- [Plugins](modules/prompt_decorators.utils.plugins.md): Plugin utilities
- [Telemetry](modules/prompt_decorators.utils.telemetry.md): Telemetry utilities

## Generator

The [Generator Module](modules/prompt_decorators.generator.md) contains code generation utilities:

- [Code Generator](modules/prompt_decorators.generator.code_gen.md): Generates decorator code
- [Test Generator](modules/prompt_decorators.generator.test_gen.md): Generates test code
- [Registry](modules/prompt_decorators.generator.registry.md): Registry management utilities

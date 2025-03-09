# Glossary

This glossary defines key terms and concepts used in the Prompt Decorators framework.

## A

### Annotation
The syntax used to apply a decorator to a prompt, consisting of the decorator prefix (`+++`), the decorator name, and optional parameters.

Example: `+++StepByStep(numbered=true)`

### Apply
The process of transforming a prompt by executing the decorator's transform function.

## C

### Category
A grouping of decorators with similar functionality or purpose, such as "Reasoning", "Format", or "Style".

### Claude Desktop
A desktop application for interacting with Anthropic's Claude AI model. Prompt Decorators integrates with Claude Desktop through the MCP protocol.

### Composite Decorator
A decorator that internally uses multiple other decorators to create a more complex transformation.

### Conflict
A situation where two or more decorators have incompatible behaviors or modify the same aspect of a prompt in contradictory ways.

## D

### Decorator
A reusable component that modifies a prompt to enhance how an LLM processes and responds to it.

### Decorator Definition
A specification of a decorator, including its name, description, category, parameters, and transform function.

### Decorator Instance
A specific instance of a decorator with particular parameter values.

### Decorator Pattern
A design pattern where objects (decorators) wrap around other objects (prompts) to modify their behavior without changing their structure.

### Decorator Registry
A catalog of available decorators that can be looked up by name.

### Dynamic Decorator
A decorator that is defined and loaded at runtime rather than being generated as code.

### Dynamic Implementation
The approach used in Prompt Decorators v0.3.0+ where decorators are loaded directly from definitions at runtime, without code generation.

## I

### Inline Syntax
The syntax for including decorators directly in prompt text using the `+++` prefix.

Example:
```
+++StepByStep(numbered=true)
Explain quantum computing.
```

### Integration
A connection between the Prompt Decorators framework and another system, such as an LLM provider or client application.

## J

### JavaScript
The language used for writing transform functions in decorator definitions.

## L

### Large Language Model (LLM)
An AI model trained on vast amounts of text data that can generate human-like text based on prompts.

## M

### MCP (Model Context Protocol)
A protocol for integrating tools with LLM clients, allowing them to extend the capabilities of the LLM.

### MCP Integration
The component of Prompt Decorators that implements the Model Context Protocol, enabling integration with MCP-compatible clients like Claude Desktop.

### MCP Server
A server that implements the Model Context Protocol and exposes Prompt Decorators functionality as MCP tools.

## P

### Parameter
A configurable option for a decorator that affects its behavior.

Example: In `StepByStep(numbered=true)`, `numbered` is a parameter with the value `true`.

### Parameter Type
The data type of a parameter, which can be `string`, `number`, `boolean`, or `enum`.

### Precedence
The rule determining which decorator takes effect when multiple decorators conflict. In Prompt Decorators, later decorators take precedence over earlier ones.

### Prompt
The input text sent to an LLM to generate a response.

### Prompt Engineering
The practice of crafting prompts to effectively communicate with and get desired outputs from LLMs.

## R

### Registry
See Decorator Registry.

## S

### Sandboxed Environment
A restricted execution environment where JavaScript transform functions run, preventing access to external resources for security.

### Stacking
The practice of applying multiple decorators to a single prompt, either inline or programmatically.

## T

### Token
The basic unit of text that LLMs process. Tokens are typically word fragments, with a word consisting of one or more tokens.

### Token Limit
The maximum number of tokens that an LLM can process in a single request, including both the prompt and the response.

### Transform Function
A JavaScript function that defines how a decorator modifies a prompt. It takes the input text and parameter values and returns the transformed text.

### Transformation
The process of modifying a prompt by applying one or more decorators.

## V

### Validator
A tool for checking decorator definitions against the framework's specifications and identifying potential issues.

## Common Decorator Categories

### Audience Decorators
Decorators that adapt content for specific audience expertise levels.

Examples: `Audience`, `ELI5`, `Technical`

### Domain Decorators
Decorators that focus on specific knowledge domains or fields.

Examples: `Scientific`, `Legal`, `Medical`

### Format Decorators
Decorators that control the structure and format of the output.

Examples: `OutputFormat`, `Bullet`, `TableFormat`

### Length Decorators
Decorators that control the verbosity or conciseness of responses.

Examples: `Concise`, `Detailed`, `Summary`

### Persona Decorators
Decorators that adopt specific roles, personalities, or expertise.

Examples: `Persona`, `AsExpert`, `Professional`

### Reasoning Decorators
Decorators that enhance logical thinking and problem-solving.

Examples: `Reasoning`, `StepByStep`, `TreeOfThought`

### Style Decorators
Decorators that modify tone, voice, and writing style.

Examples: `Tone`, `Academic`, `Creative`

## Common Decorator Parameters

### depth
Controls the level of detail or thoroughness in a response.

Possible values: `basic`, `moderate`, `comprehensive`

### format
Specifies the output format for structured responses.

Possible values: `markdown`, `json`, `html`, `csv`, etc.

### level
Indicates the expertise level for audience adaptation.

Possible values: `beginner`, `intermediate`, `expert`

### numbered
Determines whether steps or items should be numbered.

Possible values: `true`, `false`

### role
Specifies the role or persona to adopt.

Possible values: Various roles like `teacher`, `scientist`, `lawyer`, etc.

### style
Defines the writing or communication style.

Possible values: `formal`, `casual`, `technical`, `creative`, etc.

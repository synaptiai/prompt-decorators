# Prompt Decorators Specification
## Abstract

This document proposes a standardized framework for "Prompt Decorators" – a system of annotated instructions that modify the behavior and output formatting of Large Language Models (LLMs). Building on concepts from software design patterns, particularly the Decorator pattern in object-oriented programming, this standard creates a structured, extensible approach to prompt engineering. The proposed system enables consistent, reusable interaction paradigms across different AI implementations, reducing cognitive load on users while increasing the utility, reliability, and standardization of AI interactions.

## Executive Summary

Prompt Decorators address the growing complexity of AI interactions by providing a standardized syntax for modifying AI behavior. By prefixing prompts with `+++` followed by descriptive directives like `Reasoning`, `StepByStep`, or `CiteSources`, users can consistently control how AI models process and respond to requests across different platforms and implementations. This standard defines a comprehensive set of decorators, implementation patterns, compatibility considerations, and evolution mechanisms to create a robust ecosystem for structured AI interactions.

Key benefits include:
- **Reduced Cognitive Load**: Users can employ shorter, standardized instructions
- **Consistency**: More standardized behavior across compatible AI systems
- **Composability**: Decorators can be combined for complex behavior
- **Extensibility**: The framework allows for domain-specific extensions
- **Efficiency**: More structured prompts can lead to more efficient interactions

Implementations have demonstrated improvements in content quality, user satisfaction, and workflow efficiency across various domains. This standard aims to provide a foundation for more reliable, effective human-AI collaboration that can evolve with advances in AI capabilities.

## 1. Introduction and Scope

### 1.1 Purpose

This standard defines a framework for "Prompt Decorators" that:

1. MUST provide a consistent syntax for modifying AI behavior
2. SHOULD work across different LLM implementations when supported
3. SHOULD reduce prompt engineering complexity
4. SHOULD enable composition of multiple behavioral modifications
5. MAY be extended for domain-specific applications

### 1.2 Scope

This standard covers:

- Core decorator syntax and grammar
- Standard decorator definitions and behavior
- Implementation guidelines for LLM providers, application developers, and end users
- Extension mechanisms for specialized decorators
- Versioning and evolution processes

This standard does not cover:

- Internal implementation of LLM reasoning or processing
- Model-specific optimizations or capabilities
- User interface design for decorator application
- Dataset creation or model training techniques

### 1.3 Conformance

Implementations claiming conformance to this standard:

1. MUST support the core syntax defined in Section 3
2. MUST implement at least the minimal set of decorators defined in Section 4.1
3. SHOULD implement the full set of decorators defined in Section 4
4. MUST handle unsupported decorators gracefully according to Section 5.4
5. SHOULD provide documentation on supported and unsupported decorators

### 1.4 Background and Motivation

As Large Language Models become increasingly integrated into workflows across industries, the need for standardized, consistent ways to interact with these systems has become apparent. Current prompt engineering approaches are largely ad-hoc, requiring extensive documentation, reinvention, and significant cognitive overhead when switching between systems or use cases.

Prompt Decorators address this challenge by providing a systematic approach to modifying AI behavior through simple, composable annotations. Inspired by the Decorator pattern in programming and Python's function decorators, they serve as a layer of abstraction that decouples the core prompt from instructions about how to process and present the response.

### 1.5 Current Challenges in Prompt Engineering

Current prompt engineering suffers from several limitations:

- **Inconsistency**: Instructions vary widely between users, platforms, and models
- **Verbosity**: Detailed instructions consume token context that could be used for content
- **Cognitive Overhead**: Users must remember or document specific prompting techniques
- **Lack of Composability**: Combining different instruction paradigms is cumbersome
- **Undocumented Behavior**: Expected model behavior is often implicit rather than explicit

### 1.6 Benefits of Prompt Decorators

The proposed standard addresses these challenges through:

- **Standardization**: Common vocabulary and syntax across platforms and models
- **Efficiency**: Concise annotations that reduce token consumption
- **Reusability**: Consistent behaviors that can be reused across different contexts
- **Composability**: Ability to combine decorators for complex interaction patterns
- **Explicit Behavior**: Clear documentation of expected model responses
- **Reduced Cognitive Load**: Simple annotations instead of lengthy instructions

## 2. Core Principles and Design Philosophy

### 2.1 Guiding Principles

The Prompt Decorator standard is designed around these core principles:

1. **Simplicity**: Decorators should be easy to learn, remember, and apply
2. **Consistency**: Behavior should be predictable across different models and contexts
3. **Composability**: Decorators should work together without conflicts
4. **Extensibility**: The framework should allow for new decorators as needs evolve
5. **Minimalism**: Decorators should use minimal syntax and tokens
6. **Model Agnosticism**: Standards should apply across different LLM implementations
7. **Human Readability**: Syntax should be comprehensible to humans, not just machines
8. **Graceful Degradation**: Unrecognized decorators should be handled sensibly
9. **Versioning Support**: The standard should accommodate evolution over time

### 2.2 Design Choices

The standard employs the following design patterns:

- **Triple Plus Prefix** (`+++`) to clearly demarcate decorators from regular text
- **Parameter Encapsulation** using parentheses with explicit parameter names
- **Categorization** to organize decorators by function and purpose
- **Hierarchical Structure** allowing for general and specific decorator types

## 3. Syntax Specification

### 3.1 Basic Syntax

The canonical syntax for a Prompt Decorator MUST follow this pattern:

```
+++<DecoratorName>[(parameter1=value1[, parameter2=value2, ...])]
```

Where:
- `+++` is the decorator prefix that MUST be used to identify a decorator
- `<DecoratorName>` is the case-sensitive name of the decorator
- Parameters are OPTIONAL and enclosed in parentheses
- Multiple parameters MUST be separated by commas
- Parameter names and values MUST be separated by equals signs
- String values MAY be enclosed in quotes for clarity, especially when containing spaces

### 3.2 Parameter Types

Parameters MUST use one of the following types:

1. **String values**: `parameter="value"` or `parameter=value`
2. **Numeric values**: `parameter=42` or `parameter=3.14`
3. **Boolean values**: `parameter=true` or `parameter=false`
4. **Enumerated values**: `parameter=option1` (from a predefined set)
5. **Arrays**: `parameter=[item1,item2,item3]`

### 3.3 Decorator Placement and Composition

1. Decorators MUST appear at the beginning of a prompt or on a new line
2. Multiple decorators MAY be stacked, with each decorator on a new line
3. When multiple decorators are used, they MUST be applied in the order they appear
4. The `+++Version` decorator, if present, MUST be the first decorator

Example of proper composition:

```
+++Version(standard=1.0.0)
+++Reasoning(depth=comprehensive)
+++CiteSources(style=APA)
What are the environmental impacts of electric vehicles?
```

### 3.4 Versioning Syntax

To specify versions of individual decorators:

```
+++<DecoratorName>:v<VersionNumber>(parameters)
```

Example:
```
+++Reasoning:v2(depth=comprehensive)
```

### 3.5 Error Handling

1. Implementations MUST ignore syntax errors in decorators rather than failing
2. Implementations SHOULD provide warnings for malformed decorators
3. Implementations MUST proceed with processing the rest of the prompt when encountering errors
4. Implementations SHOULD document their error handling behavior

### 3.6 JSON Schema Definitions

The standard provides formal JSON Schema definitions for validating decorator implementations. These schemas are available in the `/schemas` directory:

1. **Base Decorator Schema** (`decorator.schema.json`):
   - Defines the structure of individual decorators
   - Validates decorator names, versions, and parameters
   - Includes metadata for documentation and deprecation
   - Required for all decorator implementations

2. **API Request Schema** (`api-request.schema.json`):
   - Defines the structure of API requests using decorators
   - Includes prompt text, decorator list, and metadata
   - References the base decorator schema for validation
   - Used by LLM providers implementing the standard

3. **Registry Entry Schema** (`registry-entry.schema.json`):
   - Defines how decorators are registered in the central registry
   - Includes detailed metadata, documentation, and compatibility info
   - Used for publishing decorators to the registry
   - Ensures consistent documentation and versioning

4. **Extension Package Schema** (`extension-package.schema.json`):
   - Defines how decorator extensions are packaged
   - Includes dependency management and configuration
   - References the registry entry schema for decorator definitions
   - Used for distributing collections of related decorators

#### 3.6.1 Schema Usage

Implementations MUST validate their decorator implementations against these schemas:

```bash
# Using ajv-cli
npx ajv-cli validate -s decorator.schema.json -d your-decorator.json

# Using python-jsonschema
jsonschema -i your-decorator.json decorator.schema.json
```

#### 3.6.2 Schema Versioning

The JSON schemas follow semantic versioning:
- Major version changes indicate breaking changes
- Minor version changes add features in a backward-compatible manner
- Patch version changes fix issues in a backward-compatible manner

#### 3.6.3 Schema References

JSON files can reference these schemas using the `$schema` property:

```json
{
  "$schema": "https://raw.githubusercontent.com/prompt-decorators/spec/main/schemas/decorator.schema.json",
  "name": "YourDecorator",
  "version": "1.0.0",
  ...
}
```

## 4. Categories of Prompt Decorators

Based on an analysis of common interaction patterns and effective prompt techniques, the following comprehensive set of decorators has been organized into functional categories.

### 4.1 Core Decorators

These decorators form the minimal conforming implementation and MUST be supported by any implementation claiming compliance with this standard:

| Decorator | Description | Parameters |
|-----------|-------------|------------|
| `+++Reasoning` | Explicit reasoning path before conclusion | `depth=[basic\|moderate\|comprehensive]` |
| `+++StepByStep` | Sequential problem-solving with labeled steps | `numbered=[true\|false]` |
| `+++OutputFormat` | Specify output format | `format=[json\|markdown\|yaml\|xml\|plaintext]` |
| `+++Tone` | Overall tone adjustment | `style=[formal\|casual\|friendly\|technical\|humorous]` |
| `+++Version` | Specify standard version compatibility | `standard=[semver]` |

### 4.2 Reasoning Process Decorators

These decorators modify how the AI approaches reasoning about a problem.

| Decorator | Description | Parameters |
|-----------|-------------|------------|
| `+++Reasoning` | Explicit reasoning path before conclusion | `depth=[basic\|moderate\|comprehensive]` |
| `+++StepByStep` | Sequential problem-solving with labeled steps | `numbered=[true\|false]` |
| `+++Socratic` | Question-based exploration of the topic | `iterations=[1-5]` |
| `+++Debate` | Multiple viewpoint analysis | `perspectives=[2-5]` |
| `+++FirstPrinciples` | Break down to fundamental truths | `depth=[1-5]` |
| `+++RootCause` | Systematic analysis to identify underlying causes | `method=[fivewhys\|fishbone\|pareto]` |
| `+++TreeOfThought` | Explore multiple reasoning branches | `branches=[2-5]`, `depth=[1-5]` |
| `+++Analogical` | Use analogies for reasoning and explanation | `domain=[general\|specified]` |
| `+++ForcedAnalogy` | Compare concepts through specific analogical domains | `source=[sports\|nature\|cooking\|etc]` |
| `+++Inductive` | Pattern-based reasoning from specific to general | - |
| `+++Deductive` | Logical reasoning from general to specific | - |
| `+++Abductive` | Generate best explanations from limited information | `hypotheses=[2-5]` |
| `+++RedTeam` | Challenge assumptions with adversarial analysis | `strength=[moderate\|aggressive\|steelman]` |
| `+++BlindSpots` | Identify hidden assumptions and risks | `focus=[assumptions\|risks\|biases\|all]` |
| `+++Contrarian` | Generate counterarguments to test perspectives | `approach=[outsider\|skeptic\|devil's-advocate]` |
| `+++NegativeSpace` | Uncover what isn't explicitly stated | `focus=[implications\|missing\|unstated]` |
| `+++DeepDive` | Multi-layered, progressively deeper analysis | `layers=[3-5]`, `focus=[nuance\|examples\|implications]` |

### 4.3 Output Structure Decorators

These decorators specify the structure and format of the AI's response.

| Decorator | Description | Parameters |
|-----------|-------------|------------|
| `+++OutputFormat` | Specify output format | `format=[json\|markdown\|yaml\|xml\|csv\|plaintext]` |
| `+++Schema` | Define custom structure | `schema=[schemaDefinition]` |
| `+++TableFormat` | Present data in tables | `columns=[col1,col2,...]`, `format=[markdown\|ascii\|csv]` |
| `+++Summary` | Provide condensed summary | `length=[short\|medium\|long]`, `wordCount=[number]` |
| `+++Outline` | Structured outline format | `depth=[1-5]`, `style=[numeric\|bullet\|roman]` |
| `+++Nested` | Hierarchical organization | `depth=[1-5]`, `style=[bullet\|numbered\|mixed]` |
| `+++Bullet` | Bullet point format | `style=[dash\|dot\|arrow\|star]` |
| `+++Timeline` | Chronological structure | `granularity=[day\|month\|year\|era]` |
| `+++Comparison` | Direct comparison structure | `aspects=[aspect1,aspect2,...]`, `format=[table\|prose\|bullets]` |
| `+++MECE` | Mutually exclusive, collectively exhaustive framework | `dimensions=[2-5]` |
| `+++DecisionMatrix` | Structured decision-making format | `options=[option1,option2,...]`, `criteria=[criterion1,criterion2,...]` |
| `+++Alternatives` | Generate multiple distinct alternatives | `count=[2-10]`, `diversity=[low\|medium\|high]` |
| `+++Layered` | Present at multiple explanation depths | `levels=[sentence\|paragraph\|page]`, `count=[2-5]` |
| `+++Constraints` | Apply specific limitations to the output | `wordCount=[number]`, `budget=[number]`, `timeframe=[spec]` |
| `+++Prioritize` | Rank items based on specified criteria | `criteria=[impact\|feasibility\|cost\|etc]`, `count=[number]` |

### 4.4 Decorator Conflicts and Compatibility

Some decorators may have incompatible behaviors. Implementations MUST resolve conflicts according to these rules:

1. When decorators have fundamentally incompatible requirements (e.g., `+++ELI5` and `+++Technical`), the later decorator in the sequence takes precedence
2. When facing a parameter conflict between decorators, the parameter in the later decorator takes precedence
3. Implementations SHOULD provide documentation on known decorator conflicts
4. Implementations MAY provide warnings when detecting incompatible decorator combinations

#### 4.4.1 Known Incompatibilities

| Decorator | Incompatible With | Reason |
|-----------|-------------------|--------|
| `+++ELI5` | `+++Technical`, `+++Academic` | Contradictory audience adaptation |
| `+++Concise` | `+++Detailed` | Contradictory verbosity goals |
| `+++Inductive` | `+++Deductive` | Contradictory reasoning methods |
| `+++Bullet` | `+++OutputFormat(format=json)` | Structural conflict |

### 4.5 Tone and Style Decorators

These decorators modify the linguistic style and tone of the AI's response.

| Decorator | Description | Parameters |
|-----------|-------------|------------|
| `+++Tone` | Overall tone adjustment | `style=[formal\|casual\|friendly\|technical\|humorous]` |
| `+++Audience` | Adjust for audience expertise | `level=[beginner\|intermediate\|expert\|technical]` |
| `+++ELI5` | Explain like I'm 5 years old | `strictness=[true\|false]` |
| `+++Academic` | Scholarly style | `style=[humanities\|scientific\|legal]`, `format=[APA\|MLA\|Chicago]` |
| `+++Professional` | Business-oriented language | `industry=[general\|industry]` |
| `+++Creative` | Creative writing style | `genre=[narrative\|poetry\|dialogic]` |
| `+++Concise` | Brief and to-the-point | `maxWords=[number]` |
| `+++Detailed` | Comprehensive and thorough | `depth=[moderate\|comprehensive\|exhaustive]` |
| `+++Narrative` | Story-based delivery | `structure=[classic\|nonlinear\|case-study]` |
| `+++Motivational` | Encouraging, inspiring tone | `intensity=[mild\|moderate\|high]` |
| `+++AsExpert` | Respond from specific expert role | `role=[title]`, `experience=[junior\|senior\|leading]` |
| `+++Persona` | Adopt specific stakeholder viewpoint | `role=[customer\|executive\|skeptic\|etc]` |
| `+++StyleShift` | Modify persuasion tactics or urgency | `aspect=[urgency\|persuasion\|formality]`, `level=[1-5]` |
| `+++Remix` | Reframe content for different contexts | `target=[audience]`, `context=[setting]` |
| `+++Extremes` | Present radical and minimal versions | `versions=[radical\|minimal\|both]` |

### 4.6 Verification and Quality Decorators

These decorators focus on ensuring the accuracy, balance, and quality of the AI's response.

| Decorator | Description | Parameters |
|-----------|-------------|------------|
| `+++CiteSources` | Reference backing for claims | `style=[inline\|footnote\|endnote]`, `format=[APA\|MLA\|Chicago]` |
| `+++FactCheck` | Verification of claims | `confidence=[true\|false]`, `uncertain=[mark\|exclude]` |
| `+++Limitations` | Explicit statement of limitations | `detail=[brief\|comprehensive]`, `position=[beginning\|end]` |
| `+++Confidence` | Indicate confidence in answers | `scale=[percent\|qualitative\|stars]` |
| `+++Balanced` | Ensure equal coverage of viewpoints | `perspectives=[2-5]` |
| `+++Steelman` | Present strongest version of arguments | `sides=[1-5]` |
| `+++PeerReview` | Self-critique as in academic review | `criteria=[accuracy\|methodology\|limitations\|all]` |
| `+++Precision` | Focus on exactness and accuracy | `level=[moderate\|high\|maximum]` |
| `+++Uncertainty` | Highlight areas of uncertainty | `format=[inline\|section\|confidence]` |
| `+++QualityMetrics` | Apply specific quality metrics | `metrics=[metric1,metric2,...]` |
| `+++StressTest` | Identify potential failure points | `scenarios=[3-5]`, `severity=[mild\|moderate\|extreme]` |
| `+++BreakAndBuild` | Criticize then reconstruct an idea | `breakdown=[weaknesses\|assumptions\|risks]` |
| `+++FindGaps` | Identify missing elements in an idea | `aspects=[questions\|resources\|stakeholders\|etc]` |

### 4.7 Meta-Decorators

These decorators modify the behavior of other decorators or provide higher-level control.

| Decorator | Description | Parameters |
|-----------|-------------|------------|
| `+++Refine` | Multiple improvement iterations | `iterations=[2-5]`, `focus=[clarity\|accuracy\|conciseness]` |
| `+++Combine` | Use multiple decorators | `decorators=[D1,D2,...]` |
| `+++Conditional` | Conditional application | `if=[condition]`, `then=[decorator]`, `else=[decorator]` |
| `+++Priority` | Prioritized application | `decorators=[D1,D2,...]` |
| `+++Custom` | User-defined decorator behavior | `rules=[ruleDefinition]` |
| `+++Override` | Override default behaviors | `default=[decorator]` |
| `+++Context` | Domain-specific adaptation | `domain=[domain]` |
| `+++Extension` | Extensibility mechanism | `source=[URI]` |
| `+++Version` | Version specification | `v=[semver]` |
| `+++Compatibility` | Model compatibility | `models=[M1,M2,...]` |
| `+++Chain` | Define multi-step response process | `steps=[step1,step2,...]`, `showAll=[true\|false]` |
| `+++BuildOn` | Reference previous context | `reference=[last\|specific]`, `approach=[extend\|refine\|contrast]` |

## 5. Implementation Considerations

### 5.1 For LLM Providers

LLM providers can implement this standard by:

1. **Pre-processing**: Detecting decorators and modifying the prompt programmatically
2. **Fine-tuning**: Training models to recognize and respond to decorators
3. **Documentation**: Providing clear guidance on supported decorators
4. **Fallback Mechanisms**: Handling unrecognized decorators gracefully
5. **Efficiency**: Optimizing implementation to minimize token usage

#### 5.1.1 Reference Implementation

A reference implementation for processing decorators in a provider API might look like:

```python
def process_decorators(user_prompt):
    decorators = []
    cleaned_prompt = user_prompt

    # Extract decorator patterns
    decorator_pattern = r'\+\+\+([A-Za-z]+)(?:\(([^)]+)\))?'
    matches = re.findall(decorator_pattern, user_prompt)

    for match in matches:
        decorator_name = match[0]
        params_str = match[1] if len(match) > 1 else ""

        # Parse parameters
        params = {}
        if params_str:
            param_pairs = params_str.split(',')
            for pair in param_pairs:
                if '=' in pair:
                    key, value = pair.split('=', 1)
                    params[key.strip()] = value.strip()

        decorators.append({
            "name": decorator_name,
            "parameters": params
        })

        # Remove decorator from prompt
        pattern_to_remove = f"+++{decorator_name}" + (f"({params_str})" if params_str else "")
        cleaned_prompt = cleaned_prompt.replace(pattern_to_remove, "", 1)

    return {
        "decorators": decorators,
        "cleaned_prompt": cleaned_prompt.strip()
    }

def generate_system_prompt(decorators):
    """Generate model instructions based on recognized decorators"""
    system_prompt = "You are a helpful assistant. "

    for decorator in decorators:
        if decorator["name"] == "Reasoning":
            system_prompt += "Provide detailed reasoning before giving your final answer. "
        elif decorator["name"] == "StepByStep":
            system_prompt += "Break down your response into clearly labeled steps. "
        # Add more decorator handling...

    return system_prompt
```

### 5.2 For Application Developers

Application developers integrating LLMs should consider:

1. **UI Integration**: Providing interfaces for applying decorators
2. **Template Libraries**: Creating reusable templates with decorators
3. **Validation**: Ensuring decorators are used correctly
4. **Conflict Resolution**: Handling potential conflicts between decorators
5. **Analytics**: Tracking decorator effectiveness

#### 5.2.1 Implementation Pattern for Applications

For client applications, decorator implementation could follow this pattern:

```javascript
// Example decorator implementation in a UI application
class PromptDecoratorManager {
  constructor() {
    this.availableDecorators = {
      "Reasoning": {
        description: "Provides detailed reasoning process",
        parameters: ["depth"],
        defaults: { depth: "moderate" }
      },
      "StepByStep": {
        description: "Breaks response into sequential steps",
        parameters: ["numbered"],
        defaults: { numbered: "true" }
      },
      // More decorators...
    };

    this.activeDecorators = [];
  }

  addDecorator(name, parameters = {}) {
    if (!this.availableDecorators[name]) {
      throw new Error(`Unknown decorator: ${name}`);
    }

    // Apply default parameters where not specified
    const decorator = {
      name,
      parameters: { ...this.availableDecorators[name].defaults, ...parameters }
    };

    this.activeDecorators.push(decorator);
    return this;
  }

  applyToPrompt(userPrompt) {
    let decoratedPrompt = userPrompt;

    // Prepend decorators to prompt
    for (const decorator of this.activeDecorators) {
      const paramString = Object.entries(decorator.parameters)
        .map(([key, value]) => `${key}=${value}`)
        .join(',');

      const decoratorString = paramString
        ? `+++${decorator.name}(${paramString})\n`
        : `+++${decorator.name}\n`;

      decoratedPrompt = decoratorString + decoratedPrompt;
    }

    return decoratedPrompt;
  }
}
```

### 5.3 For End Users

End users can benefit from decorators through:

1. **Personal Libraries**: Building collections of effective decorators
2. **Workflow Integration**: Incorporating decorators into standard workflows
3. **Experimentation**: Testing different decorators for specific tasks
4. **Sharing**: Exchanging effective decorator configurations
5. **Feedback**: Providing input on decorator effectiveness

#### 5.3.1 Model Instructions for Decorator Recognition

When working with models that don't natively support decorators, users can include the following in their system prompt or initial conversation:

```
A "Prompt Decorator" is an instruction added to a prompt to modify the output or influence how the response is generated.

When you see text starting with +++ followed by a decorator name (like +++Reasoning), apply the following modifications to your response:

- +++Reasoning: Begin your response with detailed explanation of your reasoning process before providing conclusions.
- +++StepByStep: Structure your response as a sequence of clearly labeled steps.
- +++Debate: Present multiple perspectives on the topic before reaching a conclusion.
- +++CiteSources: Include references or citations to support your claims.
- +++FactCheck: Verify factual accuracy and indicate uncertainty when appropriate.
- +++OutputFormat(format=X): Structure your response in the specified format (JSON, markdown, etc.).
- +++Tone(style=X): Adjust your response tone to match the specified style.

Some decorators may include parameters in parentheses, like +++Refine(iterations=3), which modify how the decorator is applied.

These definitions must always be followed when the corresponding decorator is present in a prompt. Please retain them in memory, as I will use them in future interactions.
```

### 5.4 Cross-Model Compatibility and Fallbacks

Different language models will have varying capabilities for implementing decorator behaviors. Implementation should include fallback mechanisms:

#### 5.4.1 Capability Detection

Before applying decorators, applications should detect model capabilities:

```python
def detect_model_capabilities(model_id):
    # Model capability database (would be more extensive in practice)
    model_capabilities = {
        "gpt-4": {
            "reasoning": True,
            "step_by_step": True,
            "fact_check": True,
            "debate": True,
            "output_formats": ["json", "markdown", "yaml", "xml"]
        },
        "gpt-3.5-turbo": {
            "reasoning": True,
            "step_by_step": True,
            "fact_check": False,
            "debate": True,
            "output_formats": ["json", "markdown"]
        },
        "text-bison": {
            "reasoning": False,
            "step_by_step": True,
            "fact_check": False,
            "debate": False,
            "output_formats": ["json"]
        }
    }

    return model_capabilities.get(model_id, {
        "reasoning": False,
        "step_by_step": False,
        "fact_check": False,
        "debate": False,
        "output_formats": []
    })
```

#### 5.4.2 Fallback Strategies

When a model doesn't support a decorator behavior:

1. **Notification**: Inform users when a decorator can't be applied
2. **Approximate Implementation**: Use available capabilities to approximate the desired behavior
3. **Model Switching**: Switch to a more capable model when critical decorators are requested
4. **Hybrid Approach**: Process part of the decorator functionality in middleware

### 5.5 Alternative Syntax Options

While the `+++Decorator` syntax is recommended for its visibility and compatibility, implementations MUST support the JSON format and MAY support additional formats:

#### 5.5.1 JSON Format (Required)

For API-centric applications or when working with structured data, implementations MUST support the JSON format as defined in `api-request.schema.json`:

```json
{
  "$schema": "https://raw.githubusercontent.com/prompt-decorators/spec/main/schemas/api-request.schema.json",
  "prompt": "Explain how nuclear fusion works",
  "decorators": [
    {
      "name": "Reasoning",
      "version": "1.0.0",
      "parameters": {
        "depth": "comprehensive"
      },
      "metadata": {
        "description": "Provides detailed reasoning before conclusions",
        "category": "reasoning"
      }
    },
    {
      "name": "StepByStep",
      "version": "1.0.0",
      "parameters": {
        "numbered": true
      }
    }
  ],
  "metadata": {
    "model": "gpt-4",
    "version": "1.0.0",
    "temperature": 0.7
  }
}
```

The JSON format MUST be validated against the provided schemas to ensure compatibility.

#### 5.5.2 Markdown-Style Format (Optional)

For documentation or text-heavy environments, implementations MAY support a Markdown-style format:

```markdown
<!-- @Reasoning depth=comprehensive -->
<!-- @StepByStep numbered=true -->

Explain how nuclear fusion works
```

When using the Markdown format, implementations MUST convert it to the canonical JSON format internally for processing.

#### 5.5.3 YAML Configuration (Optional)

For configuration-based systems, implementations MAY support YAML format:

```yaml
prompt: Explain how nuclear fusion works
decorators:
  - name: Reasoning
    version: 1.0.0
    parameters:
      depth: comprehensive
    metadata:
      description: Provides detailed reasoning before conclusions
      category: reasoning
  - name: StepByStep
    version: 1.0.0
    parameters:
      numbered: true
metadata:
  model: gpt-4
  version: 1.0.0
  temperature: 0.7
```

When using YAML format, implementations MUST convert it to the canonical JSON format and validate against the provided schemas.

#### 5.5.4 Format Conversion

Implementations that support multiple formats MUST:

1. Convert all formats to the canonical JSON format internally
2. Validate the converted format against the appropriate JSON schema
3. Handle conversion errors gracefully with appropriate error messages
4. Preserve all metadata and parameters during conversion

## 6. Use Cases and Examples

### 6.1 Research and Analysis

```
+++FirstPrinciples
+++CiteSources(style=inline, format=APA)
+++Limitations(position=end)
Analyze the potential impact of quantum computing on cryptography over the next decade.
```

### 6.2 Education and Learning

```
+++ELI5(strictness=true)
+++StepByStep(numbered=true)
+++Analogical(domain=everyday)
Explain how nuclear fusion works.
```

### 6.3 Decision Support

```
+++DecisionMatrix(options=on-prem,hybrid,cloud-native, criteria=cost,security,scalability,complexity)
+++StressTest(scenarios=3)
+++FindGaps(aspects=stakeholders,resources,timeline)
Should our company migrate our infrastructure to a cloud-native architecture?
```

### 6.4 Creative Writing

```
+++Creative(genre=narrative)
+++Tone(style=humorous)
+++Extremes(versions=both)
Write a short story about a robot learning to understand human emotions.
```

### 6.5 Technical Documentation

```
+++Professional(industry=software)
+++Audience(level=intermediate)
+++Layered(levels=overview,detailed,examples)
+++OutputFormat(format=markdown)
Create documentation for a RESTful API that manages user authentication.
```

### 6.6 Strategic Analysis

```
+++RedTeam(strength=steelman)
+++BlindSpots(focus=all)
+++BreakAndBuild
Our company is planning to enter the sustainable energy market with a new battery technology.
```

### 6.7 Multi-step Problem Solving

```
+++Chain(steps=summarize,critique,improve,actionize, showAll=true)
+++DeepDive(layers=3, focus=nuance)
Here's our current marketing strategy for launching in the European market...
```

## 7. Versioning and Evolution

### 7.1 Decorator Evolution Strategy

The standard includes mechanisms for decorator evolution while maintaining backward compatibility:

#### 7.1.1 Decorator Versioning

Individual decorators can specify versions:

```
+++Reasoning:v2(depth=comprehensive)
```

Implementations should interpret versioned decorators according to their specifications, with the following guidelines:

1. **Default Version**: When no version is specified, the latest stable version is assumed
2. **Version Ranges**: Implementations may specify supported version ranges
3. **Deprecation**: Implementations should support deprecated versions with appropriate warnings

#### 7.1.2 Standard Versioning

The overall standard follows semantic versioning:

```
+++Version(standard=1.2.0)
```

This decorator indicates compliance with a specific version of the standard and should be the first decorator in a sequence if used.

#### 7.1.3 Feature Detection

Implementations can use the following pattern to detect supported features:

```
+++FeatureDetect(reasoning, stepByStep, outputFormat)
```

This allows applications to programmatically determine which decorators a particular model or implementation supports.

### 7.2 Community and Ecosystem Development

#### 7.2.1 Registry and Discovery

A central registry for standard and community decorators facilitates discovery and adoption. All registry entries MUST conform to the `registry-entry.schema.json` schema:

```json
{
  "$schema": "https://raw.githubusercontent.com/prompt-decorators/spec/main/schemas/registry-entry.schema.json",
  "decoratorName": "ScientificReasoning",
  "version": "1.0.0",
  "description": "Applies scientific method reasoning process",
  "author": {
    "name": "Scientific AI Consortium",
    "email": "contact@example.org",
    "url": "https://example.org"
  },
  "parameters": [
    {
      "name": "discipline",
      "type": "enum",
      "description": "Scientific discipline context",
      "enum": ["physics", "biology", "chemistry", "general"],
      "default": "general",
      "required": false
    },
    {
      "name": "rigor",
      "type": "enum",
      "description": "Level of scientific rigor",
      "enum": ["academic", "educational", "popular"],
      "default": "educational",
      "required": false
    }
  ],
  "examples": [
    {
      "description": "Basic scientific analysis of a physics problem",
      "usage": "+++ScientificReasoning(discipline=physics, rigor=academic)",
      "result": "Analyzes the problem using formal physics methodology and academic rigor"
    }
  ],
  "compatibility": {
    "requires": ["Reasoning"],
    "conflicts": ["ELI5"],
    "minStandardVersion": "1.0.0",
    "maxStandardVersion": "2.0.0",
    "models": [
      "gpt-4",
      "gpt-3.5-turbo"
    ]
  }
}
```

#### 7.2.2 Extension Mechanism

The `+++Extension` decorator enables loading of community-defined decorators. Extension packages MUST conform to the `extension-package.schema.json` schema:

```json
{
  "$schema": "https://raw.githubusercontent.com/prompt-decorators/spec/main/schemas/extension-package.schema.json",
  "name": "scientific-reasoning-pack",
  "version": "1.0.0",
  "description": "A collection of decorators for scientific reasoning and analysis",
  "author": {
    "name": "Scientific AI Consortium",
    "email": "contact@example.org",
    "url": "https://example.org"
  },
  "license": "Apache 2.0",
  "keywords": ["science", "reasoning", "analysis"],
  "repository": {
    "type": "git",
    "url": "https://github.com/example/scientific-reasoning-pack"
  },
  "decorators": [
    {
      "decoratorName": "ScientificReasoning",
      "version": "1.0.0",
      "description": "Applies scientific method reasoning process",
      "parameters": [
        {
          "name": "discipline",
          "type": "enum",
          "description": "Scientific discipline context",
          "enum": ["physics", "biology", "chemistry", "general"],
          "default": "general"
        }
      ]
    }
  ],
  "dependencies": {
    "standard": {
      "version": "1.0.0"
    },
    "extensions": [
      {
        "name": "core-reasoning",
        "version": "1.0.0"
      }
    ]
  }
}
```

Usage example:
```
+++Extension(source=https://decorator-registry.ai/scientific-pack.json)
+++ScientificReasoning(discipline=physics)
```

#### 7.2.3 Schema Evolution

The JSON schemas for the registry and extensions follow these principles:

1. **Backward Compatibility**: Schema changes MUST maintain backward compatibility within major versions
2. **Version Alignment**: Schema versions MUST align with the standard version
3. **Migration Support**: Major version changes MUST include migration guides
4. **Validation Tools**: The community MUST maintain tools for schema validation

#### 7.2.4 Governance Model

The governance of the Prompt Decorator standard includes:

1. **Technical Committee**: Oversees standard evolution and core decorator definitions
2. **Community Working Groups**: Develop specialized decorator sets for specific domains
3. **Public Review Process**: Ensures new proposals receive adequate review and feedback
4. **Versioning Policy**: Establishes guidelines for backward compatibility and deprecation

### 7.3 Standardization Process

1. **Community Feedback**: Gathering input from AI practitioners and users
2. **Formal Specification**: Developing a comprehensive technical specification
3. **Reference Implementation**: Creating open-source implementation examples
4. **Compatibility Testing**: Ensuring consistent behavior across platforms
5. **Standards Body**: Establishing governance for ongoing development

### 7.4 Extensions and Enhancements

1. **Model-Specific Decorators**: Optimizations for specific LLM architectures
2. **Domain-Specific Decorators**: Specialized decorators for fields like medicine, law, etc.
3. **Interoperability**: Standards for decorator translation between systems
4. **Metadata Integration**: Linking decorators with metadata about responses
5. **Learning Mechanisms**: Systems that learn effective decorator patterns from usage
6. **Automated Decorator Selection**: AI-assisted decorator recommendation based on query intent

## 8. Security and Privacy Considerations

### 8.1 Security Considerations

Implementations of Prompt Decorators should consider these security aspects:

1. **Input Validation**: Implementations MUST validate decorator syntax to prevent injection attacks
2. **Resource Limitations**: Implementations SHOULD enforce limits on decorator complexity to prevent denial-of-service attacks
3. **Authorization Controls**: Implementations MAY restrict access to certain decorators based on user permissions
4. **Sandbox Execution**: When implementing custom decorators, execution SHOULD be sandboxed
5. **Audit Logging**: Implementations SHOULD log decorator usage for security monitoring

### 8.2 Privacy Considerations

Implementations should address these privacy concerns:

1. **Data Minimization**: Decorators SHOULD NOT require unnecessary personal information
2. **Purpose Limitation**: Implementations SHOULD document how decorator information is used
3. **User Control**: Users SHOULD have the ability to disable or limit decorator tracking
4. **Transparency**: Documentation SHOULD disclose how decorator usage data might be collected or analyzed
5. **Persistent Storage**: Implementations SHOULD clarify if and how decorator preferences are stored

### 8.3 Ethical Considerations

Implementers should consider these ethical aspects:

1. **Accessibility**: Decorators SHOULD be designed to work with assistive technologies
2. **Bias Mitigation**: Implementations SHOULD test decorators with diverse inputs to identify potential biases
3. **Transparency**: The effect of decorators SHOULD be made clear to users
4. **User Agency**: Users SHOULD be able to understand and control decorator effects
5. **Documentation**: Implementations SHOULD document limitations and potential issues

## 9. Testing and Validation

### 9.1 Conformance Testing

Implementations claiming conformance with this standard SHOULD implement these test procedures:

1. **Syntax Validation**: Test parsing and recognition of all core decorators
2. **Behavior Validation**: Test that each supported decorator produces the expected behavioral change
3. **Composition Testing**: Test combinations of decorators for expected interaction
4. **Error Handling**: Test handling of malformed decorators
5. **Edge Cases**: Test boundary conditions for parameter values

### 9.2 Test Suite

A reference test suite is available at `https://github.com/prompt-decorators/test-suite` with:

1. Test cases for each core decorator
2. Composition test cases
3. Error handling scenarios
4. Performance benchmarks

### 9.3 Validation Tools

These tools are available to validate decorator implementations:

1. **Decorator Validator**: Command-line tool to validate decorator syntax
2. **Behavior Test Framework**: Framework for testing decorator effects
3. **Compatibility Scanner**: Tool to check for decorator conflicts

## 10. Implementation Timeline

### 10.1 Phased Approach

Implementations are encouraged to follow this phased approach:

1. **Phase 1 (Core Support)**: Implement the five core decorators
2. **Phase 2 (Extended Support)**: Add support for common reasoning and output decorators
3. **Phase 3 (Full Support)**: Implement all standard decorators
4. **Phase 4 (Extensions)**: Support domain-specific extensions

### 10.2 Versioning Timeline

The standard will evolve according to this timeline:

1. **v1.0 (Initial Release)**: Core specification with minimal set of decorators
2. **v1.x (Minor Updates)**: Clarifications and additional decorators
3. **v2.0 (Major Update)**: Enhanced composition, additional parameters, and expanded categories

## 11. References

1. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns).
2. Python Software Foundation. (2021). [PEP 318 – Decorators for Functions and Methods](https://peps.python.org/pep-0318/).
3. Wei, J., Wang, X., Schuurmans, D., Bosma, M., et al. (2022). [Chain of Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903).
4. Yao, S., Yu, D., Zhao, J., Shafran, I., et al. (2023). [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601).
5. White, J., Fu, Q., Hays, S., Sandborn, M., et al. (2023). [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/abs/2304.01373).
6. Kojima, T., Gu, S.S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916).
7. Liu, P., Yuan, W., Fu, J., Jiang, Z., et al. (2023). [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://arxiv.org/abs/2107.13586).
8. Reynolds, L., & McDonell, K. (2021). [Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm](https://arxiv.org/abs/2102.07350).

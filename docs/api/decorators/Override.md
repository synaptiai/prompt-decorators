# Override Decorator

A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.

**Category**: Meta

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `decorator` | string | The specific decorator whose behavior to override | Required |
| `parameters` | string | JSON string specifying the parameters to override (e.g., '{"depth": "comprehensive", "focus": "methodology"}') |  |
| `behavior` | string | Optional custom behavior modification instructions that override the standard decorator interpretation |  |

## Examples

### Basic parameter override for a standard decorator

```
+++Override(decorator=StepByStep, parameters={"numbered": true, "steps": 7})
Explain how to bake bread.
```

Applies the StepByStep decorator to explain bread baking, but overrides its default parameters to ensure exactly 7 numbered steps

### Complex behavior override with custom instructions

```
+++Override(decorator=Debate, parameters={"perspectives": 2}, behavior=instead of presenting neutral perspectives, adopt strongly opposing viewpoints with clear advocacy for each position)
Discuss the ethics of gene editing.
```

Uses the Debate decorator structure for discussing gene editing ethics, but modifies its standard neutral approach to present strongly advocated opposing positions

## Model-Specific Implementations

### gpt-4o

**Instruction:** Apply the {decorator} decorator with these custom settings: {parameters}. {behavior} Follow the standard behavior of the decorator in all other aspects not explicitly modified.

**Notes:** This model handles behavior overrides well but benefits from explicit instructions about which aspects of behavior to preserve


## Implementation Guidance

### Basic parameter override for StepByStep

**Original Prompt:**
```
Explain how to bake bread.
```

**Transformed Prompt:**
```
Please apply a customized version of a standard decorator with specific modifications to its default parameters or behavior. Apply the StepByStep decorator, but with the following modifications to its standard implementation. Override the default parameters of the decorator with these specific values: {"numbered": true, "steps": 7}.

Explain how to bake bread.
```

### Complex behavior override for Debate

**Original Prompt:**
```
Discuss the ethics of gene editing.
```

**Transformed Prompt:**
```
Please apply a customized version of a standard decorator with specific modifications to its default parameters or behavior. Apply the Debate decorator, but with the following modifications to its standard implementation. Override the default parameters of the decorator with these specific values: {"perspectives": 2}. Additionally, modify the standard behavior of the decorator as follows: instead of presenting neutral perspectives, adopt strongly opposing viewpoints with clear advocacy for each position.

Discuss the ethics of gene editing.
```

## Transformation Details

**Base Instruction:** Please apply a customized version of a standard decorator with specific modifications to its default parameters or behavior.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `decorator`:
  - Format: Apply the {value} decorator, but with the following modifications to its standard implementation.

- `parameters`:
  - Format: Override the default parameters of the decorator with these specific values: {value}.

- `behavior`:
  - Format: Additionally, modify the standard behavior of the decorator as follows: {value}.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **All**: Enhances Override Override can work with any decorator, as its purpose is to modify their behavior
- **Priority**: Enhances Override Priority can help determine which Override takes precedence when multiple are applied
- **Custom**: Enhances Override Override and Custom provide complementary approaches to customization - Override modifies existing decorators while Custom creates new behaviors

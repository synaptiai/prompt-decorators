# SystemIntegration Decorator

Provides guidance for integrating with existing systems and services.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `systems` | string | External systems to integrate with | none |
| `approach` | enum | Integration approach | adapter |
| `coupling` | enum | Desired coupling level | loose |

## Approach Options

- `adapter`: Use an adapter pattern to create a compatible interface between systems.
- `direct`: Implement direct integration with minimal abstraction layers.
- `facade`: Create a facade to provide a simplified interface to the complex subsystems.
- `proxy`: Implement a proxy pattern to control access to the external systems.
- `bridge`: Use a bridge pattern to decouple abstraction from implementation.

## Coupling Options

- `loose`: Maintain loose coupling to minimize dependencies between systems.
- `moderate`: Balance coupling with performance considerations.
- `tight`: Implement tight coupling where performance is critical.

## Examples

### Basic integration with payment gateway using facade pattern

```
+++SystemIntegration(systems=payment-gateway,inventory-service, approach=facade, coupling=loose)
```

Provides guidance for implementing a facade-based integration with payment gateway and inventory services while maintaining loose coupling.

### Direct integration with tight coupling for performance

```
+++SystemIntegration(systems=database, approach=direct, coupling=tight)
```

Guides implementation of direct database integration with tight coupling for performance-critical operations.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** When implementing the solution, consider these system integration guidelines:

**Notes:** Simplified instruction for models with less context capacity.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **DesignPatterns**: Enhances SystemIntegration SystemIntegration works well with DesignPatterns to provide comprehensive architectural guidance.
- **CodeQuality**: Enhances SystemIntegration Can be combined with CodeQuality to ensure integration code meets quality standards.

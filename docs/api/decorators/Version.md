# Version Decorator

Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.

**Category**: Minimal

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `standard` | string | The semantic version of the Prompt Decorators standard to use | 1.0.0 |

## Examples

### Specify standard version for compatibility

```
+++Version(standard=1.0.0)
+++Reasoning(depth=comprehensive)
Explain quantum entanglement
```

Ensures decorators are interpreted according to version 1.0.0 of the standard

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Minimum Standard Version**: 1.0.0

## Related Decorators

- **All**: Requires Version The Version decorator should always be the first in any sequence when used

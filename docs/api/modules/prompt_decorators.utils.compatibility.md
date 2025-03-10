# compatibility

Decorator Compatibility Module.

This module provides utilities for checking compatibility between decorators.

## Module Variables

### `compatibility_checker`

Type: `CompatibilityChecker`

Value: `<prompt_decorators.utils.compatibility.CompatibilityChecker object at 0x11ae52a10>`

### `logger`

Type: `Logger`

Value: `<Logger prompt_decorators.utils.compatibility (INFO)>`

## Classes

### `CompatibilityChecker`

Checker for decorator compatibility.

#### Methods

##### `__init__`

Initialize a compatibility checker.

**Signature:** `__init__(self)`

**Parameters:**


##### `add_incompatible_pair`

Add a pair of incompatible decorators.

Args:
    decorator1: Name of the first decorator
    decorator2: Name of the second decorator
    message: Optional message explaining the incompatibility

Returns:
    None

**Signature:** `add_incompatible_pair(self, decorator1: str, decorator2: str, message: Optional[str] = None) -> None`

**Parameters:**

- `decorator1`: `str`
- `decorator2`: `str`
- `message`: `Optional` (default: `None`)

##### `add_rule`

Add a compatibility rule.

Args:
    decorator1: Name of the first decorator
    decorator2: Name of the second decorator
    rule: Dictionary with rule parameters

Returns:
    None

**Signature:** `add_rule(self, decorator1: str, decorator2: str, rule: Dict[str, Any]) -> None`

**Parameters:**

- `decorator1`: `str`
- `decorator2`: `str`
- `rule`: `Dict`

##### `check_compatibility`

Check compatibility between two decorators.

Args:
    decorator1: First decorator
    decorator2: Second decorator

Returns:
    List of compatibility issues (empty if fully compatible)

**Signature:** `check_compatibility(self, decorator1: Union[str, prompt_decorators.core.base.DecoratorBase], decorator2: Union[str, prompt_decorators.core.base.DecoratorBase]) -> List[prompt_decorators.utils.compatibility.CompatibilityIssue]`

**Parameters:**

- `decorator1`: `Union`
- `decorator2`: `Union`

**Returns:** `List`

##### `check_compatibility_group`

Check compatibility among a group of decorators.

Args:
    decorators: List of decorators to check

Returns:
    List of compatibility issues (empty if fully compatible)

**Signature:** `check_compatibility_group(self, decorators: List[Union[str, prompt_decorators.core.base.DecoratorBase]]) -> List[prompt_decorators.utils.compatibility.CompatibilityIssue]`

**Parameters:**

- `decorators`: `List`

**Returns:** `List`

### `CompatibilityIssue`

Class representing a compatibility issue between decorators.

#### Attributes

- `SEVERITY_ERROR`: `str` = `'error'`
- `SEVERITY_INFO`: `str` = `'info'`
- `SEVERITY_WARNING`: `str` = `'warning'`

#### Methods

##### `__init__`

Initialize a compatibility issue.

Args:
    message: Description of the issue
    decorator1: First decorator involved
    decorator2: Second decorator involved
    severity: Issue severity (info, warning, error)

**Signature:** `__init__(self, message: str, decorator1: Union[str, prompt_decorators.core.base.DecoratorBase], decorator2: Union[str, prompt_decorators.core.base.DecoratorBase], severity: str = 'warning')`

**Parameters:**

- `message`: `str`
- `decorator1`: `Union`
- `decorator2`: `Union`
- `severity`: `str` (default: `warning`)

## Functions

### `get_compatibility_checker`

Get the global compatibility checker.

Returns:
    The global compatibility checker instance

**Signature:** `get_compatibility_checker() -> prompt_decorators.utils.compatibility.CompatibilityChecker`

**Returns:** `CompatibilityChecker`

### `setup_core_compatibility_rules`

Set up compatibility rules for core decorators.

**Signature:** `setup_core_compatibility_rules() -> None`

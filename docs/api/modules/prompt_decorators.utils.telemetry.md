# telemetry

Telemetry Module.

This module provides an opt-in telemetry system for tracking decorator usage patterns.

## Module Variables

### `logger`

Type: `Logger`

Value: `<Logger prompt_decorators.utils.telemetry (INFO)>`

### `telemetry_manager`

Type: `TelemetryManager`

Value: `<prompt_decorators.utils.telemetry.TelemetryManager object at 0x1075dec90>`

## Classes

### `TelemetryManager`

Manager for collecting and reporting telemetry data.

This class provides utilities for collecting usage data about decorators
and reporting it for analytics purposes. All telemetry is opt-in.

#### Methods

##### `disable`

Disable telemetry collection.

**Signature:** `disable(self) -> None`

**Parameters:**


##### `enable`

Enable telemetry collection.

**Signature:** `enable(self) -> None`

**Parameters:**


##### `is_enabled`

Check if telemetry is enabled.

Args:
    self: The TelemetryManager instance

Returns:
    True if enabled, False otherwise

**Signature:** `is_enabled(self) -> bool`

**Parameters:**


**Returns:** `bool`

##### `register_callback`

Register a callback for a specific event type.

Args:
    event_type: Type of event to register for
    callback: Function to call when an event of this type occurs

Returns:
    None

**Signature:** `register_callback(self, event_type: str, callback: Callable[[Dict[str, Any]], NoneType]) -> None`

**Parameters:**

- `event_type`: `str`
- `callback`: `Callable`

##### `track_decorator_combination`

Track a combination of decorators used together.

Args:
    decorators: List of decorator information dictionaries
    prompt_length: Length of the prompt in tokens (optional)
    metadata: Additional metadata (optional)

Returns:
    None

**Signature:** `track_decorator_combination(self, decorators: List[Dict[str, Any]], prompt_length: Optional[int] = None, metadata: Optional[Dict[str, Any]] = None) -> None`

**Parameters:**

- `decorators`: `List`
- `prompt_length`: `Optional` (default: `None`)
- `metadata`: `Optional` (default: `None`)

##### `track_decorator_usage`

Track usage of a decorator.

Args:
    decorator_name: Name of the decorator
    version: Version of the decorator
    parameters: Parameters used with the decorator (optional)
    metadata: Additional metadata (optional)

Returns:
    None

**Signature:** `track_decorator_usage(self, decorator_name: str, version: str, parameters: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, Any]] = None) -> None`

**Parameters:**

- `decorator_name`: `str`
- `version`: `str`
- `parameters`: `Optional` (default: `None`)
- `metadata`: `Optional` (default: `None`)

##### `track_performance`

Track performance metrics for a decorator.

Args:
    decorator_name: Name of the decorator
    version: Version of the decorator
    execution_time: Time taken to execute the decorator in seconds
    metadata: Additional metadata (optional)

Returns:
    None

**Signature:** `track_performance(self, decorator_name: str, version: str, execution_time: float, metadata: Optional[Dict[str, Any]] = None) -> None`

**Parameters:**

- `decorator_name`: `str`
- `version`: `str`
- `execution_time`: `float`
- `metadata`: `Optional` (default: `None`)

##### `unregister_callback`

Unregister a callback for telemetry events.

Args:
    event_type: Type of event
    callback: Function to unregister

Returns:
    None

**Signature:** `unregister_callback(self, event_type: str, callback: Callable[[Dict[str, Any]], NoneType]) -> None`

**Parameters:**

- `event_type`: `str`
- `callback`: `Callable`

## Functions

### `get_telemetry_manager`

Get the global telemetry manager.

Returns:
    The global telemetry manager instance

**Signature:** `get_telemetry_manager() -> prompt_decorators.utils.telemetry.TelemetryManager`

**Returns:** `TelemetryManager`

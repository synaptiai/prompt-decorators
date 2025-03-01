# Module `prompt_decorators.utils.telemetry`

Telemetry Module

This module provides an opt-in telemetry system for tracking decorator usage patterns.

## Classes

- [`TelemetryManager`](#class-telemetrymanager): Manager for collecting and reporting telemetry data.

### Class `TelemetryManager`

Manager for collecting and reporting telemetry data.

This class provides utilities for collecting usage data about decorators
and reporting it for analytics purposes. All telemetry is opt-in.

#### Methods

- `disable() -> <class 'NoneType'>`
- `enable() -> <class 'NoneType'>`
- `is_enabled() -> <class 'bool'>`
- `register_callback(event_type, callback) -> <class 'NoneType'>`
- `track_decorator_combination(decorators, prompt_length, metadata) -> <class 'NoneType'>`
- `track_decorator_usage(decorator_name, version, parameters, metadata) -> <class 'NoneType'>`
- `track_performance(decorator_name, version, execution_time, metadata) -> <class 'NoneType'>`
- `unregister_callback(event_type, callback) -> <class 'NoneType'>`

## Functions

- [`get_telemetry_manager`](#function-get_telemetry_manager): Get the global telemetry manager.

### Function `get_telemetry_manager`

**Signature:** `get_telemetry_manager() -> <class 'prompt_decorators.utils.telemetry.TelemetryManager'>`

Get the global telemetry manager.

Returns:
    The global telemetry manager instance


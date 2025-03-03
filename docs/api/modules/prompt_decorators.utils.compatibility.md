# Module `prompt_decorators.utils.compatibility`

Decorator Compatibility Module

This module provides utilities for checking compatibility between decorators.

## Classes

- [`CompatibilityChecker`](#class-compatibilitychecker): Checker for decorator compatibility.
- [`CompatibilityIssue`](#class-compatibilityissue): Class representing a compatibility issue between decorators.

### Class `CompatibilityChecker`

Checker for decorator compatibility.

#### Methods

- `__init__()`
- `add_incompatible_pair(decorator1, decorator2, message) -> <class 'NoneType'>`
- `add_rule(decorator1, decorator2, rule) -> <class 'NoneType'>`
- `check_compatibility(decorator1, decorator2) -> typing.List[prompt_decorators.utils.compatibility.CompatibilityIssue]`
- `check_compatibility_group(decorators) -> typing.List[prompt_decorators.utils.compatibility.CompatibilityIssue]`

### Class `CompatibilityIssue`

Class representing a compatibility issue between decorators.

#### Methods

- `__init__(message, decorator1, decorator2, severity=warning)`

## Functions

- [`get_compatibility_checker`](#function-get_compatibility_checker): Get the global compatibility checker.
- [`setup_core_compatibility_rules`](#function-setup_core_compatibility_rules): Set up compatibility rules for core decorators.

### Function `get_compatibility_checker`

**Signature:** `get_compatibility_checker() -> <class 'prompt_decorators.utils.compatibility.CompatibilityChecker'>`

Get the global compatibility checker.

Returns:
    The global compatibility checker instance

### Function `setup_core_compatibility_rules`

**Signature:** `setup_core_compatibility_rules() -> <class 'NoneType'>`

Set up compatibility rules for core decorators.

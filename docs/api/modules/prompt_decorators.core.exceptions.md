# Module `prompt_decorators.core.exceptions`

Exceptions for the prompt-decorators package.

This module defines custom exceptions used throughout the package.

## Classes

- [`IncompatibleVersionError`](#class-incompatibleversionerror): Raised when a decorator version is incompatible.
- [`RegistryError`](#class-registryerror): Raised when there is an error with the decorator registry.

### Class `IncompatibleVersionError`

Raised when a decorator version is incompatible.

This exception is raised when attempting to use a decorator with a version
that is not compatible with the current version of the package.

**Inherits from:** `Exception`


### Class `RegistryError`

Raised when there is an error with the decorator registry.

This exception is raised when there is an issue with registering or
retrieving decorators from the registry.

**Inherits from:** `Exception`

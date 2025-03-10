# model_detection

Model detection and capability utilities.

This module provides utilities for detecting model capabilities and features.

## Module Variables

### `logger`

Type: `Logger`

Value: `<Logger prompt_decorators.utils.model_detection (INFO)>`

## Classes

### `ModelCapabilities`

Class to represent the capabilities of a model.

This class stores information about what a model can and cannot do,
such as supported decorator features and parameter types.

#### Attributes

- `from_dict`: `classmethod` = `<classmethod(<function ModelCapabilities.from_dict at 0x1059b6480>)>`

#### Methods

##### `__init__`

Initialize a model capabilities object.

Args:
    model_id: Unique identifier for the model
    model_family: Family or provider of the model
    version: Version of the model
    capabilities: Dictionary of capability flags and values

**Signature:** `__init__(self, model_id: str, model_family: str = 'unknown', version: str = 'unknown', capabilities: Optional[Dict[str, Any]] = None)`

**Parameters:**

- `model_id`: `str`
- `model_family`: `str` (default: `unknown`)
- `version`: `str` (default: `unknown`)
- `capabilities`: `Optional` (default: `None`)

##### `get_capability`

Get the value of a capability.

Args:
    capability: The capability to get
    default: Default value if the capability is not defined

Returns:
    The capability value, or the default if not found

**Signature:** `get_capability(self, capability: str, default: Any = None) -> Any`

**Parameters:**

- `capability`: `str`
- `default`: `Any` (default: `None`)

**Returns:** `Any`

##### `set_capability`

Set the value of a capability.

Args:
    capability: The capability to set
    value: The value to set

Returns:
    None

**Signature:** `set_capability(self, capability: str, value: Any) -> None`

**Parameters:**

- `capability`: `str`
- `value`: `Any`

##### `supports_feature`

Check if the model supports a specific feature.

Args:
    feature: The feature to check

Returns:
    True if the feature is supported, False otherwise

**Signature:** `supports_feature(self, feature: str) -> bool`

**Parameters:**

- `feature`: `str`

**Returns:** `bool`

##### `to_dict`

Convert the model capabilities to a dictionary.

Args:
    self: The ModelCapabilities instance

Returns:
    Dictionary representation of the model capabilities

**Signature:** `to_dict(self) -> Dict[str, Any]`

**Parameters:**


**Returns:** `Dict`

### `ModelDetector`

Detector for model capabilities.

This class provides utilities for detecting and querying model capabilities.

#### Attributes

- `DEFAULT_CAPABILITIES_PATH`: `PosixPath` = `PosixPath('/Users/danielbentes/prompt-decorators/config/model_capabilities.json')`

#### Methods

##### `detect_model_from_api`

Detect the model family from an API name.

Args:
    api_name: The API name or URL

Returns:
    The detected model family, or None if not detected

**Signature:** `detect_model_from_api(self, api_name: str) -> Optional[str]`

**Parameters:**

- `api_name`: `str`

**Returns:** `Optional`

##### `get_all_families`

Get all registered model families.

Args:
    self: The ModelDetector instance

Returns:
    List of all registered model families

**Signature:** `get_all_families(self) -> List[str]`

**Parameters:**


**Returns:** `List`

##### `get_all_models`

Get all registered models.

Args:
    self: The ModelDetector instance

Returns:
    List of all registered ModelCapabilities

**Signature:** `get_all_models(self) -> List[prompt_decorators.utils.model_detection.ModelCapabilities]`

**Parameters:**


**Returns:** `List`

##### `get_model_capabilities`

Get capabilities for a specific model.

Args:
    model_id: The model identifier

Returns:
    ModelCapabilities for the model, or None if not found

Note:
    This method attempts to find an exact match first, then falls back
    to a partial match if no exact match is found.

**Signature:** `get_model_capabilities(self, model_id: str) -> Optional[prompt_decorators.utils.model_detection.ModelCapabilities]`

**Parameters:**

- `model_id`: `str`

**Returns:** `Optional`

##### `get_models_by_family`

Get all models in a specific family.

Args:
    family: Model family

Returns:
    List of ModelCapabilities for models in the family

**Signature:** `get_models_by_family(self, family: str) -> List[prompt_decorators.utils.model_detection.ModelCapabilities]`

**Parameters:**

- `family`: `str`

**Returns:** `List`

##### `register_model`

Register a model's capabilities.

Args:
    model: The model capabilities to register

Returns:
    None

**Signature:** `register_model(self, model: prompt_decorators.utils.model_detection.ModelCapabilities) -> None`

**Parameters:**

- `model`: `ModelCapabilities`

## Functions

### `get_model_detector`

Get the global model detector instance.

Returns:
    The global model detector instance

**Signature:** `get_model_detector() -> prompt_decorators.utils.model_detection.ModelDetector`

**Returns:** `ModelDetector`

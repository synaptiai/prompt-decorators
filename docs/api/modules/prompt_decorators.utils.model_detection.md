# Module `prompt_decorators.utils.model_detection`

Model Detection Module

This module provides utilities for detecting and managing model capabilities.

## Classes

- [`ModelCapabilities`](#class-modelcapabilities): Class to represent the capabilities of a model.
- [`ModelDetector`](#class-modeldetector): Detector for model capabilities.

### Class `ModelCapabilities`

Class to represent the capabilities of a model.

This class stores information about what a model can and cannot do,
such as supported decorator features and parameter types.

#### Methods

- `__init__(model_id, model_family=unknown, version=unknown, capabilities)`
- `from_dict(data) -> <class 'prompt_decorators.utils.model_detection.ModelCapabilities'>`
- `get_capability(capability, default) -> typing.Any`
- `set_capability(capability, value) -> <class 'NoneType'>`
- `supports_feature(feature) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`

### Class `ModelDetector`

Detector for model capabilities.

This class provides utilities for detecting and querying model capabilities.

#### Methods

- `detect_model_from_api(api_name) -> typing.Optional[str]`
- `get_all_families() -> typing.List[str]`
- `get_all_models() -> typing.List[prompt_decorators.utils.model_detection.ModelCapabilities]`
- `get_model_capabilities(model_id) -> typing.Optional[prompt_decorators.utils.model_detection.ModelCapabilities]`
- `get_models_by_family(family) -> typing.List[prompt_decorators.utils.model_detection.ModelCapabilities]`
- `register_model(model) -> <class 'NoneType'>`

## Functions

- [`get_model_detector`](#function-get_model_detector): Get the global model detector.

### Function `get_model_detector`

**Signature:** `get_model_detector() -> <class 'prompt_decorators.utils.model_detection.ModelDetector'>`

Get the global model detector.

Returns:
    The global model detector instance

# Module `prompt_decorators.decorators.generated.decorators.quality_metrics`

Implementation of the QualityMetrics decorator.

This module provides the QualityMetrics decorator class for use in prompt engineering.

Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.

## Classes

- [`QualityMetrics`](#class-qualitymetrics): Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.

### Class `QualityMetrics`

Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.

Attributes:
    metrics: Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness). (List[Any])
    scale: Rating scale to use for evaluations. (Literal["1-5", "1-10", "percentage", "qualitative"])
    explanation: Whether to provide detailed explanations for each metric score. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(metrics, scale=1-5, explanation=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `explanation`: Get the explanation parameter value.
- `metrics`: Get the metrics parameter value.
- `name`: Get the name of the decorator.
- `scale`: Get the scale parameter value.

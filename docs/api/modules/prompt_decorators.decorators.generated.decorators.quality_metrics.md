# Module `prompt_decorators.decorators.generated.decorators.quality_metrics`

QualityMetrics Decorator

Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.

## Classes

- [`QualityMetrics`](#class-qualitymetrics): Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.

### Class `QualityMetrics`

Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(metrics, scale=QualityMetricsScaleEnum.VALUE_1_5, explanation=True)`
- `apply(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `get_version() -> <class 'prompt_decorators.core.base.Version'>`
- `is_compatible_with_version(version_str) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_json(indent) -> <class 'str'>`
- `validate() -> <class 'NoneType'>`
#### Properties

- `explanation`: Whether to provide detailed explanations for each metric score
- `metrics`: Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness)
- `scale`: Rating scale to use for evaluations

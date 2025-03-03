# Type Annotation Improvements

This document outlines a plan for improving type annotations in the Prompt Decorators codebase based on the mypy warnings identified during documentation builds.

## Priority Areas

The following files and functions have been identified as needing type annotation improvements:

### Core Module

1. `prompt_decorators/core/base.py:146`: Add type annotation for parameter `**kwargs`
2. `prompt_decorators/core/request.py:42`: Add type annotation for parameter `self`
3. `prompt_decorators/core/request.py:63`: Add type annotation for parameter `self`
4. `prompt_decorators/core/model_specific.py:33`: Add type annotation for parameter `**kwargs`
5. `prompt_decorators/core/model_specific.py:178`: Add type annotation for parameter `**params`

### Decorators Module

Multiple methods in the generated decorators need `self` parameter type annotations:

1. `prompt_decorators/decorators/generated/decorators/reasoning.py:76`
2. `prompt_decorators/decorators/generated/decorators/step_by_step.py:71`
3. `prompt_decorators/decorators/generated/decorators/tree_of_thought.py` (multiple methods)
4. `prompt_decorators/decorators/generated/decorators/output_format.py:78`
5. `prompt_decorators/decorators/generated/decorators/bullet.py` (multiple methods)
6. `prompt_decorators/decorators/generated/decorators/table_format.py` (multiple methods)
7. `prompt_decorators/decorators/generated/decorators/concise.py` (multiple methods)
8. `prompt_decorators/decorators/generated/decorators/detailed.py` (multiple methods)
9. `prompt_decorators/decorators/generated/decorators/tone.py:82`
10. `prompt_decorators/decorators/generated/decorators/fact_check.py` (multiple methods)
11. `prompt_decorators/decorators/generated/decorators/peer_review.py` (multiple methods)
12. `prompt_decorators/decorators/generated/decorators/cite_sources.py` (multiple methods)
13. `prompt_decorators/decorators/generated/decorators/chain.py` (multiple methods)
14. `prompt_decorators/decorators/generated/decorators/conditional.py` (multiple methods)
15. `prompt_decorators/decorators/generated/decorators/override.py` (multiple methods)

### Generator Module

1. `prompt_decorators/generator/registry.py:102`: Add type annotation for parameter `self`
2. `prompt_decorators/generator/registry.py:49`: Add type annotation for parameter `self`
3. `prompt_decorators/generator/code_gen.py:192`: Add type annotation for parameter `self`

### Utils Module

1. `prompt_decorators/utils/discovery.py:30`: Add type annotation for returned value
2. `prompt_decorators/utils/discovery.py:275`: Add type annotation for parameter `**parameters`
3. `prompt_decorators/utils/cache.py:33`: Add type annotation for returned value `DecoratorCache`
4. `prompt_decorators/utils/json_loader.py:43`: Add type annotation for parameter `self`
5. `prompt_decorators/utils/model_detection.py:131`: Add type annotation for returned value
6. `prompt_decorators/utils/plugins.py` (multiple methods)
7. `prompt_decorators/utils/telemetry.py:35`: Add type annotation for returned value

## Implementation Strategy

Since many of the missing type annotations are in generated code, we should focus on:

1. **Updating the code generation templates** to include proper type annotations for all methods, especially for `self` parameters.

2. **Creating a type annotation helper script** that can automatically add missing type annotations to existing files.

3. **Updating the base classes** to include proper type annotations that can be inherited by generated classes.

## Example Fixes

### For `self` parameter annotations:

```python
def some_method(self: "ClassName") -> ReturnType:
    # Method implementation
```

### For `**kwargs` annotations:

```python
def some_method(self, **kwargs: Any) -> ReturnType:
    # Method implementation
```

### For return value annotations:

```python
def some_method() -> List[str]:
    # Method implementation
    return ["result1", "result2"]
```

## Timeline

1. First, update the code generation templates to ensure all newly generated code has proper type annotations.
2. Then, create a script to add missing type annotations to existing files.
3. Finally, manually review and fix any remaining type annotation issues.

## Tracking Progress

Create a GitHub issue to track progress on type annotation improvements, with a checklist for each file that needs to be updated.

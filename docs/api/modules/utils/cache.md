# Cache Module

The `cache` module provides caching mechanisms for improved performance. It allows for caching of decorator application results and other expensive operations.

## DecoratorCache

```python
class DecoratorCache:
    """Cache for decorator application results.

    This class provides a cache for decorator application results,
    allowing for faster repeated applications of the same decorators.
    """
```

The `DecoratorCache` class provides a cache for decorator application results, allowing for faster repeated applications of the same decorators.

### Key Methods

- `get(key: str) -> Optional[str]`: Get a cached result
- `set(key: str, value: str) -> None`: Set a cached result
- `clear() -> None`: Clear the cache
- `get_stats() -> dict`: Get cache statistics

## CacheKey

```python
class CacheKey:
    """Key for the decorator cache.

    This class represents a key for the decorator cache, combining
    the decorator parameters and the prompt.
    """
```

The `CacheKey` class represents a key for the decorator cache, combining the decorator parameters and the prompt.

### Key Methods

- `from_decorator(decorator: BaseDecorator, prompt: str) -> str`: Create a cache key from a decorator and prompt
- `from_request(request: DecoratedRequest) -> str`: Create a cache key from a decorated request

## CacheManager

```python
class CacheManager:
    """Manages multiple caches.

    This class manages multiple caches, providing a unified interface
    for caching different types of objects.
    """
```

The `CacheManager` class manages multiple caches, providing a unified interface for caching different types of objects.

### Key Methods

- `get_cache(cache_name: str) -> Any`: Get a cache by name
- `register_cache(cache_name: str, cache: Any) -> None`: Register a cache
- `clear_all() -> None`: Clear all caches

## Usage Example

```python
from prompt_decorators.utils.cache import DecoratorCache, CacheKey
from prompt_decorators.decorators import Reasoning, StepByStep

# Create cache
cache = DecoratorCache()

# Create decorators
reasoning = Reasoning(depth="comprehensive")
step_by_step = StepByStep(numbered=True)

# Create prompt
prompt = "Explain how nuclear fusion works."

# Create cache keys
reasoning_key = CacheKey.from_decorator(reasoning, prompt)
step_by_step_key = CacheKey.from_decorator(step_by_step, prompt)

# Check cache
reasoning_result = cache.get(reasoning_key)
if reasoning_result is None:
    # Apply decorator
    reasoning_result = reasoning.apply(prompt)
    # Cache result
    cache.set(reasoning_key, reasoning_result)

step_by_step_result = cache.get(step_by_step_key)
if step_by_step_result is None:
    # Apply decorator
    step_by_step_result = step_by_step.apply(prompt)
    # Cache result
    cache.set(step_by_step_key, step_by_step_result)

# Get cache statistics
stats = cache.get_stats()
print(f"Cache hits: {stats['hits']}")
print(f"Cache misses: {stats['misses']}")
```

## API Reference {: #utils-cache-api-reference }

::: prompt_decorators.utils.cache

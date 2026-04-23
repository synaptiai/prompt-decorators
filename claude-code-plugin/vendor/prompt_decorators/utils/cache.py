"""Decorator Cache Module.

This module provides a caching system for decorator definitions and instances.
"""
import logging
import threading
import time
from functools import lru_cache
from typing import Any, Dict, Optional, Tuple, Type

from prompt_decorators.core.base import BaseDecorator

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DecoratorCache:
    """Cache for decorator definitions and instances.

    This class provides a caching system for decorator definitions and instances,
    with support for cache invalidation and metrics.
    """

    _instance = None

    def __new__(cls):
        """Create a singleton instance of the cache.

        Returns:
            DecoratorCache: The singleton instance
        """
        if cls._instance is None:
            cls._instance = super(DecoratorCache, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize the cache."""
        # Cache for decorator definitions
        self._definitions: Dict[str, Tuple[float, Dict[str, Any]]] = {}

        # Cache for decorator classes
        self._classes: Dict[str, Type[BaseDecorator]] = {}

        # Cache for decorator instances
        self._instances: Dict[str, Tuple[float, BaseDecorator]] = {}

        # Cache metrics
        self._metrics = {
            "definition_hits": 0,
            "definition_misses": 0,
            "class_hits": 0,
            "class_misses": 0,
            "instance_hits": 0,
            "instance_misses": 0,
            "definition_evictions": 0,
            "instance_evictions": 0,
        }

        # Cache configuration
        self._config = {
            "max_definitions": 1000,
            "max_instances": 500,
            "definition_ttl": 3600,  # 1 hour
            "instance_ttl": 1800,  # 30 minutes
        }

        # Lock for thread safety
        self._lock = threading.RLock()

    def set_config(self, config: Dict[str, Any]) -> None:
        """Update the cache configuration.

        Args:
            config: Dictionary with configuration options to update

        Returns:
            None
        """
        with self._lock:
            self._config.update(config)

    def get_config(self) -> Dict[str, Any]:
        """Get the current cache configuration.

        Args:
            self: The DecoratorCache instance

        Returns:
            Dictionary with configuration options
        """
        with self._lock:
            return self._config.copy()

    def get_metrics(self) -> Dict[str, Any]:
        """Get cache metrics.

        Args:
            self: The DecoratorCache instance

        Returns:
            Dictionary with metrics
        """
        with self._lock:
            metrics = self._metrics.copy()
            metrics.update(
                {
                    "definition_count": len(self._definitions),
                    "class_count": len(self._classes),
                    "instance_count": len(self._instances),
                }
            )
            return metrics

    def clear(self) -> None:
        """Clear the cache."""
        with self._lock:
            self._definitions.clear()
            self._classes.clear()
            self._instances.clear()
            for key in self._metrics:
                self._metrics[key] = 0

    def get_definition(self, key: str) -> Optional[Dict[str, Any]]:
        """Get a decorator definition from the cache.

        Args:
            key: The cache key for the definition

        Returns:
            The decorator definition, or None if not found or expired
        """
        with self._lock:
            if key in self._definitions:
                timestamp, definition = self._definitions[key]

                # Check if expired
                if self._is_expired(timestamp, self._config["definition_ttl"]):
                    del self._definitions[key]
                    self._metrics["definition_evictions"] += 1
                    self._metrics["definition_misses"] += 1
                    return None

                self._metrics["definition_hits"] += 1
                return definition

            self._metrics["definition_misses"] += 1
            return None

    def set_definition(self, key: str, definition: Dict[str, Any]) -> None:
        """Store a decorator definition in the cache.

        Args:
            key: The cache key for the definition
            definition: The decorator definition to store

        Returns:
            None
        """
        with self._lock:
            # Evict if cache is full
            if len(self._definitions) >= self._config["max_definitions"]:
                self._evict_definitions(1)

            self._definitions[key] = (time.time(), definition)

    def get_class(self, key: str) -> Optional[Type[BaseDecorator]]:
        """Get a decorator class from the cache.

        Args:
            key: The cache key for the class

        Returns:
            The decorator class, or None if not found
        """
        with self._lock:
            if key in self._classes:
                self._metrics["class_hits"] += 1
                return self._classes[key]

            self._metrics["class_misses"] += 1
            return None

    def set_class(self, key: str, decorator_class: Type[BaseDecorator]) -> None:
        """Store a decorator class in the cache.

        Args:
            key: The cache key for the class
            decorator_class: The decorator class to store

        Returns:
            None
        """
        with self._lock:
            self._classes[key] = decorator_class

    def get_instance(self, key: str) -> Optional[BaseDecorator]:
        """Get a decorator instance from the cache.

        Args:
            key: The cache key for the instance

        Returns:
            The decorator instance, or None if not found or expired
        """
        with self._lock:
            if key in self._instances:
                timestamp, instance = self._instances[key]

                # Check if expired
                if self._is_expired(timestamp, self._config["instance_ttl"]):
                    del self._instances[key]
                    self._metrics["instance_evictions"] += 1
                    self._metrics["instance_misses"] += 1
                    return None

                self._metrics["instance_hits"] += 1
                return instance

            self._metrics["instance_misses"] += 1
            return None

    def set_instance(self, key: str, instance: BaseDecorator) -> None:
        """Store a decorator instance in the cache.

        Args:
            key: The cache key for the instance
            instance: The decorator instance to store

        Returns:
            None
        """
        with self._lock:
            # Evict if cache is full
            if len(self._instances) >= self._config["max_instances"]:
                self._evict_instances(1)

            self._instances[key] = (time.time(), instance)

    def invalidate_definition(self, key: str) -> bool:
        """Invalidate a cached decorator definition.

        Args:
            key: The cache key for the definition

        Returns:
            True if the item was found and invalidated, False otherwise
        """
        with self._lock:
            if key in self._definitions:
                del self._definitions[key]
                self._metrics["definition_evictions"] += 1
                return True
            return False

    def invalidate_instance(self, key: str) -> bool:
        """Invalidate a cached decorator instance.

        Args:
            key: The cache key for the instance

        Returns:
            True if the item was found and invalidated, False otherwise
        """
        with self._lock:
            if key in self._instances:
                del self._instances[key]
                self._metrics["instance_evictions"] += 1
                return True
            return False

    def _is_expired(self, timestamp: float, ttl: int) -> bool:
        """Check if a cached item is expired.

        Args:
            timestamp: The timestamp when the item was cached
            ttl: Time-to-live in seconds

        Returns:
            True if expired, False otherwise
        """
        return time.time() - timestamp > ttl

    def _evict_definitions(self, count: int) -> int:
        """Evict the oldest definitions from the cache.

        Args:
            count: Number of items to evict

        Returns:
            Number of items actually evicted
        """
        # Sort by timestamp (oldest first)
        sorted_keys = sorted(
            self._definitions.keys(), key=lambda k: self._definitions[k][0]
        )

        evicted = 0
        for key in sorted_keys[:count]:
            del self._definitions[key]
            evicted += 1
            self._metrics["definition_evictions"] += 1

        return evicted

    def _evict_instances(self, count: int) -> int:
        """Evict the oldest instances from the cache.

        Args:
            count: Number of items to evict

        Returns:
            Number of items actually evicted
        """
        # Sort by timestamp (oldest first)
        sorted_keys = sorted(
            self._instances.keys(), key=lambda k: self._instances[k][0]
        )

        evicted = 0
        for key in sorted_keys[:count]:
            del self._instances[key]
            evicted += 1
            self._metrics["instance_evictions"] += 1

        return evicted


# Create a global cache instance
cache = DecoratorCache()


# Function to get the global cache
def get_cache() -> DecoratorCache:
    """Get the global decorator cache instance.

    Returns:
        The global decorator cache instance
    """
    return cache


# LRU cache for decorator instance creation
@lru_cache(maxsize=128)
def get_cached_decorator(class_name: str, param_str: str) -> Optional[BaseDecorator]:
    """Get a cached decorator instance.

    Args:
        class_name: The decorator class name
        param_str: String representation of parameters

    Returns:
        The decorator instance, or None if creation failed
    """  # This is just a basic implementation using Python's built-in LRU cache
    # The actual implementation would create the decorator instance
    # For now, this serves as a placeholder for external code to use
    return None

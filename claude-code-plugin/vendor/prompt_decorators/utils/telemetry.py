"""Telemetry Module.

This module provides an opt-in telemetry system for tracking decorator usage patterns.
"""
import json
import logging
import os
import queue
import threading
import time
import uuid
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class TelemetryManager:
    """Manager for collecting and reporting telemetry data.

    This class provides utilities for collecting usage data about decorators
    and reporting it for analytics purposes. All telemetry is opt-in.
    """

    _instance = None

    def __new__(cls):
        """Create a singleton instance of the telemetry manager.

        Returns:
            The singleton instance of the telemetry manager.
        """
        if cls._instance is None:
            cls._instance = super(TelemetryManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self) -> None:
        """Initialize the telemetry manager."""
        # Whether telemetry is enabled
        self._enabled = False

        # Unique installation ID
        self._installation_id = str(uuid.uuid4())

        # Queue for telemetry events
        self._event_queue = queue.Queue()

        # Worker thread for processing events
        self._worker_thread = None
        self._stop_worker = threading.Event()

        # Storage for telemetry data
        self._storage_path = None

        # Callbacks for telemetry events
        self._callbacks: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}

        # Load configuration
        self._load_config()

    def _load_config(self) -> None:
        """Load telemetry configuration."""
        try:
            # Get configuration directory
            config_dir = os.environ.get(
                "PROMPT_DECORATORS_CONFIG_DIR",
                os.path.expanduser("~/.prompt_decorators"),
            )
            config_path = os.path.join(config_dir, "telemetry.json")

            # Create directory if it doesn't exist
            os.makedirs(config_dir, exist_ok=True)

            # Set storage path
            self._storage_path = os.path.join(config_dir, "telemetry_data")
            os.makedirs(self._storage_path, exist_ok=True)

            # If config file exists, load it
            if os.path.exists(config_path):
                with open(config_path, "r") as f:
                    config = json.load(f)
                    self._enabled = config.get("enabled", False)
                    self._installation_id = config.get(
                        "installation_id", self._installation_id
                    )
            else:
                # Create default config
                config = {"enabled": False, "installation_id": self._installation_id}
                with open(config_path, "w") as f:
                    json.dump(config, f, indent=2)

            logger.debug(f"Telemetry {'enabled' if self._enabled else 'disabled'}")

        except Exception as e:
            logger.warning(f"Error loading telemetry configuration: {e}")
            self._enabled = False

    def enable(self) -> None:
        """Enable telemetry collection."""
        if self._enabled:
            return

        self._enabled = True
        self._save_config()
        self._start_worker()
        logger.info("Telemetry collection enabled")

    def disable(self) -> None:
        """Disable telemetry collection."""
        if not self._enabled:
            return

        self._enabled = False
        self._save_config()
        self._stop_worker_thread()
        logger.info("Telemetry collection disabled")

    def is_enabled(self) -> bool:
        """Check if telemetry is enabled.

        Args:
            self: The TelemetryManager instance

        Returns:
            True if enabled, False otherwise
        """
        return self._enabled

    def _save_config(self) -> None:
        """Save telemetry configuration."""
        try:
            config_dir = os.environ.get(
                "PROMPT_DECORATORS_CONFIG_DIR",
                os.path.expanduser("~/.prompt_decorators"),
            )
            config_path = os.path.join(config_dir, "telemetry.json")

            config = {
                "enabled": self._enabled,
                "installation_id": self._installation_id,
            }

            with open(config_path, "w") as f:
                json.dump(config, f, indent=2)

        except Exception as e:
            logger.warning(f"Error saving telemetry configuration: {e}")

    def track_decorator_usage(
        self,
        decorator_name: str,
        version: str,
        parameters: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Track usage of a decorator.

        Args:
            decorator_name: Name of the decorator
            version: Version of the decorator
            parameters: Parameters used with the decorator (optional)
            metadata: Additional metadata (optional)

        Returns:
            None
        """
        if not self._enabled:
            return

        event = {
            "type": "decorator_usage",
            "timestamp": datetime.utcnow().isoformat(),
            "decorator": {
                "name": decorator_name,
                "version": version,
                "parameters": parameters or {},
            },
            "metadata": metadata or {},
        }

        self._queue_event(event)
        self._call_callbacks("decorator_usage", event)

    def track_decorator_combination(
        self,
        decorators: List[Dict[str, Any]],
        prompt_length: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Track a combination of decorators used together.

        Args:
            decorators: List of decorator information dictionaries
            prompt_length: Length of the prompt in tokens (optional)
            metadata: Additional metadata (optional)

        Returns:
            None
        """
        if not self._enabled:
            return

        event = {
            "type": "decorator_combination",
            "timestamp": datetime.utcnow().isoformat(),
            "decorators": decorators,
            "prompt_length": prompt_length,
            "metadata": metadata or {},
        }

        self._queue_event(event)
        self._call_callbacks("decorator_combination", event)

    def track_performance(
        self,
        decorator_name: str,
        version: str,
        execution_time: float,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Track performance metrics for a decorator.

        Args:
            decorator_name: Name of the decorator
            version: Version of the decorator
            execution_time: Time taken to execute the decorator in seconds
            metadata: Additional metadata (optional)

        Returns:
            None
        """
        if not self._enabled:
            return

        event = {
            "type": "performance",
            "timestamp": datetime.utcnow().isoformat(),
            "decorator": {
                "name": decorator_name,
                "version": version,
            },
            "execution_time": execution_time,
            "metadata": metadata or {},
        }

        self._queue_event(event)
        self._call_callbacks("performance", event)

    def _queue_event(self, event: Dict[str, Any]) -> None:
        """Queue an event for processing.

        Args:
            event: Event data to queue

        Returns:
            None
        """
        # Start worker thread if not already running
        if not hasattr(self, "_worker_thread") or not self._worker_thread.is_alive():
            self._start_worker()

        try:
            self._event_queue.put(event, block=False)
        except queue.Full:
            logger.warning("Telemetry event queue is full, discarding event")

    def _start_worker(self) -> None:
        """Start the worker thread for processing events."""
        if not self._enabled:
            return

        if self._worker_thread is None or not self._worker_thread.is_alive():
            self._stop_worker.clear()
            self._worker_thread = threading.Thread(
                target=self._worker_thread_func, daemon=True
            )
            self._worker_thread.start()

    def _stop_worker_thread(self) -> None:
        """Stop the worker thread."""
        if self._worker_thread and self._worker_thread.is_alive():
            self._stop_worker.set()
            self._worker_thread.join(timeout=2.0)
            self._worker_thread = None

    def _worker_thread_func(self) -> None:
        """Thread function for processing telemetry events."""
        while not self._stop_worker.is_set():
            try:
                # Get events from queue with timeout
                try:
                    event = self._event_queue.get(timeout=1.0)
                except queue.Empty:
                    continue

                # Process the event
                self._process_event(event)

                # Mark as done
                self._event_queue.task_done()

            except Exception as e:
                logger.warning(f"Error in telemetry worker thread: {e}")
                time.sleep(1.0)

    def _process_event(self, event: Dict[str, Any]) -> None:
        """Process a telemetry event.

        Args:
            event: The event to process

        Returns:
            None
        """
        try:
            # Call registered callbacks
            event_type = event.get("type", "unknown")
            self._call_callbacks(event_type, event)

            # Log the event (in production, this would send to a telemetry service)
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"Telemetry event: {json.dumps(event)}")

        except Exception as e:
            logger.warning(f"Error processing telemetry event: {e}")

    def register_callback(
        self, event_type: str, callback: Callable[[Dict[str, Any]], None]
    ) -> None:
        """Register a callback for a specific event type.

        Args:
            event_type: Type of event to register for
            callback: Function to call when an event of this type occurs

        Returns:
            None
        """
        if event_type not in self._callbacks:
            self._callbacks[event_type] = []

        if callback not in self._callbacks[event_type]:
            self._callbacks[event_type].append(callback)

    def unregister_callback(
        self, event_type: str, callback: Callable[[Dict[str, Any]], None]
    ) -> None:
        """Unregister a callback for telemetry events.

        Args:
            event_type: Type of event
            callback: Function to unregister

        Returns:
            None
        """
        if event_type in self._callbacks:
            self._callbacks[event_type] = [
                c for c in self._callbacks[event_type] if c != callback
            ]

    def _call_callbacks(self, event_type: str, event: Dict[str, Any]) -> None:
        """Call registered callbacks for an event.

        Args:
            event_type: Type of event
            event: The event data

        Returns:
            None
        """
        if event_type not in self._callbacks:
            return

        for callback in self._callbacks[event_type]:
            try:
                callback(event)
            except Exception as e:
                logger.warning(f"Error in telemetry callback: {e}")


# Create a global telemetry manager instance
telemetry_manager = TelemetryManager()


# Function to get the global telemetry manager
def get_telemetry_manager() -> TelemetryManager:
    """Get the global telemetry manager.

    Returns:
        The global telemetry manager instance
    """
    return telemetry_manager

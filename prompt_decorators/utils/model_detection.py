"""Model detection and capability utilities.

This module provides utilities for detecting model capabilities and features.
"""

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

# Configure logging
logger = logging.getLogger(__name__)


class ModelCapabilities:
    """Class to represent the capabilities of a model.

    This class stores information about what a model can and cannot do,
    such as supported decorator features and parameter types.
    """

    def __init__(
        self,
        model_id: str,
        model_family: str = "unknown",
        version: str = "unknown",
        capabilities: Optional[Dict[str, Any]] = None,
    ):
        """Initialize a model capabilities object.

        Args:
            model_id: Unique identifier for the model
            model_family: Family or provider of the model
            version: Version of the model
            capabilities: Dictionary of capability flags and values
        """
        self.model_id = model_id
        self.model_family = model_family
        self.version = version
        self.capabilities = capabilities or {}

    def supports_feature(self, feature: str) -> bool:
        """Check if the model supports a specific feature.

        Args:
            feature: The feature to check

        Returns:
            True if the feature is supported, False otherwise
        """
        return self.capabilities.get(feature, False)

    def get_capability(self, capability: str, default: Any = None) -> Any:
        """Get the value of a capability.

        Args:
            capability: The capability to get
            default: Default value if the capability is not defined

        Returns:
            The capability value, or the default if not found
        """
        return self.capabilities.get(capability, default)

    def set_capability(self, capability: str, value: Any) -> None:
        """Set the value of a capability.

        Args:
            capability: The capability to set
            value: The value to set

        Returns:
            None
        """
        self.capabilities[capability] = value

    def to_dict(self) -> Dict[str, Any]:
        """Convert the model capabilities to a dictionary.

        Args:
            self: The ModelCapabilities instance

        Returns:
            Dictionary representation of the model capabilities
        """
        return {
            "model_id": self.model_id,
            "model_family": self.model_family,
            "version": self.version,
            "capabilities": self.capabilities,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModelCapabilities":
        """Create a model capabilities object from a dictionary.

        Args:
            data: Dictionary containing model capabilities data

        Returns:
            A new ModelCapabilities instance

        Raises:
            ValueError: If the dictionary is missing required fields
        """
        if "model_id" not in data:
            raise ValueError("Missing required field 'model_id'")

        return cls(
            model_id=data["model_id"],
            model_family=data.get("model_family", "unknown"),
            version=data.get("version", "unknown"),
            capabilities=data.get("capabilities", {}),
        )


class ModelDetector:
    """Detector for model capabilities.

    This class provides utilities for detecting and querying model capabilities.
    """

    # Default capabilities file location
    DEFAULT_CAPABILITIES_PATH = (
        Path(__file__).parent.parent.parent / "config" / "model_capabilities.json"
    )

    _instance = None

    def __new__(cls):
        """Create a singleton instance of the model detector.

        Returns:
            The singleton model detector instance
        """
        if cls._instance is None:
            cls._instance = super(ModelDetector, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize the model detector.

        This method is called once when the singleton instance is created.

        Args:
            self: The ModelDetector instance

        Returns:
            None
        """
        self._models = {}
        self._families = {}
        self._load_default_capabilities()
        self._load_builtin_capabilities()

    def _load_default_capabilities(self):
        """Load default model capabilities from the configuration file.

        This method loads model capabilities from the default configuration file
        if it exists. If the file doesn't exist or can't be parsed, a warning is
        logged but no exception is raised.

        Args:
            self: The ModelDetector instance

        Returns:
            None
        """
        try:
            capabilities_path = self.DEFAULT_CAPABILITIES_PATH
            if not capabilities_path.exists():
                logger.warning(
                    f"Default capabilities file not found: {capabilities_path}"
                )
                return

            with open(capabilities_path, "r") as f:
                data = json.load(f)

            for model_data in data.get("models", []):
                try:
                    model = ModelCapabilities.from_dict(model_data)
                    self.register_model(model)
                except Exception as e:
                    logger.warning(f"Error loading model capabilities: {e}")
        except Exception as e:
            logger.warning(f"Error loading default capabilities: {e}")

    def _load_builtin_capabilities(self):
        """Load built-in model capabilities.

        This method defines built-in capabilities for common models.
        These are used as fallbacks if no configuration file is available.

        Args:
            self: The ModelDetector instance

        Returns:
            None
        """
        # OpenAI models
        openai_models = {
            "gpt-4-turbo": {
                "max_tokens": 4096,
                "supports_functions": True,
                "supports_vision": False,
            },
            "gpt-4-turbo-16k": {
                "max_tokens": 16384,
                "supports_functions": True,
                "supports_vision": False,
            },
            "gpt-4o": {
                "max_tokens": 8192,
                "supports_functions": True,
                "supports_vision": False,
            },
            "gpt-4o-mini": {
                "max_tokens": 32768,
                "supports_functions": True,
                "supports_vision": False,
            },
            "gpt-4o-vision-preview": {
                "max_tokens": 8192,
                "supports_functions": True,
                "supports_vision": True,
            },
            "gpt-4o-vision": {
                "max_tokens": 128000,
                "supports_functions": True,
                "supports_vision": True,
            },
        }

        for model_id, capabilities in openai_models.items():
            model = ModelCapabilities(
                model_id=model_id,
                model_family="openai",
                version="latest",
                capabilities=capabilities,
            )
            self.register_model(model)

        # Anthropic models
        anthropic_models = {
            "claude-instant-1": {
                "max_tokens": 100000,
                "supports_functions": False,
                "supports_vision": False,
            },
            "claude-1": {
                "max_tokens": 100000,
                "supports_functions": False,
                "supports_vision": False,
            },
            "claude-3-5-sonnet-latest": {
                "max_tokens": 100000,
                "supports_functions": False,
                "supports_vision": False,
            },
            "claude-3-7-sonnet-latest": {
                "max_tokens": 200000,
                "supports_functions": False,
                "supports_vision": True,
            },
        }

        for model_id, capabilities in anthropic_models.items():
            model = ModelCapabilities(
                model_id=model_id,
                model_family="anthropic",
                version="latest",
                capabilities=capabilities,
            )
            self.register_model(model)

    def register_model(self, model: ModelCapabilities) -> None:
        """Register a model's capabilities.

        Args:
            model: The model capabilities to register

        Returns:
            None
        """
        self._models[model.model_id] = model

        # Register in family
        if model.model_family not in self._families:
            self._families[model.model_family] = []

        self._families[model.model_family].append(model.model_id)

    def get_model_capabilities(self, model_id: str) -> Optional[ModelCapabilities]:
        """Get capabilities for a specific model.

        Args:
            model_id: The model identifier

        Returns:
            ModelCapabilities for the model, or None if not found

        Note:
            This method attempts to find an exact match first, then falls back
            to a partial match if no exact match is found.
        """
        # Try exact match
        if model_id in self._models:
            return self._models[model_id]

        # Try partial match
        for registered_id in self._models:
            if model_id in registered_id or registered_id in model_id:
                logger.debug(
                    f"Using capabilities for {registered_id} as a match for {model_id}"
                )
                return self._models[registered_id]

        logger.warning(f"No capabilities found for model: {model_id}")
        return None

    def get_models_by_family(self, family: str) -> List[ModelCapabilities]:
        """Get all models in a specific family.

        Args:
            family: Model family

        Returns:
            List of ModelCapabilities for models in the family
        """
        if family not in self._families:
            return []

        return [self._models[model_id] for model_id in self._families[family]]

    def get_all_models(self) -> List[ModelCapabilities]:
        """Get all registered models.

        Args:
            self: The ModelDetector instance

        Returns:
            List of all registered ModelCapabilities
        """
        return list(self._models.values())

    def get_all_families(self) -> List[str]:
        """Get all registered model families.

        Args:
            self: The ModelDetector instance

        Returns:
            List of all registered model families
        """
        return list(self._families.keys())

    def detect_model_from_api(self, api_name: str) -> Optional[str]:
        """Detect the model family from an API name.

        Args:
            api_name: The API name or URL

        Returns:
            The detected model family, or None if not detected
        """
        api_name = api_name.lower()

        # Map of API name patterns to model families
        api_patterns = {
            "openai": "openai",
            "api.openai.com": "openai",
            "anthropic": "anthropic",
            "api.anthropic.com": "anthropic",
            "claude": "anthropic",
            "cohere": "cohere",
            "api.cohere.ai": "cohere",
        }

        for pattern, family in api_patterns.items():
            if pattern in api_name:
                return family

        return None


def get_model_detector() -> ModelDetector:
    """Get the global model detector instance.

    Returns:
        The global model detector instance
    """
    return ModelDetector()

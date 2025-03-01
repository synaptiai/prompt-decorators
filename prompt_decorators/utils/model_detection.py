"""
Model Detection Module

This module provides utilities for detecting and managing model capabilities.
"""

import logging
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Set, Type, Union, cast

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ModelCapabilities:
    """
    Class to represent the capabilities of a model.
    
    This class stores information about what a model can and cannot do,
    such as supported decorator features and parameter types.
    """
    
    def __init__(
        self,
        model_id: str,
        model_family: str = "unknown",
        version: str = "unknown",
        capabilities: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize model capabilities.
        
        Args:
            model_id: Unique identifier for the model
            model_family: Model family (e.g., GPT, Llama, Claude)
            version: Model version
            capabilities: Dictionary of capabilities
        """
        self.model_id = model_id
        self.model_family = model_family
        self.version = version
        self.capabilities = capabilities or {}
    
    def supports_feature(self, feature: str) -> bool:
        """
        Check if the model supports a specific feature.
        
        Args:
            feature: Feature to check
            
        Returns:
            True if the feature is supported, False otherwise
        """
        return self.capabilities.get(feature, False)
    
    def get_capability(self, capability: str, default: Any = None) -> Any:
        """
        Get a capability value.
        
        Args:
            capability: Capability to get
            default: Default value if capability not found
            
        Returns:
            Capability value or default
        """
        return self.capabilities.get(capability, default)
    
    def set_capability(self, capability: str, value: Any) -> None:
        """
        Set a capability value.
        
        Args:
            capability: Capability to set
            value: Value to set
        """
        self.capabilities[capability] = value
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert capabilities to a dictionary.
        
        Returns:
            Dictionary representation of capabilities
        """
        return {
            "model_id": self.model_id,
            "model_family": self.model_family,
            "version": self.version,
            "capabilities": self.capabilities
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ModelCapabilities':
        """
        Create a ModelCapabilities instance from a dictionary.
        
        Args:
            data: Dictionary with capability data
            
        Returns:
            New ModelCapabilities instance
        """
        return cls(
            model_id=data.get("model_id", "unknown"),
            model_family=data.get("model_family", "unknown"),
            version=data.get("version", "unknown"),
            capabilities=data.get("capabilities", {})
        )


class ModelDetector:
    """
    Detector for model capabilities.
    
    This class provides utilities for detecting and querying model capabilities.
    """
    
    # Default capabilities file location
    DEFAULT_CAPABILITIES_PATH = Path(__file__).parent.parent.parent / "config" / "model_capabilities.json"
    
    _instance = None
    
    def __new__(cls):
        """Create a singleton instance of the model detector."""
        if cls._instance is None:
            cls._instance = super(ModelDetector, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Initialize the model detector."""
        self._models: Dict[str, ModelCapabilities] = {}
        self._families: Dict[str, List[str]] = {}
        self._load_default_capabilities()
    
    def _load_default_capabilities(self):
        """Load default model capabilities from the configuration file."""
        try:
            capabilities_path = self.DEFAULT_CAPABILITIES_PATH
            if capabilities_path.exists():
                with open(capabilities_path, 'r') as f:
                    capabilities_data = json.load(f)
                    
                for model_data in capabilities_data.get("models", []):
                    model = ModelCapabilities.from_dict(model_data)
                    self.register_model(model)
            else:
                logger.info(f"Default capabilities file not found at {capabilities_path}. Using built-in defaults.")
                self._load_builtin_capabilities()
        except Exception as e:
            logger.warning(f"Error loading default capabilities: {e}. Using built-in defaults.")
            self._load_builtin_capabilities()
    
    def _load_builtin_capabilities(self):
        """Load built-in model capabilities for common models."""
        # Define capabilities for common model families
        
        # GPT models (OpenAI)
        gpt4_capabilities = ModelCapabilities(
            model_id="gpt-4",
            model_family="gpt",
            version="4.0",
            capabilities={
                "reasoning": True,
                "step_by_step": True,
                "code_generation": True,
                "json_output": True,
                "markdown_output": True,
                "max_tokens": 8192,
                "streaming": True,
                "function_calling": True,
                "multi_tool_use": True
            }
        )
        
        gpt35_capabilities = ModelCapabilities(
            model_id="gpt-3.5-turbo",
            model_family="gpt",
            version="3.5",
            capabilities={
                "reasoning": True,
                "step_by_step": True,
                "code_generation": True,
                "json_output": True,
                "markdown_output": True,
                "max_tokens": 4096,
                "streaming": True,
                "function_calling": True,
                "multi_tool_use": False
            }
        )
        
        # Claude models (Anthropic)
        claude_capabilities = ModelCapabilities(
            model_id="claude-2",
            model_family="claude",
            version="2.0",
            capabilities={
                "reasoning": True,
                "step_by_step": True,
                "code_generation": True,
                "json_output": True,
                "markdown_output": True,
                "max_tokens": 100000,
                "streaming": True,
                "function_calling": False,
                "multi_tool_use": False
            }
        )
        
        # Register all built-in models
        for model in [gpt4_capabilities, gpt35_capabilities, claude_capabilities]:
            self.register_model(model)
    
    def register_model(self, model: ModelCapabilities) -> None:
        """
        Register a model's capabilities.
        
        Args:
            model: ModelCapabilities instance
        """
        self._models[model.model_id] = model
        
        # Add to family mapping
        if model.model_family not in self._families:
            self._families[model.model_family] = []
        self._families[model.model_family].append(model.model_id)
        
        logger.debug(f"Registered model capabilities for {model.model_id}")
    
    def get_model_capabilities(self, model_id: str) -> Optional[ModelCapabilities]:
        """
        Get capabilities for a specific model.
        
        Args:
            model_id: Model identifier
            
        Returns:
            ModelCapabilities for the model, or None if not found
        """
        # Exact match
        if model_id in self._models:
            return self._models[model_id]
        
        # Try prefix matching (e.g., "gpt-4-0314" matches "gpt-4")
        for registered_id in self._models:
            if model_id.startswith(registered_id):
                return self._models[registered_id]
            
        # Try extracting family from model ID
        parts = model_id.split("-")
        if len(parts) > 0:
            family = parts[0].lower()
            if family in self._families and self._families[family]:
                # Return the first model in the family
                return self._models[self._families[family][0]]
        
        logger.warning(f"No capabilities found for model {model_id}")
        return None
    
    def get_models_by_family(self, family: str) -> List[ModelCapabilities]:
        """
        Get all models in a specific family.
        
        Args:
            family: Model family
            
        Returns:
            List of ModelCapabilities for models in the family
        """
        if family not in self._families:
            return []
            
        return [self._models[model_id] for model_id in self._families[family] if model_id in self._models]
    
    def get_all_models(self) -> List[ModelCapabilities]:
        """
        Get all registered models.
        
        Returns:
            List of all ModelCapabilities
        """
        return list(self._models.values())
    
    def get_all_families(self) -> List[str]:
        """
        Get all registered model families.
        
        Returns:
            List of all model family names
        """
        return list(self._families.keys())
    
    def detect_model_from_api(self, api_name: str) -> Optional[str]:
        """
        Try to determine a model ID from the API name.
        
        Args:
            api_name: Name of the API (e.g., "openai", "anthropic")
            
        Returns:
            Default model ID for the API, or None if not recognized
        """
        api_name = api_name.lower()
        
        # Map of API names to default models
        api_models = {
            "openai": "gpt-4",
            "anthropic": "claude-2",
            "cohere": "command",
            "huggingface": "mistral-7b-instruct"
        }
        
        return api_models.get(api_name)


# Create a global model detector instance
detector = ModelDetector()

# Function to get the global model detector
def get_model_detector() -> ModelDetector:
    """
    Get the global model detector.
    
    Returns:
        The global model detector instance
    """
    return detector 